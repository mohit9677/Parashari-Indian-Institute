import os
import re

cwd = r"d:\ParashariTeam\AB_AI"

# 1. Update courses.html HTML & JS
courses_path = os.path.join(cwd, 'courses.html')
with open(courses_path, 'r', encoding='utf-8') as f:
    courses_html = f.read()

# Add Dropdown HTML next to category filter container
dropdown_html = """
      <!-- Mobile Category Dropdown -->
      <div class="mobile-category-dropdown">
        <select id="mobileCategorySelect" class="form-control" style="background: linear-gradient(135deg, #c8960c, #8b4513); color: #fff; font-weight: bold; border-radius: 50px; text-align: center;">
          <option value="all">All Courses</option>
          <option value="Crash Course">Crash Course</option>
          <option value="Diploma">Diploma</option>
          <option value="Bachelor">Bachelor</option>
          <option value="Master">Master</option>
          <option value="Grand Master">Grand Master</option>
        </select>
      </div>
"""
if "id=\"mobileCategorySelect\"" not in courses_html:
    # insert right after <div class="category-filter-container">...</div>
    pattern = re.compile(r'(<div class="category-filter-container".*?</div>)', re.DOTALL)
    courses_html = pattern.sub(r'\1' + '\n' + dropdown_html, courses_html)

# Add Dropdown JS logic at the end inside the FILTER LOGIC block
dropdown_js = """
      // Mobile Dropdown Logic
      const mobileSelect = document.getElementById('mobileCategorySelect');
      if (mobileSelect) {
        mobileSelect.addEventListener('change', function() {
          const filterValue = this.value;
          const grid = document.getElementById('courseGrid');
          
          if (filterValue === 'all') {
            grid.classList.add('all-courses-active');
          } else {
            grid.classList.remove('all-courses-active');
          }

          const shownIds = new Set();
          courseCards.forEach(card => {
            const cardCategory = card.getAttribute('data-category');
            const courseId = card.getAttribute('data-course-id');

            if (filterValue === 'all') {
              if (courseId && shownIds.has(courseId)) {
                card.classList.add('hidden');
              } else {
                card.classList.remove('hidden');
                if (courseId) shownIds.add(courseId);
              }
            } else if (filterValue === cardCategory) {
              card.classList.remove('hidden');
            } else {
              card.classList.add('hidden');
            }
          });
        });
      }
"""
if "Mobile Dropdown Logic" not in courses_html:
    courses_html = courses_html.replace("});\n      });\n    });", "});\n      });\n" + dropdown_js + "\n    });")

# Add CSS directly to courses.html <style> tag to hide/show dropdown
mobile_css = """
    .mobile-category-dropdown {
      display: none;
      margin: 10px auto 20px auto;
      width: 90%;
      max-width: 400px;
    }
    @media (max-width: 768px) {
      .category-filter-container {
        display: none !important;
      }
      .mobile-category-dropdown {
        display: block;
      }
    }
"""
if ".mobile-category-dropdown {" not in courses_html:
    courses_html = courses_html.replace("</style>", mobile_css + "\n  </style>")

with open(courses_path, 'w', encoding='utf-8') as f:
    f.write(courses_html)

# 2. Update navbar.css for mobile layout
navbar_path = os.path.join(cwd, 'assets/css/navbar.css')
with open(navbar_path, 'r', encoding='utf-8') as f:
    navbar_css = f.read()

# Replace the display:none on navbar-cta in mobile with proper layout
new_mobile_nav_css = """
  .hamburger {
    display: flex;
    order: -1;
  }

  .nav-menu {
    display: none;
  }

  .mobile-menu .nav-menu {
    display: flex;
    flex-direction: column;
    gap: 0;
  }

  .navbar-cta {
    display: flex !important;
    order: 2;
    margin-left: auto;
    gap: 8px;
  }

  .navbar-cta .btn {
    padding: 6px 12px;
    font-size: 0.75rem;
  }
  
  .mobile-menu .navbar-cta {
    display: none !important; /* Hide duplicate in mobile menu */
  }
"""
# Very aggressive replace of the whole block to be safe
if ".navbar-cta {" in navbar_css and "display: none;" in navbar_css:
    # Just append the override at the very end of the file, it's safer
    navbar_css += "\n/* MOBILE NAVBAR OVERRIDE */\n@media (max-width: 1150px) {\n" + new_mobile_nav_css + "\n}\n"
    with open(navbar_path, 'w', encoding='utf-8') as f:
        f.write(navbar_css)

# 3. Add to main.css: 100% Placement Button CSS & Learn-More button overlap fix
main_css_path = os.path.join(cwd, 'assets/css/main.css')
with open(main_css_path, 'r', encoding='utf-8') as f:
    main_css = f.read()

placement_css = """
/* 100% Placement Floating Button */
.floating-placement-btn {
  position: fixed;
  bottom: 20px;
  left: 20px;
  background: linear-gradient(135deg, #FFD700, #FFA500);
  color: #000;
  padding: 12px 20px;
  border-radius: 50px;
  font-weight: bold;
  font-size: 0.95rem;
  box-shadow: 0 5px 15px rgba(255, 165, 0, 0.4);
  z-index: 9999;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: transform 0.3s;
}
.floating-placement-btn:hover {
  transform: translateY(-3px) scale(1.05);
  color: #000 !important;
}

/* Learn-More Button Mobile Fix */
@media (max-width: 480px) {
  .floating-placement-btn {
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: max-content;
  }
  .floating-placement-btn:hover {
    transform: translateX(-50%) translateY(-3px) scale(1.05);
  }
  
  .grid-responsive .premium-gold-card .learn-more {
    transform: scale(0.75);
    transform-origin: center;
    margin-left: -20px;
  }
}
"""
if "floating-placement-btn" not in main_css:
    with open(main_css_path, 'a', encoding='utf-8') as f:
        f.write("\n" + placement_css)

# 4. Inject 100% Placement button into courses.html and index.html
html_files = ['courses.html', 'index.html']
placement_btn_html = '  <a href="courses.html" class="floating-placement-btn"><i class="fa-solid fa-briefcase"></i> 100% Placement Support</a>\n'

for html_file in html_files:
    filepath = os.path.join(cwd, html_file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "floating-placement-btn" not in content:
        if "</body>" in content:
            new_content = content.replace("</body>", placement_btn_html + "</body>")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        print(f"Added placement button to {html_file}")

print("Python fixes applied successfully.")
