import os

mapping = {
    'Picture1.png': 'numerology.html',
    'Picture3.png': 'astrology.html',
    'Picture4.png': 'kp-astrology.html',
    'Picture5.png': 'gemstone.html',
    'Vastu.png': 'vastu.html',
    'Picture7.png': 'lal-kitab.html',
    'Picture8.png': 'face-reading.html',
    'Picture9.png': 'reiki.html',
    'Picture10.png': 'tarot.html',
    'Picture11.png': 'nakshatra.html',
    'Picture13.png': 'palmistry.html'
}

for img_name, course_file in mapping.items():
    try:
        with open(course_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Target marker to find the image container
        target_marker = '<div class="container" data-animate>\n      <img src="'
        
        # We also need to remove the truncation styles if they exist anywhere in this image tag
        # The easiest way is to split by target_marker, then find the end of the img tag
        
        if target_marker in content:
            parts = content.split(target_marker, 1)
            before = parts[0]
            after_marker = parts[1]
            
            # after_marker starts with old_image.png" alt="..." class="..." style="..."
            # we need to replace the image src, AND replace the style string
            
            end_quote_idx = after_marker.find('"')
            
            if end_quote_idx != -1:
                after_src = after_marker[end_quote_idx:]  # starts with " alt="..."
                
                # Now remove the truncating styles from the rest of the file (or just this tag)
                # Since we know the exact string, we can replace it directly
                old_style = 'max-height: 500px; object-fit: cover;'
                if old_style in after_src:
                    after_src = after_src.replace(old_style, '')
                
                # Also check without spaces just in case
                old_style_2 = 'max-height:500px;object-fit:cover;'
                if old_style_2 in after_src:
                    after_src = after_src.replace(old_style_2, '')
                    
                # We can also do a more generous replace across the whole file to make sure no images are truncated
                
                new_content = before + target_marker + f"assets/images/{img_name}" + after_src
                
                # Global replace for the truncation just to be absolutely sure
                new_content = new_content.replace('max-height: 500px;', '')
                new_content = new_content.replace('object-fit: cover;', '')
                
                with open(course_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"SUCCESS: Updated {course_file} with {img_name} and removed truncation.")
            else:
                print(f"FAIL: Couldn't find end quote in {course_file}")
        else:
            print(f"FAIL: Target marker not found in {course_file}")

    except FileNotFoundError:
        print(f"FAIL: Could not find {course_file}")
