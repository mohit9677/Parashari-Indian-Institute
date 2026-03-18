import re
with open('fee-structure.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<del style=\"color:#999;font-size:0.85em;margin-right:5px;\">(.*?)</del>', text)
if m:
    print('Current HTML price encoded as:', repr(m.group(1)))
