const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

let newHtml = html.replace(
    /<div class=\"card text-center testimonial-card-slide card-auto p-3\">\s*<img src=\"(assets\/images\/[^\"]+)\" alt=\"Student\" class=\"img-circle\">\s*<h4 class=\"color-primary mt-2\">([^<]+)<\/h4>\s*<div class=\"color-secondary stars\">([^<]+)<\/div>\s*<p class=\"card-small-text\">([^<]+)<\/p>\s*<\/div>/g,
    (match, p1, p2, p3, p4) => {
        let t = p4.trim().replace(/^"|"$/g, '');
        return `<div class="testimonial-card-slide">
            <div class="testimonial-img-wrapper">
              <img src="${p1}" alt="Student">
            </div>
            <div class="testimonial-info">
              <h4 class="color-primary">${p2}</h4>
              <div class="color-secondary stars">${p3}</div>
              <p class="card-small-text">"${t}"</p>
            </div>
          </div>`;
    }
);

fs.writeFileSync('index.html', newHtml);
console.log("Replaced successfully");
