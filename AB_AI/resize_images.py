import glob
import re

files = glob.glob('*.html')
skip_files = ['index.html', 'courses.html', 'login.html', 'register.html', 'forgot-password.html', 'contact.html', 'blog.html', 'gallery.html', 'profile.html', 'fee-structure.html', '6-stairs.html']
course_files = [f for f in files if f not in skip_files]

for course_file in course_files:
    try:
        with open(course_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Target marker to find the image container
        target_marker = '<div class="container" data-animate>\n      <img src="'
        
        if target_marker in content:
            parts = content.split(target_marker, 1)
            before = parts[0]
            after_marker = parts[1]
            
            end_quote_idx = after_marker.find('"')
            
            if end_quote_idx != -1:
                src = after_marker[:end_quote_idx]
                after_src = after_marker[end_quote_idx:]  # starts with " alt="..." class="..." style="..."
                
                # Check if it has our class="rounded-lg" style="..." which we injected manually
                # We want to replace the `width: 100%;` style with a much smaller fixed width or max-width
                # 2 inches is roughly ~200px physically on standard screens. Let's use max-width: 250px
                
                # First let's remove any existing `width: 100%;` and `height: auto;`
                after_src = after_src.replace('width: 100%;', '')
                after_src = after_src.replace('height: auto;', '')
                
                # And remove any stray spaces left behind
                after_src = after_src.replace('style=" ', 'style="')
                after_src = after_src.replace('style="  ', 'style="')
                
                # Now we precisely inject our new max-width limit right into the style tag
                # We know the style tag exists because we injected it, it starts like `style="box-shadow:` or `style=" margin:`
                
                style_idx = after_src.find('style="')
                if style_idx != -1:
                    insert_idx = style_idx + len('style="')
                    # Inject max-width: 250px; width: 100%; height: auto;
                    new_after_src = after_src[:insert_idx] + 'max-width: 250px; width: 100%; height: auto; ' + after_src[insert_idx:]
                else:
                    # Fallback if no style tag somehow
                    # Insert before the end of the img tag
                    end_tag_idx = after_src.find('>')
                    new_after_src = after_src[:end_tag_idx] + ' style="max-width: 250px; width: 100%; height: auto; display: block; margin: 0 auto; margin-bottom: 2rem;"' + after_src[end_tag_idx:]
                
                new_content = before + target_marker + src + new_after_src
                
                with open(course_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"SUCCESS: Resized image in {course_file}")
            else:
                print(f"FAIL: Couldn't find end quote in {course_file}")
        else:
            print(f"FAIL: Target marker not found in {course_file}")

    except Exception as e:
        print(f"ERROR: Could not process {course_file}: {e}")
