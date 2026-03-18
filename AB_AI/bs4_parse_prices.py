import bs4
import re

with open('fee-structure.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

def calculate_discount(cut, current):
    # Calculate discount percentage
    try:
        c1 = int(cut.replace(',', ''))
        c2 = int(current.replace(',', ''))
        percent = round(100 - (c2 / c1 * 100))
        return f' (with {percent}% discount)'
    except:
        return ''

def get_pricing_html(cut, current):
    discount_txt = calculate_discount(cut, current)
    return f'<del style="color:#999;font-size:0.85em;margin-right:5px;">₹{cut}</del> <strong style="color:#d32f2f;">₹{current}</strong> <span class="discount-text">{discount_txt}</span>'

# Pricing Scheme
prices = {
    'Crash Course': ('3,499', '2,499'),
    'Diploma': ('5,499', '4,199'),
    'Bachelor': ('11,999', '8,999'),
    'Master': ('24,999', '18,699'),
    'Grand Master': ('34,999', '24,999')
}

# The 13 Courses
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
reg_icon = soup.find('div', class_='reg-icon')
if reg_icon:
    reg_icon['style'] = reg_icon.get('style', '') + '; flex-shrink: 0;'

# 2. Advance/Elite Badges (in cat-title and fee-card-title)
# Desktop elements
for badge in soup.find_all('span', class_='gm-premium-badge'):
    text = badge.text.strip()
    if text == 'Advance':
        badge['class'] = 'popular-badge'
        badge['style'] = "background: #ff9800; color: #fff; font-size: 0.6em; margin-left:10px; padding:3px 8px; border-radius:12px;"
    elif text == 'Elite':
        badge['class'] = 'popular-badge'
        badge['style'] = "background: #673ab7; color: #fff; font-size: 0.6em; margin-left:10px; padding:3px 8px; border-radius:12px;"

# 3. 6 Stairs Mastery card (Mobile view specifically has "5 Courses")
for val in soup.find_all('div', class_='fee-meta-value'):
    if val.text.strip() == '5 Courses':
        val.string = '6 Stairs'
for btn in soup.find_all('button', class_='fee-courses-toggle'):
    if 'View 5 Courses' in btn.text:
        # replace just the text leaving child span intact
        for child in btn.contents:
            if isinstance(child, bs4.NavigableString) and 'View 5 Courses' in child:
                child.replace_with(child.replace('View 5 Courses', 'View 6 Stairs'))

# 4. Updating Courses & Pricing
def process_category(category_name, container):
    # Determine which category this is for pricing
    cat_price = None
    for key in prices:
        if key in category_name:
            cat_price = prices[key]
            break
    if not cat_price:
        return

    # Is it Diploma, Bachelor, Master?
    is_13_target = any(x in category_name for x in ['Diploma', 'Bachelor', 'Master']) and 'Grand' not in category_name

    scroll = container.find('div', class_='courses-scroll')
    if not scroll: return
    
    if is_13_target:
        # Rebuild 13 courses exactly
        # First grab a clone of an existing box to preserve styling logic
        template = scroll.find('div', class_='course-box')
        if not template: return
        scroll.clear()
        
        for i, (name, link) in enumerate(c_list, 1):
            clone = bs4.BeautifulSoup(str(template), 'html.parser').find('div', class_='course-box')
            
            # update name
            name_span = clone.find('span', class_='course-name')
            name_span.string = f"{i}. {name}"
            
            # update price
            price_span = clone.find('span', class_='course-price')
            if price_span:
                price_html = bs4.BeautifulSoup(get_pricing_html(*cat_price), 'html.parser')
                price_span.clear()
                price_span.append(price_html)
            
            # update enroll button
            enroll = clone.find('a', class_='enroll-btn')
            if enroll:
                enroll['href'] = link
            
            scroll.append(clone)
    else:
        # Just update pricing
        # Grand Master / Crash Course
        for box in scroll.find_all('div', class_='course-box'):
            price_span = box.find('span', class_='course-price')
            if price_span:
                price_html = bs4.BeautifulSoup(get_pricing_html(*cat_price), 'html.parser')
                price_span.clear()
                price_span.append(price_html)

# Desktop & Mobile Table Items
# Desktop Categories
for td in soup.find_all('td', class_='table-data-cell'):
    cat_title_div = td.find('div', class_='cat-title')
    if cat_title_div:
        # The parent `tr` has the courses-scroll
        tr = td.parent
        process_category(cat_title_div.text, tr)

# Mobile Categories
for card in soup.find_all('div', class_='fee-card'):
    title_div = card.find('div', class_='fee-card-title')
    if title_div:
        process_category(title_div.text, card)

# Write back
html_output = str(soup)
# BeautifulSoup sometimes converts & to &amp; but we want to stick to what the user had.
with open('fee-structure.html', 'w', encoding='utf-8') as f:
    f.write(html_output)

print("BeautifulSoup strictly modified the DOM structure. Complete.")
