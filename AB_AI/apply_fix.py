with open('fee-structure.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the wrong price string exactly Without Regex to avoid backtracking
wrong_price = '<del style="color:#999;font-size:0.85em;margin-right:5px;">₹3,999</del> <strong style="color:#d32f2f;">₹2,999</strong> <span class="discount-text"> (with 25% discount)</span>'
new_price = '₹2,000 - ₹3,000'

text = text.replace(wrong_price, new_price)

# Add hover CSS for desktop if missing
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
if 'course-box:hover .course-details' not in text:
    text = text.replace('/* =============  MOBILE FEE CARDS  ============= */', hover_css + '\n          /* =============  MOBILE FEE CARDS  ============= */')

with open('fee-structure.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated prices and added hover CSS.')
