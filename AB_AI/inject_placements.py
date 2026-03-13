import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    text = f.read()

placements = {
    'Shikha Pandey': 'Life Coach & Independent Consultant',
    'Priya Verma': 'Senior Faculty at Vedic Academy',
    'Amit Patel': 'Certified Vastu Consultant',
    'Anjali Gupta': 'Nadi Jyotish Expert at AstroGlobal',
    'Rohan Mehta': 'Lead Vastu Consultant',
    'Pooja Malhotra': 'Professional Tarot Reader',
    'Vikram Singh': 'KP Astrology Specialist',
    'Sneha Reddy': 'Full-time Professional Astrologer',
    'Arjun Das': 'Vedic Researcher & Author',
    'Meera Iyer': 'Corporate Behavioral Analyst',
    'Suresh Nair': 'Numerology Advisor for Startups'
}

count = 0
for name, placement in placements.items():
    pattern = rf'(<h4 class="color-primary mt-2">{name}</h4>)'
    
    # Simple check if not exactly followed by the placement p tag
    if name in text and 'class="placement-info"' not in text.split(f'{name}</h4>')[1][:200]:
        replacement = f'\\1\n              <p class="placement-info" style="font-size: 0.85em; color: #666; margin-bottom: 5px; font-weight: 500;"><i class="fas fa-briefcase" style="margin-right: 4px; color: #D4AF37;"></i> Placed as: {placement}</p>'
        text = re.sub(pattern, replacement, text, count=1)
        count += 1

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Injected placements for {count} students.")
