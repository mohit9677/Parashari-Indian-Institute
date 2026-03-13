import re

# 1. Update navbar.js
with open('assets/js/navbar.js', 'r', encoding='utf-8') as f:
    nav_content = f.read()

# Add Gemini Jyotish to crashCourseList
if "url: 'gemini-jyotish.html'" not in nav_content.split('const crashCourseList')[1].split('];')[0]:
    crash_target = "{ name: 'Feng Shui', meta: 'Feng', url: 'feng-shui.html', icon: 'fas fa-yin-yang' }"
    crash_replacement = "{ name: 'Feng Shui', meta: 'Feng', url: 'feng-shui.html', icon: 'fas fa-yin-yang' },\n  { name: 'Gemini Jyotish', meta: 'Gemini', url: 'gemini-jyotish.html', icon: 'fas fa-users' }"
    nav_content = nav_content.replace(crash_target, crash_replacement)

# Remove courses from grandMasterList
gm_list_pattern = r'(const grandMasterList = )\[[\s\S]*?\];'
nav_content = re.sub(gm_list_pattern, r'\g<1>[];', nav_content)

# Restore the Grand Master object in courseDomains if it was removed
if '/* Grand Master removed */' in nav_content:
    grand_master_domain = """{
    id: 'level-grandmaster',
    label: 'Grand Master',
    icon: 'fas fa-crown',
    description: 'Elite visionary training establishing you as a global authority in astrology.',
    specialContent: {
      title: "ASTROBHARATAI Grand Master Pass \u2013 Complete Syllabus",
      whoItIsFor: "Dedicated individuals seeking an All-in-One Lifetime Mastery Program",
      objective: "Comming soon...",
      whatYouWillLearn: [
        "Syllabus to be announced soon"
      ],
      learningOutcome: [
        "To be announced"
      ]
    },
    courses: grandMasterList
  },"""
    nav_content = nav_content.replace('/* Grand Master removed */', grand_master_domain)

with open('assets/js/navbar.js', 'w', encoding='utf-8') as f:
    f.write(nav_content)

print("Updated navbar.js")
