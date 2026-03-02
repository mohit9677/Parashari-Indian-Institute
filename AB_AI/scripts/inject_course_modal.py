import re

with open('blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add css link
if 'modal.css' not in html:
    html = html.replace('</head>', '  <link rel="stylesheet" href="assets/css/modal.css">\n</head>')

# 2. Add Modal HTML markup before closing body
modal_html = """
  <div id="courseModal" class="modal-overlay">
    <div class="modal-content">
      <button class="modal-close">&times;</button>
      <div class="modal-header">
        <h2 id="modalTitle">Course Title</h2>
        <div class="modal-meta">
          <span id="modalLearners"><i class="fas fa-users"></i> 0 learners</span>
          <span id="modalDuration"><i class="far fa-clock"></i> 0 hrs</span>
        </div>
      </div>
      <div class="modal-body" id="modalBody">
        <p>Course description goes here.</p>
      </div>
      <div class="modal-footer">
        <a href="login.html" class="btn btn-primary">Start Learning Now</a>
      </div>
    </div>
  </div>
"""
if 'id="courseModal"' not in html:
    html = html.replace('</body>', modal_html + '\n</body>')

# 3. Handle the buttons
def replacer(match):
    # match.group(0) is the full matched string: <a href="#" class="btn-course-outline">View Program</a>
    # We need to extract the title from the *previous* context, or just replace all 3 specific ones via string replace.
    pass 

# Since there are only 3 specific courses, lets just string replace them to be safe
c1 = '<a href="#" class="btn-course-outline">View Program</a>\n                            <a href="login.html" class="btn-course-primary">\n                                Start Now\n                                <div class="star-1">'
r1 = '<a href="javascript:void(0)" class="btn-course-outline" onclick=\"openCourseModal(\'Introduction to Ascendants and Planets\', \'15.2K+\', \'4 hrs\')\">View Program</a>\n                            <a href="login.html" class="btn-course-primary">\n                                Start Now\n                                <div class="star-1">'

c2 = '<a href="#" class="btn-course-outline">View Program</a>\n                            <a href="login.html" class="btn-course-primary">\n                                Start Now\n                                <div class="star-1">'
# But this would match all 3, we need to match them individually based on the header.

# Using regex to find the whole course block and replace the button inside
html = re.sub(
    r'(<h3 class="free-course-title">(.*?)</h3>\s*<div class="free-course-meta">\s*<div class="free-course-meta-item"><i class="fas fa-users"></i>(.*?)learners</div>\s*<div class="free-course-meta-item"><i class="far fa-clock"></i>(.*?)of learning</div>\s*</div>\s*<div class="free-course-actions">\s*)<a href="#" class="btn-course-outline">View Program</a>',
    lambda m: f'{m.group(1)}<a href="javascript:void(0)" class="btn-course-outline" onclick="openCourseModal(\'{m.group(2).strip()}\', \'{m.group(3).strip()}\', \'{m.group(4).strip()}\')">View Program</a>',
    html
)

# 4. Add the Javascript code
js_code = """
  <script>
    function openCourseModal(title, learners, duration) {
      document.getElementById('modalTitle').innerText = title;
      document.getElementById('modalLearners').innerHTML = '<i class="fas fa-users"></i> ' + learners + ' learners';
      document.getElementById('modalDuration').innerHTML = '<i class="far fa-clock"></i> ' + duration;
      
      const body = document.getElementById('modalBody');
      if (title.includes('Ascendants')) {
        body.innerHTML = `
          <p>This introductory course lays the foundation for understanding Vedic Astrology. You will learn about the 12 ascendants (Lagnas) and the 9 planets (Navagrahas) that shape our destinies.</p>
          <ul>
            <li>Understand the characteristics of all 12 Zodiac signs.</li>
            <li>Learn the nature, exaltation, and debilitation of planets.</li>
            <li>Discover how planets behave in different houses.</li>
            <li>Master the basics of charting a horoscope.</li>
          </ul>
        `;
      } else if (title.includes('Lal Kitab')) {
         body.innerHTML = `
          <p>Dive into the mystical world of Lal Kitab, a unique system of astrology that prioritizes practical, easily executable remedies (Totkas) without complex rituals.</p>
          <ul>
            <li>Understand the concept of Karmic debts in Lal Kitab.</li>
            <li>Learn the grammar and specific rules of the Lal Kitab system.</li>
            <li>Differentiate between traditional Vedic astrology and Lal Kitab.</li>
            <li>Discover simple remedies for common life problems.</li>
          </ul>
        `;
      } else if (title.includes('Tarot')) {
         body.innerHTML = `
          <p>Unveil the secrets of Tarot reading by mastering the four essential elements: Wands (Fire), Cups (Water), Swords (Air), and Pentacles (Earth).</p>
          <ul>
            <li>Learn the spiritual significance of the four elements.</li>
            <li>Understand how elements interact within a spread.</li>
            <li>Master the meanings of the Minor Arcana suits.</li>
            <li>Develop your intuitive reading abilities.</li>
          </ul>
        `;
      } else {
        body.innerHTML = '<p>A comprehensive guide to ' + title + '.</p>';
      }

      const modal = document.getElementById('courseModal');
      modal.style.display = 'flex';
      // trigger reflow
      void modal.offsetWidth; 
      modal.classList.add('active');
      document.body.style.overflow = 'hidden'; // prevent scrolling
    }

    document.addEventListener('DOMContentLoaded', () => {
      const modal = document.getElementById('courseModal');
      const closeBtn = document.querySelector('.modal-close');
      
      if(closeBtn) {
        closeBtn.addEventListener('click', () => {
          modal.classList.remove('active');
          setTimeout(() => { modal.style.display = 'none'; }, 300);
          document.body.style.overflow = '';
        });
      }

      window.addEventListener('click', (e) => {
        if (e.target === modal) {
          modal.classList.remove('active');
          setTimeout(() => { modal.style.display = 'none'; }, 300);
          document.body.style.overflow = '';
        }
      });
    });
  </script>
"""

if 'function openCourseModal' not in html:
    html = html.replace('</body>', js_code + '\n</body>')

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Applied Modal to blog.html')
