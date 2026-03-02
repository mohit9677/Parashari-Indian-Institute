import glob

for fpath in glob.glob('*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    count = content.count('urgency-marquee-container')
    pos = content.find('urgency-marquee-container')
    h_end = content.find('</header>')
    f_start = content.find('<footer>')
    
    if count != 1 or (f_start != -1 and pos < f_start - 3000):
        print(f"{fpath}: count={count}, pos={pos}, f_start={f_start}")

