with open('fee-structure.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Find any course-price that still contains ₹2,999 or ₹3,999 and replace its content
text = re.sub(r'<span class=\"course-price\">.*?₹2,999.*?</span>', r'<span class="course-price">₹2,000 - ₹3,000</span>', text, flags=re.DOTALL)

with open('fee-structure.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('All stragglers replaced.')
