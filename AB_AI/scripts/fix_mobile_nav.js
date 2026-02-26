const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    let changed = false;

    // We split by <div class="mobile-menu"> to only target the mobile section
    let parts = content.split('<div class="mobile-menu">');
    if (parts.length > 1) {
        let mobileMenuPart = parts[1];

        // If it doesn't already have 6-stairs.html in the mobile section
        if (!mobileMenuPart.includes('6-stairs.html')) {
            // Mobile regex for 'Explore'
            const mobileRegex = /(<li\s+class=\"nav-item\s*w-full\">\s*<a\s+href=\"courses\.html\"[^>]*>Explore<\/a>\s*<\/li>)/g;

            if (mobileMenuPart.match(mobileRegex)) {
                mobileMenuPart = mobileMenuPart.replace(mobileRegex, '$1\n<li class="nav-item w-full"><a href="6-stairs.html">6 Stairs</a></li>');
                content = parts[0] + '<div class="mobile-menu">' + mobileMenuPart;
                changed = true;
            } else {
                console.log(`Explore not found in mobile menu of ${file}`);
            }
        }
    }

    if (changed) {
        fs.writeFileSync(file, content);
        console.log(`Fixed mobile menu in ${file}`);
    }
});
