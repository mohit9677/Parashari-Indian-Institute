import re
import os

courses = [
    {"Title": "Vedic Astrology", "Image": "vedic-astrology-new.jpg", "Icon": "♈", "Link": "astrology.html", "Price": "₹2,999", "OldPrice": "₹7,999", "Discount": "63%", "Cat": "Crash Course", "Level": "Beginner", "CatColor": "#4CAF50"},
    {"Title": "Numerology", "Image": "numerology-new.jpg", "Icon": "🔢", "Link": "numerology.html", "Price": "₹9,999", "OldPrice": "₹17,000", "Discount": "41%", "Cat": "Bachelor", "Level": "Pro", "CatColor": "#9C27B0"},
    {"Title": "KP Astrology", "Image": "kp-astrology-new.jpg", "Icon": "⭐", "Link": "kp-astrology.html", "Price": "₹9,999", "OldPrice": "₹17,000", "Discount": "41%", "Cat": "Bachelor", "Level": "Pro", "CatColor": "#9C27B0"},
    {"Title": "Gemstone Science", "Image": "gemstone.jpg", "Icon": "💎", "Link": "gemstone.html", "Price": "₹4,999", "OldPrice": "₹10,000", "Discount": "50%", "Cat": "Diploma", "Level": "Popular", "CatColor": "#2196F3"},
    {"Title": "Vastu Shastra", "Image": "vastu-new.jpg", "Icon": "🏠", "Link": "vastu.html", "Price": "₹9,999", "OldPrice": "₹17,000", "Discount": "41%", "Cat": "Bachelor", "Level": "Pro", "CatColor": "#9C27B0"},
    {"Title": "Lal Kitab", "Image": "lal-kitab-new.jpg", "Icon": "📕", "Link": "lal-kitab.html", "Price": "₹4,999", "OldPrice": "₹10,000", "Discount": "50%", "Cat": "Diploma", "Level": "Popular", "CatColor": "#2196F3"},
    {"Title": "Face Reading", "Image": "face-reading-new.jpg", "Icon": "👤", "Link": "face-reading.html", "Price": "₹19,999", "OldPrice": "₹30,000", "Discount": "33%", "Cat": "Master", "Level": "Advanced", "CatColor": "#FF9800"},
    {"Title": "Reiki Healing", "Image": "healing.jpg", "Icon": "🙌", "Link": "reiki.html", "Price": "₹4,999", "OldPrice": "₹10,000", "Discount": "50%", "Cat": "Diploma", "Level": "Popular", "CatColor": "#2196F3"},
    {"Title": "Tarot Reading", "Image": "tarot-new.jpg", "Icon": "🃏", "Link": "tarot.html", "Price": "₹4,999", "OldPrice": "₹10,000", "Discount": "50%", "Cat": "Diploma", "Level": "Popular", "CatColor": "#2196F3"},
    {"Title": "Nakshatra", "Image": "gold_zodiac_wheel.png", "Icon": "✨", "Link": "nakshatra.html", "Price": "₹9,999", "OldPrice": "₹17,000", "Discount": "41%", "Cat": "Bachelor", "Level": "Pro", "CatColor": "#9C27B0"},
    {"Title": "Crystal", "Image": "crystal-healing-new.jpg", "Icon": "🔮", "Link": "crystal-healing.html", "Price": "₹4,999", "OldPrice": "₹10,000", "Discount": "50%", "Cat": "Diploma", "Level": "Popular", "CatColor": "#2196F3"},
    {"Title": "Rudraksha", "Image": "rudraksha-new.jpg", "Icon": "📿", "Link": "rudraksha.html", "Price": "₹39,999", "OldPrice": "₹50,000", "Discount": "20%", "Cat": "Grand Master", "Level": "Elite", "CatColor": "#c8960c"},
    {"Title": "Palmistry", "Image": "palmistry-new.jpg", "Icon": "✋", "Link": "palmistry.html", "Price": "₹2,999", "OldPrice": "₹7,999", "Discount": "63%", "Cat": "Crash Course", "Level": "Beginner", "CatColor": "#4CAF50"},
    {"Title": "Nadi Jyotish", "Image": "taurus-card.png", "Icon": "📜", "Link": "nadi-jyotish.html", "Price": "₹2,999", "OldPrice": "₹7,999", "Discount": "63%", "Cat": "Crash Course", "Level": "Beginner", "CatColor": "#4CAF50"},
    {"Title": "Remedy Course", "Image": "cancer-card.png", "Icon": "🕉️", "Link": "remedy-course.html", "Price": "₹19,999", "OldPrice": "₹30,000", "Discount": "33%", "Cat": "Master", "Level": "Advanced", "CatColor": "#FF9800"},
    {"Title": "Medical Astrology", "Image": "scorpio-card.png", "Icon": "⚕️", "Link": "medical-astrology.html", "Price": "₹19,999", "OldPrice": "₹30,000", "Discount": "33%", "Cat": "Master", "Level": "Advanced", "CatColor": "#FF9800"},
    {"Title": "BNN Advance", "Image": "virgo-card.jpg", "Icon": "🔍", "Link": "bnn-astrology.html", "Price": "₹39,999", "OldPrice": "₹50,000", "Discount": "20%", "Cat": "Grand Master", "Level": "Elite", "CatColor": "#c8960c"},
    {"Title": "Healing", "Image": "chakra-balancing.jpg", "Icon": "💆", "Link": "healing.html", "Price": "₹19,999", "OldPrice": "₹30,000", "Discount": "33%", "Cat": "Master", "Level": "Advanced", "CatColor": "#FF9800"},
    {"Title": "Feng Shui", "Image": "institute-building-modern.jpg", "Icon": "⛩️", "Link": "feng-shui.html", "Price": "₹9,999", "OldPrice": "₹17,000", "Discount": "41%", "Cat": "Bachelor", "Level": "Pro", "CatColor": "#9C27B0"},
    {"Title": "Past Life Prediction", "Image": "past-life.jpg", "Icon": "🕰️", "Link": "plrt.html", "Price": "₹39,999", "OldPrice": "₹50,000", "Discount": "20%", "Cat": "Grand Master", "Level": "Elite", "CatColor": "#c8960c"},
    {"Title": "Gemini Jyotish", "Image": "gemini-card.png", "Icon": "♊", "Link": "gemini-jyotish.html", "Price": "₹19,999", "OldPrice": "₹30,000", "Discount": "33%", "Cat": "Master", "Level": "Advanced", "CatColor": "#FF9800"}
]

index_courses = courses[:4]

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

index_grid_html = ""
for c in index_courses:
    index_grid_html += f'''        <div class="card" data-animate>
          <span class="discount-tag" data-discount="{c['Discount']} Discount"></span>
          <div class="card-image-container">
            <img src="assets/images/{c['Image']}" alt="{c['Title']}" class="card-image">
            <div class="card-image-overlay"></div>
          </div>
          <div class="card-body">
            <div class="card-header">
              <div class="card-header-icon">{c['Icon']}</div>
              <h3 class="card-title">{c['Title']}</h3>
            </div>
            <p>Master the concepts in the {c['Title']} program and gain deep insights.</p>
            <div class="course-footer">
              <h4 class="color-secondary mb-0"><del
                  style="color:#999;font-size:0.65em;margin-right:8px;vertical-align:middle;">{c['OldPrice']}</del><strong
                  style="color:#d32f2f;font-size:1.1em;">{c['Price']}</strong> <span class="discount-text">(with {c['Discount']}
                  discount)</span></h4>
              <a href="{c['Link']}" class="learn-more">
                <span class="circle" aria-hidden="true">
                  <span class="icon arrow"></span>
                </span>
                <span class="button-text">Learn More</span>
              </a>
            </div>
          </div>
        </div>\n'''

index_start = index_html.find('<h2 class="card-section-title">Our Courses</h2>')
grid_div_start = index_html.find('<div class="grid-responsive grid-gap-2">', index_start)
if grid_div_start != -1:
    index_grid_start = grid_div_start + len('<div class="grid-responsive grid-gap-2">')
    
    # Try multiple ways to find the end of the grid
    index_grid_end = index_html.find('</div>\n    </div>\n\n    <div class="text-center mt-2">', index_grid_start)
    if index_grid_end == -1: index_grid_end = index_html.find('</div>\\n    </div>\\n    <div class="text-center mt-2">', index_grid_start)
    if index_grid_end == -1: 
        last_course_idx = index_html.find('Master the concepts in the Gemini Jyotish', index_grid_start)
        if last_course_idx != -1:
            # find the div right after the course-footer
            footer_idx = index_html.find('class="course-footer"', last_course_idx)
            div1 = index_html.find('</div>', footer_idx) + 6
            div2 = index_html.find('</div>', div1) + 6
            index_grid_end = index_html.find('</div>', div2)

    if index_grid_end != -1:
        new_index_html = index_html[:index_grid_start] + '\n' + index_grid_html + '      ' + index_html[index_grid_end:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_index_html)
        print("index.html 4-item grid updated successfully.")


# 1. Update courses.html to restore button
with open('courses.html', 'r', encoding='utf-8') as f:
    courses_html = f.read()

upcoming_btn_str = '''      <div class="text-center mt-3 mb-2">
        <a href="upcoming-courses.html" style="text-decoration: none;">
          <button role="button" class="golden-button">
            <span class="golden-text">UpComing Courses</span>
          </button>
        </a>
      </div>
'''

if 'UpComing Courses' not in courses_html:
    gemini_idx = courses_html.find('Gemini Jyotish')
    if gemini_idx != -1:
        grid_end_idx = courses_html.find('</div>\n    </div>\n  </section>', gemini_idx)
        if grid_end_idx == -1:
          grid_end_idx = courses_html.find('</section>', gemini_idx)
          container_end = courses_html.rfind('</div>', 0, grid_end_idx)

          new_courses_html = courses_html[:container_end] + upcoming_btn_str + courses_html[container_end:]
        else:
          new_courses_html = courses_html[:grid_end_idx] + upcoming_btn_str + courses_html[grid_end_idx:]

        with open('courses.html', 'w', encoding='utf-8') as f:
            f.write(new_courses_html)
        print("courses.html button restored.")
    else:
        print("Could not find Gemini Jyotish in courses.html")
else:
    print("UpComing Courses button already exists in courses.html")
