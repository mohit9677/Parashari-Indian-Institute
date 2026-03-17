filepath = 'AB_AI/courses.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_card = '''        <!-- GRAND MASTER MEGA CARD -->
        <div class="grand-master-mega-card" data-animate data-category="Grand Master" data-course-id="grand-master" style="grid-column: 1 / -1; background: #591C21; border: 4px solid #D4AF37; border-radius: 12px; padding: 0; position: relative; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
          <span class="discount-tag" data-discount="25% Discount"></span>

          <!-- HEADER -->
          <div style="text-align: center; padding: 2.5rem 2rem 1.5rem;">
            <div style="display: inline-block; background: linear-gradient(135deg, #D4AF37, #f0c850, #D4AF37); color: #591C21; padding: 12px 35px; border-radius: 8px; font-weight: 900; font-size: 1.6rem; letter-spacing: 2px; text-transform: uppercase; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.5);">
              <i class="fas fa-graduation-cap" style="margin-right: 8px;"></i> GRAND MASTER
            </div>
            <p style="color: #D4AF37; font-size: 1rem; margin-top: 12px; margin-bottom: 0; letter-spacing: 1px; font-weight: 400;">The Ultimate Vedic Sciences Mastery &middot; 48 Weeks</p>
          </div>

          <!-- DESCRIPTION BAR -->
          <div style="background: #6b2530; border-top: 1px solid rgba(212,175,55,0.3); border-bottom: 1px solid rgba(212,175,55,0.3); padding: 1rem 2.5rem; color: #f5e6d0; font-size: 0.95rem; line-height: 1.7; text-align: left;">
            The Grand Master program is the pinnacle of our offerings &mdash; <strong><em style="color: #FFD700; font-style: italic;">48 weeks of access</em></strong> (24 weeks of live classes + recorded lectures, plus 24 additional weeks to revisit all recordings) along with the complete <strong><em style="color: #FFD700; font-style: italic;">6 Spiritual Stairs</em></strong> pathway.
          </div>

          <!-- COURSE LISTS -->
          <div style="padding: 2rem 2.5rem 1.5rem;">

            <!-- 12 SPIRITUAL PILLARS -->
            <div style="background: linear-gradient(90deg, #D4AF37, #f3e5ab, #D4AF37); color: #591C21; text-align: center; padding: 10px 20px; border-radius: 6px 6px 0 0; font-weight: 800; font-size: 1.15rem; letter-spacing: 2px;">&#10022; 12 SPIRITUAL PILLARS &#10022;</div>
            <div style="background: #fff; border: 2px solid #D4AF37; border-top: none; border-radius: 0 0 6px 6px; margin-bottom: 2rem; overflow: hidden;">
              <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; color: #333;">
                <tr><td style="padding: 13px 20px; border-bottom: 1px solid #eee; border-right: 1px solid #eee; width: 50%;"><strong style="color: #591C21; margin-right: 12px;">01</strong> Numerology</td><td style="padding: 13px 20px; border-bottom: 1px solid #eee;"><strong style="color: #591C21; margin-right: 12px;">02</strong> Vedic Astrology</td></tr>
                <tr><td style="padding: 13px 20px; border-bottom: 1px solid #eee; border-right: 1px solid #eee;"><strong style="color: #591C21; margin-right: 12px;">03</strong> KP Astrology</td><td style="padding: 13px 20px; border-bottom: 1px solid #eee;"><strong style="color: #591C21; margin-right: 12px;">04</strong> Gemstone Science</td></tr>
                <tr><td style="padding: 13px 20px; border-bottom: 1px solid #eee; border-right: 1px solid #eee;"><strong style="color: #591C21; margin-right: 12px;">05</strong> Vastu Shastra</td><td style="padding: 13px 20px; border-bottom: 1px solid #eee;"><strong style="color: #591C21; margin-right: 12px;">06</strong> Lal Kitab</td></tr>
                <tr><td style="padding: 13px 20px; border-bottom: 1px solid #eee; border-right: 1px solid #eee;"><strong style="color: #591C21; margin-right: 12px;">07</strong> Face Reading</td><td style="padding: 13px 20px; border-bottom: 1px solid #eee;"><strong style="color: #591C21; margin-right: 12px;">08</strong> Reiki Healing</td></tr>
                <tr><td style="padding: 13px 20px; border-bottom: 1px solid #eee; border-right: 1px solid #eee;"><strong style="color: #591C21; margin-right: 12px;">09</strong> Tarot Reading</td><td style="padding: 13px 20px; border-bottom: 1px solid #eee;"><strong style="color: #591C21; margin-right: 12px;">10</strong> Nakshatra</td></tr>
                <tr><td style="padding: 13px 20px; border-right: 1px solid #eee;"><strong style="color: #591C21; margin-right: 12px;">11</strong> Crystal Rudraksha</td><td style="padding: 13px 20px;"><strong style="color: #591C21; margin-right: 12px;">12</strong> Palmistry</td></tr>
              </table>
            </div>

            <!-- 6 SPIRITUAL STAIRS -->
            <div style="background: linear-gradient(90deg, #9C27B0, #ce93d8, #9C27B0); color: white; text-align: center; padding: 10px 20px; border-radius: 6px 6px 0 0; font-weight: 800; font-size: 1.15rem; letter-spacing: 2px;">&#10022; 6 SPIRITUAL STAIRS &#10022;</div>
            <div style="background: #fff; border: 2px solid #ce93d8; border-top: none; border-radius: 0 0 6px 6px; margin-bottom: 2rem; overflow: hidden;">
              <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; color: #333;">
                <tr><td style="padding: 13px 20px; border-bottom: 1px solid #f0e0f5; border-right: 1px solid #f0e0f5; width: 50%;"><strong style="color: #591C21; margin-right: 12px;">13</strong> Yantra</td><td style="padding: 13px 20px; border-bottom: 1px solid #f0e0f5;"><strong style="color: #591C21; margin-right: 12px;">14</strong> Mantra</td></tr>
                <tr><td style="padding: 13px 20px; border-bottom: 1px solid #f0e0f5; border-right: 1px solid #f0e0f5;"><strong style="color: #591C21; margin-right: 12px;">15</strong> Tantra</td><td style="padding: 13px 20px; border-bottom: 1px solid #f0e0f5;"><strong style="color: #591C21; margin-right: 12px;">16</strong> Chakra Balancing</td></tr>
                <tr><td style="padding: 13px 20px; border-right: 1px solid #f0e0f5;"><strong style="color: #591C21; margin-right: 12px;">17</strong> Remedies</td><td style="padding: 13px 20px;"><strong style="color: #591C21; margin-right: 12px;">18</strong> Past Life Regression Theory (PLRT)</td></tr>
              </table>
            </div>

            <!-- BADGES ROW -->
            <div style="display: flex; align-items: center; justify-content: center; flex-wrap: wrap; gap: 10px; margin-bottom: 1rem;">
              <span style="background: linear-gradient(135deg, #c8960c, #8b4513); color: #fff; padding: 5px 14px; border-radius: 50px; font-size: 0.8rem; font-weight: 700;">Grand Master &middot; Elite</span>
              <span style="color: #e0d5c8; font-size: 0.85rem;">&check; Certification</span>
              <span style="background: rgba(255,255,255,0.15); color: #fff; padding: 5px 14px; border-radius: 50px; font-size: 0.8rem; font-weight: 600;">&#128218; 18 Courses Total</span>
              <span style="background: #1976D2; color: #fff; padding: 5px 14px; border-radius: 50px; font-size: 0.8rem; font-weight: 600;">&#10022; 48 Weeks Access</span>
            </div>

            <!-- PRICE -->
            <div style="text-align: center; margin-bottom: 1rem;">
              <del style="color: #999; font-size: 1rem; margin-right: 10px;">&#8377;34,999</del>
              <strong style="color: #FFD700; font-size: 1.5rem;">&#8377;24,999</strong>
            </div>

            <!-- ENROLL NOW BUTTON -->
            <div style="text-align: center; padding-bottom: 0.5rem;">
              <a href="contact.html" class="learn-more" style="display: inline-flex; align-items: center; gap: 10px; text-decoration: none;">
                <span class="circle" aria-hidden="true"><span class="icon arrow"></span></span>
                <span class="button-text" style="text-transform: uppercase; font-weight: 700; letter-spacing: 1px; color: #FFD700;">ENROLL NOW</span>
              </a>
            </div>

          </div>
        </div>
        <!-- END GRAND MASTER MEGA CARD -->
'''

# Find and replace the old card block
out_lines = []
in_card = False
div_depth = 0
found = False

for line in lines:
    if not in_card:
        if '<!-- GRAND MASTER MEGA CARD -->' in line:
            in_card = True
            div_depth = 0
            found = True
            continue
        out_lines.append(line)
    else:
        if '<!-- END GRAND MASTER MEGA CARD -->' in line:
            in_card = False
            # Insert the new card
            out_lines.append(new_card)
            continue
        # skip old card lines

if found:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)
    print("Successfully rebuilt Grand Master Mega Card.")
else:
    print("ERROR: Could not find the Grand Master mega card markers.")
