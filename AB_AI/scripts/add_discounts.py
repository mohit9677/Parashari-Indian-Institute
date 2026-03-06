import os
import re

def main():
    directory = r"d:\ParashariTeam\AB_AI"
    updated_files = 0

    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # cleanup previous injected labels (handling multiple runs)
            content = re.sub(r'\n?\s*<span class="discount-tag"[^>]*></span>', '', content)
            content = re.sub(r' <span class="discount-text"[^>]*>[^<]*</span>', '', content)

            # Match <del>₹XX</del> <strong>₹YY</strong>
            pattern = r'(<del[^>]*>₹([\d,]+)</del>[\s\n\r]*<strong[^>]*>₹([\d,]+)</strong>)'
            
            matches = list(re.finditer(pattern, content))
            if matches:
                 # Work backwards to not invalidate indices
                for m in reversed(matches):
                    full_match = m.group(1)
                    orig_val = int(m.group(2).replace(',', ''))
                    disc_val = int(m.group(3).replace(',', ''))
                    
                    if orig_val > 0 and disc_val < orig_val:
                        percent = int(round((1 - disc_val / orig_val) * 100))
                        
                        replacement = f'{full_match} <span class="discount-text">(with {percent}% discount)</span>'
                        content = content[:m.start()] + replacement + content[m.end():]
                        
                        # Find actual .card container by looking at previous divs and exact classes
                        div_matches = list(re.finditer(r'<div([^>]*)>', content[:m.start()], re.IGNORECASE))
                        for div_match in reversed(div_matches):
                            attrs = div_match.group(1)
                            class_match = re.search(r'class="([^"]*)"', attrs, re.IGNORECASE)
                            if class_match:
                                classes = class_match.group(1).split()
                                if 'card' in classes:
                                    insert_pos = div_match.end()
                                    ribbon = f'\n        <span class="discount-tag" data-discount="{percent}% Discount"></span>'
                                    content = content[:insert_pos] + ribbon + content[insert_pos:]
                                    break

            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated_files += 1
                print(f"Updated {filename}")

    print(f"Total HTML files updated: {updated_files}")

if __name__ == "__main__":
    main()
