with open('AB_AI/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<div class="grid grid-2 grid-gap-2">', '<div class="grid grid-3 grid-gap-2">')
content = content.replace('<!--\n        <div class="premium-gold-card"', '<div class="premium-gold-card"')
content = content.replace('</a>\n        </div>\n        -->', '</a>\n        </div>')

with open('AB_AI/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
