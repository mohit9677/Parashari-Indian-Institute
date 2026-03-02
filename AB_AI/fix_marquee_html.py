import glob
import re

MARQUEE_HTML = """  <!-- TOP URGENCY MARQUEE -->
  <div class="urgency-marquee-container">
    <div class="urgency-marquee-content">
      <div class="marquee-item">
        <span class="marquee-icon">🎓</span> Admissions Open! Register Now for Upcoming Batches — Limited Seats Available! <div class="marquee-timer timer-pulse">Ends in: <span class="marquee-timer-val">47:59:59</span></div> <a href="register.html" class="marquee-btn">Fast Register</a>
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
        <span class="marquee-icon">🎓</span> Admissions Open! Register Now for Upcoming Batches — Limited Seats Available! <div class="marquee-timer timer-pulse">Ends in: <span class="marquee-timer-val">47:59:59</span></div> <a href="register.html" class="marquee-btn">Fast Register</a>
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
  </div>"""

broken_pattern = re.compile(r'\s*<!-- TOP URGENCY MARQUEE -->.*?(?=<footer>)', re.IGNORECASE | re.DOTALL)

html_files = glob.glob('*.html')
count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace broken block
    if broken_pattern.search(content):
        content = broken_pattern.sub('\n\n' + MARQUEE_HTML + '\n\n  ', content)
        
        # 2. Clean up known stray </div> cases
        content = re.sub(r'(<body[^>]*>)\s*</div>', r'\1', content)
        content = re.sub(r'</header>\s*</div>', r'</header>', content)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Fixed marquee in {count} files")
