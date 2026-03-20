import re

html_content = """
  <main id="mentorship-content">
    
    <!-- HERO SECTION -->
    <section class="mentorship-hero" style="position: relative; padding: 120px 20px 80px; background: linear-gradient(rgba(10,14,23,0.85), rgba(10,14,23,0.95)), url('assets/images/explore-hero-image.png') center/cover no-repeat; text-align: center; color: #fff;">
      <div class="container" style="max-width: 900px; margin: 0 auto; position: relative; z-index: 2;">
        <div style="display: inline-block; border: 1px solid rgba(212,175,55,0.5); border-radius: 30px; padding: 6px 16px; margin-bottom: 25px; color: #D4AF37; font-size: 0.85rem; letter-spacing: 1px; text-transform: uppercase;">
          <i class="fa-solid fa-star" style="margin-right: 6px;"></i> PARASHARI INSTITUTE
        </div>
        <h1 style="font-size: 3.5rem; line-height: 1.1; margin-bottom: 25px; font-weight: 700; font-family: 'Cinzel', serif;">
          1-ON-1 <span style="color: #D4AF37;">VEDIC<br>ASTROLOGY</span> MENTORSHIP
        </h1>
        <p style="font-size: 1.15rem; color: #d1d5db; line-height: 1.6; margin-bottom: 40px; max-width: 750px; margin-left: auto; margin-right: auto;">
          Personalized guidance from India's most revered Vedic scholars. Unlock the ancient wisdom of Jyotish Shastra with dedicated 24×7 mentorship support.
        </p>
        <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; margin-bottom: 60px;">
          <a href="contact.html" class="btn" style="background: #eab308; color: #1f2937; padding: 14px 32px; border-radius: 8px; font-weight: 600; font-size: 1.1rem; border: none; transition: 0.3s; box-shadow: 0 4px 14px rgba(234,179,8,0.3);">Book Your Mentor</a>
          <a href="courses.html" class="btn" style="background: transparent; color: #d1d5db; padding: 14px 32px; border-radius: 8px; font-weight: 600; font-size: 1.1rem; border: 1px solid rgba(255,255,255,0.3); transition: 0.3s;">Explore Programs</a>
        </div>
        
        <!-- Stats Row -->
        <div style="display: flex; justify-content: center; gap: 60px; flex-wrap: wrap; margin-top: 40px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 40px;">
          <div style="text-align: center;">
            <i class="fa-solid fa-user-group" style="color: #eab308; font-size: 1.5rem; margin-bottom: 15px;"></i>
            <h3 style="font-size: 1.8rem; margin: 0 0 5px; color: #fff;">5,000+</h3>
            <p style="font-size: 0.75rem; color: #9ca3af; margin: 0; text-transform: uppercase; letter-spacing: 1px;">Active Students</p>
          </div>
          <div style="text-align: center;">
            <i class="fa-solid fa-star" style="color: #eab308; font-size: 1.5rem; margin-bottom: 15px;"></i>
            <h3 style="font-size: 1.8rem; margin: 0 0 5px; color: #fff;">50+</h3>
            <p style="font-size: 0.75rem; color: #9ca3af; margin: 0; text-transform: uppercase; letter-spacing: 1px;">Expert Mentors</p>
          </div>
          <div style="text-align: center;">
            <i class="fa-solid fa-clock" style="color: #eab308; font-size: 1.5rem; margin-bottom: 15px;"></i>
            <h3 style="font-size: 1.8rem; margin: 0 0 5px; color: #fff;">24×7</h3>
            <p style="font-size: 0.75rem; color: #9ca3af; margin: 0; text-transform: uppercase; letter-spacing: 1px;">Support</p>
          </div>
        </div>
      </div>
    </section>

    <!-- WHY CHOOSE US -->
    <section style="padding: 100px 20px; background: #fafaf9;">
      <div class="container text-center" style="max-width: 1200px;">
        <span style="color: #D4AF37; font-size: 0.85rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;">WHY CHOOSE US</span>
        <h2 style="font-family: 'Cinzel', serif; font-size: 3rem; color: #591C21; margin: 10px 0 20px;">YOUR PATH TO MASTERY</h2>
        <p style="color: #6b7280; font-size: 1.1rem; max-width: 600px; margin: 0 auto 60px;">
          Experience the most comprehensive 1-on-1 Vedic astrology mentorship program in India
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; text-align: left;">
          <!-- Card 1 -->
          <div style="background: #fff; padding: 40px 30px; border-radius: 12px; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px rgba(0,0,0,0.02); transition: 0.3s; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 10px 25px rgba(0,0,0,0.05)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 6px rgba(0,0,0,0.02)';">
            <div style="width: 50px; height: 50px; background: #591C21; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 25px;">
              <i class="fa-solid fa-video" style="color: #fff; font-size: 1.2rem;"></i>
            </div>
            <h3 style="font-family: 'Cinzel', serif; font-size: 1.25rem; color: #111827; margin-bottom: 12px; font-weight: 600;">LIVE 1-ON-1 SESSIONS</h3>
            <p style="color: #6b7280; font-size: 0.95rem; line-height: 1.6; margin: 0;">Private video sessions with your dedicated Vedic astrology mentor, tailored to your learning pace and goals.</p>
          </div>
          <!-- Card 2 -->
          <div style="background: #fff; padding: 40px 30px; border-radius: 12px; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px rgba(0,0,0,0.02); transition: 0.3s; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 10px 25px rgba(0,0,0,0.05)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 6px rgba(0,0,0,0.02)';">
            <div style="width: 50px; height: 50px; background: #591C21; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 25px;">
              <i class="fa-solid fa-clock" style="color: #fff; font-size: 1.2rem;"></i>
            </div>
            <h3 style="font-family: 'Cinzel', serif; font-size: 1.25rem; color: #111827; margin-bottom: 12px; font-weight: 600;">24×7 SUPPORT</h3>
            <p style="color: #6b7280; font-size: 0.95rem; line-height: 1.6; margin: 0;">Round-the-clock assistance via chat and email. Your doubts never have to wait for the next session.</p>
          </div>
          <!-- Card 3 -->
          <div style="background: #fff; padding: 40px 30px; border-radius: 12px; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px rgba(0,0,0,0.02); transition: 0.3s; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 10px 25px rgba(0,0,0,0.05)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 6px rgba(0,0,0,0.02)';">
            <div style="width: 50px; height: 50px; background: #591C21; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 25px;">
              <i class="fa-solid fa-book-open" style="color: #fff; font-size: 1.2rem;"></i>
            </div>
            <h3 style="font-family: 'Cinzel', serif; font-size: 1.25rem; color: #111827; margin-bottom: 12px; font-weight: 600;">PERSONALIZED CURRICULUM</h3>
            <p style="color: #6b7280; font-size: 0.95rem; line-height: 1.6; margin: 0;">Custom study plans covering Parashari, Jaimini, Nadi, and KP systems based on your interests.</p>
          </div>
          <!-- Card 4 -->
          <div style="background: #fff; padding: 40px 30px; border-radius: 12px; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px rgba(0,0,0,0.02); transition: 0.3s; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 10px 25px rgba(0,0,0,0.05)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 6px rgba(0,0,0,0.02)';">
            <div style="width: 50px; height: 50px; background: #591C21; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 25px;">
              <i class="fa-solid fa-bullseye" style="color: #fff; font-size: 1.2rem;"></i>
            </div>
            <h3 style="font-family: 'Cinzel', serif; font-size: 1.25rem; color: #111827; margin-bottom: 12px; font-weight: 600;">CHART READING PRACTICE</h3>
            <p style="color: #6b7280; font-size: 0.95rem; line-height: 1.6; margin: 0;">Hands-on practice analyzing real horoscopes with expert feedback on every prediction.</p>
          </div>
          <!-- Card 5 -->
          <div style="background: #fff; padding: 40px 30px; border-radius: 12px; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px rgba(0,0,0,0.02); transition: 0.3s; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 10px 25px rgba(0,0,0,0.05)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 6px rgba(0,0,0,0.02)';">
            <div style="width: 50px; height: 50px; background: #591C21; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 25px;">
              <i class="fa-solid fa-headphones" style="color: #fff; font-size: 1.2rem;"></i>
            </div>
            <h3 style="font-family: 'Cinzel', serif; font-size: 1.25rem; color: #111827; margin-bottom: 12px; font-weight: 600;">DEDICATED MENTOR</h3>
            <p style="color: #6b7280; font-size: 0.95rem; line-height: 1.6; margin: 0;">A single mentor assigned to you for continuity, deep understanding, and consistent progress tracking.</p>
          </div>
          <!-- Card 6 -->
          <div style="background: #fff; padding: 40px 30px; border-radius: 12px; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px rgba(0,0,0,0.02); transition: 0.3s; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 10px 25px rgba(0,0,0,0.05)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 6px rgba(0,0,0,0.02)';">
            <div style="width: 50px; height: 50px; background: #591C21; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 25px;">
              <i class="fa-solid fa-shield-halved" style="color: #fff; font-size: 1.2rem;"></i>
            </div>
            <h3 style="font-family: 'Cinzel', serif; font-size: 1.25rem; color: #111827; margin-bottom: 12px; font-weight: 600;">CERTIFICATION & PLACEMENT</h3>
            <p style="color: #6b7280; font-size: 0.95rem; line-height: 1.6; margin: 0;">Earn Parashari Institute certification with 100% placement support as a professional astrologer.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- HOW IT WORKS -->
    <section style="padding: 100px 20px; background: #F3EFE9;">
      <div class="container text-center" style="max-width: 1000px;">
        <span style="color: #D4AF37; font-size: 0.85rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;">SIMPLE PROCESS</span>
        <h2 style="font-family: 'Cinzel', serif; font-size: 3rem; color: #591C21; margin: 10px 0 60px;">HOW IT WORKS</h2>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 24px; text-align: left;">
          
          <div style="background: #fff; padding: 35px 30px; border-radius: 12px; display: flex; gap: 25px; align-items: flex-start; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
            <div style="width: 65px; height: 60px; min-width: 60px; background: #591C21; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 1.4rem; font-family: 'Cinzel', serif; font-weight: 600;">
              01
            </div>
            <div>
              <h3 style="font-family: 'Cinzel', serif; font-size: 1.2rem; color: #111827; margin: 0 0 10px;">CHOOSE YOUR PATH</h3>
              <p style="color: #6b7280; font-size: 0.95rem; line-height: 1.6; margin: 0;">Select your area of interest — Parashari, Jaimini, KP, Nadi, or comprehensive Vedic astrology.</p>
            </div>
          </div>
          
          <div style="background: #fff; padding: 35px 30px; border-radius: 12px; display: flex; gap: 25px; align-items: flex-start; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
            <div style="width: 65px; height: 60px; min-width: 60px; background: #591C21; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 1.4rem; font-family: 'Cinzel', serif; font-weight: 600;">
              02
            </div>
            <div>
              <h3 style="font-family: 'Cinzel', serif; font-size: 1.2rem; color: #111827; margin: 0 0 10px;">GET MATCHED</h3>
              <p style="color: #6b7280; font-size: 0.95rem; line-height: 1.6; margin: 0;">We pair you with the perfect mentor based on your goals, level, and preferred learning style.</p>
            </div>
          </div>
          
          <div style="background: #fff; padding: 35px 30px; border-radius: 12px; display: flex; gap: 25px; align-items: flex-start; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
            <div style="width: 65px; height: 60px; min-width: 60px; background: #591C21; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 1.4rem; font-family: 'Cinzel', serif; font-weight: 600;">
              03
            </div>
            <div>
              <h3 style="font-family: 'Cinzel', serif; font-size: 1.2rem; color: #111827; margin: 0 0 10px;">START LEARNING</h3>
              <p style="color: #6b7280; font-size: 0.95rem; line-height: 1.6; margin: 0;">Begin live 1-on-1 sessions with personalized curriculum, chart practice, and 24×7 doubt support.</p>
            </div>
          </div>
          
          <div style="background: #fff; padding: 35px 30px; border-radius: 12px; display: flex; gap: 25px; align-items: flex-start; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
            <div style="width: 65px; height: 60px; min-width: 60px; background: #591C21; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 1.4rem; font-family: 'Cinzel', serif; font-weight: 600;">
              04
            </div>
            <div>
              <h3 style="font-family: 'Cinzel', serif; font-size: 1.2rem; color: #111827; margin: 0 0 10px;">GET CERTIFIED</h3>
              <p style="color: #6b7280; font-size: 0.95rem; line-height: 1.6; margin: 0;">Complete assessments, earn your Parashari Institute certification, and get placement support.</p>
            </div>
          </div>
          
        </div>
      </div>
    </section>

    <!-- MEET YOUR MENTORS -->
    <section style="padding: 100px 20px; background: #0b0f19;">
      <div class="container text-center" style="max-width: 1200px;">
        <span style="color: #D4AF37; font-size: 0.85rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;">OUR GURUS</span>
        <h2 style="font-family: 'Cinzel', serif; font-size: 3rem; color: #fff; margin: 10px 0 20px;">MEET YOUR <span style="color: #D4AF37;">MENTORS</span></h2>
        <p style="color: #9ca3af; font-size: 1.1rem; max-width: 600px; margin: 0 auto 70px;">
          Learn directly from India's most respected Vedic astrologers and scholars
        </p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; text-align: center;">
          
          <!-- Mentor 1 -->
          <div>
            <div style="position: relative; width: 200px; height: 200px; margin: 0 auto 25px;">
              <div style="position: absolute; inset: -3px; border-radius: 50%; background: linear-gradient(180deg, rgba(212,175,55,1) 0%, rgba(212,175,55,0) 100%); z-index: 0;"></div>
              <img src="assets/images/dean-profile.jpg" alt="Acharya Devendra Sharma" style="position: relative; z-index: 1; width: 100%; height: 100%; border-radius: 50%; object-fit: cover; border: 4px solid #0b0f19;">
              <div style="position: absolute; bottom: -12px; left: 50%; transform: translateX(-50%); background: #1f2937; border: 1px solid #D4AF37; border-radius: 20px; padding: 4px 12px; display: flex; align-items: center; gap: 5px; z-index: 2;">
                <i class="fa-solid fa-star" style="color: #eab308; font-size: 0.8rem;"></i>
                <span style="color: #eab308; font-weight: 700; font-size: 0.85rem;">4.9</span>
              </div>
            </div>
            <h3 style="font-family: 'Cinzel', serif; color: #fff; font-size: 1.2rem; margin: 0 0 5px;">ACHARYA DEVENDRA SHARMA</h3>
            <p style="color: #D4AF37; font-size: 0.9rem; margin: 0 0 8px;">Parashari & Jaimini Systems</p>
            <p style="color: #9ca3af; font-size: 0.85rem; margin: 0 0 4px;">25+ Years Experience</p>
            <p style="color: #9ca3af; font-size: 0.85rem; margin: 0 0 20px;">1200+ students mentored</p>
            <a href="contact.html" style="display: inline-block; border: 1px solid rgba(212,175,55,0.5); color: #D4AF37; padding: 10px 24px; border-radius: 8px; font-size: 0.9rem; font-weight: 600; text-decoration: none; transition: 0.3s;" onmouseover="this.style.background='rgba(212,175,55,0.1)';" onmouseout="this.style.background='transparent';">Book Session</a>
          </div>

          <!-- Mentor 2 -->
          <div>
            <div style="position: relative; width: 200px; height: 200px; margin: 0 auto 25px;">
              <div style="position: absolute; inset: -3px; border-radius: 50%; background: linear-gradient(180deg, rgba(212,175,55,1) 0%, rgba(212,175,55,0) 100%); z-index: 0;"></div>
              <img src="assets/images/priti dave.png" alt="Dr. Meenakshi Joshi" style="position: relative; z-index: 1; width: 100%; height: 100%; border-radius: 50%; object-fit: cover; border: 4px solid #0b0f19;">
              <div style="position: absolute; bottom: -12px; left: 50%; transform: translateX(-50%); background: #1f2937; border: 1px solid #D4AF37; border-radius: 20px; padding: 4px 12px; display: flex; align-items: center; gap: 5px; z-index: 2;">
                <i class="fa-solid fa-star" style="color: #eab308; font-size: 0.8rem;"></i>
                <span style="color: #eab308; font-weight: 700; font-size: 0.85rem;">4.8</span>
              </div>
            </div>
            <h3 style="font-family: 'Cinzel', serif; color: #fff; font-size: 1.2rem; margin: 0 0 5px;">DR. MEENAKSHI JOSHI</h3>
            <p style="color: #D4AF37; font-size: 0.9rem; margin: 0 0 8px;">Nadi & KP Astrology</p>
            <p style="color: #9ca3af; font-size: 0.85rem; margin: 0 0 4px;">18+ Years Experience</p>
            <p style="color: #9ca3af; font-size: 0.85rem; margin: 0 0 20px;">950+ students mentored</p>
            <a href="contact.html" style="display: inline-block; border: 1px solid rgba(212,175,55,0.5); color: #D4AF37; padding: 10px 24px; border-radius: 8px; font-size: 0.9rem; font-weight: 600; text-decoration: none; transition: 0.3s;" onmouseover="this.style.background='rgba(212,175,55,0.1)';" onmouseout="this.style.background='transparent';">Book Session</a>
          </div>

          <!-- Mentor 3 -->
          <div>
            <div style="position: relative; width: 200px; height: 200px; margin: 0 auto 25px;">
              <div style="position: absolute; inset: -3px; border-radius: 50%; background: linear-gradient(180deg, rgba(212,175,55,1) 0%, rgba(212,175,55,0) 100%); z-index: 0;"></div>
              <img src="assets/images/mukesh kumar.png" alt="Pandit Rameshwar Mishra" style="position: relative; z-index: 1; width: 100%; height: 100%; border-radius: 50%; object-fit: cover; border: 4px solid #0b0f19;">
              <div style="position: absolute; bottom: -12px; left: 50%; transform: translateX(-50%); background: #1f2937; border: 1px solid #D4AF37; border-radius: 20px; padding: 4px 12px; display: flex; align-items: center; gap: 5px; z-index: 2;">
                <i class="fa-solid fa-star" style="color: #eab308; font-size: 0.8rem;"></i>
                <span style="color: #eab308; font-weight: 700; font-size: 0.85rem;">5.0</span>
              </div>
            </div>
            <h3 style="font-family: 'Cinzel', serif; color: #fff; font-size: 1.2rem; margin: 0 0 5px;">PANDIT RAMESHWAR MISHRA</h3>
            <p style="color: #D4AF37; font-size: 0.9rem; margin: 0 0 8px;">Vedic Muhurta & Prashna</p>
            <p style="color: #9ca3af; font-size: 0.85rem; margin: 0 0 4px;">30+ Years Experience</p>
            <p style="color: #9ca3af; font-size: 0.85rem; margin: 0 0 20px;">1500+ students mentored</p>
            <a href="contact.html" style="display: inline-block; border: 1px solid rgba(212,175,55,0.5); color: #D4AF37; padding: 10px 24px; border-radius: 8px; font-size: 0.9rem; font-weight: 600; text-decoration: none; transition: 0.3s;" onmouseover="this.style.background='rgba(212,175,55,0.1)';" onmouseout="this.style.background='transparent';">Book Session</a>
          </div>

        </div>
      </div>
    </section>

    <!-- TESTIMONIALS / STUDENT STORIES -->
    <section style="padding: 100px 20px; background: #fafaf9;">
      <div class="container text-center" style="max-width: 1200px;">
        <span style="color: #D4AF37; font-size: 0.85rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;">TESTIMONIALS</span>
        <h2 style="font-family: 'Cinzel', serif; font-size: 3rem; color: #591C21; margin: 10px 0 60px;">STUDENT STORIES</h2>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; text-align: left;">
          
          <div style="background: #fff; padding: 40px; border-radius: 12px; border: 1px solid #e5e7eb; position: relative;">
            <i class="fa-solid fa-quote-right" style="position: absolute; right: 30px; top: 30px; font-size: 2.5rem; color: #f3f4f6;"></i>
            <div style="color: #eab308; font-size: 1rem; margin-bottom: 20px; display: flex; gap: 3px;">
              <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
            </div>
            <p style="color: #4b5563; font-style: italic; font-size: 1.05rem; line-height: 1.7; margin-bottom: 30px; min-height: 100px;">
              "The 1-on-1 mentorship at Parashari Institute transformed my understanding of Jyotish. My mentor was available even at odd hours to clear my doubts. Truly 24×7 support!"
            </p>
            <div>
              <h4 style="color: #111827; font-size: 1.05rem; margin: 0 0 4px; font-family: 'Cinzel', serif; font-weight: 700;">Priya Nair</h4>
              <p style="color: #9ca3af; font-size: 0.9rem; margin: 0;">Kerala</p>
            </div>
          </div>

          <div style="background: #fff; padding: 40px; border-radius: 12px; border: 1px solid #e5e7eb; position: relative;">
            <i class="fa-solid fa-quote-right" style="position: absolute; right: 30px; top: 30px; font-size: 2.5rem; color: #f3f4f6;"></i>
            <div style="color: #eab308; font-size: 1rem; margin-bottom: 20px; display: flex; gap: 3px;">
              <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
            </div>
            <p style="color: #4b5563; font-style: italic; font-size: 1.05rem; line-height: 1.7; margin-bottom: 30px; min-height: 100px;">
              "After trying multiple online courses, the personalized mentorship here was a game-changer. The chart reading practice with real-time feedback accelerated my learning tenfold."
            </p>
            <div>
              <h4 style="color: #111827; font-size: 1.05rem; margin: 0 0 4px; font-family: 'Cinzel', serif; font-weight: 700;">Rajesh Gupta</h4>
              <p style="color: #9ca3af; font-size: 0.9rem; margin: 0;">Delhi</p>
            </div>
          </div>

          <div style="background: #fff; padding: 40px; border-radius: 12px; border: 1px solid #e5e7eb; position: relative;">
            <i class="fa-solid fa-quote-right" style="position: absolute; right: 30px; top: 30px; font-size: 2.5rem; color: #f3f4f6;"></i>
            <div style="color: #eab308; font-size: 1rem; margin-bottom: 20px; display: flex; gap: 3px;">
              <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
            </div>
            <p style="color: #4b5563; font-style: italic; font-size: 1.05rem; line-height: 1.7; margin-bottom: 30px; min-height: 100px;">
              "From complete beginner to certified astrologer in 8 months. The dedication of my mentor and the structured curriculum made all the difference."
            </p>
            <div>
              <h4 style="color: #111827; font-size: 1.05rem; margin: 0 0 4px; font-family: 'Cinzel', serif; font-weight: 700;">Ananya Sharma</h4>
              <p style="color: #9ca3af; font-size: 0.9rem; margin: 0;">Mumbai</p>
            </div>
          </div>

        </div>
      </div>
    </section>

  </main>
"""

with open('d:\\ParashariTeam\\AB_AI\\mentorship.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace old <main id="mentorship-content">...</main> with new html_content
new_text = re.sub(r'<main id="mentorship-content".*?</main>', html_content, text, flags=re.DOTALL)

with open('d:\\ParashariTeam\\AB_AI\\mentorship.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Injected UI dynamically!")
