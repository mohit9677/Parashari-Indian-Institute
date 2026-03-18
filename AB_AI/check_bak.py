import re
try:
    with open('fee-structure.html.bak', 'r', encoding='utf-8') as f:
        text = f.read()
    prices = re.findall(r'<span class=\"course-price\">(.*?)</span>', text)
    if prices:
        for i, p in enumerate(prices[:10]):
            print(f'Bak Price {i+1}: {p}')
    else:
        print('No course-price found in fee-structure.html.bak')
except Exception as e:
    print('Error:', e)
