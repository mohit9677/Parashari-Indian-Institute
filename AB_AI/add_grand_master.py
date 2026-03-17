import re

with open('AB_AI/courses.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new Grand Master card
new_gm_card = '''
        <div class="premium-gold-card" style="padding: 0 !important;" data-animate data-category="Grand Master" data-course-id="grand-master">
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
'''

# Remove all existing placeholder Grand Master cards using non-greedy multiline matching
# The cards are specifically the ones with `data-category="Grand Master"`
content = re.sub(
    r'<div class="premium-gold-card"[^>]*data-category="Grand Master".*?<div class="course-footer">.*?</div>\s*</div>\s*</div>',
    '',
    content,
    flags=re.DOTALL
)

# Insert it before the button for upcoming courses
insertion_point = content.find('      <div class="text-center mt-3 mb-2">')

if insertion_point != -1:
    # We want to insert just before the closing </div> of the grid
    # Let's find the closing div of the `#courseGrid`
    grid_end = content.rfind('</div>', 0, insertion_point)
    if grid_end != -1:
        content = content[:grid_end] + new_gm_card + content[grid_end:]
        print('Successfully inserted new card.')
    else:
        print('Could not find grid end.')
else:
    print('Could not find insertion marker.')

with open('AB_AI/courses.html', 'w', encoding='utf-8') as f:
    f.write(content)
