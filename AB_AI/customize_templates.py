import os

courses = {
    'complete-astrology.html': {
        'title': 'Complete Astrology Course', 
        'desc': 'Discover the ancient wisdom of Vedic Astrology.', 
        'img': 'vedic-astrology-new.jpg'
    },
    'feng-shui.html': {
        'title': 'Feng Shui', 
        'desc': 'Enroll in the Feng Shui program to master the concepts and gain deep insights.', 
        'img': 'institute-building-modern.jpg'
    },
    'gemini-jyotish.html': {
        'title': 'Gemini Jyotish', 
        'desc': 'Enroll in the Gemini Jyotish program to master the concepts and gain deep insights.', 
        'img': 'gemini-card.png'
    },
    'gemstone.html': {
        'title': 'Gemstone Science', 
        'desc': 'Enroll in the Gemstone Science program to master the concepts and gain deep insights.', 
        'img': 'gemstone.jpg'
    },
    'healing.html': {
        'title': 'Healing', 
        'desc': 'Enroll in the Healing program to master the concepts and gain deep insights.', 
        'img': 'chakra-balancing.jpg'
    },
    'nakshatra.html': {
        'title': 'Nakshatra', 
        'desc': 'Enroll in the Nakshatra program to master the concepts and gain deep insights.', 
        'img': 'gold_zodiac_wheel.png'
    },
    'reiki.html': {
        'title': 'Reiki Healing', 
        'desc': 'Enroll in the Reiki Healing program to master the concepts and gain deep insights.', 
        'img': 'healing.jpg'
    },
    'student-section.html': {
        'title': 'Student Section', 
        'desc': 'Explore international and national student opportunities.', 
        'img': 'student-success-bg.jpg'
    }
}

for filename, data in courses.items():
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace('<title>Tarot Reading Course - Parashari</title>', f'<title>{data["title"]} - Parashari</title>')
    content = content.replace('<h1>Tarot Reading Course</h1>', f'<h1>{data["title"]}</h1>')
    content = content.replace('Master the mystical art of Tarot card reading to gain insights into past, present, and future.', data["desc"])
    content = content.replace('assets/images/tarot-new.jpg', f'assets/images/{data["img"]}')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Customization complete.")
