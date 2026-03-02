import re
import glob

html_files = glob.glob('*.html')

course_mappings = {
    # CRASH COURSE: 7999 -> 2999
    "astrology.html": ("₹7,999", "₹2,999"),
    "nadi-jyotish.html": ("₹7,999", "₹2,999"),
    "palmistry.html": ("₹7,999", "₹2,999"),
    
    # DIPLOMA: 10k -> 4999
    "lal-kitab.html": ("₹10,000", "₹4,999"),
    "complete-astrology.html": ("₹10,000", "₹4,999"),
    "crystal-healing.html": ("₹10,000", "₹4,999"),
    "tarot.html": ("₹10,000", "₹4,999"),
    
    # BACHELORS: 17k -> 9999
    "kp-astrology.html": ("₹17,000", "₹9,999"),
    "vastu.html": ("₹17,000", "₹9,999"),
    "numerology.html": ("₹17,000", "₹9,999"),
    
    # MASTERS: 30k -> 19999
    "remedy-course.html": ("₹30,000", "₹19,999"),
    "medical-astrology.html": ("₹30,000", "₹19,999"),
    "face-reading.html": ("₹30,000", "₹19,999"),
    
    # GRAND MASTER: 50k -> 39999
    "bnn-astrology.html": ("₹50,000", "₹39,999"),
    "rudraksha.html": ("₹50,000", "₹39,999"),
    "contact.html": ("₹50,000", "₹39,999"), # Mentorship links to contact.html
}

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    modified = False

    # 1. Update fee-structure.html specifically
    if filepath == 'fee-structure.html':
        # Crash Course
        html = re.sub(
            r'<span class="course-price">₹[0-9,\s-]+</span>\s*(<a href="(astrology\.html|nadi-jyotish\.html|palmistry\.html)")',
            r'<span class="course-price"><del style="color:#999;font-size:0.85em;margin-right:5px;">₹7,999</del> <strong style="color:#d32f2f;">₹2,999</strong></span>\n                      \1',
            html
        )
        # Diploma
        html = re.sub(
            r'<span class="course-price">₹[0-9,\s-]+</span>\s*(<a href="(lal-kitab\.html|complete-astrology\.html|crystal-healing\.html|tarot\.html)")',
            r'<span class="course-price"><del style="color:#999;font-size:0.85em;margin-right:5px;">₹10,000</del> <strong style="color:#d32f2f;">₹4,999</strong></span>\n                      \1',
            html
        )
        # Bachelors
        html = re.sub(
            r'<span class="course-price">₹[0-9,\s-]+</span>\s*(<a href="(kp-astrology\.html|vastu\.html|numerology\.html)")',
            r'<span class="course-price"><del style="color:#999;font-size:0.85em;margin-right:5px;">₹17,000</del> <strong style="color:#d32f2f;">₹9,999</strong></span>\n                      \1',
            html
        )
        # Masters
        html = re.sub(
            r'<span class="course-price">₹[0-9,\s-]+</span>\s*(<a href="(remedy-course\.html|medical-astrology\.html|face-reading\.html)")',
            r'<span class="course-price"><del style="color:#999;font-size:0.85em;margin-right:5px;">₹30,000</del> <strong style="color:#d32f2f;">₹19,999</strong></span>\n                      \1',
            html
        )
        # Grand Master
        html = re.sub(
            r'<span class="course-price">₹[0-9,\s-]+</span>\s*(<a href="(bnn-astrology\.html|rudraksha\.html|contact\.html)")',
            r'<span class="course-price"><del style="color:#999;font-size:0.85em;margin-right:5px;">₹50,000</del> <strong style="color:#d32f2f;">₹39,999</strong></span>\n                      \1',
            html
        )
        modified = True

    # 2. Update card prices in courses.html (h4 tag)
    def replace_h4(match):
        prefix = match.group(1)
        file_name = match.group(2)
        if file_name in course_mappings:
            old, new = course_mappings[file_name]
            # using br and float for clean look if needed, but side by side is best
            return f'{prefix}<del style="color:#999;font-size:0.65em;margin-right:8px;vertical-align:middle;">{old}</del><strong style="color:#d32f2f;font-size:1.1em;">{new}</strong></h4>\n              <a href="{file_name}"'
        return match.group(0)

    new_html = re.sub(r'(<h4 class="color-secondary mb-0">)₹[0-9,]+</h4>\s*<a href="([^"]+)"', replace_h4, html)
    if new_html != html:
        html = new_html
        modified = True

    # 3. Update main page grids (index.html price-display tag)
    def replace_price_display(match):
        prefix = match.group(1)
        file_name = match.group(2)
        if file_name in course_mappings:
            old, new = course_mappings[file_name]
            return f'{prefix}<del style="color:#999;font-size:0.55em;margin-right:8px;">{old}</del><span style="color:#d32f2f;">{new}</span></div>\n            <a href="{file_name}"'
        return match.group(0)

    new_html = re.sub(r'(<div class="font-2xl color-secondary price-display">)₹[0-9,]+</div>\s*<a href="([^"]+)"', replace_price_display, html)
    if new_html != html:
        html = new_html
        modified = True

    # 4. Update the individual course detail pages table (table-cell-right)
    # E.g. <td class="table-cell-right">₹15,000</td> inside astrology.html
    if filepath in course_mappings:
        old, new = course_mappings[filepath]
        def replace_td(match):
            return f'<td class="table-cell-right"><del style="color:#999;font-size:0.85em;margin-right:8px;">{old}</del> <strong style="color:#d32f2f;font-size:1.1em;">{new}</strong></td>'
        
        new_html = re.sub(r'<td class="table-cell-right">₹[0-9,]+</td>', replace_td, html)
        if new_html != html:
            html = new_html
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated pricing in {filepath}")
