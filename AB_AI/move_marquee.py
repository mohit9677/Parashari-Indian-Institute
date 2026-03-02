import os
import glob
import re

html_files = glob.glob('*.html')
updated_count = 0

marquee_pattern = re.compile(r'(\s*<!-- TOP URGENCY MARQUEE -->\s*<div class="urgency-marquee-container">[\s\S]*?</div>\s*</div>\s*)', re.IGNORECASE)
marquee_pattern_alt = re.compile(r'(\s*<!-- TOP URGENCY MARQUEE -->\s*<div class="urgency-marquee-container">.*?(?:</div>\s*){2})', re.IGNORECASE | re.DOTALL)


for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the marquee block
    match = marquee_pattern_alt.search(content)
    if match:
        marquee_html = match.group(0)
        
        # Remove it from its current position
        content = content.replace(marquee_html, '')
        
        # Strip trailing newlines from marquee html and prepare it for insertion
        marquee_cleaned = marquee_html.strip() + '\n\n'
        
        # Inject it right above <footer>
        if '<footer>' in content:
            content = content.replace('<footer>', marquee_cleaned + '  <footer>')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            print(f"Moved marquee to footer in: {file_path}")

print(f"Total files updated: {updated_count}")
