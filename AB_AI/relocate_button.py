import re
with open('courses.html', 'r', encoding='utf-8') as f:
    courses_html = f.read()

# Remove the incorrectly placed button
upcoming_btn_str = '''      <div class="text-center mt-3 mb-2">
        <a href="upcoming-courses.html" style="text-decoration: none;">
          <button role="button" class="golden-button">
            <span class="golden-text">UpComing Courses</span>
          </button>
        </a>
      </div>
'''
courses_html = courses_html.replace(upcoming_btn_str, '')

# Find the real end of the courses grid
gemini_idx = courses_html.find('Gemini Jyotish')
if gemini_idx != -1:
    # "Gemini Jyotish" card ends after a series of </div>
    # The card structure is:
    # <div class="premium-gold-card" ...>
    #   ...
    #   <div class="card-body"> ... </div>
    # </div>
    # We find the </div> for card-body, then </div> for card, then </div> for grid-responsive grid-gap-2.
    card_footer = courses_html.find('class="course-footer"', gemini_idx)
    div_after_footer = courses_html.find('</div>', card_footer) # closes learn-more
    div_after_card_body = courses_html.find('</div>', div_after_footer + 1) # closes course-footer
    div_after_card = courses_html.find('</div>', div_after_card_body + 1) # closes card-body
    div_after_grid_item = courses_html.find('</div>', div_after_card + 1) # closes premium-gold-card
    grid_end = courses_html.find('</div>', div_after_grid_item + 1) # closes grid-responsive

    new_html = courses_html[:grid_end] + upcoming_btn_str + courses_html[grid_end:]
    
    with open('courses.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("courses.html Upcoming button relocated correctly.")
