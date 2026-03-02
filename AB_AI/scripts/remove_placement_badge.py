import glob
import re

html_files = glob.glob('*.html')

badge_html = """  <!-- STICKY PLACEMENT BADGE -->
  <a href="courses.html" style="text-decoration: none;">
    <div class="placement-badge-container">
      <div class="placement-badge">
        <div class="badge-icon">🌟</div>
        <div class="badge-text">
          <span class="badge-title">100% Placement</span>
          <span class="badge-subtitle">Guaranteed Assistance</span>
        </div>
      </div>
    </div>
  </a>"""
  
badge_html_with_n = badge_html
badge_html_with_rn = badge_html.replace('\n', '\r\n')

# For cases where regex is better
pattern = r'<!-- STICKY PLACEMENT BADGE -->\s*<a href="courses\.html" style="text-decoration: none;">\s*<div class="placement-badge-container">.*?</a>'

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    # Try exact match first
    html = html.replace(badge_html_with_n, '')
    html = html.replace(badge_html_with_rn, '')
    
    # Try regex if exact match failed (because of formatting)
    html = re.sub(pattern, '', html, flags=re.DOTALL)
    
    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f"Successfully stripped placement badge from {count} files.")
