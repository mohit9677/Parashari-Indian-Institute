with open(r'd:\ParashariTeam\AB_AI\blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace featured articles
html = html.replace('<article class="blog-featured carousel-slide active">', '<article class="blog-featured carousel-slide active glass-locked">')
html = html.replace('<article class="blog-featured carousel-slide">', '<article class="blog-featured carousel-slide glass-locked">')

# Replace normal blog cards (they span two lines)
targets = [
    ('<article class="blog-card" data-category="Vedic Astrology"\n                        onclick="location.href=\'blog-mangal-dosha.html\'" style="cursor:pointer;">',
     '<article class="blog-card glass-locked" data-category="Vedic Astrology">'),
    ('<article class="blog-card" data-category="Vastu Shastra"\n                        onclick="location.href=\'blog-vastu-tips.html\'" style="cursor:pointer;">',
     '<article class="blog-card glass-locked" data-category="Vastu Shastra">'),
    ('<article class="blog-card" data-category="Lal Kitab"\n                        onclick="location.href=\'blog-lal-kitab-financial.html\'" style="cursor:pointer;">',
     '<article class="blog-card glass-locked" data-category="Lal Kitab">'),
    ('<article class="blog-card" data-category="Numerology"\n                        onclick="location.href=\'blog-numerology-life-path.html\'" style="cursor:pointer;">',
     '<article class="blog-card glass-locked" data-category="Numerology">'),
    ('<article class="blog-card" data-category="KP Astrology"\n                        onclick="location.href=\'blog-kp-astrology.html\'" style="cursor:pointer;">',
     '<article class="blog-card glass-locked" data-category="KP Astrology">'),
    ('<article class="blog-card" data-category="Student Success Stories"\n                        onclick="location.href=\'blog-student-success.html\'" style="cursor:pointer;">',
     '<article class="blog-card glass-locked" data-category="Student Success Stories">')
]

for t in targets:
    html = html.replace(t[0], t[1])

with open(r'd:\ParashariTeam\AB_AI\blog.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated blog.html")
