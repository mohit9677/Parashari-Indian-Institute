import re

with open('fee-structure.html', 'r', encoding='utf-8') as f:
    content = f.read()

courses = [
    ('Numerology (Pythagorean & Chaldean)', 'numerology.html'),
    ('Vedic Astrology (Jyotish)', 'astrology.html'),
    ('KP Astrology (Krishnamurti Padhdhati)', 'kp-astrology.html'),
    ('Gemstone Science (Ratna Vigyan)', 'gemstone.html'),
    ('Vastu Shastra', 'vastu.html'),
    ('Lal Kitab', 'lal-kitab.html'),
    ('Face Reading (Physiognomy)', 'face-reading.html'),
    ('Reiki Healing', 'reiki.html'),
    ('Tarot Reading', 'tarot.html'),
    ('Nakshatra (Lunar Mansions) 1', 'nakshatra.html'),
    ('Crystal', 'crystal-healing.html'),
    ('Rudraksha', 'rudraksha.html'),
    ('Palmistry (Chirognomy & Chiromancy)', 'palmistry.html')
]

html_str = ""
for i, (name, link) in enumerate(courses, 1):
    html_str += f'<div class="course-box"><div class="course-header"><span class="course-name">{i}. {name.replace("&", "&amp;")}</span><i class="fas fa-chevron-down course-arrow"></i></div><div class="course-details"><span class="course-price"><del style="color:#999;font-size:0.85em;margin-right:5px;">₹3,999</del> <strong style="color:#d32f2f;">₹2,999</strong> <span class="discount-text"> (with 25% discount)</span></span><a class="btn btn-primary btn-sm enroll-btn" href="{link}" style="padding: 4px 10px; font-size: 0.8em;">Enroll Now</a></div></div>'

# For Desktop, the HTML looks like this inside the td block:
desktop_pattern = r'(<!-- (Diploma|Bachelor|Master) courses: .*? -->\s*<td class="table-data-cell"><div class="courses-scroll">)(.*?)(</div></td>)'
content = re.sub(desktop_pattern, r'\g<1>' + html_str + r'\g<4>', content, flags=re.DOTALL)

# For mobile, they are inside `<div class="courses-scroll">` right after the `fee-courses-toggle` button.
# Let's find specific text blocks for Mobile Diploma, Bachelor, Master
# Mobile Diploma header contains: `<div class="fee-card-title">🎓 Diploma`
# Mobile Bachelor: `<div class="fee-card-title">🎓 Bachelor`
# Mobile Master: `<div class="fee-card-title">🎓 Master`

def replace_mobile_courses(title, text):
    # Regex to find the courses-scroll block after the specific fee-card-title
    # It looks for fee-card-title, then goes down to courses-scroll and replaces the inner content until the closing </div> of courses-scroll.
    # Note: `courses-scroll` div is closed by `</div>`. We match everything until the first `</div>\n</div>\n<!-- Card` or similar. Since courses-scroll contains child divs, we can match until `</div>\n</div>\n<!-- Card` which closes the card. Wait, `courses-scroll` is the last element in the `fee-card`. So it's closed, and then the card is closed.
    
    pattern = r'(<div class="fee-card-title">🎓 ' + title + r'.*?<div class="courses-scroll">)(.*?)(</div>\s*</div>\s*<!-- (Card \d+|END MOBILE FEE CARDS))'
    return re.sub(pattern, r'\g<1>' + html_str + r'\g<3>', text, flags=re.DOTALL)

content = replace_mobile_courses("Diploma", content)
content = replace_mobile_courses("Bachelor", content)
content = replace_mobile_courses("Master", content)

with open('fee-structure.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated fee-structure.html with 13 courses for Diploma, Bachelor, Master.")
