import os
import re

mega_card_html = """
        <!-- GRAND MASTER MEGA CARD -->
        <div class="grand-master-mega-card" data-category="Grand Master" style="grid-column: 1 / -1; background-color: #591C21; border-top: 5px solid #D4AF37; border-bottom: 5px solid #D4AF37; padding: 3rem 2rem; border-radius: 12px; margin-top: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.2); position: relative; color: white;">
          
          <div style="text-align: center; margin-bottom: 2rem;">
            <div style="display: inline-block; background: linear-gradient(135deg, #FFD700, #D4AF37); color: #591C21; padding: 10px 30px; border-radius: 8px; font-weight: 800; font-size: 1.8rem; letter-spacing: 1px; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4); text-transform: uppercase;">
              <i class="fas fa-graduation-cap"></i> GRAND MASTER
            </div>
            <div style="margin-top: 15px; color: #e0d5c8; font-size: 1.1rem; letter-spacing: 1px;">The Ultimate Vedic Sciences Mastery · 48 Weeks</div>
          </div>

          <div style="border-top: 1px solid rgba(212, 175, 55, 0.3); border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding: 1.5rem 0; margin-bottom: 2.5rem; text-align: left; line-height: 1.6; font-size: 1.05rem;">
            The Grand Master program is the pinnacle of our offerings — <strong><span style="color: #FFD700;">48 weeks of access</span></strong> (24 weeks of live classes + recorded lectures, plus 24 additional weeks to revisit all recordings) along with the complete <strong><span style="color: #FFD700;">6 Spiritual Stairs</span></strong> pathway.
          </div>

          <div style="background: linear-gradient(90deg, #D4AF37, #f3e5ab, #D4AF37); color: #591C21; text-align: center; padding: 12px; border-radius: 8px 8px 0 0; font-weight: 800; font-size: 1.2rem; letter-spacing: 2px;">
            ✦ 12 SPIRITUAL PILLARS ✦
          </div>
          <div style="background: white; border-radius: 0 0 8px 8px; padding: 0.5rem 1.5rem 1.5rem; margin-bottom: 2.5rem; color: #333;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 0 40px;">
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">01</span> Numerology</div>
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">02</span> Vedic Astrology</div>
              
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">03</span> KP Astrology</div>
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">04</span> Gemstone Science</div>
              
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">05</span> Vastu Shastra</div>
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">06</span> Lal Kitab</div>
              
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">07</span> Face Reading</div>
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">08</span> Reiki Healing</div>
              
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">09</span> Tarot Reading</div>
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">10</span> Nakshatra</div>
              
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">11</span> Crystal Healing</div>
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">12</span> Palmistry</div>
            </div>
          </div>

          <div style="background: linear-gradient(90deg, #9C27B0, #ce93d8, #9C27B0); color: white; text-align: center; padding: 12px; border-radius: 8px 8px 0 0; font-weight: 800; font-size: 1.2rem; letter-spacing: 2px;">
            ✦ 6 SPIRITUAL STAIRS ✦
          </div>
          <div style="background: white; border-radius: 0 0 8px 8px; padding: 0.5rem 1.5rem 1.5rem; margin-bottom: 2rem; color: #333;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 0 40px;">
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">13</span> Yantra</div>
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">14</span> Mantra</div>
              
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">15</span> Tantra</div>
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">16</span> Chakra Balancing</div>
              
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">17</span> Remedies</div>
              <div style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; align-items: center;"><span style="color: #591C21; font-weight: 800; margin-right: 15px;">18</span> Past Life Regression Theory (PLRT)</div>
            </div>
          </div>

          <div style="text-align: center; margin-top: 2rem;">
            <a href="contact.html" style="display: inline-block; background: linear-gradient(135deg, #FFD700, #D4AF37); color: #591C21; text-decoration: none; padding: 12px 40px; border-radius: 50px; font-weight: bold; font-size: 1.1rem; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4); text-transform: uppercase; transition: transform 0.3s ease;">
              Inquire Now
            </a>
          </div>
          
        </div>
        <!-- END GRAND MASTER MEGA CARD -->
"""

filepath = 'AB_AI/courses.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

out_lines = []
in_gm_card = False
div_depth = 0

for i, line in enumerate(lines):
    if not in_gm_card:
        # Search for our previously added normal gold card
        if 'data-category="Grand Master"' in line and 'class="premium-gold-card"' in line:
            in_gm_card = True
            div_depth = line.count('<div') - line.count('</div')
            continue
        out_lines.append(line)
    else:
        div_depth += line.count('<div') - line.count('</div')
        if div_depth <= 0:
            in_gm_card = False

# Insert mega card at the end of the courseGrid
insertion_idx = -1
for i in range(len(out_lines)-1, -1, -1):
    if '<div class="text-center mt-3 mb-2">' in out_lines[i] or '<!-- Upcoming Courses Button -->' in out_lines[i] or '<a href="upcoming-courses.html"' in out_lines[i] or 'type="button" class="golden-button"' in out_lines[i]:
        insertion_idx = i
        break

if insertion_idx != -1:
    for i in range(insertion_idx - 1, -1, -1):
        if '</div>' in out_lines[i]:
            out_lines.insert(i, mega_card_html)
            print("Successfully inserted mega card.")
            break
else:
    print("Could not find insertion index.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(out_lines)
