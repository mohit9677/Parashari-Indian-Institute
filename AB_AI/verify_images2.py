import os
cwd = r"d:\ParashariTeam\AB_AI"

with open(os.path.join(cwd, 'courses.html'), 'r', encoding='utf-8') as f:
    content = f.read()
    if "feng-shui-astrology.jpg" in content:
        print("YES! feng-shui-astrology.jpg is in courses.html")
    else:
        print("NO! feng-shui-astrology.jpg is NOT in courses.html")
