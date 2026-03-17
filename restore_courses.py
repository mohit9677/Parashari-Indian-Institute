import re

with open('AB_AI/courses.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix hidden visibility
content = content.replace(
    '<div class="premium-gold-card" style="display: none !important; padding: 0 !important;" data-animate data-category="Grand Master"',
    '<div class="premium-gold-card" style="padding: 0 !important;" data-animate data-category="Grand Master"'
)

# Update Javascript query selector logic
old_logic = '''            if (filterValue === 'all') {
              // De-duplication logic for "All Courses"
              if (courseId && shownIds.has(courseId)) {
                card.classList.add('hidden');
              } else {
                card.classList.remove('hidden');
                if (courseId) shownIds.add(courseId);
              }
            }'''
new_logic = '''            if (filterValue === 'all') {
              // Hide Grand Master cards from All Courses view
              if (cardCategory === 'Grand Master') {
                card.classList.add('hidden');
              } else {
                // De-duplication logic for "All Courses"
                if (courseId && shownIds.has(courseId)) {
                  card.classList.add('hidden');
                } else {
                  card.classList.remove('hidden');
                  if (courseId) shownIds.add(courseId);
                }
              }
            }'''
content = content.replace(old_logic, new_logic)

old_logic_mob = '''            if (filterValue === 'all') {
              if (courseId && shownIds.has(courseId)) {
                card.classList.add('hidden');
              } else {
                card.classList.remove('hidden');
                if (courseId) shownIds.add(courseId);
              }
            }'''
new_logic_mob = '''            if (filterValue === 'all') {
              if (cardCategory === 'Grand Master') {
                card.classList.add('hidden');
              } else {
                if (courseId && shownIds.has(courseId)) {
                  card.classList.add('hidden');
                } else {
                  card.classList.remove('hidden');
                  if (courseId) shownIds.add(courseId);
                }
              }
            }'''
content = content.replace(old_logic_mob, new_logic_mob)

# Add URL parameter check
url_check = '''          });
        });
      }

      // Handle URL parameters for category selection
      const urlParams = new URLSearchParams(window.location.search);
      const categoryParam = urlParams.get('category');
      if (categoryParam) {
        // Try desktop tab
        const targetTab = document.querySelector(`.filter-tab[data-filter="${categoryParam}"]`);
        if (targetTab) {
          targetTab.click();
        } else {
          // Try mobile dropdown
          const mobileSelect = document.getElementById('mobileCategorySelect');
          if (mobileSelect) {
            mobileSelect.value = categoryParam;
            mobileSelect.dispatchEvent(new Event('change'));
          }
        }
      }
    });'''
content = content.replace('''          });
        });
      }
    });''', url_check)
    
# Fast Register
content = content.replace(
'''      <img src="" id="qvImage" class="qv-image" alt="Course Image">
      <div class="qv-body">
        <h3 id="qvTitle" class="qv-title">Course Title</h3>
        <p id="qvDesc" class="qv-desc">Course Description</p>''',
'''      <div class="qv-body">
        <p id="qvDesc" class="qv-desc">Course Description</p>''')
        
content = content.replace("qvEnrollBtn.href = btn.getAttribute('href');", 'qvEnrollBtn.href = "register.html";')

with open('AB_AI/courses.html', 'w', encoding='utf-8') as f:
    f.write(content)
