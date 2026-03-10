import os

# Course data including the two description paragraphs and first bullet
courses = {
    'complete-astrology.html': {
        'desc1': 'The Complete Astrology Course is a comprehensive program that covers all aspects of Vedic astrology from birth chart analysis to advanced prediction techniques, giving you a thorough command of this ancient science.',
        'desc2': 'Learn to interpret planetary positions, houses, nakshatras, dashas, and transits to provide accurate and insightful readings for yourself and others.',
        'bullet1': '✓ Birth chart reading &amp; analysis',
        'module1': 'Introduction to Vedic Astrology',
        'module3': 'Nakshatras &amp; Their Influence',
        'module4': 'Dasha Systems &amp; Predictions',
        'module5': 'Advanced Yoga &amp; Remedies',
    },
    'feng-shui.html': {
        'desc1': 'Feng Shui is a powerful ancient art and science that focuses on balancing energies in any given space to assure health and good fortune for people inhabiting it.',
        'desc2': 'Learn to apply Feng Shui principles to homes and offices, use the Bagua map, select auspicious colors and materials, and create spaces that support your goals and aspirations.',
        'bullet1': '✓ Bagua map and energy mapping',
        'module1': 'Introduction to Feng Shui',
        'module3': 'Bagua Map &amp; Its Applications',
        'module4': 'Feng Shui for Homes',
        'module5': 'Feng Shui for Business',
    },
    'gemini-jyotish.html': {
        'desc1': 'Gemini Jyotish (Jaimini Astrology) is an advanced and highly precise branch of Vedic astrology that uses special dashas, padas, and yogas for extremely accurate life predictions.',
        'desc2': 'Learn the unique Jaimini system of chart analysis, Chara Dasha, Karakamsha, Arudha Padas, and other sophisticated techniques to offer deep and precise astrological analysis.',
        'bullet1': '✓ Jaimini Sutras &amp; principles',
        'module1': 'Introduction to Jaimini Astrology',
        'module3': 'Chara Dasha System',
        'module4': 'Karakamsha &amp; Padas',
        'module5': 'Predictive Techniques',
    },
    'gemstone.html': {
        'desc1': 'Gemstone Science involves the study of precious and semi-precious stones and their alignment with planetary energies to bring luck, health, and prosperity to the wearer.',
        'desc2': 'Learn to identify gemstones, understand their planetary correspondences, and prescribe the right gemstones as powerful astrological remedies.',
        'bullet1': '✓ Gemstone identification &amp; quality',
        'module1': 'Introduction to Gemstone Science',
        'module3': 'Gemstone Quality &amp; Grading',
        'module4': 'Prescribing Gemstones',
        'module5': 'Activation &amp; Wearing Rituals',
    },
    'healing.html': {
        'desc1': 'Healing encompasses a wide range of techniques designed to balance the mind, body, and spirit by removing energy blockages and restoring the natural flow of life force energy.',
        'desc2': 'Learn powerful healing modalities including chakra balancing, aura cleansing, pranic healing, and various energy healing practices to promote total well-being.',
        'bullet1': '✓ Chakra system &amp; balancing',
        'module1': 'Introduction to Energy Healing',
        'module3': 'Aura Reading &amp; Cleansing',
        'module4': 'Pranic Healing Techniques',
        'module5': 'Advanced Energy Work',
    },
    'nakshatra.html': {
        'desc1': 'Nakshatra study dives deep into the 27 lunar mansions of Vedic astrology, each with its own deity, symbol, and influence, offering profound micro-level insights into personality and life events.',
        'desc2': 'Learn the qualities, lords, and influences of all 27 Nakshatras, understand Nakshatra-based compatibility, and use this system for highly detailed astrological predictions.',
        'bullet1': '✓ All 27 Nakshatras in depth',
        'module1': 'Introduction to Nakshatras',
        'module3': 'Nakshatra Lords &amp; Deities',
        'module4': 'Nakshatra Compatibility',
        'module5': 'Muhurta &amp; Electional Astrology',
    },
    'reiki.html': {
        'desc1': 'Reiki is a Japanese energy healing technique developed by Mikao Usui that involves the channeling of universal life force energy through the hands to promote physical, emotional, and spiritual healing.',
        'desc2': 'Learn all levels of Reiki from beginner to master, understand the chakra system, practice distant healing, and use sacred Reiki symbols to amplify healing energy.',
        'bullet1': '✓ Reiki Level 1, 2 &amp; Master',
        'module1': 'Introduction to Reiki',
        'module3': 'Reiki Level 2 &mdash; Symbols &amp; Distance',
        'module4': 'Reiki Master Level',
        'module5': 'Chakra Balancing with Reiki',
    },
    'student-section.html': {
        'desc1': 'Welcome to the Parashari Institute Student Section. Here you will find all the resources, mentorship programs, and support you need to excel in your spiritual and astrological studies.',
        'desc2': 'Access study materials, connect with faculty, schedule one-on-one sessions, and join a vibrant community of like-minded learners from across the country and around the world.',
        'bullet1': '✓ Study materials &amp; resources',
        'module1': 'Orientation &amp; Onboarding',
        'module3': 'Mentorship Sessions',
        'module4': 'Community &amp; Events',
        'module5': 'Assessments &amp; Certification',
    },
}

# The old line text to match (exactly as stored in the HTML with indentation)
OLD_DESC1 = '                    <p>Tarot is a powerful divination tool using 78 symbolic cards to provide guidance, insights, and\r\n                        answers to life\'s questions. Each card carries deep archetypal meanings that reveal hidden\r\n                        truths, future possibilities, and spiritual guidance.</p>'

OLD_DESC2 = '                    <p>Learn to read Major Arcana, Minor Arcana, and Court Cards, master various spreads, and develop\r\n                        your intuition to provide accurate, meaningful readings.</p>'

OLD_BULLET1 = '                        <li class="mb-0-75">\u2713 78 card meanings &amp; symbolism</li>'

OLD_MODULE1 = '                        <li class="mb-0-75"><strong>Module 1:</strong> Tarot History &amp; Structure</li>'
OLD_MODULE3 = '                        <li class="mb-0-75"><strong>Module 3:</strong> Minor Arcana &amp; Suits</li>'
OLD_MODULE4 = '                        <li class="mb-0-75"><strong>Module 4:</strong> Court Cards &amp; Personalities</li>'
OLD_MODULE5 = '                        <li class="mb-0-75"><strong>Module 5:</strong> Spreads &amp; Reading Techniques</li>'

for filename, d in courses.items():
    if not os.path.exists(filename):
        print(f'Skipping {filename}: not found')
        continue

    with open(filename, 'rb') as f:
        raw = f.read()

    content = raw.decode('utf-8')

    # Replace description 1
    new_desc1 = f'                    <p>{d["desc1"]}</p>'
    content = content.replace(OLD_DESC1, new_desc1)

    # Replace description 2
    new_desc2 = f'                    <p>{d["desc2"]}</p>'
    content = content.replace(OLD_DESC2, new_desc2)

    # Replace bullet 1
    new_bullet1 = f'                        <li class="mb-0-75">{d["bullet1"]}</li>'
    content = content.replace(OLD_BULLET1, new_bullet1)

    # Replace module 1 if still old
    new_module1 = f'                        <li class="mb-0-75"><strong>Module 1:</strong> {d["module1"]}</li>'
    content = content.replace(OLD_MODULE1, new_module1)

    # Replace module 3 if still old
    new_module3 = f'                        <li class="mb-0-75"><strong>Module 3:</strong> {d["module3"]}</li>'
    content = content.replace(OLD_MODULE3, new_module3)

    # Replace module 4 if still old
    new_module4 = f'                        <li class="mb-0-75"><strong>Module 4:</strong> {d["module4"]}</li>'
    content = content.replace(OLD_MODULE4, new_module4)

    # Replace module 5 if still old
    new_module5 = f'                        <li class="mb-0-75"><strong>Module 5:</strong> {d["module5"]}</li>'
    content = content.replace(OLD_MODULE5, new_module5)

    # Also fix alt attr on the image
    content = content.replace('alt="Tarot Reading"', f'alt="{filename.replace(\".html\", \"\").replace(\"-\", \" \").title()}"')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Updated: {filename}')

print("All done!")
