"""Fix the 7 files - inject before </tbody> in comparison table."""
import os

failing_files = [
    "vastu.html", "reiki.html", "lal-kitab.html", "kp-astrology.html",
    "gemstone.html", "face-reading.html", "astrology.html"
]

new_rows = """                        <tr>\r
                            <td>Extended 48-Week Access</td>\r
                            <td class="col-diploma"><i class="fas fa-times c-icon cross"></i></td>\r
                            <td class="col-bachelors"><i class="fas fa-times c-icon cross"></i></td>\r
                            <td class="col-masters"><i class="fas fa-times c-icon cross"></i></td>\r
                            <td class="col-grand-master"><i class="fas fa-check c-icon check"></i></td>\r
                        </tr>\r
                        <tr>\r
                            <td>Free 6 Spiritual Stairs Pathway</td>\r
                            <td class="col-diploma"><i class="fas fa-times c-icon cross"></i></td>\r
                            <td class="col-bachelors"><i class="fas fa-times c-icon cross"></i></td>\r
                            <td class="col-masters"><i class="fas fa-times c-icon cross"></i></td>\r
                            <td class="col-grand-master"><i class="fas fa-check c-icon check"></i></td>\r
                        </tr>\r
                        <tr>\r
                            <td><strong>Digital Badge / E-Certificate</strong></td>\r
                            <td class="col-diploma"><i class="fas fa-check c-icon check"></i></td>\r
                            <td class="col-bachelors"><i class="fas fa-check c-icon check"></i></td>\r
                            <td class="col-masters"><i class="fas fa-check c-icon check"></i></td>\r
                            <td class="col-grand-master"><i class="fas fa-check c-icon check"></i></td>\r
                        </tr>\r
"""

os.chdir(r"d:\ParashariTeam\AB_AI")

for fname in failing_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Extended 48-Week Access' in content:
        print(f"SKIP {fname}: Already has rows")
        continue
    
    # Find the </tbody> in the comparison table
    idx = content.find('</tbody>')
    if idx == -1:
        print(f"SKIP {fname}: No </tbody> found")
        continue
    
    # Insert the new rows right before </tbody>
    content = content[:idx] + new_rows + content[idx:]
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"FIXED {fname}")

print("\nDone!")
