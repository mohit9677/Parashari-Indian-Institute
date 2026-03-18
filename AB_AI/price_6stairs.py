import bs4

with open('fee-structure.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

discount_html = '<del style="color:#999;font-size:0.85em;margin-right:5px;">₹3,999</del> <strong style="color:#d32f2f;">₹2,999</strong> <span class="discount-text"> (with 25% discount)</span>'

# Find all 6 Stairs Mastery sections
# Desktop
for tr in soup.find_all('tr'):
    cat = tr.find('div', class_='cat-title')
    scroll = tr.find('div', class_='courses-scroll')
    if cat and scroll and '6 Stairs Mastery' in cat.text:
        # replace the price on its children
        for box in scroll.find_all('div', class_='course-box'):
            price_span = box.find('span', class_='course-price')
            if price_span:
                price_span.clear()
                price_span.append(bs4.BeautifulSoup(discount_html, 'html.parser'))

# Mobile
for card in soup.find_all('div', class_='fee-card'):
    cat = card.find('div', class_='fee-card-title')
    scroll = card.find('div', class_='courses-scroll')
    if cat and scroll and '6 Stairs Mastery' in cat.text:
        for box in scroll.find_all('div', class_='course-box'):
            price_span = box.find('span', class_='course-price')
            if price_span:
                price_span.clear()
                price_span.append(bs4.BeautifulSoup(discount_html, 'html.parser'))

with open('fee-structure.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("6 Stairs Mastery pricing updated!")
