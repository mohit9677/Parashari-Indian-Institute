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

        # Regular expression to find the hero image in the stacked layout and replace its src
        # The hero image is currently: <img src="assets/images/..." alt="..." class="rounded-lg" style="width: 100%; height: auto; max-height: 500px; object-fit: cover; box-shadow: 0 10px 30px rgba(0,0,0,0.1); margin: 0 auto; display: block; margin-bottom: 2rem;">
        
        pattern = r'(<div class="container" data-animate>\s*<img src="assets/images/)[^"]+(")'
        
        # Replace the filename
        new_content = re.sub(pattern, rf'\g<1>{img_name}\g<2>', content)
        
        if content != new_content:
            with open(course_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {course_file} with {img_name}")
        else:
            print(f"No match found to replace in {course_file}")
            
    except FileNotFoundError:
        print(f"Could not find {course_file}")
