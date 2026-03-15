import os
cwd = r"d:\ParashariTeam\AB_AI"

with open("verify_out.txt", "w", encoding="utf-8") as out:
    with open(os.path.join(cwd, 'courses.html'), 'r', encoding='utf-8') as f:
        content = f.read()
        if "gemini jyotishi.png" in content:
            out.write("YES! gemini jyotishi.png is in courses.html\n")
        else:
            out.write("NO! gemini jyotishi.png is NOT in courses.html\n")

    with open(os.path.join(cwd, 'assets/js/courses-data.js'), 'r', encoding='utf-8') as f:
        content = f.read()
        if "feng-shui-astrology.jpg" in content:
            out.write("YES! feng-shui-astrology.jpg is in courses-data.js\n")
        else:
            out.write("NO! feng-shui-astrology.jpg is NOT in courses-data.js\n")
        
        if "mobile numerology.png" in content:
            out.write("YES! mobile numerology.png is in courses-data.js\n")
        else:
            out.write("NO! mobile numerology.png is NOT in courses-data.js\n")

    with open(os.path.join(cwd, 'courses.html'), 'r', encoding='utf-8') as f:
        content = f.read()
        if "mobile numerology.png" in content:
            out.write("YES! mobile numerology.png is in courses.html\n")
        else:
            out.write("NO! mobile numerology.png is NOT in courses.html\n")
