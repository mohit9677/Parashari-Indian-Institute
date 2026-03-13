import re
import glob

files = glob.glob('*.html')
skip_files = ['index.html', 'courses.html', 'login.html', 'register.html', 'forgot-password.html', 'contact.html', 'blog.html', 'gallery.html', 'profile.html', 'fee-structure.html', '6-stairs.html']
course_files = [f for f in files if f not in skip_files]

def run():
    count = 0
    # The pattern string
    pattern = (
        r'<section style="padding-top: 60px;">\s*'
        r'<div class="container">\s*'
        r'<div class="grid grid-2 grid-gap-3">\s*'
        r'<div data-animate>\s*'
        r'(<h1[^>]*>.*?</h1>)\s*'
        r'(<p[^>]*>.*?</p>)\s*'
        r'(.*?)\s*'
        r'</div>\s*'
        r'<div data-animate>\s*'
        r'(<img.*?>)\s*'
        r'</div>\s*'
        r'</div>\s*'
        r'</div>\s*'
        r'</section>'
    )
    section_pattern = re.compile(pattern, re.DOTALL)

    for filepath in course_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        match = section_pattern.search(content)
        if not match:
            print(f"Skipping {filepath} - no match")
            continue
            
        h1 = match.group(1)
        sub_p = match.group(2)
        rest_content = match.group(3)
        img = match.group(4)
        
        img_src_match = re.search(r'src="([^"]+)"', img)
        img_alt_match = re.search(r'alt="([^"]+)"', img)
        src = img_src_match.group(1) if img_src_match else ''
        alt = img_alt_match.group(1) if img_alt_match else ''
        
        new_img = f'<img src="{src}" alt="{alt}" class="rounded-lg" style="width: 100%; height: auto; max-height: 500px; object-fit: cover; box-shadow: 0 10px 30px rgba(0,0,0,0.1); margin: 0 auto; display: block; margin-bottom: 2rem;">'
        
        new_section = (
            f'<section style="padding-top: 60px;">\n'
            f'    <div class="container text-center">\n'
            f'      {h1}\n'
            f'      {sub_p}\n'
            f'    </div>\n'
            f'    <div class="container" data-animate>\n'
            f'      {new_img}\n'
            f'    </div>\n'
            f'    <div class="container" data-animate>\n'
            f'      {rest_content}\n'
            f'    </div>\n'
            f'  </section>'
        )
        
        content = content[:match.start()] + new_section + content[match.end():]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        count += 1
        
    print(f"Successfully processed {count} files.")

if __name__ == '__main__':
    run()
