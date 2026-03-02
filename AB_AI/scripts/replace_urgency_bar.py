import os
import glob
import re
import shutil

html_files = glob.glob('*.html')
backup_dir = 'backup_marquee_revert'

if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Backup files
for file_path in html_files:
    shutil.copy2(file_path, os.path.join(backup_dir, file_path))
print(f"Backed up {len(html_files)} files to {backup_dir}/")

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Replace HTML Block
    # Look for <!-- TOP URGENCY MARQUEE --> and replace everything up to <footer>
    html_pattern = re.compile(r'<!--\s*TOP URGENCY MARQUEE\s*-->.*?<footer', re.DOTALL | re.IGNORECASE)
    
    NEW_BAR_HTML = """  <!-- MODERN URGENCY BAR -->
  <div class="announcement-bar" id="urgencyBar">
    <div class="announcement-left">
      <div class="fire-icon animate-pulse">🔥</div>
      <div class="announcement-text-slider">
        <span class="slide-text active">Admissions Open – Limited Seats Available</span>
      </div>
    </div>
    <div class="announcement-center">
      <div class="timer-container" id="urgencyTimer">
        <span class="timer-label">Ends in:</span>
        <span class="blinking-dot"></span>
        <span id="countdownText" class="timer-val">12d : 08h : 14m : 33s</span>
      </div>
    </div>
    <div class="announcement-right">
      <div class="cta-wrapper">
        <a href="register.html" class="cta-button" id="urgencyCta">Register Now</a>
        <div class="cta-microcopy">Secure Your Seat Before It's Gone</div>
      </div>
    </div>
  </div>

  <footer"""
    
    if html_pattern.search(content):
        content = html_pattern.sub(NEW_BAR_HTML, content)
        modified = True

    # 2. Replace JS Block
    js_pattern = re.compile(r'<!--\s*URGENCY TIMER JS\s*-->.*?</script>', re.DOTALL | re.IGNORECASE)
    
    NEW_TIMER_JS = """  <!-- MODERN URGENCY JS -->
  <script>
    document.addEventListener('DOMContentLoaded', function () {
      // Set Target Date: March 31, 2026, 11:59:59 PM
      // Months are 0-indexed in JS, so 2 = March
      let targetDate = new Date(2026, 2, 31, 23, 59, 59).getTime();

      const countdownText = document.getElementById('countdownText');
      const urgencyCta = document.getElementById('urgencyCta');
      const slideText = document.querySelector('.slide-text');
      const blinkingDot = document.querySelector('.blinking-dot');
      const timerLabel = document.querySelector('.timer-label');

      function updateTimer() {
        const now = new Date().getTime();
        const distance = targetDate - now;

        if (distance <= 0) {
          if(countdownText) countdownText.innerHTML = "Admissions Closing Soon";
          if(countdownText) countdownText.style.color = "#fff";
          if(timerLabel) timerLabel.style.display = "none";
          if(blinkingDot) blinkingDot.style.display = "none";
          if(urgencyCta) {
            urgencyCta.innerText = "Apply Now";
            urgencyCta.classList.add('expired-cta');
          }
          if(slideText) slideText.innerText = "Last Chance to Register!";
          return;
        }

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        const dDisp = days < 10 ? "0" + days : days;
        const hDisp = hours < 10 ? "0" + hours : hours;
        const mDisp = minutes < 10 ? "0" + minutes : minutes;
        const sDisp = seconds < 10 ? "0" + seconds : seconds;

        if(countdownText) {
          countdownText.innerHTML = `${dDisp}d : ${hDisp}h : ${mDisp}m : ${sDisp}s`;
        }
      }

      // Initial call
      updateTimer();
      // Update every second
      setInterval(updateTimer, 1000);

      // Subtle pulse on text every 5s
      if(slideText) {
        setInterval(() => {
          slideText.style.transform = 'scale(1.02)';
          slideText.style.color = '#FFD700';
          setTimeout(() => {
            slideText.style.transform = 'scale(1)';
            slideText.style.color = '#fff';
          }, 800);
        }, 5000);
      }
    });
  </script>"""

    if js_pattern.search(content):
        content = js_pattern.sub(NEW_TIMER_JS, content)
        modified = True

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {file_path}")

print("Done updating HTML files.")
