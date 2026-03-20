import re

try:
    with open('d:\\ParashariTeam\\AB_AI\\courses.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update image
    html = html.replace('assets/images/about-hero-image.png', 'assets/images/1-1-mentorship.png')
    
    # 2. Extract mentorship section
    # Let's locate the <section id="mentorship-section">
    start_idx = html.find('<section id="mentorship-section"')
    end_idx = html.find('</section>', start_idx) + len('</section>')
    
    if start_idx != -1 and end_idx != -1:
        mentor_html = html[start_idx:end_idx]
        html = html.replace(mentor_html, '')
        
        # 3. Find the upcoming courses div wrapper
        # '<div class="text-center mt-3 mb-2">\n          <a href="upcoming-courses.html"'
        # Let's use regex to find the whole div
        up_pattern = r'(<div class="text-center mt-3 mb-2">\s*<a href="upcoming-courses\.html".*?</a>\s*</div>)'
        up_match = re.search(up_pattern, html, flags=re.DOTALL)
        if up_match:
            wrapper_html = up_match.group(1)
            # Insert the mentor_html right after the wrapper_html
            new_replacement = wrapper_html + '\n\n' + mentor_html
            html = html.replace(wrapper_html, new_replacement)
            print('Moved mentor section successfully in courses.html.')
        else:
            print('Could not find upcoming courses wrapper in courses.html.')
            # Put it back where it was
            # Find footer or <section class="light-bg">
            light_idx = html.find('<section class="light-bg">')
            if light_idx != -1:
                html = html[:light_idx] + mentor_html + '\n\n  ' + html[light_idx:]
            
        with open('d:\\ParashariTeam\\AB_AI\\courses.html', 'w', encoding='utf-8') as f:
            f.write(html)
    else:
        print('Could not find mentorship section.')

except Exception as e:
    print(f"Error processing courses.html: {e}")

# Now highlight in navbar
def highlight_navbar_item(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # We search for <a href="mentorship.html">1-on-1 Mentorship</a>
        # and replace it with:
        # <a href="mentorship.html" style="color: #D4AF37; font-weight: 800; display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-star" style="color: #D4AF37; font-size: 0.8rem;"></i> 1-on-1 Mentorship</a>
        
        # But we only want to do it in the dropdown menu.
        # Let's just do a naive replace first:
        old_link = '<a href="mentorship.html">1-on-1 Mentorship</a>'
        new_link = '<a href="mentorship.html" style="color: #D4AF37; font-weight: 800; background: rgba(212,175,55,0.05); border-left: 3px solid #D4AF37; padding-left: 12px; display: flex; align-items: center; justify-content: space-between;">1-on-1 Mentorship <i class="fa-solid fa-star" style="font-size: 0.75rem; color: #D4AF37;"></i></a>'
        
        if old_link in html:
            html = html.replace(old_link, new_link)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Highlighted mentorship in {filename}")
        else:
            print(f"Old link not found in {filename}")
            
    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Update all main files that have the navbar
for filename in ['index.html', 'courses.html', 'profile.html', 'contact.html', 'blog.html', 'fee-structure.html', '6-stairs.html', 'mentorship.html']:
    import os
    path = os.path.join('d:\\ParashariTeam\\AB_AI', filename)
    if os.path.exists(path):
        highlight_navbar_item(path)

print("Done with python script!")
