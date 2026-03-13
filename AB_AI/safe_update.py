import re

with open('fee-structure.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Desktop Crash Course Append
desktop_crash_target = '''                  <div class="course-box">
                    <div class="course-header">
                      <span class="course-name">15. Feng Shui</span>
                      <i class="fas fa-chevron-down course-arrow"></i>
                    </div>
                    <div class="course-details">
                      <span class="course-price"><del style="color:#999;font-size:0.85em;margin-right:5px;">₹3,999</del>
                        <strong style="color:#d32f2f;">₹2,999</strong> <span class="discount-text">(with 25% discount)</span></span>
                      <a href="feng-shui.html" class="btn btn-primary btn-sm enroll-btn" style="padding: 4px 10px; font-size: 0.8em;">Enroll Now</a>
                    </div>
                  </div>'''

desktop_crash_append = '''                  <div class="course-box">
                    <div class="course-header">
                      <span class="course-name">16. Gemini Jyotish</span>
                      <i class="fas fa-chevron-down course-arrow"></i>
                    </div>
                    <div class="course-details">
                      <span class="course-price"><del style="color:#999;font-size:0.85em;margin-right:5px;">₹3,999</del>
                        <strong style="color:#d32f2f;">₹2,999</strong> <span class="discount-text">(with 25% discount)</span></span>
                      <a href="gemini-jyotish.html" class="btn btn-primary btn-sm enroll-btn" style="padding: 4px 10px; font-size: 0.8em;">Enroll Now</a>
                    </div>
                  </div>'''

if desktop_crash_target in text:
    text = text.replace(desktop_crash_target, desktop_crash_target + "\n" + desktop_crash_append)
    print("Desktop crash course updated.")
else:
    print("Desktop crash course target not found.")

# 2. Mobile Crash Course Append & Count update
mobile_crash_list_target = '''          <ul class="fee-course-list">
            <li>Past Life Regression Theory</li>
            <li>Palmistry</li>
            <li>Face Reading</li>
            <li>Numerology</li>
            <li>Rudraksha Remedies</li>
            <li>Vedic Astrology</li>
            <li>Tarot Reading</li>
          </ul>'''
          
mobile_crash_list_new = '''          <ul class="fee-course-list">
            <li>Past Life Regression Theory</li>
            <li>Palmistry</li>
            <li>Face Reading</li>
            <li>Numerology</li>
            <li>Rudraksha Remedies</li>
            <li>Vedic Astrology</li>
            <li>Tarot Reading</li>
            <li>Gemini Jyotish</li>
          </ul>'''

if mobile_crash_list_target in text:
    text = text.replace(mobile_crash_list_target, mobile_crash_list_new)
    # Be careful not to replace it globally, just the first occurences which are in Crash Course
    text = text.replace('<div class="fee-meta-value">7 Courses</div>', '<div class="fee-meta-value">8 Courses</div>', 1)
    text = text.replace('📚 View 7 Courses <span class="toggle-icon">▼</span>', '📚 View 8 Courses <span class="toggle-icon">▼</span>', 1)
    print("Mobile crash course updated.")
else:
    print("Mobile crash course list target not found.")

# 3. Empty Desktop Grand Master
start_marker = '<!-- Grand Master courses: BNN Advanced, Rudraksha Remedies, 1-on-1 Mentorship -->\n              <td class="table-data-cell">\n                <div class="courses-scroll">'
end_marker = '                </div>\n              </td>\n            </tr>\n          </tbody>'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    text = text[:start_idx + len(start_marker)] + "\n" + text[end_idx:]
    print("Desktop Grand Master emptied.")
else:
    print("Desktop Grand Master target not found.")

# 4. Empty Mobile Grand Master
start_mobile_search = '<!-- Card 5: Grand Master -->'
end_mobile_search = '<!-- END MOBILE FEE CARDS -->'

start_mob_idx = text.find(start_mobile_search)
end_mob_idx = text.find(end_mobile_search, start_mob_idx)

if start_mob_idx != -1 and end_mob_idx != -1:
    mob_sub = text[start_mob_idx:end_mob_idx]
    
    # We replace the specific courses values
    mob_sub_new = mob_sub.replace('<div class="fee-meta-value">3 Courses</div>', '<div class="fee-meta-value">0 Courses</div>')
    mob_sub_new = mob_sub_new.replace('📚 View 3 Courses', '📚 View 0 Courses')
    
    # Strip the inner lists
    mob_sub_new = re.sub(r'<ul class="fee-course-list">[\s\S]*?</ul>', '<ul class="fee-course-list">\n          </ul>', mob_sub_new)
    
    text = text[:start_mob_idx] + mob_sub_new + text[end_mob_idx:]
    print("Mobile Grand Master emptied.")
else:
    print("Mobile Grand Master target not found.")

with open('fee-structure.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated successfully")
