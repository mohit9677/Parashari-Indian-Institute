import os
import glob
import re

html_files = glob.glob('*.html')
js_files = glob.glob('assets/js/*.js')

files_to_check = html_files + js_files

updated_intro = 0

# 1. Update text "Intro Course" -> "Crash Course"
for file_path in files_to_check:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('Intro Course', 'Crash Course')
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_intro += 1

print(f"Renamed 'Intro Course' to 'Crash Course' in {updated_intro} files.")

# 2. Update fee-structure.html prices
try:
    with open('fee-structure.html', 'r', encoding='utf-8') as f:
        fee_html = f.read()
    
    # Prices to update:
    # Crash Course: 7999 -> 2999
    # Diploma: 10000 -> 4999
    # Bachelors: 17000 -> 9999
    # Masters: 30000 -> 19999
    # Grand Master: 50000 -> 39999
    
    def replace_fee(html, level_name, old_fee, new_fee):
        # Look for the row containing the level name and replace its fee
        # The structure is like:
        # <td class="table-data-cell table-data-right">₹old_fee</td>
        # We want:
        # <td class="table-data-cell table-data-right"><del class="text-muted" style="color: #999; font-size: 0.85em;">₹old_fee</del> <strong style="color: #d32f2f;">₹new_fee</strong></td>
        
        # A simple regex to find the fee cell right after the level name cell
        pattern = rf'(<td[^>]*>{level_name}.*?</td>\s*<td class="table-data-cell table-data-right">)₹?[0-9,]+(</td>)'
        replacement = rf'\1<del class="text-muted" style="color: #999; font-size: 0.85em; margin-right: 5px;">₹{old_fee}</del> <strong style="color: #d32f2f;">₹{new_fee}</strong>\2'
        
        return re.sub(pattern, replacement, html, flags=re.DOTALL | re.IGNORECASE)

    fee_html = replace_fee(fee_html, 'Crash Course', '7,999', '2,999')
    fee_html = replace_fee(fee_html, 'Diploma', '10,000', '4,999')
    fee_html = replace_fee(fee_html, 'Bachelors', '17,000', '9,999')
    fee_html = replace_fee(fee_html, 'Masters', '30,000', '19,999')
    fee_html = replace_fee(fee_html, 'Grand Master', '50,000', '39,999')
    
    # Also update the basic text mentions if any
    fee_html = re.sub(r'₹15,000', r'<del class="text-muted" style="color: #999; font-size: 0.85em; margin-right: 5px;">₹15,000</del> <strong style="color: #d32f2f;">₹4,999</strong>', fee_html)
    
    with open('fee-structure.html', 'w', encoding='utf-8') as f:
        f.write(fee_html)
        
    print("Updated prices in fee-structure.html")
except Exception as e:
    print("Error updating fee structure:", e)
