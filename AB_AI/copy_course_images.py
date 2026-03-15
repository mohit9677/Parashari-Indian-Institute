import os
import shutil

source_dir = r"D:\ParashariTeam"
target_dir = r"d:\ParashariTeam\AB_AI\assets\images"

images = [
    "Financial Astrology (Artha).png",
    "(Face Reading) Western Physiognomy (Character Analysis.png",
    "Lal Kitab Basics.png",
    "Medical Astrology.png",
    "The BNN Intensive A 14-Day Mastery of Bhrigu Nandi Nadi.png",
    "Modern Career Astrology.png",
    "Business Numerology.png",
    "Vedic Numerology.png",
    "Nadi Jyotish.png",
    "Healing.png"
]

os.makedirs(target_dir, exist_ok=True)

for img in images:
    src_path = os.path.join(source_dir, img)
    dst_path = os.path.join(target_dir, img)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Copied {img}")
    else:
        print(f"Skipped {img} - File not found")

