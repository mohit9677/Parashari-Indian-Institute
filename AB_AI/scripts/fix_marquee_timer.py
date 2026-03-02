import os
import glob
import re

html_files = glob.glob('*.html')

# We need to replace the old broken calculation with the correct one.
# Old:
# const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
# const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
# const seconds = Math.floor((distance % (1000 * 60)) / 250);
#
# New:
# const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
# const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
# const seconds = Math.floor((distance % (1000 * 60)) / 1000);

OLD_JS = """          const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
          const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
          const seconds = Math.floor((distance % (1000 * 60)) / 250);"""

NEW_JS = """          const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
          const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
          const seconds = Math.floor((distance % (1000 * 60)) / 1000);"""


updated_count = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if OLD_JS in content:
        content = content.replace(OLD_JS, NEW_JS)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1
        print(f"Updated: {file_path}")

print(f"Total files updated: {updated_count}")
