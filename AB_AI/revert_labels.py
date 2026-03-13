import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Reverse the change from fix_labels2.py
new_text = re.sub(
    r'<h4 class="header-sm" style="color: #0000FF !important;">Pro Bachelors</h4>',
    r'<h4 class="color-primary header-sm">Pro Bachelors</h4>',
    text
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Reverted instances:", text.count('<h4 class="color-primary header-sm">Pro Bachelors</h4>'))
