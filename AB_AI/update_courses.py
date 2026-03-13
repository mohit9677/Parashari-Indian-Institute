import re

def get_description(title):
    title_lower = title.lower()
    if 'vastu' in title_lower:
        return "Master the ancient science of architecture. Transform spaces to attract positive energy, prosperity, and lasting harmony into your life."
    elif 'numerology' in title_lower:
        return "Unlock the hidden meaning behind numbers. Use this powerful knowledge to attract success, improve relationships, and align with your potential."
    elif 'palmistry' in title_lower:
        return "Decode the lines of destiny hidden in your hands. Master this art to confidently guide yourself and others through life's defining moments."
    elif 'tarot' in title_lower:
        return "Connect with your intuition through Tarot. Learn how to interpret the cards accurately to provide deep insights and empowering guidance."
    elif 'face ' in title_lower or 'physiognomy' in title_lower:
        return "Read facial features to reveal hidden personality traits. Enhance your relationships and negotiation skills by truly understanding anyone."
    elif 'heal' in title_lower or 'reiki' in title_lower or 'crystal' in title_lower or 'chakra' in title_lower:
        return "Harness universal energy for profound healing. Learn to clear energetic blocks, restore vitality, and bring deep peace to the mind and body."
    elif 'lal kitab' in title_lower or 'remedy' in title_lower or 'rudraksha' in title_lower or 'gemstone' in title_lower or 'mantra' in title_lower or 'yantra' in title_lower or 'tantra' in title_lower:
        return "Discover potent traditional remedies. Learn precise, practical solutions to overcome life's biggest obstacles and manifest your desired outcomes."
    elif 'nadi' in title_lower or 'kp ' in title_lower or 'bnn' in title_lower or 'parashari' in title_lower or 'nakshatra' in title_lower:
        return "Dive into advanced predictive techniques. Gain mastery over specialized systems that offer pinpoint accuracy and clarity for the future."
    elif 'past life' in title_lower or 'plrt' in title_lower:
        return "Uncover unresolved past karma to heal current life blocks. Empower yourself to live with greater clarity, purpose, and emotional freedom."
    elif 'astrology' in title_lower or 'jyotish' in title_lower or 'horoscope' in title_lower:
        return "Discover the profound secrets of astrology. Learn practical techniques to guide life choices, anticipate events, and help others find their path."
    else:
        return f"Deepen your understanding of {title}. Gain unique insights and practical skills that will empower you to create positive change in your life."

with open('courses.html', 'r', encoding='utf-8') as f:
    text = f.read()

def replacer(match):
    full_match = match.group(0)
    title = match.group(1)
    old_desc = match.group(2)
    new_desc = get_description(title)
    return full_match.replace(f"<p>{old_desc}</p>", f'<p class="course-desc-text">{new_desc}</p>')

new_text = re.sub(r'<h3 class="card-title">(.*?)</h3>\s*</div>\s*<p>(.*?)</p>', replacer, text, flags=re.DOTALL)

css_rule = """
    /* Guarantee structured alignment for all course cards */
    .course-desc-text {
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
      min-height: 60px; /* Aligns textual height across varying card lengths */
      margin-bottom: 12px;
      line-height: 1.4;
    }
"""

if ".course-desc-text {" not in new_text:
    new_text = new_text.replace("</style>", css_rule + "\n  </style>")

with open('courses.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated courses.html successfully")
