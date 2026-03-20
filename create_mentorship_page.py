import re

try:
    with open('d:\\ParashariTeam\\AB_AI\\courses.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Match everything up to the end of the header
    header_match = re.search(r'(.*?</header>)', html, re.DOTALL)
    
    # Match the urgency marquee and everything below it (footer, scripts)
    footer_match = re.search(r'(  <!-- TOP URGENCY MARQUEE -->.*)', html, re.DOTALL)

    if header_match and footer_match:
        content = """
  <main id="mentorship-content" style="min-height: 50vh; padding: 6rem 5%; background: #fdfdfd; display: flex; flex-direction: column; align-items: center; justify-content: center;">
    <div class="container text-center">
      <div style="display: inline-block; background: #D4AF37; color: #fff; padding: 6px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; margin-bottom: 15px; text-transform: uppercase;">
        🌟 Special Feature
      </div>
      <h1 style="color: #8b0000; font-size: 3rem; margin-bottom: 1rem;">1-on-1 Mentorship</h1>
      <p style="color: #666; font-size: 1.2rem; max-width: 600px; margin: 0 auto;">
        Detailed mentorship information will be provided here.
      </p>
    </div>
  </main>
"""
        new_html = header_match.group(1) + content + footer_match.group(1)
        new_html = new_html.replace("<title>Courses - ", "<title>1-on-1 Mentorship - ")
        
        with open('d:\\ParashariTeam\\AB_AI\\mentorship.html', 'w', encoding='utf-8') as out:
            out.write(new_html)
        print("Success: mentorship.html created.")
    else:
        print("Error: Could not find header or footer bounds.")
except Exception as e:
    print(f"Error: {e}")
