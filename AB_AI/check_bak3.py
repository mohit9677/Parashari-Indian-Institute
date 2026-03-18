import re
try:
    with open('fee-structure.html.bak', 'r', encoding='utf-8') as f:
        text = f.read()
    match = re.search(r'<div class=\"course-box\">.*?</div></div>', text, re.DOTALL)
    if match:
        print('Course Box HTML:')
        print(match.group(0))
except Exception as e:
    print('Error:', e)
