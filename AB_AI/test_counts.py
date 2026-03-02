import glob

for fpath in glob.glob('*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    count = content.count('urgency-marquee-container')
    print(f"{fpath}: {count}")

