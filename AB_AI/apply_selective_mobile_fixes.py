import os
import re

cwd = r"d:\ParashariTeam\AB_AI"
courses_path = os.path.join(cwd, 'courses.html')
main_css_path = os.path.join(cwd, 'assets/css/main.css')

# --- 1. Fix the Learn More Button Overlap in main.css ---
with open(main_css_path, 'r', encoding='utf-8') as f:
    main_css = f.read()

learn_more_fix = """
/* Learn-More Button Mobile Fix */
@media (max-width: 480px) {
  .premium-gold-card .learn-more {
    transform: scale(0.75);
    transform-origin: left center;
    margin-right: -25px; /* Offset the scaling visually if needed */
  }
}
"""

if "/* Learn-More Button Mobile Fix */" not in main_css:
    main_css += "\n" + learn_more_fix
    with open(main_css_path, 'w', encoding='utf-8') as f:
        f.write(main_css)
    print("Injected Learn More button CSS fix into main.css")
else:
    print("Learn More button CSS fix already exists in main.css")


# --- 2. Inject Mobile Category Dropdown into courses.html ---
with open(courses_path, 'r', encoding='utf-8') as f:
    courses_html = f.read()

dropdown_html = """
      <!-- Mobile Category Dropdown -->
      <div class="mobile-category-dropdown">
        <select id="mobileCategorySelect" class="form-control" style="background: linear-gradient(135deg, #c8960c, #8b4513); color: #fff; font-weight: bold; border-radius: 50px; text-align: center; font-size: 1rem; padding: 12px; width: 100%; border: 2px solid #e0d5c8; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);">
          <option value="all">All Courses</option>
          <option value="Crash Course">Crash Course</option>
          <option value="Diploma">Diploma</option>
          <option value="Bachelor">Bachelor</option>
          <option value="Master">Master</option>
        </select>
      </div>
"""

# Insert the dropdown above the category-filter-container
if "<!-- Mobile Category Dropdown -->" not in courses_html:
    courses_html = courses_html.replace(
        '<!-- Category Filter -->',
        dropdown_html + '\n      <!-- Category Filter -->'
    )
    print("Injected Mobile Category Dropdown HTML into courses.html")

dropdown_css = """
/* Mobile Dropdown CSS */
.mobile-category-dropdown { display: none; margin-bottom: 20px; }
@media (max-width: 768px) {
  .category-filter-container { display: none !important; }
  .mobile-category-dropdown { display: block; }
}
"""

if "/* Mobile Dropdown CSS */" not in courses_html:
    # Insert css right before closing </head>
    courses_html = courses_html.replace('</head>', f'<style>{dropdown_css}</style>\n</head>')
    print("Injected Mobile Dropdown CSS into courses.html")

dropdown_js = """
    // Mobile Dropdown Logic
    const mobileSelect = document.getElementById('mobileCategorySelect');
    if(mobileSelect) {
      mobileSelect.addEventListener('change', function() {
        const selectedFilter = this.value;
        // Trigger the existing tab logic
        const targetTab = document.querySelector(`.filter-tab[data-filter="${selectedFilter}"]`);
        if (targetTab) {
          targetTab.click();
        }
      });
    }
"""

if "// Mobile Dropdown Logic" not in courses_html:
    # Insert js right before closing </body>
    courses_html = courses_html.replace('</body>', f'<script>{dropdown_js}</script>\n</body>')
    print("Injected Mobile Dropdown JS into courses.html")

with open(courses_path, 'w', encoding='utf-8') as f:
    f.write(courses_html)

print("Selective mobile fixes applied successfully.")
