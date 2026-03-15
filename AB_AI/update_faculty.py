import os
import shutil
import re

source_dir = r"D:\ParashariTeam"
dest_dir = r"d:\ParashariTeam\AB_AI\assets\images"
profile_html_path = r"d:\ParashariTeam\AB_AI\profile.html"

images_to_copy = [
    "Dr Sushma Bharti.png",
    "Purvi.png",
    "Dr. Shila Shah.png",
    "bhavna shah.png",
    "priti dave.png",
    "asmita acharya.png",
    "mukesh kumar.png",
    "gaytri khasa.png",
    "Divyank Raj.png",
    "Sunita Singh.png"
]

# 1. Copy images
for img in images_to_copy:
    src = os.path.join(source_dir, img)
    dst = os.path.join(dest_dir, img)
    if os.path.exists(src):
        try:
            shutil.copy2(src, dst)
            print(f"Copied {img}")
        except Exception as e:
            print(f"Failed to copy {img}: {e}")
    else:
        print(f"Source image not found: {src}")

# 2. Rebuild HTML String for the Faculty portion
html_cards_data = [
    {
        "img": "Dr Sushma Bharti.png",
        "name": "Dr. Sushma Bharti",
        "role": "Medical Astrology Specialist",
        "education": "PhD in Vedic Astrology | MA(Psychology)",
        "bio": "10 years of experience. Specialization in clinical psychology."
    },
    {
        "img": "Purvi.png",
        "name": "Purvi",
        "role": "Astrologer",
        "education": "Specialization in Vedic Astrology",
        "bio": "Experience of 5 years. Currently working with Astrosage & adiastro app."
    },
    {
        "img": "Dr. Shila Shah.png",
        "name": "Dr. Shila Shah",
        "role": "Prashna Kundli Specialist",
        "education": "PhD in Prashna Kundli (2024)",
        "bio": "From Shree Maharshee College of University. Private tuition in Astrology for 5 years. <br>Email: shilashah8@gmail.com | Mob: 9820877434 / 7208182464"
    },
    {
        "img": "bhavna shah.png",
        "name": "Dr. Bhavna Shah",
        "role": "Astrology Expert",
        "education": "PhD in sub niryan kp navmansh and astakvarga (7th house divorce yog)",
        "bio": "21 years of experience. Private tuition in astrology since 2010."
    },
    {
        "img": "priti dave.png",
        "name": "Priti Dave",
        "role": "Energy Healer & Coach",
        "education": "B.Sc. Micro. CMLT, Pathological Technologist",
        "bio": "27 years experience as paramedical in Dr. Lal. Retired as Operational Manager W. Bengal and Orissa."
    },
    {
        "img": "asmita acharya.png",
        "name": "Dr. Asmita Acharya",
        "role": "Vedic Astrologer & Palmist",
        "education": "Post graduation in Berhampur University",
        "bio": "20 years of experience. <br>Email: Smitaacharya2@gmail.com | Mob: 9871886717"
    },
    {
        "img": "mukesh kumar.png",
        "name": "Mukesh Kumar Sawarkar",
        "role": "Vedic Jyotishi",
        "education": "Master in Vedic Astrology (Acharya)",
        "bio": "7 years of experience in Vedic Astrology."
    },
    {
        "img": "gaytri khasa.png",
        "name": "Gaytri Khasa",
        "role": "Lal Kitab, Vedic & KP Specialist",
        "education": "Masters Degree",
        "bio": "8 years of experience. <br>Email: astrogaytri5000@gmail.com | Mob: 9311091152"
    },
    {
        "img": "Divyank Raj.png",
        "name": "Divyank Raj",
        "role": "Astrology & Healing Expert",
        "education": "PhD in Astrology | Master in Astrology",
        "bio": "Multiple certifications in Palmistry, Face Reading, Tarot, Numerology, Reiki Healing, Angel Therapy, Satvik Tantra, Lal Kitab, KP & Nadi."
    },
    {
        "img": "Sunita Singh.png",
        "name": "Sunita Singh",
        "role": "Vedic, Lal Kitab & Rudraksha Expert",
        "education": "Acharya & Shastri from MCVA | MA Jyotish (Pursuing)",
        "bio": "Specialist in Gemology and Rudraksha with multiple PG Diplomas."
    }
]

def build_card_html(card):
    return f"""
        <!-- Faculty Card: {card['name']} -->
        <div class="faculty-card">
          <div class="faculty-img-wrapper">
            <img src="assets/images/{card['img']}" alt="{card['name']}" class="faculty-img">
          </div>
          <div class="faculty-info">
            <h4 class="faculty-name">{card['name']}</h4>
            <p class="faculty-role">{card['role']}</p>
            <div class="faculty-bio">
              <span class="faculty-education">{card['education']}</span>
              <p>{card['bio']}</p>
            </div>
          </div>
        </div>"""

html_cards_block = "".join([build_card_html(c) for c in html_cards_data])

# Duplicate for the infinite scroll marquee
full_marquee_content = "\n" + html_cards_block + "\n\n        <!-- DUPLICATE SET FOR INFINITE LOOP -->\n" + html_cards_block + "\n"

# 3. Inject into profile.html
try:
    with open(profile_html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the track container and replace contents
    pattern = re.compile(r'(<div class="faculty-3d-scroll-track">).*?(      </div>\n    </div>\n    </div>\n    </div>\n  </section>)', re.DOTALL)
    
    # We matched the track opening div and the closing tags of the section.
    # We will reconstruct carefully manually instead to avoid breaking the layout boundaries.
    
    # Let's target purely between <div class="faculty-3d-scroll-track"> and its closing tag.
    # This requires looking closely at the file bounds.
    start_tag = '<div class="faculty-3d-scroll-track">'
    end_pattern = '      </div>\n    </div>\n    </div>\n    </div>\n  </section>'
    
    # The current profile.html has:
    # <div class="faculty-3d-scroll-track">
    # [all the 10 faculty cards including the DUPLICATE comment]
    # </div>
    # </div> 
    # </div>...
    
    # Simpler regex purely based on the section
    new_content = re.sub(
        r'(<div class="faculty-3d-scroll-track">).*?(      </div>\n    </div>\n    </div>\n    </div>\n  </section>)', 
        r'\1' + full_marquee_content + r'\n\2', 
        content, 
        flags=re.DOTALL
    )

    if new_content != content:
        with open(profile_html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully updated profile.html with new faculty cards.")
    else:
        print("No changes made to profile.html (regex match failed)")
except Exception as e:
    print(f"Error processing profile.html: {e}")

