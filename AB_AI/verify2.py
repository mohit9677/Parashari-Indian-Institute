with open('fee-structure.html', 'r', encoding='utf-8') as f:
    text = f.read()

import os
print('Current size:', os.path.getsize('fee-structure.html'))
print('Crash Course price count:', text.count('₹2,499'))
print('Diploma price count:', text.count('₹4,199'))
print('Master price count:', text.count('₹18,699'))

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
if 'course-box:hover .course-details' not in text:
    text = text.replace('/* =============  MOBILE FEE CARDS  ============= */', hover_css + '\n          /* =============  MOBILE FEE CARDS  ============= */')
    with open('fee-structure.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Hover CSS added.')
else:
    print('Hover CSS already present.')
