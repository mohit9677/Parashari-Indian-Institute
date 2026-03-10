import os
import re

html_content = open('courses.html', 'r', encoding='utf-8').read()
links = re.findall(r'href=[\'\"]([^\'\"]+\.html)[\'\"]', html_content)

missing = []
for link in set(links):
    if not os.path.exists(link):
        missing.append(link)

print("MISSING HTML FILES:")
for m in sorted(missing):
    print(m)
