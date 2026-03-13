import re

with open('courses.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<h3 class="card-title">(.*?)</h3>\s*</div>\s*<p>(.*?)</p>', text, re.DOTALL)

unique_titles = {}
for title, desc in matches:
    if title not in unique_titles:
        unique_titles[title] = desc.strip()

for title, desc in unique_titles.items():
    print(f"TITLE: {title}")
    # print(f"DESC: {desc}")
