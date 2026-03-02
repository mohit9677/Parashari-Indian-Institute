with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all href="#" with href="login.html" strictly for the btn-course-primary Start Now buttons
old = '<a href="#" class="btn-course-primary">\n                                Start Now'
old_crlf = old.replace('\n', '\r\n')
new = '<a href="login.html" class="btn-course-primary">\n                                Start Now'

import re
# Use regex to be safe about spaces
content = re.sub(
    r'<a href="#" class="btn-course-primary">\s*Start Now',
    r'<a href="login.html" class="btn-course-primary">\n                                Start Now',
    content
)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated Start Now links to login.html')
