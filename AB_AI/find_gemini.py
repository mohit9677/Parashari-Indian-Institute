import os
cwd = r"d:\ParashariTeam\AB_AI"

files_to_check = ['courses.html', 'assets/js/courses-data.js']

with open("find_gemini_out.txt", "w", encoding="utf-8") as out:
    for f in files_to_check:
        filepath = os.path.join(cwd, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            out.write(f"--- Checking {f} ---\n")
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if 'gemini' in line.lower() or 'jyotish' in line.lower():
                    out.write(f"Line {i+1}: {line.strip()}\n")
            
            out.write("\nChecking for mobile numerology / feng shui:\n")
            for i, line in enumerate(lines):
                if 'mobile numerology' in line.lower() or 'feng shui' in line.lower():
                    out.write(f"Line {i+1}: {line.strip()}\n")
