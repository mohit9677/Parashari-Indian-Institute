import codecs

courses = [
    {"Title": "Vedic Astrology", "Image": "vedic-astrology-new.jpg", "Icon": "♈", "Link": "astrology.html", "Price": "₹2,999", "OldPrice": "₹7,999", "Discount": "63%", "Cat": "Crash Course", "Level": "Beginner", "CatColor": "#4CAF50"},
    {"Title": "Nadi Jyotish", "Image": "taurus-card.png", "Icon": "📜", "Link": "nadi-jyotish.html", "Price": "₹2,999", "OldPrice": "₹7,999", "Discount": "63%", "Cat": "Crash Course", "Level": "Beginner", "CatColor": "#4CAF50"},
    {"Title": "Lal Kitab", "Image": "lal-kitab-new.jpg", "Icon": "📕", "Link": "lal-kitab.html", "Price": "₹4,999", "OldPrice": "₹10,000", "Discount": "50%", "Cat": "Diploma", "Level": "Popular", "CatColor": "#2196F3"},
    {"Title": "Remedy Course", "Image": "cancer-card.png", "Icon": "🕉️", "Link": "remedy-course.html", "Price": "₹19,999", "OldPrice": "₹30,000", "Discount": "33%", "Cat": "Master", "Level": "Advanced", "CatColor": "#FF9800"}
]

index_grid_html = ""
for c in courses:
    index_grid_html += f'''        <div class="premium-gold-card" style="padding: 0 !important;" data-animate data-category="{c['Cat']}">
          <span class="discount-tag" data-discount="{c['Discount']} Discount"></span>
          <div class="card-image-container">
            <img src="assets/images/{c['Image']}" alt="{c['Title']}" class="card-image">
          </div>
          <div class="card-body">
            <div class="card-header">
              <div class="card-header-icon">{c['Icon']}</div>
              <h3 class="card-title">{c['Title']}</h3>
            </div>
            <p>Enroll in the {c['Title']} program to master the concepts and gain deep insights.</p>
            <div class="mb-1">
              <span class="category-badge" style="background:{c['CatColor']}">{c['Cat']} · {c['Level']}</span>
              <span class="certification-badge">✓ Certification</span>
            </div>
            <h4 class="color-secondary mb-1 text-center"><del
                style="color:#999;font-size:0.65em;margin-right:8px;vertical-align:middle;">{c['OldPrice']}</del><strong
                style="color:#FFD700;font-size:1.1em;">{c['Price']}</strong></h4>
            <div class="course-footer">
              <a href="{c['Link']}" class="learn-more">
                <span class="circle" aria-hidden="true">
                  <span class="icon arrow">
                  </span>
                </span>
                <span class="button-text">Learn More</span>
              </a>
            </div>
          </div>
        </div>\n'''

with codecs.open('index.html', 'r', 'utf-8') as f:
    index_html = f.read()

index_start = index_html.find('<h2 class="card-section-title">Our Courses</h2>')
grid_div_start = index_html.find('<div class="grid-responsive grid-gap-2">', index_start)
if grid_div_start != -1:
    index_grid_start = grid_div_start + len('<div class="grid-responsive grid-gap-2">')
    
    last_course_idx = index_html.find('Master the concepts in the Remedy Course program', index_grid_start)
    if last_course_idx != -1:
        footer_idx = index_html.find('class="course-footer"', last_course_idx)
        div1 = index_html.find('</div>', footer_idx) + 6
        div2 = index_html.find('</div>', div1) + 6
        index_grid_end = index_html.find('</div>', div2)

        if index_grid_end != -1:
            new_index_html = index_html[:index_grid_start] + '\n' + index_grid_html + '      ' + index_html[index_grid_end:]
            with codecs.open('index.html', 'w', 'utf-8') as f:
                f.write(new_index_html)
            print("index.html cards matched to courses.html successfully.")
        else:
            print("Failed to find grid end.")
    else:
        print("Failed to find last course.")
else:
    print("Failed to find grid start.")
