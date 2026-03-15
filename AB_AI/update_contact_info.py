import os
import re

cwd = r"d:\ParashariTeam\AB_AI"

def update_contact_info():
    # Regular expressions for the old patterns
    email_pattern = re.compile(r'info@parashari\.com', re.IGNORECASE)
    
    # Matches href="tel:+919999999999", href="tel:+91 9999-999-999", href="tel:+919005703159" etc
    tel_href_pattern = re.compile(r'href="tel:\+91\s*(9999999999|9999-999-999|9005703159)"')
    
    # Matches the display text: +91 9999-999-999, +919999999999, +91 9005703159
    phone_text_pattern = re.compile(r'\+91\s*(9999-999-999|9999999999|9005703159)')

    new_email = "info@astrobharatai.com"
    new_tel_href = 'href="tel:+919621051159"'
    new_phone_text = "+91 962 105 1159"

    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    new_content = email_pattern.sub(new_email, content)
                    new_content = tel_href_pattern.sub(new_tel_href, new_content)
                    new_content = phone_text_pattern.sub(new_phone_text, new_content)

                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated {file}")
                except Exception as e:
                    print(f"Failed to process {file}: {e}")

if __name__ == "__main__":
    update_contact_info()
