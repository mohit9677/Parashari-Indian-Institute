import os
import re

# 1. Update courses-data.js
js_file = 'assets/js/courses-data.js'
if os.path.exists(js_file):
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hide Grand Master objects in the JS array
    # They look like: { ... isCategory: "Grand Master", ... },
    # We can just change isCategory to "Hidden" or just comment out the block.
    # The safest regex replace is to replace "Grand Master" with "Hidden" for category assignments
    new_content = content.replace('isCategory: "Grand Master"', 'isCategory: "Hidden"')
    # Also the mapping object -> "Grand Master": { label: "Elite", tier: 5, color: "#c8960c" }
    # Better leave the mapping so it doesn't break if a hidden item exists, but we can hide it from UI by changing the tier or just hide the button in JS. 
    # The search UI generates buttons from unique categories in the data. If no item has Grand Master, the button won't appear.
    
    if new_content != content:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated courses-data.js")

# 2. Update navbar.js
nav_file = 'assets/js/navbar.js'
if os.path.exists(nav_file):
    with open(nav_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # In navbar.js there might be a dropdown section for Grand Master
    # Let's see if we can just comment out the block that has label: 'Grand Master'
    # Or just replace the label with 'Hidden' and maybe JS handles it.
    # Actually, simplest is to just comment the lines from { label: 'Grand Master' up to the closing },
    # Since it's a JS object in an array:
    # { label: 'Grand Master', courses: [ ... ] },
    pattern = re.compile(r'\{\s*label:\s*[\'"]Grand Master[\'"],[\s\S]*?\},(?=\s*\{|\])')
    new_content = re.sub(pattern, '/* Grand Master removed */\n', content)
    
    if new_content != content:
        with open(nav_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated navbar.js")
