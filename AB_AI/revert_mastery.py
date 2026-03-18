import bs4
with open('fee-structure.html', 'r', encoding='utf-8') as f:
    text = f.read()
soup = bs4.BeautifulSoup(text, 'html.parser')

def get_pricing_html(cut, current):
    try:
        c1 = int(cut.replace(',', ''))
        c2 = int(current.replace(',', ''))
        percent = round(100 - (c2 / c1 * 100))
        discount_txt = f' (with {percent}% discount)'
    except:
        discount_txt = ''
    return f'<del style="color:#999;font-size:0.85em;margin-right:5px;">₹{cut}</del> <strong style="color:#d32f2f;">₹{current}</strong> <span class="discount-text">{discount_txt}</span>'

# We ONLY want to reset 6 Stairs Mastery back to original or clear its invalid prices.
# Actually, the user's instructions for 6 Stairs Mastery was just text change.
# Let's check what 6 Stairs Mastery currently has for prices and what it had originally.
# Wait, I did git checkout fee-structure.html. Let me just re-run the whole parser with exact match bugfix instead!
