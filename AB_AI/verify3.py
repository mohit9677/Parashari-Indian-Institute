with open('fee-structure.html', 'r', encoding='utf-8') as f:
    text = f.read()

count_crash = text.count('₹2,499')
count_diploma = text.count('₹4,199')
count_bach = text.count('₹8,999')
count_master = text.count('₹18,699')
count_grand = text.count('₹24,999')

print(f'Crash Course: {count_crash} (Expected 32: 16*2)')
print(f'Diploma: {count_diploma} (Expected 26: 13*2)')
print(f'Bachelor: {count_bach} (Expected 26: 13*2)')
print(f'Master: {count_master} (Expected 26: 13*2)')
print(f'Grand Master: {count_grand} (Expected 12 or 24 or 26 depending on original count)')

# Check 6 Stairs Mastery price still original
print('6 Stairs Flexible Pricing count:', text.count('Flexible Pricing'))
