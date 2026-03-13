import re

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
            content = f.read()

        # Lenient replace: just look for the first img inside <div class="container" data-animate> which represents our hero
        # And specifically the one we injected with style="width: 100%; height: auto; max-height: 500px...
        
        pattern = r'(<img src=")[^"]+(" alt="[^"]*" class="rounded-lg" style="width: 100%; height: auto; max-height: 500px;)'
        
        new_content = re.sub(pattern, rf'\g<1>assets/images/{img_name}\g<2>', content)
        
        if content != new_content:
            with open(course_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"SUCCESS: Updated {course_file} with {img_name}")
        else:
            print(f"FAIL: No match found to replace in {course_file}")
            
    except FileNotFoundError:
        print(f"Could not find {course_file}")
