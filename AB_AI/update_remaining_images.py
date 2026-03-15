import os
import shutil
import re

source_dir = r"D:\ParashariTeam"
target_dir = r"d:\ParashariTeam\AB_AI\assets\images"

images_to_copy = [
    "mobile numerology.png",
    "gemini jyotishi.png",
    "feng-shui-astrology.jpg"
]

os.makedirs(target_dir, exist_ok=True)

for img in images_to_copy:
    src_path = os.path.join(source_dir, img)
    dst_path = os.path.join(target_dir, img)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Copied {img}")
    else:
        print(f"Skipped {img} - File not found")

updates = {
    "Mobile Numerology": "assets/images/mobile numerology.png",
    "Feng Shui": "assets/images/feng-shui-astrology.jpg",
    "Gemini Jyotish": "assets/images/gemini jyotishi.png"
}

cwd = r'd:\ParashariTeam\AB_AI'

# Update courses-data.js
js_file = os.path.join(cwd, 'assets/js/courses-data.js')
if os.path.exists(js_file):
    with open(js_file, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    for title, img_path in updates.items():
        if title == "Gemini Jyotish":
            continue # Not in courses-data.js
        def repl(m):
            print(f"Replacing {m.group(2)} with {img_path} for JS Title: {title}")
            return m.group(1) + img_path + '"'
        
        pattern = re.compile(r'(title:\s*"[^"]*' + re.escape(title) + r'[^"]*".*?image:\s*")([^"]+)(")', re.DOTALL)
        js_content = pattern.sub(repl, js_content, count=1)

    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("JS updated.")

# Update courses.html
html_file = os.path.join(cwd, 'courses.html')
if os.path.exists(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    for title, img_path in updates.items():
        blocks = re.split(r'(<div)', html_content)
        # We need to recombine blocks because split strips the delimiter, but wait, the group(1) returns the delimiter.
        # Actually it's easier to iterate lines or search. But HTML is multiline.
        # Let's do something simpler: find <h3 class="card-title">TITLE_TEXT</h3>
        # and replace the nearest preceding <img src="..."> in courses.html.
        
        # Let's use a robust approach for courses.html
        html_blocks = re.split(r'(<div class="premium-gold-card"|<div class="card")', html_content)
        for i in range(len(html_blocks)):
            if title in html_blocks[i] and 'class="card-title"' in html_blocks[i]:
                def repl_html(m):
                    print(f"Replacing {m.group(2)} with {img_path} for HTML Title: {title}")
                    return m.group(1) + img_path + '"'
                html_blocks[i] = re.sub(r'(<img src=")([^"]+)(")', repl_html, html_blocks[i], count=1)
                
        html_content = ''.join(html_blocks)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("HTML updated.")

print("Done updating image references.")
