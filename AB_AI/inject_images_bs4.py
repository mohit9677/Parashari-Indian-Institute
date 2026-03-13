from bs4 import BeautifulSoup
import os

mapping = {
    'Picture13.png': 'face-reading.html',
    'Picture5.png': 'numerology.html',
    'Picture4.png': 'palmistry.html',
    'Picture3.png': 'tarot.html',
    'Picture7.png': 'nadi-jyotish.html',
    'jyotish vedic astrology.png': 'astrology.html',
    'Vastu.png': 'vastu.html',
    'Gemini_Generated_Image_x9p88cx9p88cx9p8.png': 'lal-kitab.html', 
    'Picture10.png': 'remedy-course.html',
    'Picture9.png': 'medical-astrology.html',
    'Picture8.png': 'rudraksha.html',
    'Picture11.png': 'complete-astrology.html',
    'Picture1.png': 'bnn-astrology.html'
}

for img_name, course_file in mapping.items():
    try:
        with open(course_file, 'r', encoding='utf-8') as f:
            html = f.read()

        soup = BeautifulSoup(html, 'html.parser')
        
        # Find the first image after the padding-top: 60px section 
        # (This is the hero image block we generated earlier)
        hero_sections = soup.find_all('section', style="padding-top: 60px;")
        
        if hero_sections:
            img = hero_sections[0].find('img')
            if img:
                img['src'] = f"assets/images/{img_name}"
                
                with open(course_file, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                print(f"SUCCESS: Updated {course_file} with {img_name}")
            else:
                print(f"FAIL: No img found in hero section of {course_file}")
        else:
            print(f"FAIL: No hero section found in {course_file}")

    except Exception as e:
        print(f"ERROR processing {course_file}: {e}")
