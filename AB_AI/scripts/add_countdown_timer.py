import glob
import re

html_files = glob.glob('*.html')

# 1. Update urgency.css to style the timer
css_timer_styles = """
/* COUNTDOWN TIMER STYLES */
.marquee-timer {
    display: inline-flex;
    align-items: center;
    background: rgba(0,0,0,0.3);
    padding: 3px 10px;
    border-radius: 4px;
    margin-left: 10px;
    font-family: monospace;
    font-size: 1.1em;
    font-weight: bold;
    color: #FFD700;
    letter-spacing: 1px;
}
.timer-pulse {
    animation: pulse-red 1s infinite alternate;
}
@keyframes pulse-red {
    from { color: #FFD700; }
    to { color: #ffeb3b; text-shadow: 0 0 5px #ffeb3b; }
}
"""

with open('assets/css/urgency.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'marquee-timer' not in css_content:
    with open('assets/css/urgency.css', 'a', encoding='utf-8') as f:
        f.write(css_timer_styles)

# 2. Add the JS logic to run the countdown
timer_js = """
  <!-- URGENCY TIMER JS -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      // Set end date to 2 days from now for consistent urgency
      let endDate = new Date();
      endDate.setDate(endDate.getDate() + 2);
      endDate.setHours(23, 59, 59);

      const timerElements = document.querySelectorAll('.marquee-timer-val');
      
      if(timerElements.length > 0) {
        setInterval(function() {
          const now = new Date().getTime();
          const distance = endDate.getTime() - now;

          if (distance < 0) {
             // Reset timer to 2 days if it expires
             endDate = new Date();
             endDate.setDate(endDate.getDate() + 2);
             return;
          }

          const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
          const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
          const seconds = Math.floor((distance % (1000 * 60)) / 1000);

          const timeString = 
            (hours < 10 ? "0" + hours : hours) + ":" + 
            (minutes < 10 ? "0" + minutes : minutes) + ":" + 
            (seconds < 10 ? "0" + seconds : seconds);

          timerElements.forEach(el => {
              el.innerText = timeString;
          });
        }, 1000);
      }
    });
  </script>
"""

# HTML pattern to inject the timer into
old_marquee = '<div class="marquee-item">\n        <span class="marquee-icon">🎓</span> Admissions Open! Register Now for Upcoming Batches — Limited Seats Available! \n        <a href="register.html" class="marquee-btn">Fast Register</a>\n      </div>'
new_marquee = '<div class="marquee-item">\n        <span class="marquee-icon">🎓</span> Admissions Open! Register Now for Upcoming Batches — Limited Seats Available! \n        <div class="marquee-timer timer-pulse">Ends in: <span class="marquee-timer-val">47:59:59</span></div>\n        <a href="register.html" class="marquee-btn">Fast Register</a>\n      </div>'

updated_count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # We might have trailing spaces or different line endings, so let's do a more robust regex sub
    if 'marquee-timer timer-pulse' not in content:
        # Find exactly the first marquee item text block and replace it
        pattern = r'<span class="marquee-icon">🎓</span> Admissions Open! Register Now for Upcoming Batches — Limited Seats Available! \s*<a href="register.html" class="marquee-btn">'
        replacement = r'<span class="marquee-icon">🎓</span> Admissions Open! Register Now for Upcoming Batches — Limited Seats Available! <div class="marquee-timer timer-pulse">Ends in: <span class="marquee-timer-val">47:59:59</span></div> <a href="register.html" class="marquee-btn">'
        
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            modified = True
            
    if '<!-- URGENCY TIMER JS -->' not in content:
        content = content.replace('</body>', timer_js + '\n</body>')
        modified = True
        
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1

print(f"Added countdown timers to {updated_count} HTML files.")
