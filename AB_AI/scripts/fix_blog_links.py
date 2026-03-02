with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('blog-card" data-category="Vedic Astrology">',
     'blog-card" data-category="Vedic Astrology" onclick="location.href=\'blog-mangal-dosha.html\'" style="cursor:pointer;">'),
    ('blog-card" data-category="Vastu Shastra">',
     'blog-card" data-category="Vastu Shastra" onclick="location.href=\'blog-vastu-tips.html\'" style="cursor:pointer;">'),
    ('blog-card" data-category="Lal Kitab">',
     'blog-card" data-category="Lal Kitab" onclick="location.href=\'blog-lal-kitab-financial.html\'" style="cursor:pointer;">'),
    ('blog-card" data-category="Numerology">',
     'blog-card" data-category="Numerology" onclick="location.href=\'blog-numerology-life-path.html\'" style="cursor:pointer;">'),
    ('blog-card" data-category="KP Astrology">',
     'blog-card" data-category="KP Astrology" onclick="location.href=\'blog-kp-astrology.html\'" style="cursor:pointer;">'),
    ('blog-card" data-category="Student Success Stories">',
     'blog-card" data-category="Student Success Stories" onclick="location.href=\'blog-student-success.html\'" style="cursor:pointer;">'),
]

for old, new in replacements:
    content = content.replace(old, new, 1)

grid_links = [
    ('<a href="#">Mangal Dosha', '<a href="blog-mangal-dosha.html">Mangal Dosha'),
    ('<a href="#">10 Essential Vastu', '<a href="blog-vastu-tips.html">10 Essential Vastu'),
    ('<a href="#">Lal Kitab', '<a href="blog-lal-kitab-financial.html">Lal Kitab'),
    ('<a href="#">Calculate Your Life', '<a href="blog-numerology-life-path.html">Calculate Your Life'),
    ('<a href="#">Introduction to KP', '<a href="blog-kp-astrology.html">Introduction to KP'),
    ('<a href="#">From Enthusiast', '<a href="blog-student-success.html">From Enthusiast'),
]

for old, new in grid_links:
    content = content.replace(old, new, 1)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done! All blog card links updated.')
