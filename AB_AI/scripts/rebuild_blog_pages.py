import os

HEADER = '''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Parashari Indian Institute</title>
  <link rel="stylesheet" href="assets/css/main.css">
  <link rel="stylesheet" href="assets/css/navbar.css">
  <link rel="stylesheet" href="assets/css/footer.css">
  <link rel="stylesheet" href="assets/css/responsive.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="assets/css/loader.css">
  <link rel="stylesheet" href="assets/css/search.css">
  <link rel="stylesheet" href="assets/css/chatbot.css">
</head>

<body>

  <div class="header-top">
    <div class="header-top-content">
      <div class="header-top-left">
        <div class="header-top-item"><span class="header-top-icon">📞</span><a href="tel:+919999999999">+91
            9999-999-999</a></div>
        <div class="header-top-item"><span class="header-top-icon">✉️</span><a
            href="mailto:info@parashari.com">info@parashari.com</a></div>
      </div>
      <div class="header-top-right">Online Classes | ISO Certified</div>
    </div>
  </div>

  <header>
    <nav class="navbar">
      <ul class="nav-menu">

        <li class="nav-item search-nav-item">
          <div class="search-container">
            <div class="container-input">
              <input type="text" placeholder="Search all courses" name="text" class="input" id="courseSearchInput">
              <svg fill="#000000" width="20px" height="20px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M790.588 1468.235c-373.722 0-677.647-303.924-677.647-677.647 0-373.722 303.925-677.647 677.647-677.647 373.723 0 677.647 303.925 677.647 677.647 0 373.723-303.924 677.647-677.647 677.647Zm596.781-160.715c120.396-138.692 193.807-319.285 193.807-516.932C1581.176 354.748 1226.428 0 790.588 0S0 354.748 0 790.588s354.748 790.588 790.588 790.588c197.647 0 378.24-73.411 516.932-193.807l516.028 516.142 79.963-79.963-516.142-516.028Z"
                  fill-rule="evenodd"></path>
              </svg>
            </div>
            <div id="searchResults" class="search-results"></div>
          </div>
        </li>

        <li class="nav-item"><a href="index.html">Home</a></li>
        <li class="nav-item"><a href="profile.html">About Us</a></li>

        <li class="nav-item dropdown">
          <a href="javascript:void(0)">Courses <i class="fas fa-chevron-down"
              style="font-size: 0.8em; margin-left: 4px;"></i></a>
          <ul class="dropdown-menu">
            <li class="dropdown-item"><a href="astrology.html">Vedic Astrology</a></li>
            <li class="dropdown-item"><a href="nadi-jyotish.html">Nadi Jyotish</a></li>
            <li class="dropdown-item"><a href="lal-kitab.html">Lal Kitab Remedies</a></li>
            <li class="dropdown-item"><a href="remedy-course.html">Remedy Course (Upaay Gyaan)</a></li>
            <li class="dropdown-item"><a href="kp-astrology.html">KP Astrology</a></li>
            <li class="dropdown-item"><a href="bnn-astrology.html">BNN (Advanced Techniques)</a></li>
            <li class="dropdown-item"><a href="crystal-healing.html">Crystal Healing</a></li>
            <li class="dropdown-item"><a href="medical-astrology.html">Medical Astrology</a></li>
            <li class="dropdown-item"><a href="complete-astrology.html">Complete Astrology Course</a></li>
            <li class="dropdown-item"><a href="rudraksha.html">Rudraksha Remedies</a></li>
            <li class="dropdown-item"><a href="vastu.html">Vastu Shastra</a></li>
            <li class="dropdown-item"><a href="palmistry.html">Palmistry</a></li>
            <li class="dropdown-item"><a href="face-reading.html">Face Reading</a></li>
            <li class="dropdown-item"><a href="tarot.html">Tarot Reading</a></li>
            <li class="dropdown-item"><a href="numerology.html">Numerology</a></li>
            <li class="dropdown-item"><a href="mentorship.html">1-on-1 Mentorship</a></li>
          </ul>
        </li>
        <li class="nav-item"><a href="fee-structure.html">Fee Structure</a></li>
        <li class="nav-item"><a href="courses.html">Explore</a></li>
        <li class="nav-item"><a href="blog.html" class="active">Blog</a></li>
        <li class="nav-item"><a href="6-stairs.html">6 Stairs</a></li>
        <li class="nav-item"><a href="gallery.html">Gallery</a></li>
        <li class="nav-item"><a href="contact.html">Contact</a></li>
      </ul>

      <div class="navbar-cta">
        <a href="login.html" class="btn btn-outline btn-sm">Login</a>
        <a href="register.html" class="btn btn-primary btn-sm">Register</a>
      </div>

      <button class="hamburger" title="Toggle navigation menu" aria-label="Toggle navigation menu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </nav>

    <div class="mobile-menu">
      <ul class="nav-menu mobile-menu-nav">
        <li class="nav-item w-full"><a href="index.html">Home</a></li>
        <li class="nav-item w-full"><a href="profile.html">About Us</a></li>
        <li class="nav-item w-full"><a href="courses.html">Courses</a></li>
        <li class="nav-item w-full"><a href="fee-structure.html">Fee Structure</a></li>
        <li class="nav-item w-full"><a href="courses.html">Explore</a></li>
        <li class="nav-item w-full"><a href="blog.html" class="active">Blog</a></li>
        <li class="nav-item w-full"><a href="6-stairs.html">6 Stairs</a></li>
        <li class="nav-item w-full"><a href="gallery.html">Gallery</a></li>
        <li class="nav-item w-full"><a href="contact.html">Contact</a></li>
      </ul>
      <div class="navbar-cta">
        <a href="login.html" class="btn btn-outline btn-sm">Login</a>
        <a href="register.html" class="btn btn-primary btn-sm">Register</a>
      </div>
    </div>

    <div class="tablet-search-container">
      <div class="search-container">
        <div class="container-input">
          <input type="text" placeholder="Search all courses" name="text" class="input" id="courseSearchInput2">
          <svg fill="#666" width="20px" height="20px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
            <path d="M790.588 1468.235c-373.722 0-677.647-303.924-677.647-677.647 0-373.722 303.925-677.647 677.647-677.647 373.723 0 677.647 303.925 677.647 677.647 0 373.723-303.924 677.647-677.647 677.647Zm596.781-160.715c120.396-138.692 193.807-319.285 193.807-516.932C1581.176 354.748 1226.428 0 790.588 0S0 354.748 0 790.588s354.748 790.588 790.588 790.588c197.647 0 378.24-73.411 516.932-193.807l516.028 516.142 79.963-79.963-516.142-516.028Z" fill-rule="evenodd"></path>
          </svg>
          <div class="search-results"></div>
        </div>
      </div>
    </div>
  </header>'''

FOOTER = '''
  <footer>
    <div class="footer-content">
      <div class="footer-section">
        <h4>About Parashari</h4>
        <p>Preserving and promoting authentic Vedic wisdom since 1998.</p>
        <div class="social-wrapper">
          <a href="https://www.instagram.com/astrobharatai?igsh=Z2M2ZW82OXBxaGNr" target="_blank" rel="noopener noreferrer" class="icon instagram">
            <span class="tooltip">Instagram</span>
            <i class="fab fa-instagram"></i>
          </a>
          <a href="https://www.youtube.com/@astrobharatai" target="_blank" rel="noopener noreferrer" class="icon youtube">
            <span class="tooltip">YouTube</span>
            <i class="fab fa-youtube"></i>
          </a>
          <a href="https://x.com/AstroBharatAI" target="_blank" rel="noopener noreferrer" class="icon twitter">
            <span class="tooltip">Twitter</span>
            <i class="fab fa-twitter"></i>
          </a>
          <a href="https://www.linkedin.com/company/astrobharatai/" target="_blank" rel="noopener noreferrer" class="icon linkedin">
            <span class="tooltip">LinkedIn</span>
            <i class="fab fa-linkedin-in"></i>
          </a>
        </div>
      </div>
      <div class="footer-section">
        <h4>Quick Links</h4>
        <ul class="footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="profile.html">About Us</a></li>
          <li><a href="fee-structure.html">Fee Structure</a></li>
          <li><a href="courses.html">Explore</a></li>
          <li><a href="blog.html">Blog</a></li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer-section">
        <h4>Programs</h4>
        <ul class="footer-links">
          <li><a href="courses.html">Crash Course</a></li>
          <li><a href="courses.html">Diploma</a></li>
          <li><a href="courses.html">Bachelor</a></li>
          <li><a href="courses.html">Master</a></li>
          <li><a href="courses.html">Grand Master</a></li>
          <li><a href="6-stairs.html">6 Stairs</a></li>
        </ul>
      </div>
      <div class="footer-section">
        <h4>Contact</h4>
        <div class="contact-info">
          <div class="contact-icon">📍</div>
          <div class="contact-text">
            <p class="p-reset">123 Vedic Street, Delhi - 110001</p>
          </div>
        </div>
        <div class="contact-info">
          <div class="contact-icon">📞</div>
          <div class="contact-text">
            <p class="p-reset"><a href="tel:+919005703159">+91 9005703159</a></p>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-bottom-content">
        <div class="copyright">
          <p class="p-reset">&copy; 2024 Parashari Institute. All rights reserved.</p>
        </div>
        <div class="developer-credit">Designed by <a href="#">Our Team</a></div>
      </div>
    </div>
  </footer>

  <script src="assets/js/navbar.js"></script>
  <script src="assets/js/form-validation.js"></script>
  <script src="assets/js/main.js"></script>
  <script src="assets/js/loader.js"></script>
  <script src="assets/js/search.js"></script>
  <script src="assets/js/chatbot.js"></script>
</body>

</html>'''

# ─────────────────────────────────────────────
# Page content definitions
# ─────────────────────────────────────────────

pages = {
    'blog-mangal-dosha.html': {
        'title': 'Mangal Dosha: Myths, Reality & Remedies',
        'hero_icon': '🔴',
        'hero_title': 'Mangal Dosha: Myths, Reality, and Effective Remedies',
        'hero_sub': 'Vedic Astrology · By Dr. Aadesh Sharma · 26 Feb 2026',
        'back': True,
        'sections': [
            ('what', 'What is Mangal Dosha?',
             '''<div class="grid grid-2 grid-gap-3">
          <div data-animate>
            <p>Mangal Dosha (also called Kuja Dosha or Chevvai Dosham) occurs when Mars (Mangal) is placed in specific houses of the birth chart. According to classical Vedic texts, Mars in the 1st, 4th, 7th, 8th, or 12th house from the Ascendant, Moon, or Venus creates this Dosha.</p>
            <p>It is said to cause turbulence in a person's married life if their partner does not also carry the same Dosha. However, the actual impact varies significantly based on the overall strength of the horoscope.</p>
            <ul class="list-reset">
              <li class="mb-0-75">✓ Affects approximately 40–50% of all horoscopes</li>
              <li class="mb-0-75">✓ Severity depends on the house and sign of Mars</li>
              <li class="mb-0-75">✓ Can be fully cancelled (Dosha Parihara) in many cases</li>
              <li>✓ Proper remediation leads to a harmonious marriage</li>
            </ul>
          </div>
          <div data-animate>
            <img src="assets/images/aries-card.png" alt="Mangal Dosha" class="rounded-lg">
          </div>
        </div>'''),
            ('myth', 'Myths vs. Reality', '''<div class="grid grid-2 grid-gap-2">
          <div class="card card-auto p-4" data-animate>
            <h3 class="color-primary mb-1 text-center">Common Myths</h3>
            <ul class="list-reset">
              <li class="mb-0-75">❌ Always causes death of spouse</li>
              <li class="mb-0-75">❌ Makes a person unmarriageable</li>
              <li class="mb-0-75">❌ Affects only women</li>
              <li>❌ Cannot be remedied</li>
            </ul>
          </div>
          <div class="card card-auto p-4" data-animate>
            <h3 class="color-primary mb-1 text-center">Reality</h3>
            <ul class="list-reset">
              <li class="mb-0-75">✓ Rarely causes such extreme outcomes</li>
              <li class="mb-0-75">✓ Cancelled by several planetary combinations</li>
              <li class="mb-0-75">✓ Equally applicable to both genders</li>
              <li>✓ Multiple powerful remedies exist</li>
            </ul>
          </div>
        </div>
        <table class="program-table mt-2">
          <tr class="table-row"><td class="table-cell-bold">Mars in 1st House</td><td class="table-cell-right">Self-assertion issues, aggression in marriage</td></tr>
          <tr class="table-row"><td class="table-cell-bold">Mars in 4th House</td><td class="table-cell-right">Domestic discord, property disputes</td></tr>
          <tr class="table-row"><td class="table-cell-bold">Mars in 7th House</td><td class="table-cell-right">Conflicts with partner, delay in marriage</td></tr>
          <tr class="table-row"><td class="table-cell-bold">Mars in 8th House</td><td class="table-cell-right">Most intense form — health of spouse affected</td></tr>
          <tr><td class="table-cell-bold">Mars in 12th House</td><td class="table-cell-right">Emotional disconnection, hidden conflicts</td></tr>
        </table>''', 'light-bg'),
            ('remedies', 'Effective Remedies for Mangal Dosha', '''<div class="grid grid-3 grid-gap-2">
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">🔱</div>
            <h4>Mangal Puja & Yagna</h4>
            <p>Hanuman Chalisa recitation every Tuesday and Mangal havan performed by a qualified priest.</p>
          </div>
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">💍</div>
            <h4>Gemstone Therapy</h4>
            <p>Wearing a Red Coral (Moonga) set in gold or copper ring on the ring finger of the right hand.</p>
          </div>
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">🌿</div>
            <h4>Kumbh Vivah</h4>
            <p>A symbolic ceremonial marriage to a banana tree or idol of Lord Vishnu before the actual wedding.</p>
          </div>
        </div>'''),
        ],
        'cta_title': 'Get Your Mangal Dosha Analysis Done',
        'cta_sub': 'Our certified Vedic astrologers provide a complete Mangal Dosha report with personalized remedies.',
        'cta_link': 'astrology.html',
        'cta_label': 'Explore Vedic Astrology Course',
    },

    'blog-vastu-tips.html': {
        'title': '10 Essential Vastu Tips for Prosperity',
        'hero_icon': '🏠',
        'hero_title': '10 Essential Vastu Tips for Prosperity and Peace in Your Home',
        'hero_sub': 'Vastu Shastra · By Pt. Ramakant · 25 Feb 2026',
        'back': True,
        'sections': [
            ('intro', 'What is Vastu Shastra?', '''<div class="grid grid-2 grid-gap-3">
          <div data-animate>
            <p>Vastu Shastra is the ancient Indian science of architecture and spatial harmony. It teaches us how to align our living spaces with the five natural elements — Earth, Water, Fire, Air, and Space.</p>
            <p>A well-aligned Vastu home promotes health, wealth and positive relationships. Even small changes can have a dramatic effect on the energy of your living space.</p>
            <ul class="list-reset">
              <li class="mb-0-75">✓ Based on 5 natural elements (Pancha Bhoota)</li>
              <li class="mb-0-75">✓ Eight cardinal directions govern different life areas</li>
              <li class="mb-0-75">✓ Works for homes, offices, and commercial spaces</li>
              <li>✓ Can be applied to existing buildings with remedies</li>
            </ul>
          </div>
          <div data-animate>
            <img src="assets/images/taurus-card.png" alt="Vastu Shastra" class="rounded-lg">
          </div>
        </div>'''),
            ('elements', 'The 5 Elements & Their Directions', '''<table class="program-table">
          <tr class="table-row"><td class="table-cell-bold">Water (Jal)</td><td class="table-cell-right">North-East — Pooja Room, Underground Tank</td></tr>
          <tr class="table-row"><td class="table-cell-bold">Fire (Agni)</td><td class="table-cell-right">South-East — Kitchen, Electrical Panels</td></tr>
          <tr class="table-row"><td class="table-cell-bold">Earth (Prithvi)</td><td class="table-cell-right">South-West — Master Bedroom, Heavy Furniture</td></tr>
          <tr class="table-row"><td class="table-cell-bold">Air (Vayu)</td><td class="table-cell-right">North-West — Guest Room, Large Windows</td></tr>
          <tr><td class="table-cell-bold">Space (Akash)</td><td class="table-cell-right">Centre (Brahmasthan) — Must remain open</td></tr>
        </table>''', 'light-bg'),
            ('tips', '10 Quick Vastu Fixes', '''<div class="grid grid-2 grid-gap-2">
          <div class="card card-auto p-4" data-animate>
            <h3 class="color-primary mb-1">Entrance & Bedroom</h3>
            <ul class="list-reset">
              <li class="mb-0-75">✓ Main entrance in North, East, or North-East</li>
              <li class="mb-0-75">✓ Sleep with head towards South or East</li>
              <li class="mb-0-75">✓ Master bedroom in South-West corner</li>
              <li>✓ No mirror directly opposite the bed</li>
            </ul>
          </div>
          <div class="card card-auto p-4" data-animate>
            <h3 class="color-primary mb-1">Kitchen & Energy</h3>
            <ul class="list-reset">
              <li class="mb-0-75">✓ Kitchen in the South-East; cook facing East</li>
              <li class="mb-0-75">✓ Bowl of sea salt in corners — replace monthly</li>
              <li class="mb-0-75">✓ Wind chime in North-West for air element</li>
              <li>✓ Brahmasthan (centre) must be open & clean</li>
            </ul>
          </div>
        </div>'''),
        ],
        'cta_title': 'Get a Full Vastu Analysis for Your Home or Office',
        'cta_sub': 'Our certified Vastu experts perform online or on-site evaluations with full reports.',
        'cta_link': 'vastu.html',
        'cta_label': 'Explore Vastu Shastra Course',
    },

    'blog-lal-kitab-financial.html': {
        'title': 'Lal Kitab Remedies for Financial Stability',
        'hero_icon': '📕',
        'hero_title': 'Lal Kitab Remedies for Financial Stability and Career Growth',
        'hero_sub': 'Lal Kitab · By Anjali Verma · 24 Feb 2026',
        'back': True,
        'sections': [
            ('intro', 'What is Lal Kitab?', '''<div class="grid grid-2 grid-gap-3">
          <div data-animate>
            <p>Lal Kitab is a series of five Urdu books authored between 1939–1952, offering a unique system of astrology and karma-based remedies. Unlike classical Vedic remedies involving expensive rituals, Lal Kitab remedies use everyday actions accessible to everyone.</p>
            <ul class="list-reset">
              <li class="mb-0-75">✓ Simple, cost-effective daily remedies</li>
              <li class="mb-0-75">✓ Based on karmic debt and planetary placement</li>
              <li class="mb-0-75">✓ Works alongside classical Vedic analysis</li>
              <li>✓ Highly effective for financial and career issues</li>
            </ul>
          </div>
          <div data-animate>
            <img src="assets/images/gemini-card.png" alt="Lal Kitab" class="rounded-lg">
          </div>
        </div>'''),
            ('planets', 'Planetary Indicators of Financial Problems', '''<table class="program-table">
          <tr class="table-row"><td class="table-cell-bold">Jupiter (Guru)</td><td class="table-cell-right">Debilitated → Poor savings, banking loss, failed investments</td></tr>
          <tr class="table-row"><td class="table-cell-bold">Venus (Shukra)</td><td class="table-cell-right">Combust → Luxury debt, failed partnerships, low income</td></tr>
          <tr class="table-row"><td class="table-cell-bold">Mercury (Budh)</td><td class="table-cell-right">With Ketu → Business confusion, poor communication</td></tr>
          <tr class="table-row"><td class="table-cell-bold">Rahu</td><td class="table-cell-right">6th/8th house → Sudden losses, fraudulent schemes</td></tr>
          <tr><td class="table-cell-bold">Saturn (Shani)</td><td class="table-cell-right">Retrograde in 2nd → Delayed payments, blocked savings</td></tr>
        </table>''', 'light-bg'),
            ('remedies', 'Top 7 Lal Kitab Remedies for Wealth', '''<div class="grid grid-3 grid-gap-2">
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">🐜</div>
            <h4>Feed Black Ants</h4>
            <p>Offer sweet bread daily to black ants to strengthen Mercury — planet of trade and business logic.</p>
          </div>
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">🪙</div>
            <h4>Silver Square in Wallet</h4>
            <p>Carry a solid square piece of silver in your wallet to strengthen the Moon and improve cash flow.</p>
          </div>
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">🟡</div>
            <h4>Thursday Yellow Practice</h4>
            <p>Wear yellow on Thursdays and donate gram flour sweets to a temple to activate Jupiter's blessings.</p>
          </div>
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">🧹</div>
            <h4>Respect Sweepers</h4>
            <p>Give a small offering to street sweepers to pacify Rahu and prevent sudden financial reversals.</p>
          </div>
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">⚫</div>
            <h4>Donate on Saturdays</h4>
            <p>Offer black sesame seeds and mustard oil to a temple on Saturday evenings to combat Saturn debt cycles.</p>
          </div>
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">🫙</div>
            <h4>Full Kitchen Vessels</h4>
            <p>Always keep kitchen pots partially filled — an empty vessel symbolises scarcity in Lal Kitab tradition.</p>
          </div>
        </div>'''),
        ],
        'cta_title': 'Get a Personalized Lal Kitab Chart Reading',
        'cta_sub': 'Our Lal Kitab specialists prescribe the exact remedies for your unique planetary configuration.',
        'cta_link': 'lal-kitab.html',
        'cta_label': 'Explore Lal Kitab Course',
    },

    'blog-numerology-life-path.html': {
        'title': 'Calculate Your Life Path Number',
        'hero_icon': '🔢',
        'hero_title': 'Calculate Your Life Path Number: Unlocking Your True Potential',
        'hero_sub': 'Numerology · By Suresh Nair · 22 Feb 2026',
        'back': True,
        'sections': [
            ('intro', 'What is Numerology?', '''<div class="grid grid-2 grid-gap-3">
          <div data-animate>
            <p>Numerology is the ancient science that studies the mystical relationship between numbers and life events. Your Life Path Number — the most significant number in your numerology chart — reveals your core personality traits, innate talents, and the overarching theme of your life's journey.</p>
            <ul class="list-reset">
              <li class="mb-0-75">✓ Derived entirely from your birth date</li>
              <li class="mb-0-75">✓ Ranges from 1–9 plus Master Numbers 11, 22, 33</li>
              <li class="mb-0-75">✓ Reveals life purpose, strengths and challenges</li>
              <li>✓ Can guide career, relationships and major decisions</li>
            </ul>
          </div>
          <div data-animate>
            <img src="assets/images/cancer-card.png" alt="Numerology" class="rounded-lg">
          </div>
        </div>'''),
            ('calc', 'How to Calculate Your Life Path Number', '''<div class="card card-auto p-4 mb-2" data-animate>
          <h3 class="color-primary mb-1">Step-by-Step Example: 15th October 1988</h3>
          <table class="program-table">
            <tr class="table-row"><td class="table-cell-bold">Day</td><td class="table-cell-right">15 → 1 + 5 = <strong>6</strong></td></tr>
            <tr class="table-row"><td class="table-cell-bold">Month (October)</td><td class="table-cell-right">10 → 1 + 0 = <strong>1</strong></td></tr>
            <tr class="table-row"><td class="table-cell-bold">Year</td><td class="table-cell-right">1988 → 1+9+8+8 = 26 → 2+6 = <strong>8</strong></td></tr>
            <tr><td class="table-cell-bold">Life Path Number</td><td class="table-cell-right">6 + 1 + 8 = 15 → 1+5 = <strong>6 — The Nurturer</strong></td></tr>
          </table>
        </div>''', 'light-bg'),
            ('numbers', 'All 9 Life Path Numbers', '''<div class="grid grid-3 grid-gap-2">
          <div class="card text-center card-auto p-3" data-animate><div class="font-3xl mb-1">1️⃣</div><h4>The Leader</h4><p>Independent, pioneering, driven, self-reliant</p></div>
          <div class="card text-center card-auto p-3" data-animate><div class="font-3xl mb-1">2️⃣</div><h4>The Peacemaker</h4><p>Cooperative, intuitive, diplomatic</p></div>
          <div class="card text-center card-auto p-3" data-animate><div class="font-3xl mb-1">3️⃣</div><h4>The Communicator</h4><p>Creative, social, expressive, joyful</p></div>
          <div class="card text-center card-auto p-3" data-animate><div class="font-3xl mb-1">4️⃣</div><h4>The Builder</h4><p>Practical, hardworking, disciplined</p></div>
          <div class="card text-center card-auto p-3" data-animate><div class="font-3xl mb-1">5️⃣</div><h4>The Adventurer</h4><p>Freedom-loving, versatile, restless</p></div>
          <div class="card text-center card-auto p-3" data-animate><div class="font-3xl mb-1">6️⃣</div><h4>The Nurturer</h4><p>Compassionate, responsible, harmonious</p></div>
          <div class="card text-center card-auto p-3" data-animate><div class="font-3xl mb-1">7️⃣</div><h4>The Seeker</h4><p>Analytical, introspective, mystical</p></div>
          <div class="card text-center card-auto p-3" data-animate><div class="font-3xl mb-1">8️⃣</div><h4>The Achiever</h4><p>Ambitious, authoritative, material</p></div>
          <div class="card text-center card-auto p-3" data-animate><div class="font-3xl mb-1">9️⃣</div><h4>The Humanitarian</h4><p>Compassionate, wise, altruistic</p></div>
        </div>'''),
        ],
        'cta_title': 'Discover Your Complete Numerology Profile',
        'cta_sub': 'Life Path is just the start. Learn Name Numbers, Destiny Numbers and Karmic Debt in our full course.',
        'cta_link': 'numerology.html',
        'cta_label': 'Explore Numerology Course',
    },

    'blog-kp-astrology.html': {
        'title': 'Introduction to KP Astrology',
        'hero_icon': '⭐',
        'hero_title': 'Introduction to KP Astrology: How It Differs From Traditional Vedic',
        'hero_sub': 'KP Astrology · By Vikram Singh · 20 Feb 2026',
        'back': True,
        'sections': [
            ('intro', 'What is KP Astrology?', '''<div class="grid grid-2 grid-gap-3">
          <div data-animate>
            <p>Krishnamurti Paddhati (KP) is a highly refined astrological system created by Prof. K.S. Krishnamurti. While it originates from Vedic Astrology, it incorporates the revolutionary Sub-Lord theory that makes event-timing predictions remarkably precise.</p>
            <ul class="list-reset">
              <li class="mb-0-75">✓ Developed in India between 1939–1972</li>
              <li class="mb-0-75">✓ Uses Placidus house system (not equal whole-sign)</li>
              <li class="mb-0-75">✓ Sub-Lord theory enables day-accurate predictions</li>
              <li>✓ Ideal for Prashna (horary) chart analysis</li>
            </ul>
          </div>
          <div data-animate>
            <img src="assets/images/leo-card.png" alt="KP Astrology" class="rounded-lg">
          </div>
        </div>'''),
            ('diff', 'KP vs. Vedic: Key Differences', '''<table class="program-table">
          <tr class="table-row"><td class="table-cell-bold">House Division</td><td class="table-cell-right">KP: Placidus (unequal) vs. Vedic: Whole-sign</td></tr>
          <tr class="table-row"><td class="table-cell-bold">Predictive Basis</td><td class="table-cell-right">KP: Star + Sub-Lord chain vs. Vedic: Planet dignities</td></tr>
          <tr class="table-row"><td class="table-cell-bold">Ayanamsa</td><td class="table-cell-right">KP: Unique KP Ayanamsa vs. Vedic: Lahiri</td></tr>
          <tr class="table-row"><td class="table-cell-bold">Event Timing</td><td class="table-cell-right">KP: Day-accurate via Sub-Sub vs. Vedic: Broad Dasha periods</td></tr>
          <tr><td class="table-cell-bold">Cusp Analysis</td><td class="table-cell-right">KP: Sub-Lord of cusp decides outcome vs. Vedic: House lord</td></tr>
        </table>''', 'light-bg'),
            ('sublord', 'The Star Lord — Sub-Lord Hierarchy', '''<div class="grid grid-3 grid-gap-2">
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">🌟</div>
            <h4>Planet Layer</h4>
            <p>The planet in whose Nakshatra another planet sits gives the primary signification</p>
          </div>
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">⭐</div>
            <h4>Star Lord Layer</h4>
            <p>The Nakshatra lord modifies and channels the energy of the planet above it</p>
          </div>
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">✨</div>
            <h4>Sub-Lord Layer</h4>
            <p>The Sub-Lord determines whether the result is positive, negative, or absent entirely</p>
          </div>
        </div>'''),
        ],
        'cta_title': 'Master the KP System with Our Expert Faculty',
        'cta_sub': 'Our KP Astrology Certification Course takes you from basics to pinpoint event-timing techniques.',
        'cta_link': 'kp-astrology.html',
        'cta_label': 'Explore KP Astrology Course',
    },

    'blog-student-success.html': {
        'title': "From Enthusiast to Professional: Rahul's Journey",
        'hero_icon': '🎓',
        'hero_title': "From Enthusiast to Professional: Rahul's Journey with Parashari",
        'hero_sub': 'Student Success · By Parashari Institute · 18 Feb 2026',
        'back': True,
        'sections': [
            ('story', "Rahul's Story", '''<div class="grid grid-2 grid-gap-3">
          <div data-animate>
            <p>Rahul Verma came to the Parashari Institute three years ago as a software engineer looking for answers during a period of personal uncertainty. Today, he runs a flourishing astrology consultancy with over 200 active clients across India, Dubai, and Canada.</p>
            <p>Like many of our students, his journey began with a personal crisis and a chance encounter with a chart reading. What followed was a systematic, structured education that transformed a casual interest into a full-time vocation.</p>
            <ul class="list-reset">
              <li class="mb-0-75">✓ 200+ active clients across 3 countries</li>
              <li class="mb-0-75">✓ First paying client within 8 months of joining</li>
              <li class="mb-0-75">✓ Now mentors 12 junior students of his own</li>
              <li>✓ Guest faculty at Parashari Institute events</li>
            </ul>
          </div>
          <div data-animate>
            <img src="assets/images/virgo-card.jpg" alt="Student Success" class="rounded-lg">
          </div>
        </div>'''),
            ('courses', 'Courses Rahul Completed', '''<table class="program-table">
          <tr class="table-row"><td class="table-cell-bold">Vedic Astrology (Parashari)</td><td class="table-cell-right">6 months — Natal chart, Dasha, Divisional charts</td></tr>
          <tr class="table-row"><td class="table-cell-bold">KP Astrology Certification</td><td class="table-cell-right">4 months — Sub-Lord theory, Prashna, Event timing</td></tr>
          <tr class="table-row"><td class="table-cell-bold">Lal Kitab Remedies</td><td class="table-cell-right">2 months — Practical karmic remedies, Debt analysis</td></tr>
          <tr><td class="table-cell-bold">Grand Master Mentorship</td><td class="table-cell-right">Ongoing — Advanced techniques, Client skills, Ethics</td></tr>
        </table>''', 'light-bg'),
            ('why', 'Why Parashari Works', '''<div class="grid grid-3 grid-gap-2">
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">📚</div>
            <h4>Structured Curriculum</h4>
            <p>From foundation to specialization — every module builds on the last with no gaps in knowledge.</p>
          </div>
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">👨‍🏫</div>
            <h4>Expert Faculty</h4>
            <p>Learn directly from practicing astrologers with decades of real-world consultation experience.</p>
          </div>
          <div class="card text-center card-auto p-3" data-animate>
            <div class="font-3xl mb-1">🤝</div>
            <h4>Career Support</h4>
            <p>We help students build their first client base through mentorship, referrals, and portfolio workshops.</p>
          </div>
        </div>'''),
        ],
        'cta_title': 'Start Your Own Journey Today',
        'cta_sub': 'Join thousands of students who have transformed their passion for astrology into a professional calling.',
        'cta_link': 'courses.html',
        'cta_label': 'Explore Our Courses',
    },
}

# ─────────────────────────────────────────────
# Build each page
# ─────────────────────────────────────────────

for filename, data in pages.items():
    parts = [HEADER.format(title=data['title'])]

    # Hero section
    parts.append(f'''
  <section class="hero-section hero-gradient" style="position: relative;">
    <div class="container">
      <p style="margin-bottom:0.5rem;"><a href="blog.html" style="color:var(--secondary-color); text-decoration:none;">← Back to All Blogs</a></p>
      <h1 class="color-secondary">{data["hero_icon"]} {data["hero_title"]}</h1>
      <p>{data["hero_sub"]}</p>
    </div>
  </section>
''')

    # Content sections
    for i, section in enumerate(data['sections']):
        s_id = section[0]
        s_title = section[1]
        s_html = section[2]
        s_class = section[3] if len(section) > 3 else ''
        sec_class = f'section {s_class}'.strip()
        parts.append(f'''
  <section class="{sec_class}">
    <div class="container">
      <h2 class="card-section-title">{s_title}</h2>
      {s_html}
    </div>
  </section>
''')

    # CTA section
    parts.append(f'''
  <section class="light-bg">
    <div class="container text-center">
      <h2 class="mb-1-5">{data["cta_title"]}</h2>
      <p class="mb-2">{data["cta_sub"]}</p>
      <a href="{data["cta_link"]}" class="btn btn-primary btn-lg">{data["cta_label"]}</a>
    </div>
  </section>
''')

    parts.append(FOOTER)

    content = '\n'.join(parts)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Generated: {filename}')

print('All 6 blog detail pages rebuilt.')
