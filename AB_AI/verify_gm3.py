import os

target_files = [
    "vastu.html", "tarot.html", "rudraksha.html", "reiki.html",
    "numerology.html", "palmistry.html", "nakshatra.html", "lal-kitab.html",
    "kp-astrology.html", "gemstone.html", "face-reading.html", 
    "crystal-healing.html", "astrology.html"
]

checks = [
    'id="grand-master"',
    'data-program="grand-master"',
    '(Advanced)',
    'tier-grand-master',
    'col-grand-master',
    'Extended 48-Week Access',
    'Free 6 Spiritual Stairs',
    'Grand Master',
    '48 WEEKS',
    '24,999',
]

os.chdir(r"d:\ParashariTeam\AB_AI")

lines = []
for fname in target_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    missing = [c for c in checks if c not in content]
    if missing:
        lines.append("FAIL " + fname + ": " + str(missing))
    else:
        lines.append("OK " + fname)

with open('verify_results.md', 'w', encoding='utf-8') as f:
    f.write("# Verification Results\n\n")
    for l in lines:
        f.write("- " + l + "\n")
