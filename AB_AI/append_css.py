with open(r'd:\ParashariTeam\AB_AI\assets\css\blog.css', 'a', encoding='utf-8') as f:
    f.write('''
/* Glassmorphism Lock Effect */
.glass-locked {
    position: relative;
    cursor: not-allowed !important;
    user-select: none;
    pointer-events: auto !important;
}
.glass-locked::after {
    content: '🚫 Coming Soon';
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
    font-weight: bold;
    color: #333;
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
''')
print("CSS appended to blog.css")
