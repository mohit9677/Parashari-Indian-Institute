import os
import re

cwd = r"d:\ParashariTeam\AB_AI"
navbar_css_path = os.path.join(cwd, 'assets/css/navbar.css')

# --- 1. Remove from navbar.css ---
with open(navbar_css_path, 'r', encoding='utf-8') as f:
    navbar_css = f.read()

# Pattern to match the exact injected CSS block
# The injection was:
# /* Ultra-Compact Mobile Navbar Overrides */
# ...
# }
css_pattern = re.compile(r'\n?/\* Ultra-Compact Mobile Navbar Overrides \*/.*?}\n}\n?', re.DOTALL)

new_navbar_css = css_pattern.sub('\n', navbar_css)
if new_navbar_css != navbar_css:
    with open(navbar_css_path, 'w', encoding='utf-8') as f:
        f.write(new_navbar_css)
    print("Reverted CSS from navbar.css")
else:
    print("CSS snippet not found in navbar.css")

# --- 2. Remove from HTML files ---
# Pattern to match the exact injected HTML block
html_pattern = re.compile(r'\n?  <!-- Mobile Ultra-Compact Navbar Buttons -->\s*<div class="mobile-navbar-actions">.*?</div>\s*</div>\n?', re.DOTALL)

for root, dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                new_content = html_pattern.sub('\n', content)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Reverted HTML in {file}")
            except Exception as e:
                print(f"Failed to process {file}: {e}")

print("Reversion complete.")
