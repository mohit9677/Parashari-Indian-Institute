const fs = require('fs');
const path = require('path');

const directoryPath = '.';

function processFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');

    // Check if it already has tablet-search-container
    if (!content.includes('tablet-search-container')) return;

    // If it's outside the header, we move it.
    // Usually it's inside <section class="brand-hero"> or just after </header>

    const searchRegex = /<!-- Tablet Search Bar[^>]*-->[\s\S]*?<div class="tablet-search-container"[\s\S]*?<\/div>\s*<\/div>/g;
    const searchMatch = content.match(searchRegex);

    if (searchMatch) {
        const searchBar = searchMatch[0];
        // Remove it from current location
        content = content.replace(searchRegex, '');

        // Find </nav> and insert it after
        if (content.includes('</nav>')) {
            content = content.replace('</nav>', '</nav>\n    ' + searchBar.trim());
            fs.writeFileSync(filePath, content);
            console.log(`Updated ${filePath}`);
        }
    } else {
        // Try a simpler match if comments are missing or structure is slightly different
        const simpleRegex = /<div class="tablet-search-container"[\s\S]*?<\/div>(\s*<\/div>)?/g;
        const simpleMatch = content.match(simpleRegex);
        if (simpleMatch) {
            // But only if it's NOT already in the header
            const headerEndIndex = content.indexOf('</header>');
            const searchIndex = content.indexOf('class="tablet-search-container"');

            if (searchIndex > headerEndIndex) {
                const searchBar = simpleMatch[0];
                content = content.replace(simpleRegex, '');
                if (content.includes('</nav>')) {
                    content = content.replace('</nav>', '</nav>\n    ' + searchBar.trim());
                    fs.writeFileSync(filePath, content);
                    console.log(`Updated (simple) ${filePath}`);
                }
            }
        }
    }
}

fs.readdirSync(directoryPath).forEach(file => {
    if (file.endsWith('.html')) {
        processFile(path.join(directoryPath, file));
    }
});
