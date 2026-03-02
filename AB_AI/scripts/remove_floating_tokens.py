import os
import glob
import re

html_files = glob.glob('*.html')

# Regex to match the floating tokens block
token_pattern = re.compile(r'<!--\s*FLYING REGISTER TOKENS\s*-->.*?</div>', re.DOTALL | re.IGNORECASE)

updated_count = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if token_pattern.search(content):
        # Remove the block
        content = token_pattern.sub('', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1
        print(f"Removed tokens from: {file_path}")

print(f"Total files updated: {updated_count}")
