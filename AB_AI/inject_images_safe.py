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
            content = f.read()

        # The image we care about is right after the <div class="container" data-animate>
        # that sits beneath the <section style="padding-top: 60px;">
        
        target_marker = '<div class="container" data-animate>\n      <img src="'
        
        if target_marker in content:
            parts = content.split(target_marker, 1)
            before = parts[0]
            after_marker = parts[1]
            
            # after_marker starts with old_image.png" alt="..."
            end_quote_idx = after_marker.find('"')
            
            if end_quote_idx != -1:
                after = after_marker[end_quote_idx:]
                new_content = before + target_marker + f"assets/images/{img_name}" + after
                
                with open(course_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"SUCCESS: Updated {course_file} with {img_name}")
            else:
                print(f"FAIL: Couldn't find end quote in {course_file}")
        else:
            print(f"FAIL: Target marker not found in {course_file}")

    except FileNotFoundError:
        print(f"Could not find {course_file}")
