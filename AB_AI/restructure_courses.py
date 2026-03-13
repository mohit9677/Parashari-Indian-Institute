import re
import glob
import os

files = glob.glob('*.html')
skip_files = ['index.html', 'courses.html', 'login.html', 'register.html', 'forgot-password.html', 'contact.html', 'blog.html', 'gallery.html', 'profile.html', 'fee-structure.html', '6-stairs.html']
course_files = [f for f in files if f not in skip_files]

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the hero section
    # Note: astrology.html has a broken div: `<section class="hero-section hero-gradient" style="position: relative;">\n\n    </div>`
    # We need a robust regex to capture from <section class="hero-section" to </section>
    
    hero_pattern = re.compile(r'<section class="hero-section hero-gradient"[^>]*>([\s\S]*?)</section>')
    hero_match = hero_pattern.search(content)
    
    if not hero_match:
        return False
        
    hero_content = hero_match.group(1)
    
    # Extract h1 and p
    h1_match = re.search(r'(<h1[^>]*>[\s\S]*?</h1>)', hero_content)
    p_match = re.search(r'(<p>[\s\S]*?</p>)', hero_content)
    
    if not h1_match or not p_match:
        return False
        
    h1_tag = h1_match.group(1)
    p_tag = p_match.group(1)
    
    # Let's add styling to h1 and p so they look good in the main grid
    h1_styled = h1_tag.replace('class="color-secondary"', 'class="color-primary" style="font-size: 2.5rem; margin-bottom: 0.5rem;"')
    p_styled = p_tag.replace('<p>', '<p style="font-size: 1.2rem; color: #666; margin-bottom: 2rem; font-weight: 500;">')
    
    header_injection = f"{h1_styled}\n          {p_styled}\n          "
    
    # Remove the hero section entirely
    content = content[:hero_match.start()] + content[hero_match.end():]
    
    # Now find the next <section> and add some top padding since we removed the hero
    next_section_pattern = re.compile(r'<section>')
    content = next_section_pattern.sub('<section style="padding-top: 60px;">', content, count=1)
    
    # Find the first <div data-animate> inside this section to inject the headers
    animate_pattern = re.compile(r'(<div data-animate>\s*)')
    content = animate_pattern.sub(r'\1' + header_injection.replace('\\', '\\\\'), content, count=1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return True

processed_count = 0
for f in course_files:
    if process_file(f):
        processed_count += 1
        print(f"Processed {f}")

print(f"\nTotal processed: {processed_count}")
