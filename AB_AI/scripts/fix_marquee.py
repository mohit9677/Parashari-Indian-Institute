import glob
import re

count = 0
for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    changed = False

    # Target 1: Add missing </div> at the end of the urgency marquee block
    target1 = '        <a href="register.html" class="marquee-btn">Apply Now</a>\n      </div>\n    </div>'
    replacement1 = '        <a href="register.html" class="marquee-btn">Apply Now</a>\n      </div>\n    </div>\n  </div>'
    
    # We only apply if it's not already fixed (i.e. if the replacement is NOT already there)
    if target1 in html and replacement1 not in html:
        html = html.replace(target1, replacement1)
        changed = True

    # Target 2: Remove dangling </div> at the start of body
    body_fix_patterns = [
        ('<body style="background-color: #ffffff;">\n</div>', '<body style="background-color: #ffffff;">'),
        ('<body>\n</div>', '<body>'),
        ('<body class="light-theme">\n</div>', '<body class="light-theme">')
    ]

    for target2, rep2 in body_fix_patterns:
        if target2 in html:
            html = html.replace(target2, rep2)
            changed = True
            
    # Also handle cases where there might be spaces or carriage returns
    # Using regex for generic body tag followed by exactly \s*</div>
    dangling_div_pattern = re.compile(r'(<body[^>]*>)\s*</div>')
    
    # Wait, the string replacement is safer. Let's try regex if string replacement misses any.
    match = dangling_div_pattern.search(html)
    if match:
        html = dangling_div_pattern.sub(r'\1', html)
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1
        
print(f'Fixed missing and dangling tags in {count} files.')
