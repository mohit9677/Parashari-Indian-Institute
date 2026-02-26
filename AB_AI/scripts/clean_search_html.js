const fs = require('fs');
const path = require('path');

const directoryPath = '.';

function processFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');

    // Check if it already has tablet-search-container
    if (!content.includes('tablet-search-container')) return;

    // The search block usually looks like this after my messy script:
    // <div class="tablet-search-container"
    //   >
    //   <div class="search-container">
    //     <div class="container-input">
    //       <input ... >
    //       <svg ... </svg>
    //     </div>
    // </header>

    // We want to replace the whole messy tablet-search-container block with a clean one and CLOSE it properly.

    const cleanSearchBlock = `    <div class="tablet-search-container">
      <div class="search-container">
        <div class="container-input">
          <input type="text" placeholder="Search all courses" name="text" class="input" id="courseSearchInput">
          <svg fill="#666" width="20px" height="20px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
            <path d="M790.588 1468.235c-373.722 0-677.647-303.924-677.647-677.647 0-373.722 303.925-677.647 677.647-677.647 373.723 0 677.647 303.925 677.647 677.647 0 373.723-303.924 677.647-677.647 677.647Zm596.781-160.715c120.396-138.692 193.807-319.285 193.807-516.932C1581.176 354.748 1226.428 0 790.588 0S0 354.748 0 790.588s354.748 790.588 790.588 790.588c197.647 0 378.24-73.411 516.932-193.807l516.028 516.142 79.963-79.963-516.142-516.028Z" fill-rule="evenodd"></path>
          </svg>
        </div>
        <div class="search-results"></div>
      </div>
    </div>`;

    // Regex to find the broken tablet-search-container block
    // It starts with <div class="tablet-search-container" and ends with something messy before </header>
    const messyRegex = /<!-- Tablet Search Bar[^>]*-->[\s\S]*?<div class="tablet-search-container"[\s\S]*?(?=<\/header>)/g;

    if (content.match(messyRegex)) {
        content = content.replace(messyRegex, cleanSearchBlock + '\n  ');
        fs.writeFileSync(filePath, content);
        console.log(`Cleaned up ${filePath}`);
    }
}

fs.readdirSync(directoryPath).forEach(file => {
    if (file.endsWith('.html')) {
        processFile(path.join(directoryPath, file));
    }
});
