with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the custom inline search bar block (lines 145-157) with the standard one
old = '''            <div style="max-width: 420px; margin-bottom: 1rem;">
                <div class="container-input"
                    style="background: white; border-radius: 30px; display: flex; align-items: center; padding: 0.4rem 1rem; gap: 0.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
                    <svg fill="#aaa" width="16px" height="16px" viewBox="0 0 1920 1920"
                        xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M790.588 1468.235c-373.722 0-677.647-303.924-677.647-677.647 0-373.722 303.925-677.647 677.647-677.647 373.723 0 677.647 303.925 677.647 677.647 0 373.723-303.924 677.647-677.647 677.647Zm596.781-160.715c120.396-138.692 193.807-319.285 193.807-516.932C1581.176 354.748 1226.428 0 790.588 0S0 354.748 0 790.588s354.748 790.588 790.588 790.588c197.647 0 378.24-73.411 516.932-193.807l516.028 516.142 79.963-79.963-516.142-516.028Z"
                            fill-rule="evenodd"></path>
                    </svg>
                    <input type="text" placeholder="Search blogs, topics, categories..." id="blogSearchInput"
                        style="border: none; outline: none; width: 100%; font-size: 0.95rem; background: transparent;">
                </div>
            </div>'''

# Remove CRLF from old to match file
old_crlf = old.replace('\n', '\r\n')

new = '''            <div class="search-container" style="margin-bottom: 1.2rem;">
                <div class="container-input">
                    <input type="text" placeholder="Search blogs, topics, categories..." name="text" class="input" id="blogSearchInput">
                    <svg fill="#000000" width="20px" height="20px" viewBox="0 0 1920 1920"
                        xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M790.588 1468.235c-373.722 0-677.647-303.924-677.647-677.647 0-373.722 303.925-677.647 677.647-677.647 373.723 0 677.647 303.925 677.647 677.647 0 373.723-303.924 677.647-677.647 677.647Zm596.781-160.715c120.396-138.692 193.807-319.285 193.807-516.932C1581.176 354.748 1226.428 0 790.588 0S0 354.748 0 790.588s354.748 790.588 790.588 790.588c197.647 0 378.24-73.411 516.932-193.807l516.028 516.142 79.963-79.963-516.142-516.028Z"
                            fill-rule="evenodd"></path>
                    </svg>
                    <div class="search-results" id="blogSearchResults"></div>
                </div>
            </div>'''

if old_crlf in content:
    content = content.replace(old_crlf, new.replace('\n', '\r\n'), 1)
    print('Replaced with CRLF match')
elif old in content:
    content = content.replace(old, new, 1)
    print('Replaced with LF match')
else:
    # Try fuzzy: find by unique snippet
    marker = 'max-width: 420px; margin-bottom: 1rem;'
    if marker in content:
        # Find start of the div wrapping this
        idx = content.index(marker)
        start = content.rindex('<div', 0, idx)
        # Find the closing </div> after this whole block (the wrapper div)
        depth = 0
        pos = start
        while pos < len(content):
            if content[pos:pos+4] == '<div':
                depth += 1
            elif content[pos:pos+6] == '</div>':
                depth -= 1
                if depth == 0:
                    end = pos + 6
                    break
            pos += 1
        content = content[:start] + new.replace('\n', '\r\n') + content[end:]
        print('Replaced via fuzzy find, start:', start, 'end:', end)
    else:
        print('ERROR: Could not find target block')

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done.')
