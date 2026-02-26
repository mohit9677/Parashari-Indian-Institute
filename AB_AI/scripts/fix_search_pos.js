const fs = require('fs');
const path = require('path');

const directoryPath = '.';

function processFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');

    // Check if it already has tablet-search-container
    if (!content.includes('tablet-search-container')) return;

    // Remove the search container from wherever it is (inside header)
    const searchRegex = /<!-- Tablet Search Bar[^>]*-->[\s\S]*?<div class="tablet-search-container"[\s\S]*?<\/div>(\s*<\/div>)?/g;
    const matches = content.match(searchRegex);

    if (matches) {
        let searchBar = matches[0];

        // Clean up the search bar: remove absolute positioning and inline styles I added
        searchBar = searchBar.replace(/style="position: absolute;[^"]*"/g, '');
        searchBar = searchBar.replace(/style="background: #f8f9fa; color: #333; border: 1px solid #ccc;"/g, '');

        // Remove it from current location
        content = content.replace(searchRegex, '');

        // Find </header> and insert it just before it
        if (content.includes('</header>')) {
            content = content.replace('</header>', '\n    ' + searchBar.trim() + '\n  </header>');
            fs.writeFileSync(filePath, content);
            console.log(`Updated ${filePath}`);
        }
    }
}

fs.readdirSync(directoryPath).forEach(file => {
    if (file.endsWith('.html')) {
        processFile(path.join(directoryPath, file));
    }
});
