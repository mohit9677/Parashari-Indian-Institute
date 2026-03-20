import re

with open(r'd:\ParashariTeam\AB_AI\blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace featured articles
html = re.sub(r'<article class="blog-featured carousel-slide active">', '<article class="blog-featured carousel-slide active glass-locked">', html)
html = re.sub(r'<article class="blog-featured carousel-slide">', '<article class="blog-featured carousel-slide glass-locked">', html)

# Replace normal blog cards (removing their onclick and cursor pointer to fix them properly)
html = re.sub(
    r'<article class="blog-card"([^>]*)onclick="location\.href=\'[^\']*\'"[^>]*>', 
    r'<article class="blog-card glass-locked"\1>', 
    html
)

with open(r'd:\ParashariTeam\AB_AI\blog.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML regex replacement done.")
