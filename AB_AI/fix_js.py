import os

cwd = r'd:\\ParashariTeam\\AB_AI'
file_path = os.path.join(cwd, 'assets/js/courses-data.js')

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace icon: "<i class="fa-xxx"></i>" with icon: '<i class="fa-xxx"></i>'
import re
# We need to find lines like: icon: "<i class="fa-solid fa-om"></i>",
# And change the outer double quotes to single quotes.
# e.g. icon: "<i class=\"fa-solid fa-om\"></i>", if they were escaped, but they are not escaped.

# Let's just do a regex replace:
# r'icon:\s*"(<i[^>]+></i>)"' -> r"icon: '\1'"

patched_content = re.sub(r'icon:\s*"(<i[^>]+></i>)"', r"icon: '\1'", content)

if content != patched_content:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(patched_content)
    print("Fixed syntax in courses-data.js")
else:
    print("No changes needed in courses-data.js")
