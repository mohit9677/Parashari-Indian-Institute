import re

# 1. Restore Grand Master button in courses.html
with open('courses.html', 'r', encoding='utf-8') as f:
    courses_html = f.read()

btn_target = '<!-- <button class="filter-tab" data-filter="Grand Master">Grand Master</button> -->'
if btn_target in courses_html:
    courses_html = courses_html.replace(btn_target, '<button class="filter-tab" data-filter="Grand Master">Grand Master</button>')

# For the cards, they have display: none !important; which is functionally empty for the user. We leave them hidden.
with open('courses.html', 'w', encoding='utf-8') as f:
    f.write(courses_html)
print("Updated courses.html")


# 2. Fix fee-structure.html
with open('fee-structure.html', 'r', encoding='utf-8') as f:
    fee_html = f.read()

# Remove the injected style tag
style_block = '<style>\n  .premium-gold-card[data-category="Grand Master"], .card[data-category="Grand Master"], div[data-category="Grand Master"] { display: none !important; }\n  .fee-card-title:contains("Grand Master") { display: none; }\n</style>'
# wait, the injected string was slightly different earlier, let's just do a regex
style_pattern = r'<style>\n\s*\.premium-gold-card\[data-category="Grand Master"\].*?display: none; \}\n\s*</style>'
fee_html = re.sub(r'<style>\n\s*\.premium-gold-card\[data-category="Grand Master"\][\s\S]*?</style>', '', fee_html)
# Also try a simpler replace if regex fails
fee_html = fee_html.replace('<style>\n  .premium-gold-card[data-category="Grand Master"], .card[data-category="Grand Master"], div[data-category="Grand Master"] { display: none !important; }\n  .fee-card-title:contains("Grand Master") { display: none; }</style>', '')

# Restore the titles
fee_html = fee_html.replace('<!-- <div class="cat-title">🎓 Grand Master</div> -->', '<div class="cat-title">🎓 Grand Master</div>')
fee_html = fee_html.replace('<!-- <div class="fee-card-title">🎓 Grand Master</div> -->', '<div class="fee-card-title">🎓 Grand Master</div>')

# Empty the desktop courses block. 
# Looks like: <td class="table-data-cell">\n                <div class="courses-scroll">\n (courses here) \n                </div>\n              </td>
# We can find the Grand Master row and empty its courses-scroll div contents.
# Alternatively, we just know what the courses were: BNN Advanced, Rudraksha, Mentorship.
bnn_course = r'<div class="course-box">[\s\S]*?<span class="course-name">[^<]*?BNN[\s\S]*?</div>[\s\S]*?</div>'
rudraksha_course = r'<div class="course-box">[\s\S]*?<span class="course-name">[^<]*?Rudraksha[\s\S]*?</div>[\s\S]*?</div>'
mentorship_course = r'<div class="course-box">[\s\S]*?<span class="course-name">[^<]*?1-on-1 Mentorship[\s\S]*?</div>[\s\S]*?</div>'

fee_html = re.sub(bnn_course, '', fee_html)
fee_html = re.sub(rudraksha_course, '', fee_html)
fee_html = re.sub(mentorship_course, '', fee_html)

# Now for the mobile block:
# <ul class="fee-course-list">\n            <li>BNN Advanced...
fee_html = fee_html.replace('<li>BNN Advanced (Bhrigu Nandi Nadi)</li>', '')
fee_html = fee_html.replace('<li>1-on-1 Mentorship</li>', '')
fee_html = fee_html.replace('<li>Rudraksha Remedies</li>', '')

with open('fee-structure.html', 'w', encoding='utf-8') as f:
    f.write(fee_html)
print("Updated fee-structure.html")
