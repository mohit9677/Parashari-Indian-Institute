import re

try:
    with open('d:\\ParashariTeam\\AB_AI\\mentorship.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Regex to remove MEET YOUR MENTORS section
    # Matches from <!-- MEET YOUR MENTORS --> to right before <!-- TESTIMONIALS / STUDENT STORIES -->
    html = re.sub(r'<!-- MEET YOUR MENTORS -->.*?<!-- TESTIMONIALS / STUDENT STORIES -->', '<!-- TESTIMONIALS / STUDENT STORIES -->', html, flags=re.DOTALL)

    new_section = r"""
    <!-- FINAL CTA -->
    <section style="padding: 100px 20px; background: #111827; text-align: center; border-top: 1px solid rgba(255,255,255,0.05);">
      <div class="container" style="max-width: 800px; margin: 0 auto;">
        <h2 style="font-family: 'Cinzel', serif; font-size: 3rem; color: #fff; margin: 0 0 20px; line-height: 1.2;">
          BEGIN YOUR <span style="color: #D4AF37;">VEDIC</span><br>
          <span style="color: #D4AF37;">JOURNEY</span> TODAY
        </h2>
        <p style="color: #9ca3af; font-size: 1.1rem; line-height: 1.6; margin: 0 auto 40px; max-width: 600px;">
          Join thousands of students who have transformed their lives through the ancient wisdom of Vedic astrology.
        </p>
        <a href="contact.html" class="btn" style="display: inline-flex; align-items: center; gap: 10px; background: #eab308; color: #111827; padding: 15px 35px; border-radius: 8px; font-weight: 700; font-size: 1.1rem; text-decoration: none; transition: 0.3s; box-shadow: 0 4px 15px rgba(234,179,8,0.2);" onmouseover="this.style.transform='translateY(-2px)';" onmouseout="this.style.transform='translateY(0)';">
          Start Your Mentorship <i class="fa-solid fa-arrow-right"></i>
        </a>
      </div>
    </section>
"""

    # Add new section before </main>
    if "<!-- FINAL CTA -->" not in html:
        html = html.replace('</main>', new_section + '\n  </main>')

    with open('d:\\ParashariTeam\\AB_AI\\mentorship.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Modifications successful!")
except Exception as e:
    print(f"Error: {e}")
