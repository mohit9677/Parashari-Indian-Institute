import os
import re

cwd = r"d:\ParashariTeam\AB_AI"

# 1. Remove the old floating placement button from HTML headers
html_files = ['courses.html', 'index.html']

for filename in html_files:
    filepath = os.path.join(cwd, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove floating button if exists
    content = content.replace('  <a href="courses.html" class="floating-placement-btn"><i class="fa-solid fa-briefcase"></i> 100% Placement Support</a>\n', '')
    content = content.replace('<a href="courses.html" class="floating-placement-btn"><i class="fa-solid fa-briefcase"></i> 100% Placement Support</a>', '')

    # Insert into navbar
    placement_nav_btn = '      <a href="courses.html" class="navbar-placement-btn"><i class="fa-solid fa-briefcase"></i> <span class="full-text">100% Placement</span></a>\n'
    if "navbar-placement-btn" not in content:
        # insert right before the hamburger button
        content = content.replace('<button class="hamburger"', placement_nav_btn + '      <button class="hamburger"')
        print(f"Injected navbar placement button into {filename}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Update navbar CSS
navbar_path = os.path.join(cwd, 'assets/css/navbar.css')
with open(navbar_path, 'r', encoding='utf-8') as f:
    navbar_css = f.read()

# Replace the previous mobile override completely
pattern = re.compile(r'/\* MOBILE NAVBAR OVERRIDE \*/.*?}(?=\n*$|\n*/\*|)', re.DOTALL)
new_mobile_css = """/* MOBILE NAVBAR OVERRIDE */
@media (max-width: 1150px) {

  .navbar {
    padding: 10px 15px !important;
    display: flex;
    flex-wrap: nowrap !important;
    align-items: center;
    justify-content: space-between;
    min-height: 60px; /* Keep height constrained */
  }

  .hamburger {
    display: flex;
    order: -1; /* Far left */
    margin: 0;
  }

  .nav-menu {
    display: none;
  }

  .mobile-menu .nav-menu {
    display: flex;
    flex-direction: column;
    gap: 0;
  }

  .navbar-placement-btn {
    display: flex;
    order: 1; /* Middle */
    align-items: center;
    justify-content: center;
    font-size: 0.75rem;
    font-weight: bold;
    color: #000 !important;
    background: linear-gradient(135deg, #FFD700, #FFA500);
    padding: 5px 10px;
    border-radius: 5px;
    text-decoration: none;
    white-space: nowrap;
    margin: 0 5px;
    box-shadow: 0 2px 8px rgba(255, 165, 0, 0.4);
  }
  .navbar-placement-btn i {
    margin-right: 4px;
  }
  @media (max-width: 480px) {
     .navbar-placement-btn {
        font-size: 0.65rem;
        padding: 4px 6px;
     }
  }

  .navbar-cta {
    display: flex !important;
    order: 2; /* Far right */
    margin: 0;
    gap: 4px;
    align-items: center;
  }

  .navbar-cta .btn {
    padding: 5px 8px;
    font-size: 0.70rem;
    white-space: nowrap;
    line-height: 1;
    min-height: unset;
  }
  
  .mobile-menu .navbar-cta {
    display: none !important; /* Hide duplicate in mobile menu */
  }

}
"""

if "/* MOBILE NAVBAR OVERRIDE */" in navbar_css:
    navbar_css = pattern.sub(new_mobile_css, navbar_css)
else:
    navbar_css += "\n" + new_mobile_css

with open(navbar_path, 'w', encoding='utf-8') as f:
    f.write(navbar_css)
print("Updated navbar CSS.")

# Remove the `.floating-placement-btn` css from main.css just to clean up
main_css_path = os.path.join(cwd, 'assets/css/main.css')
with open(main_css_path, 'r', encoding='utf-8') as f:
    main_css = f.read()

# simple removal of floating placement css block
pattern_main = re.compile(r'/\* 100% Placement Floating Button \*/.*?}(?=\n\n|\n/\*|$)', re.DOTALL)
main_css = pattern_main.sub('', main_css)
with open(main_css_path, 'w', encoding='utf-8') as f:
    f.write(main_css)

print("Removed floating button CSS.")
