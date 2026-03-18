with open('diff_fee.txt', 'r', encoding='utf-16le') as f:
    diff = f.read()

import re

old_matches = re.findall(r'-(<td class=\"table-data-cell\"><div class=\"courses-scroll\">.*?)(?=^[\+\s])', diff, re.M | re.DOTALL)
output = ""
for j, old_html in enumerate(old_matches):
    output += f"\n--- SECTION {j+1} ---\n"
    courses = re.findall(r'<div class=\"course-header\"><span class=\"course-name\">(.*?)</span>.*?<span class=\"course-price\">(.*?)</span>', old_html)
    for i, c in enumerate(courses):
        output += f"Course: {c[0]} -> Price: {c[1][:40]}...\n"
with open('all_old_prices.txt', 'w', encoding='utf-8') as f:
    f.write(output)
