import glob

html_files = glob.glob('*.html')

flags_html = """  <!-- CORNER SCROLLING FLAGS -->
  <div class="corner-ribbon-wrapper">
    <a href="register.html" class="corner-ribbon-link">
      <div class="corner-flags-marquee">
        <!-- Text repeated for seamless looping -->
        <div class="corner-flags-item">
          <span class="corner-flag-icon">🚩</span> REGISTER FAST 
        </div>
        <div class="corner-flags-item">
          <span class="corner-flag-icon">🚩</span> REGISTER FAST 
        </div>
        <div class="corner-flags-item">
          <span class="corner-flag-icon">🚩</span> REGISTER FAST 
        </div>
        <div class="corner-flags-item">
          <span class="corner-flag-icon">🚩</span> REGISTER FAST 
        </div>
        <div class="corner-flags-item">
          <span class="corner-flag-icon">🚩</span> REGISTER FAST 
        </div>
        <div class="corner-flags-item">
          <span class="corner-flag-icon">🚩</span> REGISTER FAST 
        </div>
      </div>
    </a>
  </div>
"""

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Let's insert it right before the closing body tag
    if 'corner-ribbon-wrapper' not in html:
        new_html = html.replace('</body>', flags_html + '\n</body>')
        if new_html != html:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_html)
            count += 1

print(f"Injected corner flags into {count} files.")
