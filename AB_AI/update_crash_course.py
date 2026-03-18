import bs4

with open('fee-structure.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

new_courses = [
    "1. Past Life Regression Theory (PLRT)",
    "2. Bhoomi Vastu (Site Energetics) & Prasada Vastu (Architectural Integration)",
    "3. Modern Western Palmistry.",
    "4. Mobile Numerology",
    "5. (Face Reading) Western Physiognomy (Character Analysis)",
    "6. Financial Astrology (Artha)",
    "7. Lal Kitab Basics",
    "8. Medical Astrology",
    "9. The BNN Intensive: A 14-Day Mastery of Bhrigu Nandi Nadi.",
    "10. Modern Career Astrology",
    "11. Business Numerology",
    "12. Vedic Numerology",
    "13. Nadi Jyotish",
    "14. Healing",
    "15. Feng Shui",
    "16. Gemini Jyotishi"
]

def update_crash_courses(scroll_div):
    boxes = scroll_div.find_all('div', class_='course-box')
    # Make sure we iterate up to 16 times depending on what exists
    for i, box in enumerate(boxes):
        if i < len(new_courses):
            name_span = box.find('span', class_='course-name')
            if name_span:
                name_span.string = new_courses[i]

# Find Crash Course sections
# Desktop
table = soup.find('table', class_='table-full')
if table:
    for tr in table.find_all('tr'):
        cat_box = tr.find('div', class_='category-box')
        scroll = tr.find('div', class_='courses-scroll')
        if cat_box and scroll:
            title = cat_box.find('div', class_='cat-title')
            if title and 'Crash Course' in title.text:
                update_crash_courses(scroll)

# Mobile
for card in soup.find_all('div', class_='fee-card'):
    title = card.find('div', class_='fee-card-title')
    scroll = card.find('div', class_='courses-scroll')
    if title and scroll and 'Crash Course' in title.text:
        update_crash_courses(scroll)

# Ensure the DOM hasn't been reconfigured terribly since html.parser preserves formatting relatively well.
with open('fee-structure.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Crash Course names successfully updated!")
