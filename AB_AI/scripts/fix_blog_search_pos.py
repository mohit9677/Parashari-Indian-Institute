with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The search bar to REMOVE from inside hero-header
old_inner_search = '''            <div class="search-container" style="margin-bottom: 1.2rem;">
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
            </div>
            <h1>Parashari Blogs</h1>'''

new_inner = '            <h1>Parashari Blogs</h1>'

# The tablet-search-container block to INSERT before </header>
tablet_search = '''    <div class="tablet-search-container">
      <div class="search-container">
        <div class="container-input">
          <input type="text" placeholder="Search blogs, topics, categories..." name="text" class="input" id="blogSearchInput">
          <svg fill="#666" width="20px" height="20px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M790.588 1468.235c-373.722 0-677.647-303.924-677.647-677.647 0-373.722 303.925-677.647 677.647-677.647 373.723 0 677.647 303.925 677.647 677.647 0 373.723-303.924 677.647-677.647 677.647Zm596.781-160.715c120.396-138.692 193.807-319.285 193.807-516.932C1581.176 354.748 1226.428 0 790.588 0S0 354.748 0 790.588s354.748 790.588 790.588 790.588c197.647 0 378.24-73.411 516.932-193.807l516.028 516.142 79.963-79.963-516.142-516.028Z"
              fill-rule="evenodd"></path>
          </svg>
          <div class="search-results"></div>
        </div>
      </div>
    </div>
    </header>'''

# Step 1: Remove search from inside hero-header
found = False
for sep in ['\n', '\r\n']:
    old_check = old_inner_search.replace('\n', sep)
    if old_check in content:
        content = content.replace(old_check, new_inner.replace('\n', sep), 1)
        print(f'Removed inner search bar (sep={repr(sep)})')
        found = True
        break

if not found:
    # Fuzzy: just find the h1 line and if there's a search-container before it, remove it
    marker = 'id="blogSearchInput"'
    if marker in content:
        idx = content.index(marker)
        # Find start of this block
        start = content.rindex('\n', 0, idx) 
        start = content.rindex('\n', 0, start)
        start = content.rindex('\n', 0, start) + 1
        # Find end - closing of the wrapping div + the h1
        end_marker = '<h1>Parashari Blogs</h1>'
        end = content.index(end_marker, idx)
        content = content[:start] + content[end:]
        print('Removed inner search bar (fuzzy)')
    else:
        print('Inner search bar already removed or not found')

# Step 2: Insert tablet-search-container before </header>
close_header = '    </header>'
if close_header in content:
    content = content.replace(close_header, tablet_search, 1)
    print('Inserted tablet-search-container')
else:
    print('ERROR: </header> not found')

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
