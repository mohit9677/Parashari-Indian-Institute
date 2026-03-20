import os

css_path = r'd:\ParashariTeam\AB_AI\assets\css\blog.css'

new_css = '''

/* --- ADDED FOR GLASSMORPHISM LOCK --- */
.glass-locked {
    position: relative;
    cursor: not-allowed !important;
    user-select: none;
    pointer-events: auto !important;
}

.glass-locked::after {
    content: '\\f023  Coming Soon';
    font-family: 'Font Awesome 6 Free', 'Font Awesome 5 Free', sans-serif;
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
    filter: blur(20px) grayscale(100%);
    opacity: 0.1;
}

.glass-locked * {
    pointer-events: none !important;
}

.glass-locked:hover {
    transform: none !important;
    box-shadow: 0 12px 30px rgba(89, 28, 33, 0.08) !important;
}
'''

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(new_css)

print("Appended successfully.")
