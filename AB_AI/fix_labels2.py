import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Change <h4 class="color-primary header-sm">Pro Bachelors</h4> to blue
new_text = re.sub(
    r'<h4 class="color-primary header-sm">Pro Bachelors</h4>',
    r'<h4 class="header-sm" style="color: #0000FF !important;">Pro Bachelors</h4>',
    text
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Replaced instances:", text.count('Pro Bachelors'))
