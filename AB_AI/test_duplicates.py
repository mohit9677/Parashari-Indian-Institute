import glob

for fpath in glob.glob('*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    count = content.count('<!-- TOP URGENCY MARQUEE -->')
    if count != 1:
        print(f"{fpath}: {count}")
    
    header_end = content.find('</header>')
    marquee_start = content.find('<!-- TOP URGENCY MARQUEE -->')
    footer_start = content.find('<footer>')
    
    if count == 1 and marquee_start < header_end + 150:
         print(f"{fpath}: Marquee is near the top (header_end={header_end}, marquee_start={marquee_start})")
         
    if count == 1 and footer_start != -1 and marquee_start < footer_start - 1000:
         print(f"{fpath}: Marquee is far from footer")

