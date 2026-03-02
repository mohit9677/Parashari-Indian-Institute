import os
import glob
import re

html_files = glob.glob('*.html')

# 1. CSS Link String
CSS_LINK = '  <link rel="stylesheet" href="assets/css/urgency.css">\n'

# 2. Marquee HTML (placed immediately after <body> tag)
MARQUEE_HTML = """
  <!-- TOP URGENCY MARQUEE -->
  <div class="urgency-marquee-container">
    <div class="urgency-marquee-content">
      <div class="marquee-item">
        <span class="marquee-icon">🎓</span> Admissions Open! Register Now for Upcoming Batches — Limited Seats Available! 
        <a href="register.html" class="marquee-btn">Fast Register</a>
      </div>
      <div class="marquee-item">
        <span class="marquee-icon">🔥</span> Fast Track Your Career with 100% Placement Assistance 
        <a href="courses.html" class="marquee-btn">View Courses</a>
      </div>
      <div class="marquee-item">
        <span class="marquee-icon">⭐</span> Join Parashari Institute Today — Scholarship Available for Top Performers! 
        <a href="register.html" class="marquee-btn">Apply Now</a>
      </div>
      <!-- Duplicate for seamless scrolling -->
      <div class="marquee-item">
        <span class="marquee-icon">🎓</span> Admissions Open! Register Now for Upcoming Batches — Limited Seats Available! 
        <a href="register.html" class="marquee-btn">Fast Register</a>
      </div>
      <div class="marquee-item">
        <span class="marquee-icon">🔥</span> Fast Track Your Career with 100% Placement Assistance 
        <a href="courses.html" class="marquee-btn">View Courses</a>
      </div>
      <div class="marquee-item">
        <span class="marquee-icon">⭐</span> Join Parashari Institute Today — Scholarship Available for Top Performers! 
        <a href="register.html" class="marquee-btn">Apply Now</a>
      </div>
    </div>
  </div>
"""

# 3. Sticky Badge HTML (placed just before </body> tag)
BADGE_HTML = """
  <!-- STICKY PLACEMENT BADGE -->
  <a href="courses.html" style="text-decoration: none;">
    <div class="placement-badge-container">
      <div class="placement-badge">
        <div class="badge-icon">🌟</div>
        <div class="badge-text">
          <span class="badge-title">100% Placement</span>
          <span class="badge-subtitle">Guaranteed Assistance</span>
        </div>
      </div>
    </div>
  </a>
"""

updated_count = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False

    # Inject CSS Link inside <head> if not exists
    if 'urgency.css' not in content:
        content = content.replace('</head>', CSS_LINK + '</head>')
        modified = True
        
    # Inject Marquee right after <body> if not exists
    if 'urgency-marquee-container' not in content:
        # Some bodies might have attributes, so we use regex
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + MARQUEE_HTML, content, count=1)
        modified = True
        
    # Inject Sticky Badge right before </body> if not exists
    if 'placement-badge-container' not in content:
        content = content.replace('</body>', BADGE_HTML + '\n</body>')
        modified = True

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1
        print(f"Updated: {file_path}")

print(f"Total files injected: {updated_count}")
