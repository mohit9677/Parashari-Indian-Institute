import glob
import re

html_files = glob.glob('*.html')

new_tokens_html = """  <!-- FLYING REGISTER TOKENS -->
  <div class="floating-tokens-container">
    <a href="register.html" class="floating-token token-1">REGISTER NOW</a>
    <a href="register.html" class="floating-token token-2">REGISTER NOW</a>
    <a href="register.html" class="floating-token token-3">REGISTER NOW</a>
  </div>"""

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if 'CORNER SCROLLING FLAGS' in html:
        new_html = re.sub(r'  <!-- CORNER SCROLLING FLAGS -->.*?</div>(?=\s*</body>)', new_tokens_html, html, flags=re.DOTALL)
        
        if new_html != html:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_html)
            count += 1

print(f"Injected floating tokens into {count} files.")
