with open('diff_fee.txt', 'r', encoding='utf-16le') as f:
    diff = f.read()

import re

old_matches = re.findall(r'-(<td class=\"table-data-cell\"><div class=\"courses-scroll\">.*?)(?=^[\+\s])', diff, re.M | re.DOTALL)
if old_matches:
    diploma_html = old_matches[0]
    courses = re.findall(r'<div class=\"course-header\"><span class=\"course-name\">(.*?)</span>.*?<span class=\"course-price\">(.*?)</span>', diploma_html)
    for i, c in enumerate(courses):
        print(f'{c[0]}: {c[1][:50]}')
