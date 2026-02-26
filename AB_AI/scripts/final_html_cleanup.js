const fs = require('fs');
const path = require('path');

const directoryPath = '.';

function processFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');

    // Look for the specific pattern that Step 670 showed:
    // <section class="brand-hero" style="position: relative;">
    //     
    //     </div>

    const orphanedDiv = /<section class="brand-hero" style="position: relative;">\s*<\/div>/g;
    const orphanedDiv2 = /<section class="hero-header">\s*<\/div>/g;

    if (content.match(orphanedDiv)) {
        content = content.replace(orphanedDiv, '<section class="brand-hero" style="position: relative;">');
        fs.writeFileSync(filePath, content);
        console.log(`Fixed orphaned div in ${filePath}`);
    }
    if (content.match(orphanedDiv2)) {
        content = content.replace(orphanedDiv2, '<section class="hero-header">');
        fs.writeFileSync(filePath, content);
        console.log(`Fixed orphaned div2 in ${filePath}`);
    }
}

fs.readdirSync(directoryPath).forEach(file => {
    if (file.endsWith('.html')) {
        processFile(path.join(directoryPath, file));
    }
});
