import glob

files = glob.glob('*.html')
skip_files = ['index.html', 'courses.html', 'login.html', 'register.html', 'forgot-password.html', 'contact.html', 'blog.html', 'gallery.html', 'profile.html', 'fee-structure.html', '6-stairs.html']
course_files = [f for f in files if f not in skip_files]

for course_file in course_files:
    try:
        with open(course_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # The images currently have style="max-width: 250px; width: 100%; height: auto; ..."
        # OR style="max-width: 250px; width: 100%; height: auto; display: block; margin: 0 auto; margin-bottom: 2rem;"
        
        target_marker = '<div class="container" data-animate>\n      <img src="'
        
        if target_marker in content:
            parts = content.split(target_marker, 1)
            before = parts[0]
            after_marker = parts[1]
            
            end_quote_idx = after_marker.find('"')
            
            if end_quote_idx != -1:
                src = after_marker[:end_quote_idx]
                after_src = after_marker[end_quote_idx:]  # starts with " alt="..." class="..." style="..."
                
                # Replace the wrong tiny width with a moderately large width (80-85% of container)
                after_src = after_src.replace('max-width: 250px; width: 100%;', 'width: 85%; max-width: 1000px;')
                after_src = after_src.replace('max-width: 250px;', 'width: 85%; max-width: 1000px;')

                # Make sure it's centered block (if not already there)
                if 'display: block;' not in after_src:
                    style_idx = after_src.find('style="')
                    if style_idx != -1:
                        insert_idx = style_idx + len('style="')
                        after_src = after_src[:insert_idx] + 'display: block; margin: 0 auto; ' + after_src[insert_idx:]

                new_content = before + target_marker + src + after_src
                
                with open(course_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"SUCCESS: Adjusted image in {course_file}")
            else:
                print(f"FAIL: Couldn't find end quote in {course_file}")
        else:
            print(f"FAIL: Target marker not found in {course_file}")

    except Exception as e:
        print(f"ERROR: Could not process {course_file}: {e}")
