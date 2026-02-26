const fs = require('fs');

// 1. Update navbar.js Mega Menu links
let navbar = fs.readFileSync('assets/js/navbar.js', 'utf8');
navbar = navbar.replace(/{ name: 'Yantra', meta: 'Sacred Geometry', url: '6-stairs\.html'/g, "{ name: 'Yantra', meta: 'Sacred Geometry', url: 'yantra.html'");
navbar = navbar.replace(/{ name: 'Mantra', meta: 'Vibrational Science', url: '6-stairs\.html'/g, "{ name: 'Mantra', meta: 'Vibrational Science', url: 'mantra.html'");
navbar = navbar.replace(/{ name: 'Tantra', meta: 'Esoteric Practices', url: '6-stairs\.html'/g, "{ name: 'Tantra', meta: 'Esoteric Practices', url: 'tantra.html'");
navbar = navbar.replace(/{ name: 'Chakra Balancing', meta: 'Energy Centers', url: '6-stairs\.html'/g, "{ name: 'Chakra Balancing', meta: 'Energy Centers', url: 'chakra-balancing.html'");
navbar = navbar.replace(/{ name: 'Remedies', meta: 'Astrological Solutions', url: '6-stairs\.html'/g, "{ name: 'Remedies', meta: 'Astrological Solutions', url: '6-stairs-remedies.html'");
navbar = navbar.replace(/{ name: 'PLRT', meta: 'Past Life Regression', url: '6-stairs\.html'/g, "{ name: 'PLRT', meta: 'Past Life Regression', url: 'plrt.html'");
fs.writeFileSync('assets/js/navbar.js', navbar);
console.log('Updated navbar.js links');

// 2. Update 6-stairs.html cards
let stairsHtml = fs.readFileSync('6-stairs.html', 'utf8');

// The tricky part: replacing `href="#"` for each specific card. 
// We can use a regex that matches the card title and replaces the href="#" that follows it inside the same card block.
const elements = [
    { title: 'Yantra', link: 'yantra.html' },
    { title: 'Mantra', link: 'mantra.html' },
    { title: 'Tantra', link: 'tantra.html' },
    { title: 'Chakra Balancing', link: 'chakra-balancing.html' },
    { title: 'Remedies', link: '6-stairs-remedies.html' },
    { title: 'Past Life Regression Theory', link: 'plrt.html' }
];

elements.forEach(el => {
    // Regex matches <h3 class="card-title">Title</h3> then anything until <a href="#" ...
    const regex = new RegExp(`(<h3 class="card-title">${el.title}<\\/h3>[\\s\\S]*?<a href=")#(" class="learn-more">)`, "g");
    stairsHtml = stairsHtml.replace(regex, `$1${el.link}$2`);
});

fs.writeFileSync('6-stairs.html', stairsHtml);
console.log('Updated 6-stairs.html links');
