const fs = require('fs');
const path = require('path');

const directoryPath = __dirname;

const newHTML = `<div class="social-wrapper">
          <a href="https://www.instagram.com/astrobharatai?igsh=Z2M2ZW82OXBxaGNr" target="_blank" rel="noopener noreferrer" class="icon instagram">
            <span class="tooltip">Instagram</span>
            <i class="fab fa-instagram"></i>
          </a>
          <a href="https://www.youtube.com/@astrobharatai" target="_blank" rel="noopener noreferrer" class="icon youtube">
            <span class="tooltip">YouTube</span>
            <i class="fab fa-youtube"></i>
          </a>
          <a href="https://x.com/AstroBharatAI" target="_blank" rel="noopener noreferrer" class="icon twitter">
            <span class="tooltip">Twitter</span>
            <i class="fab fa-twitter"></i>
          </a>
          <a href="https://www.linkedin.com/company/astrobharatai/" target="_blank" rel="noopener noreferrer" class="icon linkedin">
            <span class="tooltip">LinkedIn</span>
            <i class="fab fa-linkedin-in"></i>
          </a>
        </div>`;

// Regex matches <div class="social-links"> up to the first closing </div>
const regex = /<div class="social-links">[\s\S]*?<\/div>/g;

let totalReplaced = 0;

fs.readdir(directoryPath, (err, files) => {
    if (err) {
        return console.log('Unable to scan directory: ' + err);
    }
    files.forEach(file => {
        if (path.extname(file) === '.html') {
            const filePath = path.join(directoryPath, file);
            let content = fs.readFileSync(filePath, 'utf8');
            if (regex.test(content)) {
                content = content.replace(regex, newHTML);
                fs.writeFileSync(filePath, content, 'utf8');
                console.log(`Updated ${file}`);
                totalReplaced++;
            }
        }
    });
    console.log(`\nCompleted! Replaced in ${totalReplaced} files.`);
});
