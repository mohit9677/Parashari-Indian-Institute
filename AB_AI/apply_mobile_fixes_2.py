import os

cwd = r"d:\ParashariTeam\AB_AI"

html_files = ['courses.html', 'index.html']
for filename in html_files:
    filepath = os.path.join(cwd, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    placement_btn = '  <a href="courses.html" class="floating-placement-btn"><i class="fa-solid fa-briefcase"></i> 100% Placement Support</a>\n'

    if "floating-placement-btn" not in content:
        if "</body>" in content:
            content = content.replace("</body>", placement_btn + "</body>")
            current_write = True
        elif "</html>" in content:
            content = content.replace("</html>", placement_btn + "</html>")
            current_write = True
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added placement button to {filename}")

# Fix courses.html category dropdown
filepath = os.path.join(cwd, 'courses.html')
with open(filepath, 'r', encoding='utf-8') as f:
    courses_html = f.read()

dropdown_html = """
      <!-- Mobile Category Dropdown -->
      <div class="mobile-category-dropdown">
        <select id="mobileCategorySelect" class="form-control" style="background: linear-gradient(135deg, #FFD700, #FFA500); color: #000; font-weight: bold; border-radius: 50px; text-align: center; font-size: 1rem;">
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
    tag_to_find = '<div class="category-filter-container">'
    if tag_to_find in courses_html:
        courses_html = courses_html.replace(tag_to_find, dropdown_html + "\n" + tag_to_find)
        print("Added dropdown HTML")

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
    replace_tag = "});\n      });\n    });"
    if replace_tag in courses_html:
        courses_html = courses_html.replace(replace_tag, "});\n      });\n" + dropdown_js + "\n    });")
        print("Added dropdown JS")

mobile_css = """
    .mobile-category-dropdown {
      display: none;
      margin: 10px auto 20px auto;
      width: 90%;
      max-width: 400px;
    }
    .mobile-category-dropdown select {
       padding: 12px 20px;
       border: 2px solid #D4AF37;
       box-shadow: 0 4px 15px rgba(212, 175, 55, 0.2);
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
    print("Added dropdown CSS")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(courses_html)

print("Done with fix script 2")
