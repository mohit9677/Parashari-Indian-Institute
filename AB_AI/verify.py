with open('fee-structure.html', 'r', encoding='utf-8') as f:
    text = f.read()

count_wrong = text.count('₹3,999')
count_right = text.count('₹2,000 - ₹3,000')

print(f'Wrong prices remaining: {count_wrong}')
print(f'Restored prices: {count_right}')

css_present = 'course-box:hover .course-details' in text
print(f'Hover CSS present: {css_present}')
