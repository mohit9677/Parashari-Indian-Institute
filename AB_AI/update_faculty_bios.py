import os
import re

profile_html_path = r"d:\ParashariTeam\AB_AI\profile.html"

# Rewrite the HTML cards data to expand bios, strip PII, and maintain consistent card heights
html_cards_data = [
    {
        "img": "Dr Sushma Bharti.png",
        "name": "Dr. Sushma Bharti",
        "role": "Medical Astrology Specialist",
        "education": "PhD in Vedic Astrology | MA(Psychology)",
        "bio": "With over 10 years of profound experience bridging the gap between clinical psychology and ancient Vedic sciences, Dr. Bharti offers a uniquely holistic approach to medical astrology and mental well-being."
    },
    {
        "img": "Purvi.png",
        "name": "Purvi",
        "role": "Consultant Astrologer",
        "education": "Specialization in Vedic Astrology",
        "bio": "A dedicated practitioner with 5 years of active consultative experience. Purvi specializes in modern applications of traditional Vedic principles, helping hundreds of clients navigate their life paths with clarity."
    },
    {
        "img": "Dr. Shila Shah.png",
        "name": "Dr. Shila Shah",
        "role": "Prashna Kundli Specialist",
        "education": "PhD in Prashna Kundli (2024)",
        "bio": "An esteemed scholar from Shree Maharshee College of University, Dr. Shah brings deep academic rigor and practical intuition to Prashna Kundli interpretation and private astrological mentorship."
    },
    {
        "img": "bhavna shah.png",
        "name": "Dr. Bhavna Shah",
        "role": "Advanced Timing Expert",
        "education": "PhD in KP, Astakvarga & Sub Niryan",
        "bio": "With an incredible 21 years of mastery in KP astrology and divisional charts, Dr. Bhavna specializes in precise event timing and the complex analysis of Navamsha dynamics."
    },
    {
        "img": "priti dave.png",
        "name": "Priti Dave",
        "role": "Energy Healer & Life Coach",
        "education": "Science Graduate | Pathological Technologist",
        "bio": "Transitioning from a 27-year illustrious medical career as an Operational Manager in healthcare, Priti now channels her deep understanding of human pathology into transformative energy healing and life coaching."
    },
    {
        "img": "asmita acharya.png",
        "name": "Dr. Asmita Acharya",
        "role": "Vedic Astrologer & Palmist",
        "education": "Post-Graduate | Berhampur University",
        "bio": "Bringing 20 years of seasoned expertise in both Vedic charting and classical Palmistry, Dr. Asmita provides comprehensive readings that blend celestial alignments with physiological signatures."
    },
    {
        "img": "mukesh kumar.png",
        "name": "Mukesh Kumar Sawarkar",
        "role": "Traditional Vedic Jyotishi",
        "education": "Master in Vedic Astrology (Acharya)",
        "bio": "A passionate Acharya rooted in traditional Parashari principles. With 7 years of focused dedication, Mukesh delivers precise, classically-founded predictions and effective, simple remedial measures."
    },
    {
        "img": "gaytri khasa.png",
        "name": "Gaytri Khasa",
        "role": "Predictive Analytics Expert",
        "education": "Master's Degree Scholar",
        "bio": "A versatile practitioner with 8 years of experience seamlessly synthesizing Lal Kitab remedies, traditional Vedic frameworks, and modern KP methodologies for highly accurate insights."
    },
    {
        "img": "Divyank Raj.png",
        "name": "Divyank Raj",
        "role": "Occult Sciences Polymath",
        "education": "PhD in Astrology | Master in Astrology",
        "bio": "A remarkable polymath of occult sciences holding advanced degrees and certifications across Palmistry, Tarot, Reiki, Satvik Tantra, and Nadi Astrology, offering a truly multi-dimensional perspective."
    },
    {
        "img": "Sunita Singh.png",
        "name": "Sunita Singh",
        "role": "Remedial Consultant",
        "education": "Acharya & Shastri (MCVA)",
        "bio": "A highly accredited expert in esoteric remedies. Sunita specializes in translating complex planetary afflictions into actionable, powerful solutions through Lal Kitab, Gemology, and authentic Rudraksha therapy."
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
              <span class="faculty-education" style="display:block; margin-bottom:0.5rem; font-size:0.85rem; color:var(--primary-color); font-weight:600;">{card['education']}</span>
              <p style="font-size:0.9rem; line-height:1.6; color:var(--dark-text);">{card['bio']}</p>
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
    new_content = re.sub(
        r'(<div class="faculty-3d-scroll-track">).*?(      </div>\n    </div>\n    </div>\n    </div>\n  </section>)', 
        r'\1' + full_marquee_content + r'\n\2', 
        content, 
        flags=re.DOTALL
    )

    if new_content != content:
        with open(profile_html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully updated profile.html with revised faculty bios.")
    else:
        print("No changes made to profile.html (regex match failed)")
except Exception as e:
    print(f"Error processing profile.html: {e}")
