const fs = require('fs');
const path = require('path');

const dir = '.';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

// 1. Update all HTML files to include '6 Stairs' in the navbars
files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    let changed = false;

    // Desktop Nav
    const desktopRegex = /(<li\s+class=\"nav-item\">\s*<a\s+href=\"courses\.html\"[^>]*>Explore<\/a>\s*<\/li>)/g;
    if (content.match(desktopRegex) && !content.includes('6-stairs.html')) {
        content = content.replace(desktopRegex, '$1\n        <li class="nav-item"><a href="6-stairs.html">6 Stairs</a></li>');
        changed = true;
    }

    // Mobile Nav
    const mobileRegex = /(<li\s+class=\"nav-item w-full\">\s*<a\s+href=\"courses\.html\"[^>]*>Explore<\/a>\s*<\/li>)/g;
    if (content.match(mobileRegex) && !content.includes('6-stairs.html"')) {
        content = content.replace(mobileRegex, '$1\n        <li class="nav-item w-full"><a href="6-stairs.html">6 Stairs</a></li>');
        changed = true;
    }

    if (changed) {
        fs.writeFileSync(file, content);
        console.log(`Updated navbar in ${file}`);
    }
});

console.log('Navbars updated.');

// 2. Create 6-stairs.html
if (fs.existsSync('courses.html')) {
    let coursesContent = fs.readFileSync('courses.html', 'utf8');

    // Replace Title
    coursesContent = coursesContent.replace(/<title>.*<\/title>/, '<title>6 Stairs - Parashari Indian Institute</title>');

    // Replace Hero Section
    coursesContent = coursesContent.replace(/(<section class=\"hero-header\">[\s\S]*?<h1>).*?(<\/h1>[\s\S]*?<p class=\"hero-header-subtitle\">).*?(<\/p>[\s\S]*?<\/section>)/, '$16 Stairs Programs$2Discover the 6 mystical paths to spiritual and life mastery$3');

    // Replace Section Title
    coursesContent = coursesContent.replace(/<h2>Explore Our Programs<\/h2>\s*<p class=\"color-light-text\">.*?<\/p>/, '<h2>The 6 Stairs to Mastery</h2>\n<p class=\"color-light-text\">Explore Yantra, Mantra, Tantra, Chakra Balancing, Remedies, and PLRT.</p>');

    // Replace Cards
    const cardsHtml = `
<div class="card" data-animate data-category="6 Stairs">
    <div class="card-image-container">
        <img src="assets/images/aries-card.png" alt="Yantra" class="card-image">
        <div class="card-image-overlay"></div>
    </div>
    <div class="card-body">
        <div class="card-header">
            <div class="card-header-icon">✡️</div>
            <h3 class="card-title">Yantra</h3>
        </div>
        <p>Master sacred geometrical diagrams used for worship, meditation, and balancing cosmic energies.</p>
        <div class="mb-1">
            <span class="category-badge" style="background:#E91E63">✨ 6 Stairs</span>
            <span class="certification-badge">✓ Certification</span>
        </div>
        <div class="course-footer">
            <h4 class="color-secondary mb-0">Contact Us</h4>
            <a href="#" class="learn-more">
                <span class="circle" aria-hidden="true"><span class="icon arrow"></span></span>
                <span class="button-text">Learn More</span>
            </a>
        </div>
    </div>
</div>

<div class="card" data-animate data-category="6 Stairs">
    <div class="card-image-container">
        <img src="assets/images/taurus-card.png" alt="Mantra" class="card-image">
        <div class="card-image-overlay"></div>
    </div>
    <div class="card-body">
        <div class="card-header">
            <div class="card-header-icon">📿</div>
            <h3 class="card-title">Mantra</h3>
        </div>
        <p>Learn the science of sacred sounds and vibrations to manifest desires and achieve spiritual elevation.</p>
        <div class="mb-1">
            <span class="category-badge" style="background:#E91E63">✨ 6 Stairs</span>
            <span class="certification-badge">✓ Certification</span>
        </div>
        <div class="course-footer">
            <h4 class="color-secondary mb-0">Contact Us</h4>
            <a href="#" class="learn-more">
                <span class="circle" aria-hidden="true"><span class="icon arrow"></span></span>
                <span class="button-text">Learn More</span>
            </a>
        </div>
    </div>
</div>

<div class="card" data-animate data-category="6 Stairs">
    <div class="card-image-container">
        <img src="assets/images/gemini-card.png" alt="Tantra" class="card-image">
        <div class="card-image-overlay"></div>
    </div>
    <div class="card-body">
        <div class="card-header">
            <div class="card-header-icon">🧘</div>
            <h3 class="card-title">Tantra</h3>
        </div>
        <p>Explore the ancient esoteric practices for expanding consciousness and channeling divine energy.</p>
        <div class="mb-1">
            <span class="category-badge" style="background:#E91E63">✨ 6 Stairs</span>
            <span class="certification-badge">✓ Certification</span>
        </div>
        <div class="course-footer">
            <h4 class="color-secondary mb-0">Contact Us</h4>
            <a href="#" class="learn-more">
                <span class="circle" aria-hidden="true"><span class="icon arrow"></span></span>
                <span class="button-text">Learn More</span>
            </a>
        </div>
    </div>
</div>

<div class="card" data-animate data-category="6 Stairs">
    <div class="card-image-container">
        <img src="assets/images/cancer-card.png" alt="Chakra Balancing" class="card-image">
        <div class="card-image-overlay"></div>
    </div>
    <div class="card-body">
        <div class="card-header">
            <div class="card-header-icon">🌀</div>
            <h3 class="card-title">Chakra Balancing</h3>
        </div>
        <p>Understand the 7 vital energy centers of the body and techniques to cleanse and align them.</p>
        <div class="mb-1">
            <span class="category-badge" style="background:#E91E63">✨ 6 Stairs</span>
            <span class="certification-badge">✓ Certification</span>
        </div>
        <div class="course-footer">
            <h4 class="color-secondary mb-0">Contact Us</h4>
            <a href="#" class="learn-more">
                <span class="circle" aria-hidden="true"><span class="icon arrow"></span></span>
                <span class="button-text">Learn More</span>
            </a>
        </div>
    </div>
</div>

<div class="card" data-animate data-category="6 Stairs">
    <div class="card-image-container">
        <img src="assets/images/leo-card.png" alt="Remedies" class="card-image">
        <div class="card-image-overlay"></div>
    </div>
    <div class="card-body">
        <div class="card-header">
            <div class="card-header-icon">🌿</div>
            <h3 class="card-title">Remedies</h3>
        </div>
        <p>Discover practical astrological and spiritual remedies (Upaay) for solving complex life problems.</p>
        <div class="mb-1">
            <span class="category-badge" style="background:#E91E63">✨ 6 Stairs</span>
            <span class="certification-badge">✓ Certification</span>
        </div>
        <div class="course-footer">
            <h4 class="color-secondary mb-0">Contact Us</h4>
            <a href="#" class="learn-more">
                <span class="circle" aria-hidden="true"><span class="icon arrow"></span></span>
                <span class="button-text">Learn More</span>
            </a>
        </div>
    </div>
</div>

<div class="card" data-animate data-category="6 Stairs">
    <div class="card-image-container">
        <img src="assets/images/virgo-card.jpg" alt="PLRT" class="card-image">
        <div class="card-image-overlay"></div>
    </div>
    <div class="card-body">
        <div class="card-header">
            <div class="card-header-icon">⏳</div>
            <h3 class="card-title">Past Life Regression Theory</h3>
        </div>
        <p>Delve into the science of past lives to heal present traumas and uncover karmic patterns.</p>
        <div class="mb-1">
            <span class="category-badge" style="background:#E91E63">✨ 6 Stairs</span>
            <span class="certification-badge">✓ Certification</span>
        </div>
        <div class="course-footer">
            <h4 class="color-secondary mb-0">Contact Us</h4>
            <a href="#" class="learn-more">
                <span class="circle" aria-hidden="true"><span class="icon arrow"></span></span>
                <span class="button-text">Learn More</span>
            </a>
        </div>
    </div>
</div>
`;

    // Replace the grid content
    coursesContent = coursesContent.replace(/(<div class=\"grid-responsive grid-gap-2\">)[\s\S]*?(<\/div>\s*<\/div>\s*<\/section>)/, '$1\n        ' + cardsHtml + '\n        $2');

    // Fix the active class in the navbar for 6-stairs.html specifically
    coursesContent = coursesContent.replace(/<a href=\"courses.html\" class=\"active\">Explore<\/a>/, '<a href="courses.html">Explore</a>');

    // Remove the 6-stairs added locally to make it easier effectively
    // It's cleaner to remove the older added one and ensure the new active is correctly bound.
    coursesContent = coursesContent.replace(/<a href=\"6-stairs.html\">6 Stairs<\/a>/, '<a href="6-stairs.html" class="active">6 Stairs</a>');

    fs.writeFileSync('6-stairs.html', coursesContent);
    console.log('6-stairs.html created and tailored.');
}
