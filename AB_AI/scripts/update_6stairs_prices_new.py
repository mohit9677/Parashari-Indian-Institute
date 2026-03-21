import os
import re
from bs4 import BeautifulSoup

# Define the exact file paths we know contain 6 stairs prices
base_dir = r"d:\ParashariTeam\AB_AI"
files_to_check = [
    "6-stairs.html",
    "yantra.html",
    "mantra.html",
    "tantra.html",
    "chakra-balancing.html",
    "6-stairs-remedies.html",
    "plrt-6-stairs.html"
]

# For the dedicated pages, we can just replace 3,499 with 3,999 and 2,499 with 2,999 globally 
# because these pages are exclusively for 6 Stairs courses.
for file_name in files_to_check:
    file_path = os.path.join(base_dir, file_name)
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Simple replace
    new_content = content.replace("₹3,499", "₹3,999").replace("₹2,499", "₹2,999")
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated dedicated page: {file_name}")

# Now for pages that contain BOTH 6 stairs and other courses, we need carefully scoped replacements.
# fee-structure.html
fee_file = os.path.join(base_dir, "fee-structure.html")
if os.path.exists(fee_file):
    with open(fee_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    modified = False
    # Desktop
    for tr in soup.find_all('tr'):
        cat = tr.find('div', class_='cat-title')
        scroll = tr.find('div', class_='courses-scroll')
        if cat and scroll and '6 Stairs' in cat.text:
            for box in scroll.find_all('div', class_='course-box'):
                price_span = box.find('span', class_='course-price')
                if price_span:
                    old_html = str(price_span)
                    new_html = old_html.replace('₹3,499', '₹3,999').replace('₹2,499', '₹2,999')
                    if old_html != new_html:
                        new_span = BeautifulSoup(new_html, 'html.parser')
                        price_span.replace_with(new_span)
                        modified = True
                        
    # Mobile
    for card in soup.find_all('div', class_='fee-card'):
        cat = card.find('div', class_='fee-card-title')
        scroll = card.find('div', class_='courses-scroll')
        if cat and scroll and '6 Stairs' in cat.text:
            for box in scroll.find_all('div', class_='course-box'):
                price_span = box.find('span', class_='course-price')
                if price_span:
                    old_html = str(price_span)
                    new_html = old_html.replace('₹3,499', '₹3,999').replace('₹2,499', '₹2,999')
                    if old_html != new_html:
                        new_span = BeautifulSoup(new_html, 'html.parser')
                        price_span.replace_with(new_span)
                        modified = True

    if modified:
        with open(fee_file, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print("Updated fee-structure.html via BeautifulSoup")
    else:
        # Fallback to regex if bs4 structure was different
        pass
        
# For index.html
index_file = os.path.join(base_dir, "index.html")
if os.path.exists(index_file):
    with open(index_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # In index.html, we look for premium-gold-card with data-category="6 Stairs"
    def replace_index_price(match):
        text = match.group(0)
        return text.replace("₹3,499", "₹3,999").replace("₹2,499", "₹2,999")
    
    new_content = re.sub(
        r'<div class="premium-gold-card"[^>]*data-category="6 Stairs".*?</div>\s*</div>\s*</div>',
        replace_index_price,
        content,
        flags=re.DOTALL
    )
    if new_content != content:
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Updated index.html")
        
# For courses.html
courses_file = os.path.join(base_dir, "courses.html")
if os.path.exists(courses_file):
    with open(courses_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # In courses.html, 6 Stairs is maybe not in courses-data.js? 
    # Let's replace within elements that clearly say "6 Stairs Mastery"
    def replace_courses_price(match):
        text = match.group(0)
        return text.replace("₹3,499", "₹3,999").replace("₹2,499", "₹2,999")
        
    new_content = re.sub(
        r'<div class="mb-4">.*?<h2\b[^>]*>.*?6 Stairs Mastery.*?</h2>(.*?)</div>\s*<!--',
        replace_courses_price,
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    # Also just in case it's generated, let's look for exact prices in 6 stairs blocks
    if new_content == content:
        # fallback chunk replacer
        chunks = content.split('<h2')
        new_chunks = []
        for chunk in chunks:
            if '6 Stairs' in chunk:
                chunk = chunk.replace("₹3,499", "₹3,999").replace("₹2,499", "₹2,999")
            new_chunks.append(chunk)
        new_content = '<h2'.join(new_chunks)

    if new_content != content:
        with open(courses_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Updated courses.html")

print("Price update script finished.")
