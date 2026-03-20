import re

with open('blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

# For featured carousel items
html = re.sub(
    r'<article class="blog-featured(.*?)(?<!glass-locked)">',
    r'<article class="blog-featured\1 glass-locked">',
    html
)

# For normal blog cards, we need to add the class and remove onclick="location.href=..." and style="cursor:pointer;"
html = re.sub(
    r'<article class="blog-card"([^>]*)onclick="location\.href=\'[^\']*\'"\s*style="cursor:pointer;"([^>]*)>',
    r'<article class="blog-card glass-locked"\1\2>',
    html
)

# Also catch any other blog cards without onclick just in case
html = re.sub(
    r'<article class="blog-card(.*?)(?<!glass-locked)">',
    r'<article class="blog-card\1 glass-locked">',
    html
)

# Make links unclickable by adding a class if we want, or rely on CSS pointer-events:none
# CSS covers this via `.glass-locked * { pointer-events: none }`

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML modified successfully.")
