filepath = 'AB_AI/courses.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Find the block from <!-- GRAND MASTER MEGA CARD --> to <!-- END GRAND MASTER MEGA CARD -->
start_marker = "<!-- GRAND MASTER MEGA CARD -->"
end_marker = "<!-- END GRAND MASTER MEGA CARD -->"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_card = """<!-- GRAND MASTER MEGA CARD -->
        <div class="grand-master-mega-card" data-animate data-category="Grand Master" data-course-id="grand-master" style="grid-column: 1 / -1; background: #591C21; border: 3px solid #D4AF37; padding: 0; position: relative; overflow: hidden; font-family: 'Poppins', sans-serif;">
          
          <span class="discount-tag" data-discount="29% DISCOUNT" style="z-index: 10;"></span>

          <!-- HEADER -->
          <div style="text-align: center; padding: 3rem 2rem 1.5rem;">
            <div style="display: inline-block; background: linear-gradient(to right, #eabd55, #f5d78a, #eabd55); color: #591C21; padding: 12px 40px; border-radius: 6px; font-weight: 800; font-size: 1.5rem; letter-spacing: 1.5px; text-transform: uppercase;">
              <i class="fas fa-graduation-cap" style="margin-right: 8px;"></i> GRAND MASTER
            </div>
            <p style="color: #8c7b7d; font-size: 1.05rem; margin-top: 15px; margin-bottom: 0; font-weight: 400;">The Ultimate Vedic Sciences Mastery &middot; 48 Weeks</p>
          </div>

          <!-- DESCRIPTION BAR -->
          <div style="border-top: 1px solid rgba(212,175,55,0.4); border-bottom: 1px solid rgba(212,175,55,0.4); padding: 1.2rem 2.5rem; color: #e6ddde; font-size: 0.95rem; line-height: 1.6; text-align: left; margin-bottom: 2rem;">
            The Grand Master program is the pinnacle of our offerings &mdash; <strong style="color: #FFD700; font-weight: 700;">48 weeks of access</strong> (24 weeks of live classes + recorded lectures, plus 24 additional weeks to revisit all recordings) along with the complete <strong style="color: #FFD700; font-weight: 700;">6 Spiritual Stairs</strong> pathway.
          </div>

          <!-- COURSE LISTS -->
          <div style="padding: 0 2.5rem 1.5rem;">

            <!-- 12 SPIRITUAL PILLARS -->
            <div style="background: #e3ca88; color: #591C21; text-align: center; padding: 12px 20px; border-radius: 8px 8px 0 0; font-weight: 800; font-size: 1.05rem; letter-spacing: 1px; border: 1px solid #e3ca88;">
              <i class="fas fa-gem" style="font-size: 0.8em; margin-right: 5px;"></i> 12 SPIRITUAL PILLARS <i class="fas fa-gem" style="font-size: 0.8em; margin-left: 5px;"></i>
            </div>
            <div style="background: #fff; border: 1px solid #e3ca88; border-top: none; border-radius: 0 0 8px 8px; margin-bottom: 2.5rem; overflow: hidden;">
              <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; color: #333;">
                <tr><td style="padding: 14px 25px; border-bottom: 1px solid #f0e8d9; border-right: 1px solid #f0e8d9; width: 50%;"><strong style="color: #591C21; margin-right: 15px;">01</strong> Numerology</td><td style="padding: 14px 25px; border-bottom: 1px solid #f0e8d9;"><strong style="color: #591C21; margin-right: 15px;">02</strong> Vedic Astrology</td></tr>
                <tr><td style="padding: 14px 25px; border-bottom: 1px solid #f0e8d9; border-right: 1px solid #f0e8d9;"><strong style="color: #591C21; margin-right: 15px;">03</strong> KP Astrology</td><td style="padding: 14px 25px; border-bottom: 1px solid #f0e8d9;"><strong style="color: #591C21; margin-right: 15px;">04</strong> Gemstone Science</td></tr>
                <tr><td style="padding: 14px 25px; border-bottom: 1px solid #f0e8d9; border-right: 1px solid #f0e8d9;"><strong style="color: #591C21; margin-right: 15px;">05</strong> Vastu Shastra</td><td style="padding: 14px 25px; border-bottom: 1px solid #f0e8d9;"><strong style="color: #591C21; margin-right: 15px;">06</strong> Lal Kitab</td></tr>
                <tr><td style="padding: 14px 25px; border-bottom: 1px solid #f0e8d9; border-right: 1px solid #f0e8d9;"><strong style="color: #591C21; margin-right: 15px;">07</strong> Face Reading</td><td style="padding: 14px 25px; border-bottom: 1px solid #f0e8d9;"><strong style="color: #591C21; margin-right: 15px;">08</strong> Reiki Healing</td></tr>
                <tr><td style="padding: 14px 25px; border-bottom: 1px solid #f0e8d9; border-right: 1px solid #f0e8d9;"><strong style="color: #591C21; margin-right: 15px;">09</strong> Tarot Reading</td><td style="padding: 14px 25px; border-bottom: 1px solid #f0e8d9;"><strong style="color: #591C21; margin-right: 15px;">10</strong> Nakshatra</td></tr>
                <tr><td style="padding: 14px 25px; border-right: 1px solid #f0e8d9;"><strong style="color: #591C21; margin-right: 15px;">11</strong> Crystal Rudraksha</td><td style="padding: 14px 25px;"><strong style="color: #591C21; margin-right: 15px;">12</strong> Palmistry</td></tr>
              </table>
            </div>

            <!-- 6 SPIRITUAL STAIRS -->
            <div style="background: linear-gradient(90deg, #A24EB5, #C47BD7, #A24EB5); color: white; text-align: center; padding: 12px 20px; border-radius: 8px 8px 0 0; font-weight: 800; font-size: 1.05rem; letter-spacing: 1px; border: 1px solid #A24EB5;">
              <i class="fas fa-gem" style="font-size: 0.8em; margin-right: 5px;"></i> 6 SPIRITUAL STAIRS <i class="fas fa-gem" style="font-size: 0.8em; margin-left: 5px;"></i>
            </div>
            <div style="background: #fff; border: 1px solid #A24EB5; border-top: none; border-radius: 0 0 8px 8px; margin-bottom: 2rem; overflow: hidden;">
              <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; color: #333;">
                <tr><td style="padding: 14px 25px; border-bottom: 1px solid #f3e6f5; border-right: 1px solid #f3e6f5; width: 50%;"><strong style="color: #591C21; margin-right: 15px;">13</strong> Yantra</td><td style="padding: 14px 25px; border-bottom: 1px solid #f3e6f5;"><strong style="color: #591C21; margin-right: 15px;">14</strong> Mantra</td></tr>
                <tr><td style="padding: 14px 25px; border-bottom: 1px solid #f3e6f5; border-right: 1px solid #f3e6f5;"><strong style="color: #591C21; margin-right: 15px;">15</strong> Tantra</td><td style="padding: 14px 25px; border-bottom: 1px solid #f3e6f5;"><strong style="color: #591C21; margin-right: 15px;">16</strong> Chakra Balancing</td></tr>
                <tr><td style="padding: 14px 25px; border-right: 1px solid #f3e6f5;"><strong style="color: #591C21; margin-right: 15px;">17</strong> Remedies</td><td style="padding: 14px 25px;"><strong style="color: #591C21; margin-right: 15px;">18</strong> Past Life Regression Theory (PLRT)</td></tr>
              </table>
            </div>

            <!-- BADGES ROW -->
            <div style="display: flex; align-items: center; justify-content: center; flex-wrap: wrap; gap: 15px; margin-bottom: 1.5rem;">
              <span style="background: #D4AF37; color: #591C21; padding: 6px 18px; border-radius: 50px; font-size: 0.85rem; font-weight: 700; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">Grand Master &middot; Elite</span>
              <span style="color: #4CAF50; font-size: 0.9rem; font-weight: bold;">&check; <span style="color: #e0d5c8; font-weight: normal;">Certification</span></span>
              <span style="background: rgba(0,0,0,0.3); color: #fff; padding: 6px 18px; border-radius: 50px; font-size: 0.85rem; font-weight: 600;">&#128218; 18 Courses Total</span>
              <span style="background: #196b9c; color: #fff; padding: 6px 18px; border-radius: 50px; font-size: 0.85rem; font-weight: 600;">&#10022; 48 Weeks Access</span>
            </div>

            <!-- PRICE -->
            <div style="text-align: center; margin-bottom: 1.5rem;">
              <del style="color: #999; font-size: 1.1rem; margin-right: 12px; font-weight: 500;">&#8377;34,999</del>
              <strong style="color: #FFD700; font-size: 1.8rem; letter-spacing: 1px;">&#8377;24,999</strong>
            </div>

            <!-- ENROLL NOW BUTTON -->
            <div style="text-align: center; padding-bottom: 1rem;">
              <a href="contact.html" style="display: inline-flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #d3a444, #f5d78a, #d3a444); color: #591C21; text-decoration: none; padding: 12px 35px; border-radius: 50px; font-weight: 800; font-size: 1rem; letter-spacing: 1px; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4); text-transform: uppercase;">
                <span style="background: #591C21; color: #D4AF37; display: flex; align-items: center; justify-content: center; width: 24px; height: 24px; border-radius: 50%; margin-right: 12px; font-size: 0.8rem;"><i class="fas fa-chevron-right"></i></span>
                ENROLL NOW
              </a>
            </div>

          </div>
        </div>"""
    
    new_content = content[:start_idx] + new_card + content[end_idx + len(end_marker):]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Mega card rewritten explicitly matching screenshot details.")
else:
    print("Could not find mega card markers.")
