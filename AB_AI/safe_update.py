import os

def update_courses_html():
    filepath = 'AB_AI/courses.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_gm_card = """        <div class="premium-gold-card" style="padding: 0 !important;" data-animate data-category="Grand Master" data-course-id="grand-master">
          <span class="discount-tag" data-discount="Premium Program"></span>
          <div class="card-image-container">
            <img src="assets/images/parashari-group-image.png" alt="Grand Master Program" class="card-image">
          </div>
          <div class="card-body">
            <div class="card-header">
              <div class="card-header-icon"><i class="fas fa-crown"></i></div>
              <h3 class="card-title">Grand Master Program</h3>
            </div>
            <p class="course-desc-text" style="min-height: auto;">An elite all-in-one mastery program including Vedic Astrology, Numerology, KP, Vastu, Palmistry, Tarot, and 6 Stairs. Elevate your consciousness and gain mastery.</p>
            <div class="course-desc-text" style="font-size: 0.85em; margin-bottom: 12px; color: #555; min-height: auto;">
               <strong>Duration:</strong> 48 Weeks (24 Weeks Live + 24 Weeks Recording Access) <br>
               <strong>Includes:</strong> Complete 6 Stairs Sciences (Yantra, Mantra, Tantra, Chakra Balancing, Remedies, PLRT)
            </div>
            <div class="mb-1">
              <span class="category-badge" style="background:#c8960c">Grand Master · Elite</span>
              <span class="certification-badge">✓ Lifetime Alumni Access</span>
            </div>
            <h4 class="color-secondary mb-1 text-center"><del
                style="color:#999;font-size:0.65em;margin-right:8px;vertical-align:middle;">₹34,999</del><strong
                style="color:#FFD700;font-size:1.1em;">₹24,999</strong></h4>
            <div class="course-footer">
              <a href="contact.html" class="learn-more">
                <span class="circle" aria-hidden="true">
                  <span class="icon arrow"></span>
                </span>
                <span class="button-text">Inquire Now</span>
              </a>
            </div>
          </div>
        </div>
"""

    out_lines = []
    in_gm_card = False
    div_depth = 0
    
    for i, line in enumerate(lines):
        if not in_gm_card:
            if '<div class="premium-gold-card"' in line and 'data-category="Grand Master"' in line:
                in_gm_card = True
                div_depth = line.count('<div') - line.count('</div')
                continue
            out_lines.append(line)
        else:
            div_depth += line.count('<div') - line.count('</div')
            if div_depth <= 0:
                in_gm_card = False
                
    # Now find the insertion point, which is just before: '      <div class="text-center mt-3 mb-2">'
    # We will search from the end
    insertion_idx = -1
    for i in range(len(out_lines)-1, -1, -1):
        if '<div class="text-center mt-3 mb-2">' in out_lines[i] or '<!-- Upcoming Courses Button -->' in out_lines[i] or '<a href="upcoming-courses.html"' in out_lines[i] or 'type="button" class="golden-button"' in out_lines[i]:
            insertion_idx = i
            break
            
    if insertion_idx != -1:
        # We need to insert just before the closing </div> of the #courseGrid
        # Let's walk backwards from insertion_idx to find the closing div
        for i in range(insertion_idx - 1, -1, -1):
            if '</div>' in out_lines[i]:
                out_lines.insert(i, new_gm_card)
                print("Successfully inserted new Grand Master card.")
                break
    else:
        print("Could not find insertion index. Looking for courseGrid closing tags...")
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)

if __name__ == '__main__':
    update_courses_html()
