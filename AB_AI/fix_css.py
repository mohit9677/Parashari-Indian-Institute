with open(r'assets\css\blog.css', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

clean_lines = []
for line in lines:
    if 'echo' in line and ('>' in line or '>>' in line):
        break
    clean_lines.append(line)

css = '''
/* Glassmorphism Lock Effect */
.glass-locked {
    position: relative;
    cursor: not-allowed !important;
    user-select: none;
    pointer-events: auto !important; /* To capture hover */
}
.glass-locked::after {
    content: '🚫 Coming Soon';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.45);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    font-weight: bold;
    color: white;
    border-radius: inherit;
    cursor: not-allowed !important;
}
.glass-locked * {
    pointer-events: none !important;
}
.glass-locked:hover {
    transform: none !important;
    box-shadow: 0 12px 30px rgba(89, 28, 33, 0.08) !important;
}
'''
with open(r'assets\css\blog.css', 'w', encoding='utf-8') as f:
    f.writelines(clean_lines)
    f.write(css)

print('Fixed blog.css')
