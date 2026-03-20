import re
import os

html_path = r'd:\ParashariTeam\AB_AI\blog.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace featured articles
html = re.sub(r'<article class="blog-featured carousel-slide active">', '<article class="blog-featured carousel-slide active glass-locked">', html)
html = re.sub(r'<article class="blog-featured carousel-slide">', '<article class="blog-featured carousel-slide glass-locked">', html)

# Strip out onclick entirely and add class
html = re.sub(
    r'<article class="blog-card"([^>]*)onclick="location\.href=\'[^\']*\'"[^>]*>', 
    r'<article class="blog-card glass-locked"\1>', 
    html
)

# And catch any generic <article class="blog-card"> missing it
html = re.sub(
    r'<article class="blog-card"(?! glass-locked\b)', 
    r'<article class="blog-card glass-locked"', 
    html
)

# Hide free courses section
html = html.replace('<section class="free-courses-section">', '<section class="free-courses-section" style="display: none;">')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied HTML modifications to blog.html")
