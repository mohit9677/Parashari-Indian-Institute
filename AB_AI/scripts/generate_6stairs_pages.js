const fs = require('fs');
const path = require('path');

const baseHtml = fs.readFileSync('palmistry.html', 'utf8');

const courses = [
    {
        file: 'yantra.html',
        icon: '✡️',
        name: 'Yantra',
        subtitle: 'Sacred Geometry',
        desc: 'Master sacred geometrical diagrams used for worship, meditation, and balancing cosmic energies.',
        image: 'assets/images/aries-card.png'
    },
    {
        file: 'mantra.html',
        icon: '📿',
        name: 'Mantra',
        subtitle: 'Vibrational Science',
        desc: 'Learn the science of sacred sounds and vibrations to manifest desires and achieve spiritual elevation.',
        image: 'assets/images/taurus-card.png'
    },
    {
        file: 'tantra.html',
        icon: '🧘',
        name: 'Tantra',
        subtitle: 'Esoteric Practices',
        desc: 'Explore the ancient esoteric practices for expanding consciousness and channeling divine energy.',
        image: 'assets/images/gemini-card.png'
    },
    {
        file: 'chakra-balancing.html',
        icon: '🌀',
        name: 'Chakra Balancing',
        subtitle: 'Energy Centers',
        desc: 'Understand the 7 vital energy centers of the body and techniques to cleanse and align them.',
        image: 'assets/images/cancer-card.png'
    },
    {
        file: '6-stairs-remedies.html',
        icon: '🌿',
        name: 'Remedies',
        subtitle: 'Astrological Solutions',
        desc: 'Discover practical astrological and spiritual remedies (Upaay) for solving complex life problems.',
        image: 'assets/images/leo-card.png'
    },
    {
        file: 'plrt.html',
        icon: '⏳',
        name: 'Past Life Regression Theory',
        subtitle: 'PLRT',
        desc: 'Delve into the science of past lives to heal present traumas and uncover karmic patterns.',
        image: 'assets/images/virgo-card.jpg'
    }
];

courses.forEach(course => {
    let content = baseHtml;

    // Title
    content = content.replace(/<title>.*?<\/title>/, `<title>${course.name} - Parashari Indian Institute</title>`);

    // Active nav class fix (remove active from Courses dropdown if any, or leave it as is, but we are copying Palmistry which already has Courses active)

    // Hero section
    content = content.replace(/<h1 class=\"color-secondary\">.*?<\/h1>/, `<h1 class="color-secondary">${course.icon} ${course.name} (${course.subtitle})</h1>`);
    content = content.replace(/<section class=\"hero-section hero-gradient\">\s*<div class=\"container\">\s*<h1 class=\"color-secondary\">.*?<\/h1>\s*<p>.*?<\/p>/,
        `<section class="hero-section hero-gradient">\n    <div class="container">\n      <h1 class="color-secondary">${course.icon} ${course.name} (${course.subtitle})</h1>\n      <p>${course.desc}</p>`);

    // Understanding Title
    content = content.replace(/<h2>Understanding Palmistry<\/h2>/, `<h2>Understanding ${course.name}</h2>`);

    // Paragraphs
    content = content.replace(/<p>Hasta Shastra or Palmistry is an ancient divination practice.*?<\/p>\s*<p>Each line and.*?<\/p>/s,
        `<p>${course.desc} Embark on a journey to deeply understand the fundamental principles and practical applications of this mystic science.</p>\n          <p>This program is designed to provide you with comprehensive knowledge, allowing you to incorporate these ancient techniques into modern-day contexts.</p>`);

    // List
    content = content.replace(/<ul class=\"list-reset\">\s*<li class=\"mb-0-75\">.*?<\/li>\s*<li class=\"mb-0-75\">.*?<\/li>\s*<li class=\"mb-0-75\">.*?<\/li>\s*<li>.*?<\/li>\s*<\/ul>/s,
        `<ul class="list-reset">
            <li class="mb-0-75">✓ Core fundamentals and philosophy</li>
            <li class="mb-0-75">✓ Advanced practical techniques</li>
            <li class="mb-0-75">✓ Real-life case studies and applications</li>
            <li>✓ Spiritual and practical guidance</li>
          </ul>`);

    // Image
    content = content.replace(/<img src=\"https:\/\/images.unsplash.com\/photo-1532619675605[^\"]*\" alt=\"Palmistry\"/,
        `<img src="${course.image}" alt="${course.name}"`);

    // PG Program Title
    content = content.replace(/<h2 class=\"card-section-title\">Our Palmistry PG Program<\/h2>/, `<h2 class="card-section-title">Our ${course.name} Program</h2>`);

    // Success Stories Title
    content = content.replace(/<h2 class=\"card-section-title\">Palmistry Success Stories<\/h2>/, `<h2 class="card-section-title">${course.name} Success Stories</h2>`);

    // Ready to master
    content = content.replace(/<h2 class=\"mb-1-5\">Ready to Master Palmistry\?<\/h2>/, `<h2 class="mb-1-5">Ready to Master ${course.name}?</h2>`);
    content = content.replace(/<p class=\"mb-2\">Join our Palmistry PG program and unlock the secrets of the palm.<\/p>/, `<p class="mb-2">Join our ${course.name} program and unlock an ancient science.</p>`);

    fs.writeFileSync(course.file, content);
    console.log(`Created ${course.file}`);
});
