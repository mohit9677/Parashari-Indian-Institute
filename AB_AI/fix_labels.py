import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The pattern is exactly: <span class="category-badge" style="background:#9C27B0">Bachelor · Pro</span>
# We replace it with #0000FF
new_text = re.sub(
    r'<span class="category-badge" style="background:#9C27B0">Bachelor',
    r'<span class="category-badge" style="background:#0000FF">Bachelor',
    text
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Replaced instances:", text.count('#9C27B0">Bachelor'))
