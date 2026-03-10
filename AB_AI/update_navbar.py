import os

new_array_code = """const allCoursesList = [
  { name: 'Vedic Astrology', meta: 'Vedic Analysis', url: 'astrology.html', icon: 'fas fa-om' },
  { name: 'Numerology', meta: 'Number Science', url: 'numerology.html', icon: 'fas fa-sort-numeric-up' },
  { name: 'KP Astrology', meta: 'Stellar Astrology', url: 'kp-astrology.html', icon: 'fas fa-star' },
  { name: 'Gemstone Science', meta: 'Precious Stones', url: 'gemstone.html', icon: 'fas fa-gem' },
  { name: 'Vastu Shastra', meta: 'Space Harmony', url: 'vastu.html', icon: 'fas fa-home' },
  { name: 'Lal Kitab', meta: 'Practical Solutions', url: 'lal-kitab.html', icon: 'fas fa-book' },
  { name: 'Face Reading', meta: 'Physiognomy', url: 'face-reading.html', icon: 'fas fa-user' },
  { name: 'Reiki Healing', meta: 'Energy Healing', url: 'reiki.html', icon: 'fas fa-hand-holding-medical' },
  { name: 'Tarot Reading', meta: 'Card Divination', url: 'tarot.html', icon: 'fas fa-clone' },
  { name: 'Nakshatra', meta: 'Constellations', url: 'nakshatra.html', icon: 'fas fa-moon' },
  { name: 'Crystal', meta: 'Energy Balancing', url: 'crystal-healing.html', icon: 'fas fa-gem' },
  { name: 'Rudraksha', meta: 'Sacred Beads', url: 'rudraksha.html', icon: 'fas fa-seedling' },
  { name: 'Palmistry', meta: 'Hand Analysis', url: 'palmistry.html', icon: 'fas fa-hand-paper' },
  { name: 'Nadi Jyotish', meta: 'Precision Timing', url: 'nadi-jyotish.html', icon: 'fas fa-scroll' },
  { name: 'Remedy Course', meta: 'Upaay Gyaan', url: 'remedy-course.html', icon: 'fas fa-hand-holding-heart' },
  { name: 'Medical Astrology', meta: 'Health & Wellness', url: 'medical-astrology.html', icon: 'fas fa-heartbeat' },
  { name: 'BNN Advance', meta: 'Bhrigu Nandi Nadi', url: 'bnn-astrology.html', icon: 'fas fa-code-branch' },
  { name: 'Healing', meta: 'Holistic Wellness', url: 'healing.html', icon: 'fas fa-leaf' },
  { name: 'Feng Shui', meta: 'Energy Flow', url: 'feng-shui.html', icon: 'fas fa-yin-yang' },
  { name: 'Past Life Prediction', meta: 'Karma Analysis', url: 'plrt.html', icon: 'fas fa-hourglass-half' },
  { name: 'Gemini Jyotish', meta: 'Twin Logic', url: 'gemini-jyotish.html', icon: 'fas fa-users' }
];"""

with open(r'D:\ParashariTeam\AB_AI\assets\js\navbar.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Find the start and end of allCoursesList
start_idx = js_content.find('const allCoursesList = [')
end_idx = js_content.find('];', start_idx) + 2

if start_idx != -1 and end_idx != -1:
    new_js = js_content[:start_idx] + new_array_code + js_content[end_idx:]
    with open(r'D:\ParashariTeam\AB_AI\assets\js\navbar.js', 'w', encoding='utf-8') as f:
        f.write(new_js)
    print("navbar.js successfully updated with the 21 courses.")
else:
    print("Could not find allCoursesList in navbar.js")
