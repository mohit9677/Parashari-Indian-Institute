import os

emoji_map = {
    '♈': '<i class="fa-solid fa-om"></i>',
    '📜': '<i class="fa-solid fa-scroll"></i>',
    '✋': '<i class="fa-solid fa-hand-sparkles"></i>',
    '📕': '<i class="fa-solid fa-book-journal-whills"></i>',
    '💎': '<i class="fa-regular fa-gem"></i>',
    '🃏': '<i class="fa-solid fa-layer-group"></i>',
    '⭐': '<i class="fa-solid fa-star"></i>',
    '🏠': '<i class="fa-solid fa-house-chimney"></i>',
    '🔢': '<i class="fa-solid fa-hashtag"></i>',
    '🕉️': '<i class="fa-solid fa-om"></i>',
    '⚕️': '<i class="fa-solid fa-staff-snake"></i>',
    '👤': '<i class="fa-solid fa-user"></i>',
    '🔍': '<i class="fa-solid fa-magnifying-glass"></i>',
    '📿': '<i class="fa-solid fa-om"></i>',
    '🤝': '<i class="fa-solid fa-handshake-angle"></i>',
    '🙌': '<i class="fa-solid fa-hands-holding-circle"></i>',
    '✨': '<i class="fa-solid fa-star-half-stroke"></i>',
    '🔮': '<i class="fa-solid fa-gem"></i>',
    '⛩️': '<i class="fa-solid fa-torii-gate"></i>',
    '🕰️': '<i class="fa-solid fa-hourglass-half"></i>',
    '📈': '<i class="fa-solid fa-chart-line"></i>',
    '💼': '<i class="fa-solid fa-briefcase"></i>',
    '📱': '<i class="fa-solid fa-mobile-screen"></i>',
    '🏢': '<i class="fa-solid fa-building"></i>',

    '✡️': '<i class="fa-solid fa-dharmachakra"></i>',
    '🧘': '<i class="fa-solid fa-person-praying"></i>',
    '🌀': '<i class="fa-solid fa-hurricane"></i>',
    '🌿': '<i class="fa-solid fa-leaf"></i>',
    '⏳': '<i class="fa-solid fa-hourglass-half"></i>'
}

cwd = r'd:\ParashariTeam\AB_AI'

target_files = [
    'assets/js/courses-data.js',
    'courses.html',
    '6-stairs.html'
]
for file in os.listdir(cwd):
    if file.endswith('.html'):
        target_files.append(file)

target_files = list(set(target_files))

for rel_path in target_files:
    full_path = os.path.join(cwd, rel_path)
    if not os.path.exists(full_path):
        continue
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    for emoji, icon in emoji_map.items():
        if emoji in content:
            if rel_path == 'assets/js/courses-data.js':
                # they are inside double quotes: "♈"
                content = content.replace(f'"{emoji}"', f'"{icon}"')
                content = content.replace(f"'{emoji}'", f"'{icon}'")
            else:
                content = content.replace(emoji, icon)
    
    if content != original_content:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {rel_path}')
