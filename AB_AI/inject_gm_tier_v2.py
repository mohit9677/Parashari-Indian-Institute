"""
inject_gm_tier_v2.py
Adds Grand Master tier to all 13 course pages:
  1. Grand Master filter tab button (already done by v1)
  2. Grand Master tab content (cloned from Masters with Advanced labels)
  3. Grand Master column in comparison table header
  4. Grand Master column in each comparison table row
  5. Two new differentiating rows (48-week access, 6 Stairs free)
"""
import re
import os

target_files = [
    "vastu.html", "tarot.html", "rudraksha.html", "reiki.html",
    "numerology.html", "palmistry.html", "nakshatra.html", "lal-kitab.html",
    "kp-astrology.html", "gemstone.html", "face-reading.html", 
    "crystal-healing.html", "astrology.html"
]

def extract_div_block(text, start_marker):
    """Extract a complete <div ...>...</div> block using brace-counting on raw text."""
    start_idx = text.find(start_marker)
    if start_idx == -1:
        return None, -1
    
    depth = 0
    i = start_idx
    while i < len(text):
        # Look for <div or </div
        if text[i:i+4] == '<div' and (i+4 >= len(text) or text[i+4] in (' ', '>', '\r', '\n', '\t')):
            depth += 1
            i += 4
        elif text[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                return text[start_idx:i+6], i+6
            i += 6
        else:
            i += 1
    return None, -1


def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    changes_made = False

    # --- 1. CSS: Add grand-master tier styles if not present ---
    if '.tier-grand-master' not in content:
        content = content.replace(
            '.comparison-table th.tier-masters { background: #e0d5c8; }',
            '.comparison-table th.tier-masters { background: #e0d5c8; }\n        .comparison-table th.tier-grand-master { background: #d4a991; }'
        )
        content = content.replace(
            '.col-masters { background: #e0d5c8 !important; }',
            '.col-masters { background: #e0d5c8 !important; }\n        .col-grand-master { background: #d4a991 !important; }'
        )
        changes_made = True

    # --- 2. Filter Tab: Add Grand Master button if not present ---
    if 'data-program="grand-master"' not in content:
        content = content.replace(
            '<button class="filter-tab" data-program="masters">Masters</button>',
            '<button class="filter-tab" data-program="masters">Masters</button>\r\n                <button class="filter-tab" data-program="grand-master">Grand Master</button>'
        )
        changes_made = True

    # --- 3. Grand Master Tab Content (clone from Masters) ---
    if 'id="grand-master"' not in content:
        masters_block, end_idx = extract_div_block(content, '<div id="masters" class="program-tab-content"')
        
        if masters_block:
            gm_block = masters_block
            
            # Change ID
            gm_block = gm_block.replace('id="masters"', 'id="grand-master"')
            
            # Ensure display: none
            gm_block = gm_block.replace('display: block;', 'display: none;')
            if 'display: none;' not in gm_block:
                gm_block = gm_block.replace('class="program-tab-content"', 'class="program-tab-content" style="display: none;"')
            
            # Rename "Masters in X" to "Grand Master X"
            gm_block = gm_block.replace('Masters in ', 'Grand Master ')
            
            # Add (Advanced) to module names
            gm_block = re.sub(r'(<strong>Module \d+:[^<]*)', r'\1 (Advanced)', gm_block)
            
            # Duration: 48 WEEKS
            gm_block = re.sub(r'<strong>Duration:</strong>\s*\d+\s*WEEKS[^<\r\n]*', '<strong>Duration:</strong> 48 WEEKS comprehensive program', gm_block)
            
            # Pricing
            gm_block = re.sub(r'Regular Price: ₹[\d,]+', 'Regular Price: ₹34,999', gm_block)
            gm_block = re.sub(r'>₹[\d,]+<', '>₹24,999<', gm_block)
            
            # Save badge
            gm_block = re.sub(r'Save \d+% Today', 'Save 29% Today', gm_block)

            # Insert after masters block
            insert_point = end_idx
            insert_html = "\r\n\r\n            <!-- GRAND MASTER TAB -->\r\n            " + gm_block
            content = content[:insert_point] + insert_html + content[insert_point:]
            changes_made = True
            print(f"  [OK] Grand Master tab content injected")
        else:
            print(f"  [WARN] Could not find masters block in {file_path}")

    # --- 4. Comparison Table: Add Grand Master column header ---
    if 'tier-grand-master' not in content:
        gm_header = '                            <th class="tier-grand-master">\r\n                                <span class="tier-title">Grand Master</span>\r\n                                <span class="tier-price">₹24,999</span>\r\n                            </th>'
        
        content = re.sub(
            r'(<th class="tier-masters">[\s\S]*?</th>)',
            r'\1\r\n' + gm_header,
            content,
            count=1
        )
        changes_made = True
        print(f"  [OK] Grand Master table header added")

    # --- 5. Comparison Table: Add Grand Master column to each row ---
    if 'col-grand-master' not in content:
        def add_gm_column(match):
            masters_td = match.group(0)
            gm_td = masters_td.replace('col-masters', 'col-grand-master')
            return masters_td + '\r\n                            ' + gm_td
        
        content = re.sub(r'<td class="col-masters">.*?</td>', add_gm_column, content)
        changes_made = True
        print(f"  [OK] Grand Master columns added to all rows")

    # --- 6. Differentiating rows (before Digital Badge) ---
    if 'Extended 48-Week Access' not in content:
        new_rows = '                        <tr>\r\n                            <td>Extended 48-Week Access</td>\r\n                            <td class="col-diploma"><i class="fas fa-times c-icon cross"></i></td>\r\n                            <td class="col-bachelors"><i class="fas fa-times c-icon cross"></i></td>\r\n                            <td class="col-masters"><i class="fas fa-times c-icon cross"></i></td>\r\n                            <td class="col-grand-master"><i class="fas fa-check c-icon check"></i></td>\r\n                        </tr>\r\n                        <tr>\r\n                            <td>Free 6 Spiritual Stairs Pathway</td>\r\n                            <td class="col-diploma"><i class="fas fa-times c-icon cross"></i></td>\r\n                            <td class="col-bachelors"><i class="fas fa-times c-icon cross"></i></td>\r\n                            <td class="col-masters"><i class="fas fa-times c-icon cross"></i></td>\r\n                            <td class="col-grand-master"><i class="fas fa-check c-icon check"></i></td>\r\n                        </tr>\r\n'
        
        content = re.sub(
            r'(\s*<tr>\s*<td><strong>Digital Badge)',
            '\r\n' + new_rows + r'\1',
            content,
            count=1
        )
        changes_made = True
        print(f"  [OK] Differentiating rows added")

    if changes_made:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  => Saved {file_path}")
    else:
        print(f"  => No changes needed for {file_path}")


if __name__ == "__main__":
    os.chdir(r"d:\ParashariTeam\AB_AI")
    for f in target_files:
        if os.path.exists(f):
            print(f"\nProcessing: {f}")
            process_file(f)
        else:
            print(f"File not found: {f}")
    print("\n=== Done ===")
