import os

# 1. Clean up and update blog.css
css_path = r'd:\ParashariTeam\AB_AI\assets\css\blog.css'
with open(css_path, 'rb') as f:
    content_bytes = f.read()

# Replace utf-16 null bytes if they exist due to Powershell
content_str = content_bytes.replace(b'\x00', b'').decode('utf-8', errors='ignore')

# Truncate at the end of original file before our mangled additions
marker = '/* Filtering Animations */'
idx = content_str.find(marker)

if idx != -1:
    # also find where the keyframes end to keep them
    end_keyframes = content_str.find('}', idx)
    if end_keyframes != -1:
        clean_css = content_str[:end_keyframes + 1] + '\n\n'
    else:
        clean_css = content_str[:idx] + '\n\n'
else:
    clean_css = content_str + '\n\n'

new_css = '''/* Glassmorphism Lock Effect */
.glass-locked {
    position: relative;
    cursor: not-allowed !important;
    user-select: none;
    pointer-events: auto !important;
}

.glass-locked::after {
    content: '\\f023  Coming Soon';
    font-family: 'Font Awesome 5 Free', 'Font Awesome 6 Free', sans-serif;
    font-weight: 900;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.45);
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    color: #333;
    border-radius: inherit;
    cursor: not-allowed !important;
}

.glass-locked .blog-card-img, 
.glass-locked .blog-featured-img img {
    filter: blur(15px) grayscale(100%);
    opacity: 0.2;
}

.glass-locked * {
    pointer-events: none !important;
}

.glass-locked:hover {
    transform: none !important;
    box-shadow: 0 12px 30px rgba(89, 28, 33, 0.08) !important;
}
'''

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(clean_css + new_css)

# 2. Update blog.html to hide free courses
html_path = r'd:\ParashariTeam\AB_AI\blog.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Make sure it isn't already hidden
if 'class="free-courses-section"' in html_content and 'style="display: none;"' not in html_content.split('class="free-courses-section"')[1][:20]:
    html_content = html_content.replace('<section class="free-courses-section">', '<section class="free-courses-section" style="display: none;">')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

print("Cleanup and updates successful.")
