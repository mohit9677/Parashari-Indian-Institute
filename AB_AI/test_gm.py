import re
import os

target_files = [
    "vastu.html", "tarot.html", "rudraksha.html", "reiki.html",
    "numerology.html", "palmistry.html", "nakshatra.html", "lal-kitab.html",
    "kp-astrology.html", "gemstone.html", "face-reading.html", 
    "crystal-healing.html", "astrology.html"
]

def process_file(file_path, is_test=False):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already apparently processed
    if 'data-program="grand-master"' in content:
        print(f"Skipping {file_path} (already processed)")
        return

    # 1. CSS changes
    content = content.replace(
        '.comparison-table th.tier-masters { background: #e0d5c8; }',
        '.comparison-table th.tier-masters { background: #e0d5c8; }\n        .comparison-table th.tier-grand-master { background: #d4a991; }'
    )
    content = content.replace(
        '.col-masters { background: #e0d5c8 !important; }',
        '.col-masters { background: #e0d5c8 !important; }\n        .col-grand-master { background: #d4a991 !important; }'
    )

    # 2. Filter Tab
    content = content.replace(
        '<button class="filter-tab" data-program="masters">Masters</button>',
        '<button class="filter-tab" data-program="masters">Masters</button>\n                <button class="filter-tab" data-program="grand-master">Grand Master</button>'
    )

    # 3. Master > Grand Master block
    # Using regex to find the masters block. 
    # It starts with `<div id="masters" class="program-tab-content"` and ends before `</div>\n    </section>` or `<!-- COMPARISON TABLE SECTION -->`
    
    match = re.search(r'(<div id="masters" class="program-tab-content"[\s\S]*?</div>\s*</div>\s*</div>)', content)
    if not match:
        # Some structure might differ slightly. We look for the masters block up to the closing tags at that level.
        # Fallback regex looking for the ending `<!-- COMPARISON...`
        match = re.search(r'(<div id="masters" class="program-tab-content"[\s\S]*?)</div>\s*</section>', content)
        if not match:
            print(f"Could not find masters block in {file_path}")
            return
        
        # We just take the whole captured block and assume it ends cleanly.
        # Actually a safer way is just to duplicate the masters tab content precisely.
        # We can extract it by counting divs. Let's do a reliable div matcher.

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
                if text[i+1] == '/':
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
                if text[i] != '/':
                    tag_name += text[i]
            elif in_tag and text[i].isspace():
                if not tag_name: continue
                # we have tag_name
                
        return None, -1

    masters_block, end_idx = extract_masters_block(content)

    if not masters_block:
        print(f"Could not extract masters block securely in {file_path}")
        return

    # Transform the masters block into grand-master block
    gm_block = masters_block.replace('id="masters"', 'id="grand-master"')
    gm_block = gm_block.replace('Masters in ', 'Grand Master ')
    gm_block = re.sub(r'(<strong>Module \d+:[^<]*)</strong>', r'\1 (Advanced)</strong>', gm_block)
    # The duration might be 16 WEEKS, 12 WEEKS, etc depending on the course. 
    # Just blind replace "WEEKS" with a regex that targets the number. Actually, masters is usually 16 or somewhat.
    # The user says: 48 weeks.
    gm_block = re.sub(r'<strong>Duration:</strong> \d+ WEEKS [^<]*', '<strong>Duration:</strong> 48 WEEKS comprehensive program', gm_block)
    # Update regular price to 34,999
    gm_block = re.sub(r'Regular Price: ₹\d+(?:,\d+)*', 'Regular Price: ₹34,999', gm_block)
    # Update discounted price to 24,999 - It's wrapped in `>₹...<`
    gm_block = re.sub(r'>₹\d+(?:,\d+)*<', '>₹24,999<', gm_block)

    # Insert gm block right after masters block
    content = content[:end_idx] + "\n\n" + (" "*12) + "<!-- GRAND MASTER TAB -->\n" + gm_block + content[end_idx:]

    # 4. Table headers
    header_find = '                            <th class="tier-masters">\n                                <span class="tier-title">Masters</span>\n                                <span class="tier-price">₹18,699</span>\n                            </th>'
    header_gm = '                            <th class="tier-grand-master">\n                                <span class="tier-title">Grand Master</span>\n                                <span class="tier-price">₹24,999</span>\n                            </th>'
    if header_find not in content:
        # Fallback fuzzy find
        content = re.sub(
            r'(<th class="tier-masters">[\s\S]*?</th>)',
            r'\1\n                            <th class="tier-grand-master">\n                                <span class="tier-title">Grand Master</span>\n                                <span class="tier-price">₹24,999</span>\n                            </th>',
            content
        )
    else:
        content = content.replace(header_find, header_find + '\n' + header_gm)

    # 5. Table rows (for existing modules)
    # Find all `<td class="col-masters">...</td>` and append `<td class="col-grand-master"><i class="fas fa-check c-icon check"></i></td>`
    # Also we want doing this line by line or with regex.
    content = re.sub(
        r'(<td class="col-masters">[\s\S]*?</td>)',
        r'\1\n                            <td class="col-grand-master"><i class="fas fa-check c-icon check"></i></td>',
        content
    )

    # 6. New differentiating rows
    # We must insert them right before the Digital Badge / E-Certificate row
    new_rows = """                        <tr>
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
                        </tr>
                        <tr>"""
    content = re.sub(
        r'(\s*<tr>\s*<td><strong>Digital Badge / E-Certificate)',
        '\n' + new_rows + r'\1',
        content,
        count=1
    )

    out_file = file_path if not is_test else file_path.replace(".html", "_test.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Successfully processed {file_path}")

if __name__ == "__main__":
    os.chdir(r"d:\\ParashariTeam\\AB_AI")
    for f in target_files:
        if os.path.exists(f):
            # Test first just on numerology.html
            if f == "numerology.html":
                process_file(f, is_test=True)
            # We will uncomment the real run after test
            # process_file(f, is_test=False)
