import re
import os
import glob

target_files = [
    "vastu.html", "tarot.html", "rudraksha.html", "reiki.html",
    "numerology.html", "palmistry.html", "nakshatra.html", "lal-kitab.html",
    "kp-astrology.html", "gemstone.html", "face-reading.html", 
    "crystal-healing.html", "astrology.html"
]

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already processed
    if 'data-program="grand-master"' in content:
        print(f"Skipping {file_path} (already processed)")
        return

    # --- 1. CSS Adds ---
    if '.tier-grand-master' not in content:
        content = content.replace(
            '.comparison-table th.tier-masters { background: #e0d5c8; }',
            '.comparison-table th.tier-masters { background: #e0d5c8; }\n        .comparison-table th.tier-grand-master { background: #d4a991; }'
        )
        content = content.replace(
            '.col-masters { background: #e0d5c8 !important; }',
            '.col-masters { background: #e0d5c8 !important; }\n        .col-grand-master { background: #d4a991 !important; }'
        )

    # --- 2. Filter Tab ---
    if 'data-program="grand-master"' not in content:
        content = content.replace(
            '<button class="filter-tab" data-program="masters">Masters</button>',
            '<button class="filter-tab" data-program="masters">Masters</button>\n                <button class="filter-tab" data-program="grand-master">Grand Master</button>'
        )

    # --- 3. Extract and Replicate Masters Block ---
    def extract_masters_block(text):
        start_idx = text.find('<div id="masters" class="program-tab-content"')
        if start_idx == -1: return None, -1
        
        div_count = 0
        in_tag = False
        tag_name = ""
        is_closing = False
        
        for i in range(start_idx, len(text)):
            if text[i] == '<':
                in_tag = True
                tag_name = ""
                if i+1 < len(text) and text[i+1] == '/':
                    is_closing = True
                else:
                    is_closing = False
            elif text[i] == '>':
                in_tag = False
                if tag_name.startswith("div "): tag_name = "div"
                if tag_name == "div":
                    if not is_closing:
                        div_count += 1
                    else:
                        div_count -= 1
                        if div_count == 0:
                            return text[start_idx:i+1], i+1
            elif in_tag and not text[i].isspace():
                if text[i] != '/' and not is_closing:
                    tag_name += text[i]
                elif is_closing and text[i] != '/':
                    tag_name += text[i]
            elif in_tag and text[i].isspace():
                if not tag_name: continue
                # we have tag_name
                
        return None, -1

    masters_block, end_idx = extract_masters_block(content)

    if masters_block and 'Grand Master' not in masters_block:
        # Transform the masters block into grand-master block
        gm_block = masters_block.replace('id="masters"', 'id="grand-master"')
        
        # Make it display none by default just in case masters isn't
        gm_block = gm_block.replace('display: block;', 'display: none;')
        if 'display: none;' not in gm_block:
            gm_block = gm_block.replace('class="program-tab-content"', 'class="program-tab-content" style="display: none;"')
        
        # Names
        gm_block = gm_block.replace('Masters in ', 'Grand Master ')
        # Add (Advanced) to module names explicitly inside the card titles
        gm_block = re.sub(r'(<strong>Module \d+:[^<]*)', r'\1 (Advanced)', gm_block)
        
        # Duration info updates
        gm_block = re.sub(r'<strong>Duration:</strong> \d+ WEEKS [^\n<]*', r'<strong>Duration:</strong> 48 WEEKS comprehensive program', gm_block)
        
        # Pricing updates
        gm_block = re.sub(r'Regular Price: ₹[\d,]+', 'Regular Price: ₹34,999', gm_block)
        # Big price find
        gm_block = re.sub(r'>₹[\d,]+<', '>₹24,999<', gm_block)

        # Append right after masters block
        content = content[:end_idx] + "\n\n" + (" "*12) + "<!-- GRAND MASTER TAB -->\n" + (" "*12) + gm_block + content[end_idx:]
    else:
        print(f"Could not extract masters block securely in {file_path}")

    # --- 4. Table headers ---
    header_gm = '                            <th class="tier-grand-master">\n                                <span class="tier-title">Grand Master</span>\n                                <span class="tier-price">₹24,999</span>\n                            </th>'
    
    # Needs to match all variations of the Masters header
    content = re.sub(
        r'(<th class="tier-masters">[\s\S]*?</th>)',
        r'\1\n' + header_gm,
        content,
        count=1
    )

    # --- 5. Table rows for existing modules ---
    # Need to match `</td>` and `</tr>` closely to inject inside the row
    # The current approach is matching `col-masters` td and appending `col-grand-master` td
    
    # We do a split by <tr> and </tr> to be safer
    new_rows = []
    lines = content.splitlines(True)
    in_tbody = False
    
    # We can also do a regex replacement on lines containing `col-masters`
    for i, line in enumerate(lines):
        if '<td class="col-masters">' in line and '</tr>' in lines[i+1]:
            # we need to add the grand-master column here
            pass

    # A better regex for adding the grand master column to EACH row that has `col-masters`
    # Match `<td class="col-masters">...</td>` and add `<td class="col-grand-master">...</td>`
    # Wait, the content in masters might be a check or a cross. Grand master has checks everywhere masters has, PLUS new ones.
    # The user asked: "add the same modules as in the master but with a 'advance' label in it" (we did this in the grid above).
    # Then "add the grand master category in the tick/cross table and add some more fields for differentiating"
    
    def repl_col_masters(match):
        masters_td = match.group(0)
        # Grand master has everything masters has (checks)
        # So we just copy the masters td exactly, but switch the class
        gm_td = masters_td.replace('col-masters', 'col-grand-master')
        return masters_td + '\n                            ' + gm_td

    content = re.sub(r'<td class="col-masters">.*?</td>', repl_col_masters, content)

    # --- 6. New differentiating rows ---
    # Insert them right before "Digital Badge / E-Certificate"
    differentiating_rows = """                        <tr>
                            <td>Extended 48-Week Access</td>
                            <td class="col-diploma"><i class="fas fa-times c-icon cross"></i></td>
                            <td class="col-bachelors"><i class="fas fa-times c-icon cross"></i></td>
                            <td class="col-masters"><i class="fas fa-times c-icon cross"></i></td>
                            <td class="col-grand-master"><i class="fas fa-check c-icon check"></i></td>
                        </tr>
                        <tr>
                            <td>Free 6 Spiritual Stairs Pathway</td>
                            <td class="col-diploma"><i class="fas fa-times c-icon cross"></i></td>
                            <td class="col-bachelors"><i class="fas fa-times c-icon cross"></i></td>
                            <td class="col-masters"><i class="fas fa-times c-icon cross"></i></td>
                            <td class="col-grand-master"><i class="fas fa-check c-icon check"></i></td>
                        </tr>\n"""
                        
    content = re.sub(
        r'(\s*<tr>\s*<td><strong>Digital)',
        differentiating_rows + r'\1',
        content,
        count=1
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Successfully processed {file_path}")

if __name__ == "__main__":
    os.chdir(r"d:\\ParashariTeam\\AB_AI")
    for f in target_files:
        if os.path.exists(f):
            process_file(f)
        else:
            print(f"File not found: {f}")
