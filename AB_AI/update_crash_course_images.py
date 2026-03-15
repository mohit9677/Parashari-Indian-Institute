import os
import re

updates = {
    "Financial Astrology (Artha)": "assets/images/Financial Astrology (Artha).png",
    "(Face Reading) Western Physiognomy": "assets/images/(Face Reading) Western Physiognomy (Character Analysis.png",
    "Lal Kitab Basics": "assets/images/Lal Kitab Basics.png",
    "Medical Astrology": "assets/images/Medical Astrology.png",
    "BNN Intensive": "assets/images/The BNN Intensive A 14-Day Mastery of Bhrigu Nandi Nadi.png",
    "Modern Career Astrology": "assets/images/Modern Career Astrology.png",
    "Business Numerology": "assets/images/Business Numerology.png",
    "Vedic Numerology": "assets/images/Vedic Numerology.png",
    "Nadi Jyotish": "assets/images/Nadi Jyotish.png",
    "Healing": "assets/images/Healing.png"
}

cwd = r'd:\\ParashariTeam\\AB_AI'

# Update courses-data.js
js_file = os.path.join(cwd, 'assets/js/courses-data.js')
if os.path.exists(js_file):
    with open(js_file, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    for title, img_path in updates.items():
        # Let's use re.sub with a function to avoid index shifting issues
        def repl(m):
            print(f"Replacing {m.group(2)} with {img_path} for JS Title: {title}")
            return m.group(1) + img_path + '"'
        
        # pattern: (title: "TITLE_TEXT".*?image:\s*")(OLD_IMG_PATH)"
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
        # pattern: ( <img src=" ) ( OLD_IMG ) ( " alt="[^"]*" class="card-image">\s*</div>\s*<div class="card-body">\s*<div class="card-header">\s*<div class="card-header-icon">.*?</div>\s*<h3 class="card-title">TITLE_TEXT )
        
        # We need something matching backwards. Or we simply find all blocks and replace the img part.
        blocks = re.split(r'(<div class="premium-gold-card")', html_content)
        # blocks will be a list where strings alternate between normal text and the delimiter
        # Let's iterate and if title is in the block, we regex replace the img src in that block
        
        for i in range(len(blocks)):
            if title in blocks[i] and 'class="card-title"' in blocks[i]:
                def repl_html(m):
                    print(f"Replacing {m.group(2)} with {img_path} for HTML Title: {title}")
                    return m.group(1) + img_path + '"'
                blocks[i] = re.sub(r'(<img src=")([^"]+)(")', repl_html, blocks[i], count=1)
                break
                
        html_content = ''.join(blocks)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("HTML updated.")

print("Done updating image references.")
