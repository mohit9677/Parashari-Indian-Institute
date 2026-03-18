with open('diff_fee.txt', 'r', encoding='utf-16le') as f:
    diff = f.read()

import re

# Find old html lines
old_matches = re.findall(r'-(<td class=\"table-data-cell\"><div class=\"courses-scroll\">.*?)(?=^[\+\s])', diff, re.M | re.DOTALL)
for j, old_html in enumerate(old_matches):
    print(f'Section {j+1}')
    courses = re.findall(r'<div class=\"course-header\"><span class=\"course-name\">(.*?)</span>.*?<span class=\"course-price\">(.*?)</span>', old_html)
    for i, c in enumerate(courses[:2]):
        print(f"Course {i+1}: Price: {c[1]}")
    print('-'*20)

