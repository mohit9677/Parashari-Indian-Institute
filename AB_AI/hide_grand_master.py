import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content
        
        # 1. Hide the Grand Master link from footers and navbars
        link_str = '<li><a href="courses.html">Grand Master</a></li>'
        if link_str in new_content:
            new_content = new_content.replace(link_str, '<!-- ' + link_str + ' -->')

        # 2. Specific fixes for courses.html
        if filepath == 'courses.html':
            # Hide the filter button
            btn_str = '<button class="filter-tab" data-filter="Grand Master">Grand Master</button>'
            if btn_str in new_content:
                new_content = new_content.replace(btn_str, '<!-- ' + btn_str + ' -->')

            # Move Gemini Jyotish to Crash Course
            # We find the gemini-jyotish card and change its category and badge
            # data-category="Grand Master" data-course-id="gemini-jyotish"
            new_content = new_content.replace(
                'data-category="Grand Master" data-course-id="gemini-jyotish"', 
                'data-category="Crash Course" data-course-id="gemini-jyotish"'
            )
            # Find the badge specifically inside the Gemini Jyotish block
            # Since doing this neatly with regex can be tricky, let's use a targeted regex replacing the badge just for gemini
            
            gemini_block_pattern = r'(data-course-id="gemini-jyotish"[\s\S]*?)<span class="category-badge" style="background:#c8960c">Grand Master · Elite</span>'
            new_content = re.sub(gemini_block_pattern, r'\g<1><span class="category-badge" style="background:#ff9800">Crash Course</span>', new_content)

            # Hide all remaining Grand Master cards
            # We replace `data-category="Grand Master"` with `data-category="Hidden"`
            # and add `display: none !important;` to the style
            
            # The cards look like:
            # <div class="premium-gold-card" style="padding: 0 !important;" data-animate data-category="Grand Master" data-course-id="rudraksha">
            # We can use regex to hide them
            gm_card_pattern = r'(<div class="premium-gold-card" style=")(padding: 0 !important;)(" data-animate data-category="Grand Master")'
            new_content = re.sub(gm_card_pattern, r'\g<1>display: none !important; \g<2>\g<3>', new_content)
            
            # Also for the old card style if any
            old_card_pattern = r'(<div class="card" data-animate data-category="Grand Master")'
            new_content = re.sub(old_card_pattern, r'<div class="card" style="display: none !important;" data-animate data-category="Hidden"', new_content)
            
        # 3. fee-structure.html has a Grand Master section
        if filepath == 'fee-structure.html':
            # Hide the Grand Master title and card
            # <div class="cat-title">🎓 Grand Master</div>
            new_content = new_content.replace('<div class="cat-title">🎓 Grand Master</div>', '<!-- <div class="cat-title">🎓 Grand Master</div> -->')
            new_content = new_content.replace('<div class="fee-card-title">🎓 Grand Master</div>', '<!-- <div class="fee-card-title">🎓 Grand Master</div> -->')
            
            # Since fee structure has a whole grid and cards, it's safer to just inject a CSS rule at the top to hide them
            if '<style>' in new_content:
                new_content = new_content.replace('<style>', '<style>\n  .premium-gold-card[data-category="Grand Master"], .card[data-category="Grand Master"], div[data-category="Grand Master"] { display: none !important; }\n  .fee-card-title:contains("Grand Master") { display: none; }')

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"SUCCESS: Updated {filepath}")

    except Exception as e:
        print(f"ERROR: Could not process {filepath}: {e}")
