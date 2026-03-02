import glob
import re

html_files = glob.glob('*.html')
pattern = re.compile(r'\s*<!-- TOP URGENCY MARQUEE -->\s*<div class="urgency-marquee-container">.*?</div>\s*</div>\s*', re.IGNORECASE | re.DOTALL)

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = pattern.findall(content)
    if len(matches) > 1 or (len(matches) == 1 and content.find('<!-- TOP URGENCY MARQUEE -->') < content.find('</header>') + 100):
        print(f"{fpath} has {len(matches)} marquees. Fix needed.")
        
        # Remove ALL marquees
        content = pattern.sub('', content)
        
        # Re-add exactly ONE marquee right before <footer>
        marquee_html = matches[0] if len(matches) > 0 else ''
        if '<footer>' in content and marquee_html:
            content = content.replace('<footer>', marquee_html.strip() + '\n\n  <footer>')
            
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {fpath}")

