import os
import re

cwd = r"d:\ParashariTeam\AB_AI"

def revert_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove placement buttons
    content = re.sub(r'<a href="courses\.html" class="navbar-placement-btn">.*?</a>\s*', '', content)
    content = re.sub(r'<a href="courses\.html" class="floating-placement-btn">.*?</a>\s*', '', content)

    # 2. Remove mobile category dropdown block from courses.html
    # Finds <!-- Mobile Category Dropdown --> up to the next </div>
    content = re.sub(r'<!-- Mobile Category Dropdown -->\s*<div class="mobile-category-dropdown">.*?</div>\s*', '', content, flags=re.DOTALL)
    
    # Remove the JS Logic appended at the bottom
    content = re.sub(r'// Mobile Dropdown Logic.*?}\s*\}\);\s*\}\s*', '', content, flags=re.DOTALL)

    # Remove the CSS appended at the bottom
    content = re.sub(r'\.mobile-category-dropdown\s*\{.*?\}\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'\.mobile-category-dropdown select\s*\{.*?\}\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'@media \(max-width:\s*768px\)\s*\{\s*\.category-filter-container\s*\{\s*display:\s*none !important;\s*\}\s*\.mobile-category-dropdown\s*\{\s*display:\s*block;\s*\}\s*\}\s*', '', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

revert_html(os.path.join(cwd, 'courses.html'))
revert_html(os.path.join(cwd, 'index.html'))

# 3. Remove navbar.css OVERRIDE block
navbar_path = os.path.join(cwd, 'assets/css/navbar.css')
with open(navbar_path, 'r', encoding='utf-8') as f:
    nav_css = f.read()

# The pattern is /* MOBILE NAVBAR OVERRIDE */ followed by the @media query block.
# We added this twice potentially, but we'll remove it everywhere
nav_css = re.sub(r'/\* MOBILE NAVBAR OVERRIDE \*/\s*@media \(max-width: 1150px\) \{.*?\n\}\s*\n', '', nav_css, flags=re.DOTALL)

# Re-save
with open(navbar_path, 'w', encoding='utf-8') as f:
    f.write(nav_css)

# Also undo the learn-more button mobile fix from main.css if it exists
main_css_path = os.path.join(cwd, 'assets/css/main.css')
with open(main_css_path, 'r', encoding='utf-8') as f:
    main_css = f.read()

# The block started with /* Learn-More Button Mobile Fix */ up to the closing brace
main_css = re.sub(r'/\* Learn-More Button Mobile Fix \*/\s*@media \(max-width: 480px\) \{.*?\n\}\s*\n', '', main_css, flags=re.DOTALL)

with open(main_css_path, 'w', encoding='utf-8') as f:
    f.write(main_css)

print("Reverted all mobile UI additions.")
