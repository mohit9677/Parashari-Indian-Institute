import os

# Course data: title, subtitle, icon, description, intro2, bullet points, modules, why_study_title, cta_title, cta_desc, img
courses = {
    'complete-astrology.html': {
        'title': 'Complete Astrology Course',
        'subtitle': 'Master the Complete System of Vedic Astrological Sciences',
        'icon': '🌟',
        'desc1': 'The Complete Astrology Course is a comprehensive program that covers all aspects of Vedic astrology—from birth chart analysis to advanced prediction techniques—giving you a thorough command of this ancient science.',
        'desc2': 'Learn to interpret planetary positions, houses, nakshatras, dashas, and transits to provide accurate and insightful readings for yourself and others.',
        'bullets': ['Birth chart reading & analysis', 'Planetary strengths & yogas', 'Dasha & transit predictions', 'Remedial astrology techniques'],
        'module1': 'Foundations of Vedic Astrology',
        'module2': 'Planets, Signs & Houses',
        'module3': 'Nakshatras & Their Influence',
        'module4': 'Dasha Systems & Predictions',
        'module5': 'Advanced Yoga & Remedies',
        'module6': 'Professional Consultation Skills',
        'why_h': 'Why Study Complete Astrology?',
        'why1_title': 'Career Opportunity', 'why1_desc': 'Build a rewarding career as a professional Vedic astrologer.',
        'why2_title': 'Deep Wisdom', 'why2_desc': 'Unlock the secrets of time, fate, and human psychology.',
        'why3_title': 'Help Others', 'why3_desc': 'Provide meaningful guidance to people facing life challenges.',
        'cta_h': 'Ready to Master Vedic Astrology?',
        'cta_p': 'Join our complete astrology program and transform your understanding of the cosmos.',
        'program_title': 'Our Complete Astrology Program',
        'img': 'vedic-astrology-new.jpg',
    },
    'feng-shui.html': {
        'title': 'Feng Shui',
        'subtitle': 'Harmonize Your Space for Health, Wealth & Happiness',
        'icon': '⛩️',
        'desc1': 'Feng Shui is a powerful ancient Chinese art and science that focuses on balancing energies in any given space to assure health and good fortune for people inhabiting it.',
        'desc2': 'Learn to apply Feng Shui principles to homes and offices, use the Bagua map, select auspicious colors and materials, and create spaces that support your goals and aspirations.',
        'bullets': ['Bagua map and energy mapping', 'Five elements theory', 'Auspicious colors & materials', 'Remedies for negative energy'],
        'module1': 'Introduction to Feng Shui',
        'module2': 'Five Elements & Energies',
        'module3': 'Bagua Map & Its Applications',
        'module4': 'Feng Shui for Homes',
        'module5': 'Feng Shui for Business',
        'module6': 'Advanced Remedies & Cures',
        'why_h': 'Why Study Feng Shui?',
        'why1_title': 'Home Transformation', 'why1_desc': 'Transform your living space into a sanctuary of positive energy.',
        'why2_title': 'Career Growth', 'why2_desc': 'Become a certified Feng Shui consultant and help clients thrive.',
        'why3_title': 'Well-being', 'why3_desc': 'Improve health, relationships and finances through space design.',
        'cta_h': 'Ready to Master Feng Shui?',
        'cta_p': 'Join our Feng Shui program and learn to create harmonious environments.',
        'program_title': 'Our Feng Shui Diploma Program',
        'img': 'institute-building-modern.jpg',
    },
    'gemini-jyotish.html': {
        'title': 'Gemini Jyotish',
        'subtitle': 'Advanced Precision Astrology for Accurate Predictions',
        'icon': '♊',
        'desc1': 'Gemini Jyotish (Jaimini Astrology) is an advanced and highly precise branch of Vedic astrology that uses special dashas, padas, and yogas for extremely accurate life predictions.',
        'desc2': 'Learn the unique Jaimini system of chart analysis, Chara Dasha, Karakamsha, Arudha Padas, and other sophisticated techniques to offer deep and precise astrological analysis.',
        'bullets': ['Jaimini Sutras & principles', 'Chara Dasha calculations', 'Karakamsha & Arudha Padas', 'Accurate event prediction'],
        'module1': 'Introduction to Jaimini Astrology',
        'module2': 'Jaimini Sutras & Principles',
        'module3': 'Chara Dasha System',
        'module4': 'Karakamsha & Padas',
        'module5': 'Predictive Techniques',
        'module6': 'Case Studies & Practice',
        'why_h': 'Why Study Gemini Jyotish?',
        'why1_title': 'Advanced Skills', 'why1_desc': 'Gain advanced predictive skills beyond basic Parashari astrology.',
        'why2_title': 'Precision', 'why2_desc': 'Use powerful Jaimini methods for highly accurate predictions.',
        'why3_title': 'Expertise', 'why3_desc': 'Stand out as an expert in rare and specialized astrological systems.',
        'cta_h': 'Ready to Master Gemini Jyotish?',
        'cta_p': 'Join our Gemini Jyotish program and unlock advanced prediction techniques.',
        'program_title': 'Our Gemini Jyotish Program',
        'img': 'gemini-card.png',
    },
    'gemstone.html': {
        'title': 'Gemstone Science',
        'subtitle': 'Harness the Healing Power of Precious Stones',
        'icon': '💎',
        'desc1': 'Gemstone Science involves the study of precious and semi-precious stones and their alignment with planetary energies to bring luck, health, and prosperity to the wearer.',
        'desc2': 'Learn to identify gemstones, understand their planetary correspondences, and prescribe the right gemstones as powerful astrological remedies.',
        'bullets': ['Gemstone identification & quality', 'Planetary gem correspondences', 'Prescribing remedial gemstones', 'Wearing & activation rituals'],
        'module1': 'Introduction to Gemstone Science',
        'module2': 'Planetary Gem Correspondences',
        'module3': 'Gemstone Quality & Grading',
        'module4': 'Prescribing Gemstones',
        'module5': 'Activation & Wearing Rituals',
        'module6': 'Professional Gemstone Practice',
        'why_h': 'Why Study Gemstone Science?',
        'why1_title': 'Unique Specialty', 'why1_desc': 'Offer gemstone remedies as a complementary astrology service.',
        'why2_title': 'Powerful Remedies', 'why2_desc': 'Help clients harness planetary energies through the right stones.',
        'why3_title': 'Business Opportunity', 'why3_desc': 'Build a career in gemstone consultation and jewelry advisory.',
        'cta_h': 'Ready to Master Gemstone Science?',
        'cta_p': 'Join our Gemstone Science Diploma and learn the power of precious stones.',
        'program_title': 'Our Gemstone Science Diploma',
        'img': 'gemstone.jpg',
    },
    'healing.html': {
        'title': 'Healing',
        'subtitle': 'Unlock the Power of Energy Healing for Mind, Body & Soul',
        'icon': '💆',
        'desc1': 'Healing encompasses a wide range of techniques designed to balance the mind, body, and spirit by removing energy blockages and restoring the natural flow of life force energy.',
        'desc2': 'Learn powerful healing modalities including chakra balancing, aura cleansing, pranic healing, and various energy healing practices to promote total well-being.',
        'bullets': ['Chakra system & balancing', 'Aura reading & cleansing', 'Pranic healing techniques', 'Meditation & breathwork'],
        'module1': 'Introduction to Energy Healing',
        'module2': 'The Chakra System',
        'module3': 'Aura Reading & Cleansing',
        'module4': 'Pranic Healing Techniques',
        'module5': 'Advanced Energy Work',
        'module6': 'Professional Healing Practice',
        'why_h': 'Why Study Healing?',
        'why1_title': 'Personal Wellness', 'why1_desc': 'Transform your own health and well-being with healing practices.',
        'why2_title': 'Help Others', 'why2_desc': 'Become a certified healer and guide others to total wellness.',
        'why3_title': 'Growing Field', 'why3_desc': 'Join the booming holistic health and wellness industry.',
        'cta_h': 'Ready to Master the Art of Healing?',
        'cta_p': 'Join our Healing program and unlock your innate ability to heal.',
        'program_title': 'Our Healing Master Program',
        'img': 'chakra-balancing.jpg',
    },
    'nakshatra.html': {
        'title': 'Nakshatra',
        'subtitle': 'Unlock the Mysteries of the 27 Lunar Mansions',
        'icon': '✨',
        'desc1': 'Nakshatra study dives deep into the 27 lunar mansions of Vedic astrology, each with its own deity, symbol, and influence, offering profound micro-level insights into personality and life events.',
        'desc2': 'Learn the qualities, lords, and influences of all 27 Nakshatras, understand Nakshatra-based compatibility, and use this system for highly detailed astrological predictions.',
        'bullets': ['All 27 Nakshatras in depth', 'Nakshatra lords & deities', 'Compatibility analysis', 'Muhurta & electional astrology'],
        'module1': 'Introduction to Nakshatras',
        'module2': 'The 27 Nakshatra Profiles',
        'module3': 'Nakshatra Lords & Deities',
        'module4': 'Nakshatra Compatibility',
        'module5': 'Muhurta & Electional Astrology',
        'module6': 'Advanced Nakshatra Predictions',
        'why_h': 'Why Study Nakshatras?',
        'why1_title': 'Deeper Accuracy', 'why1_desc': 'Enhance your astrological predictions with Nakshatra precision.',
        'why2_title': 'Compatibility', 'why2_desc': 'Offer Nakshatra-based compatibility analysis for matchmaking.',
        'why3_title': 'Electional Astrology', 'why3_desc': 'Help clients choose the most auspicious timing for key events.',
        'cta_h': 'Ready to Master Nakshatra Astrology?',
        'cta_p': 'Join our Nakshatra program and deepen your command over Vedic astrology.',
        'program_title': 'Our Nakshatra Bachelor Program',
        'img': 'gold_zodiac_wheel.png',
    },
    'reiki.html': {
        'title': 'Reiki Healing',
        'subtitle': 'Channel Universal Life Force Energy for Total Healing',
        'icon': '🙌',
        'desc1': 'Reiki is a Japanese energy healing technique developed by Mikao Usui that involves the channeling of universal life force energy through the hands to promote physical, emotional, and spiritual healing.',
        'desc2': 'Learn all levels of Reiki from beginner to master, understand the chakra system, practice distant healing, and use sacred Reiki symbols to amplify healing energy.',
        'bullets': ['Reiki Level 1, 2 & Master', 'Sacred Reiki symbols', 'Distant healing techniques', 'Chakra balancing with Reiki'],
        'module1': 'Introduction to Reiki',
        'module2': 'Reiki Level 1 — Self Healing',
        'module3': 'Reiki Level 2 — Symbols & Distance',
        'module4': 'Reiki Master Level',
        'module5': 'Chakra Balancing with Reiki',
        'module6': 'Professional Reiki Practice',
        'why_h': 'Why Study Reiki Healing?',
        'why1_title': 'Personal Healing', 'why1_desc': 'Heal yourself and maintain high energy levels daily.',
        'why2_title': 'Help Family & Friends', 'why2_desc': 'Offer Reiki healing to loved ones any time, any place.',
        'why3_title': 'Professional Practice', 'why3_desc': 'Build a rewarding career as a certified Reiki healer.',
        'cta_h': 'Ready to Master Reiki Healing?',
        'cta_p': 'Join our Reiki Healing Diploma and begin your healing journey today.',
        'program_title': 'Our Reiki Healing Diploma Program',
        'img': 'healing.jpg',
    },
    'student-section.html': {
        'title': 'Student Section',
        'subtitle': 'Resources, Mentorship & Support for Every Student',
        'icon': '🎓',
        'desc1': 'Welcome to the Parashari Institute Student Section. Here you will find all the resources, mentorship programs, and support you need to excel in your spiritual and astrological studies.',
        'desc2': 'Access study materials, connect with faculty, schedule one-on-one sessions, and join a vibrant community of like-minded learners from across the country and around the world.',
        'bullets': ['Study materials & resources', 'One-on-one mentorship sessions', 'Student community access', 'Placement & career support'],
        'module1': 'Orientation & Onboarding',
        'module2': 'Course Materials & Resources',
        'module3': 'Mentorship Sessions',
        'module4': 'Community & Events',
        'module5': 'Assessments & Certification',
        'module6': 'Career Support & Placement',
        'why_h': 'Why Join the Student Section?',
        'why1_title': 'Guided Learning', 'why1_desc': 'Get structured support from expert mentors throughout your journey.',
        'why2_title': 'Community', 'why2_desc': 'Connect with thousands of fellow students and practitioners.',
        'why3_title': 'Career Support', 'why3_desc': 'Get placement assistance and build your professional network.',
        'cta_h': 'Ready to Begin Your Journey?',
        'cta_p': 'Register now and get full access to all student resources and mentorship.',
        'program_title': 'Student Section Benefits',
        'img': 'student-success-bg.jpg',
    },
}

for filename, d in courses.items():
    if not os.path.exists(filename):
        continue

    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()

    # Title tag
    c = c.replace('Tarot Reading - Parashari Indian Institute', d['title'] + ' - Parashari Indian Institute')

    # Hero h1
    c = c.replace('<h1 class="color-secondary">🃏 Tarot Reading</h1>', f'<h1 class="color-secondary">{d["icon"]} {d["title"]}</h1>')

    # Hero subtitle
    c = c.replace('<p>Divine Guidance Through Sacred Cards of Wisdom</p>', f'<p>{d["subtitle"]}</p>')

    # What is section h2
    c = c.replace('<h2>What is Tarot Reading?</h2>', f'<h2>What is {d["title"]}?</h2>')

    # Description paragraph 1
    c = c.replace(
        "Tarot is a powerful divination tool using 78 symbolic cards to provide guidance, insights, and\r\n                        answers to life's questions. Each card carries deep archetypal meanings that reveal hidden\r\n                        truths, future possibilities, and spiritual guidance.",
        d['desc1']
    )
    # Description paragraph 2
    c = c.replace(
        "Learn to read Major Arcana, Minor Arcana, and Court Cards, master various spreads, and develop\r\n                        your intuition to provide accurate, meaningful readings.",
        d['desc2']
    )

    # Bullet points
    c = c.replace(
        "<li class=\"mb-0-75\">✓ 78 card meanings &amp; symbolism</li>",
        f'<li class="mb-0-75">✓ {d["bullets"][0]}</li>'
    )
    c = c.replace(
        "<li class=\"mb-0-75\">✓ Multiple spread techniques</li>",
        f'<li class="mb-0-75">✓ {d["bullets"][1]}</li>'
    )
    c = c.replace(
        "<li class=\"mb-0-75\">✓ Intuitive development</li>",
        f'<li class="mb-0-75">✓ {d["bullets"][2]}</li>'
    )
    c = c.replace(
        "<li>✓ Past, present, future guidance</li>",
        f'<li>✓ {d["bullets"][3]}</li>'
    )

    # Program section title
    c = c.replace('<h2 class="card-section-title">Our Tarot Reading Diploma Program</h2>', f'<h2 class="card-section-title">{d["program_title"]}</h2>')

    # Modules
    c = c.replace('<strong>Module 1:</strong> Tarot History &amp; Structure', f'<strong>Module 1:</strong> {d["module1"]}')
    c = c.replace('<strong>Module 2:</strong> Major Arcana Cards (0-21)', f'<strong>Module 2:</strong> {d["module2"]}')
    c = c.replace('<strong>Module 3:</strong> Minor Arcana &amp; Suits', f'<strong>Module 3:</strong> {d["module3"]}')
    c = c.replace('<strong>Module 4:</strong> Court Cards &amp; Personalities', f'<strong>Module 4:</strong> {d["module4"]}')
    c = c.replace('<strong>Module 5:</strong> Spreads &amp; Reading Techniques', f'<strong>Module 5:</strong> {d["module5"]}')
    c = c.replace('<strong>Module 6:</strong> Professional Tarot Practice', f'<strong>Module 6:</strong> {d["module6"]}')

    # Why Study section
    c = c.replace('<h2 class="card-section-title">Why Study Tarot?</h2>', f'<h2 class="card-section-title">{d["why_h"]}</h2>')
    c = c.replace('<h4>Career Advancement</h4>', f'<h4>{d["why1_title"]}</h4>')
    c = c.replace('<p>Become a professional tarot reader with a growing client base.</p>', f'<p>{d["why1_desc"]}</p>')
    c = c.replace('<h4>Personal Growth</h4>', f'<h4>{d["why2_title"]}</h4>')
    c = c.replace('<p>Develop deep intuition and spiritual connection through cards.</p>', f'<p>{d["why2_desc"]}</p>')
    c = c.replace('<h4>Help Others</h4>', f'<h4>{d["why3_title"]}</h4>')
    c = c.replace('<p>Guide people through life challenges with divine wisdom.</p>', f'<p>{d["why3_desc"]}</p>')

    # CTA section
    c = c.replace('<h2 class="mb-1-5">Ready to Master Tarot Reading?</h2>', f'<h2 class="mb-1-5">{d["cta_h"]}</h2>')
    c = c.replace('<p class="mb-2">Join our Tarot program and unlock the mysteries of the cards.</p>', f'<p class="mb-2">{d["cta_p"]}</p>')

    # Image
    c = c.replace('src="assets/images/tarot-new.jpg" alt="Tarot Reading"', f'src="assets/images/{d["img"]}" alt="{d["title"]}"')
    c = c.replace('assets/images/tarot-new.jpg', f'assets/images/{d["img"]}')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(c)

print("All files updated successfully!")
