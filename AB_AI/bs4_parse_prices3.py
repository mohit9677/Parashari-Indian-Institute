import bs4
import re

with open('fee-structure.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

def get_pricing_html(cut, current):
    try:
        c1 = int(cut.replace(',', ''))
        c2 = int(current.replace(',', ''))
        percent = round(100 - (c2 / c1 * 100))
        discount_txt = f' (with {percent}% discount)'
    except:
        discount_txt = ''
    return f'<del style="color:#999;font-size:0.85em;margin-right:5px;">₹{cut}</del> <strong style="color:#d32f2f;">₹{current}</strong> <span class="discount-text">{discount_txt}</span>'

# Pricing Scheme 
prices = {
    'Grand Master': ('34,999', '24,999'),
    'Crash Course': ('3,499', '2,499'),
    'Bachelor': ('11,999', '8,999'),
    'Master': ('24,999', '18,699'),
    'Diploma': ('5,499', '4,199')
}

c_list = [
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

# 1. Circle
for reg_icon in soup.find_all('div', class_='reg-icon'):
    style = reg_icon.get('style', '')
    if 'flex-shrink' not in style:
        reg_icon['style'] = style + '; flex-shrink: 0;'

# 2. Advance/Elite Badges
for badge in soup.find_all('span', class_='gm-premium-badge'):
    text = badge.text.strip()
    if text == 'Advance':
        badge['class'] = ['popular-badge']
        badge['style'] = "background: #ff9800; color: #fff; font-size: 0.6em; margin-left:10px; padding:3px 8px; border-radius:12px;"
    elif text == 'Elite':
        badge['class'] = ['popular-badge']
        badge['style'] = "background: #673ab7; color: #fff; font-size: 0.6em; margin-left:10px; padding:3px 8px; border-radius:12px;"

# 3. 6 Stairs Mastery
for val in soup.find_all('div', class_='fee-meta-value'):
    if val.text.strip() == '5 Courses':
        val.string = '6 Stairs'
for btn in soup.find_all('button', class_='fee-courses-toggle'):
    if 'View 5 Courses' in btn.text:
        for child in btn.contents:
            if isinstance(child, bs4.NavigableString) and 'View 5 Courses' in child:
                new_str = child.replace('View 5 Courses', 'View 6 Stairs')
                child.replace_with(bs4.NavigableString(new_str))

# 4. Courses & Pricing Update
def process_course_list(category_name, scroll_div):
    matched_key = None
    for key in prices:
        if key == 'Master' and 'Mastery' in category_name:
            continue
        if key in category_name:
            matched_key = key
            break
            
    if not matched_key:
        return
        
    cat_price = prices[matched_key]
    is_13_target = matched_key in ['Diploma', 'Bachelor', 'Master']
    
    if is_13_target:
        # Rebuild perfectly
        boxes = scroll_div.find_all('div', class_='course-box')
        if not boxes: return
        template_html = str(boxes[0])
        scroll_div.clear()
        
        for i, (name, link) in enumerate(c_list, 1):
            clone_soup = bs4.BeautifulSoup(template_html, 'html.parser')
            clone = clone_soup.find('div', class_='course-box')
            
            name_span = clone.find('span', class_='course-name')
            if name_span: name_span.string = f"{i}. {name}"
                
            price_span = clone.find('span', class_='course-price')
            if price_span:
                price_span.clear()
                price_span.append(bs4.BeautifulSoup(get_pricing_html(*cat_price), 'html.parser'))
                
            enroll = clone.find('a', class_='enroll-btn')
            if enroll: enroll['href'] = link
                
            scroll_div.append(clone)
    else:
        # Crash Course & Grand Master
        update_active = True
        for child in scroll_div.children:
            if isinstance(child, bs4.Tag):
                if child.name == 'div' and '--- Plus 6 Spiritual Stairs FREE ---' in child.text:
                    update_active = False 
                
                if child.name == 'div' and 'course-box' in child.get('class', []):
                    if update_active:
                        price_span = child.find('span', class_='course-price')
                        if price_span:
                            price_span.clear()
                            price_span.append(bs4.BeautifulSoup(get_pricing_html(*cat_price), 'html.parser'))

# Process desktop
table = soup.find('table', class_='table-full')
if table:
    for tr in table.find_all('tr'):
        cat_box = tr.find('div', class_='category-box')
        scroll = tr.find('div', class_='courses-scroll')
        if cat_box and scroll:
            title = cat_box.find('div', class_='cat-title')
            if title:
                process_course_list(title.text, scroll)

# Process mobile
for card in soup.find_all('div', class_='fee-card'):
    title = card.find('div', class_='fee-card-title')
    scroll = card.find('div', class_='courses-scroll')
    if title and scroll:
        process_course_list(title.text, scroll)

html_output = str(soup)

# Add hover CSS
hover_css = '''
          @media (min-width: 769px) {
            .course-box:hover .course-details {
              display: flex;
            }
            .course-box:hover .course-arrow {
              transform: rotate(180deg);
            }
          }
'''
if 'course-box:hover .course-details' not in html_output:
    html_output = html_output.replace('/* =============  MOBILE FEE CARDS  ============= */', hover_css + '\n          /* =============  MOBILE FEE CARDS  ============= */')

with open('fee-structure.html', 'w', encoding='utf-8') as f:
    f.write(html_output)

print("Successfully processed fee-structure.html")
