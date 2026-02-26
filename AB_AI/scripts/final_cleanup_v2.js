const fs = require('fs');
const path = require('path');

const directoryPath = '.';

function processFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');

    // Check if it already has tablet-search-container
    if (!content.includes('tablet-search-container')) return;

    // 1. Fix the messy section around line 100 (orphaned search results or divs)
    // Looking for search-results not inside tablet-search-container
    const badPartRegex = /<\/nav>\s*<div class="search-results"><\/div>\s*<\/div>/g;
    if (content.match(badPartRegex)) {
        content = content.replace(badPartRegex, '</nav>');
        console.log(`Fixed bad results div in ${filePath}`);
    }

    // 2. Fix the orphaned </div> in hero sections
    const heroDivRegex = /(<section class="[^"]*-hero"[^>]*>)\s*<\/div>/g;
    if (content.match(heroDivRegex)) {
        content = content.replace(heroDivRegex, '$1');
        console.log(`Fixed orphaned hero div in ${filePath}`);
    }

    // 3. Ensure tablet-search-container is clean and has id=courseSearchInput if missing
    // My previous script might have left some attributes messy.

    fs.writeFileSync(filePath, content);
}

fs.readdirSync(directoryPath).forEach(file => {
    if (file.endsWith('.html')) {
        processFile(path.join(directoryPath, file));
    }
});
