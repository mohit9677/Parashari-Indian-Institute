import re

FULL_HEADER = '''    <div class="header-top">
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
                    <!-- Search Bar Injected -->
                    <div class="search-container">
                        <div class="container-input">
                            <input type="text" placeholder="Search all courses" name="text" class="input"
                                id="courseSearchInput">
                            <svg fill="#000000" width="20px" height="20px" viewBox="0 0 1920 1920"
                                xmlns="http://www.w3.org/2000/svg">
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
    </header>'''

IMPROVED_STYLES = '''
    <style>
        /* Page Layout */
        .blog-detail-page { background: #f4f2ef; padding: 3rem 0 4rem; }
        .blog-detail-wrap { max-width: 860px; margin: 0 auto; padding: 0 1.5rem; }

        /* Card */
        .blog-detail-card { background: white; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 24px rgba(89,28,33,0.08); margin-bottom: 3rem; }

        /* Article Header area */
        .blog-article-header { padding: 2.5rem 2.5rem 0; text-align: left; }
        .blog-header-badge { display: inline-block; background: var(--primary-color); color: white; padding: 0.35rem 1rem; border-radius: 30px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 1rem; }
        .blog-detail-title { font-size: 2rem; color: var(--dark-text); line-height: 1.3; margin-bottom: 0.8rem; }
        .blog-detail-meta { display: flex; gap: 1.2rem; font-size: 0.88rem; color: #888; flex-wrap: wrap; padding-bottom: 1.5rem; border-bottom: 1px solid #f0eded; }
        .blog-detail-meta span i { margin-right: 0.35rem; color: var(--primary-color); }

        /* Hero image - constrained */
        .blog-hero-img-wrap { padding: 1.5rem 2.5rem; }
        .blog-hero-img { width: 100%; max-height: 320px; object-fit: cover; border-radius: 10px; display: block; }

        /* Article body */
        .blog-article-body { padding: 0 2.5rem 2.5rem; font-size: 1rem; line-height: 1.85; color: #333; }
        .blog-article-body h3 { font-size: 1.25rem; color: var(--primary-color); margin: 2rem 0 0.8rem; padding-left: 0.8rem; border-left: 4px solid var(--primary-color); }
        .blog-article-body p { margin-bottom: 1rem; }

        /* Tables */
        .data-table { width: 100%; border-collapse: collapse; margin: 1.2rem 0 1.8rem; font-size: 0.9rem; border-radius: 8px; overflow: hidden; }
        .data-table th { background: var(--primary-color); color: white; padding: 0.8rem 1rem; text-align: left; }
        .data-table td { padding: 0.75rem 1rem; border: 1px solid #e8e0e0; }
        .data-table tr:nth-child(even) td { background: #f9f4f4; }

        /* Highlight box */
        .highlight-box { background: #fff8e1; border-left: 4px solid #ffc107; padding: 1.2rem 1.4rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0; }

        /* Quote */
        .quote-block { background: linear-gradient(135deg, #591c21, #8b1a20); color: white; border-radius: 12px; padding: 1.8rem 2rem; margin: 1.5rem 0; font-size: 1.1rem; font-style: italic; line-height: 1.6; }

        /* Remedy cards */
        .remedy-card { display: flex; align-items: flex-start; gap: 1rem; background: #faf8f8; border: 1px solid #efe8e8; border-radius: 10px; padding: 1rem; margin-bottom: 0.8rem; }
        .remedy-num { min-width: 38px; height: 38px; background: var(--primary-color); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1rem; flex-shrink: 0; }

        /* Number / Direction grids */
        .num-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.8rem; margin: 1.2rem 0 1.8rem; }
        .num-card { border: 2px solid #e8d8d8; border-radius: 10px; padding: 1rem; text-align: center; }
        .num-card .big-num { font-size: 2.4rem; font-weight: 800; color: var(--primary-color); line-height: 1; }
        .num-card h4 { margin: 0.3rem 0 0.2rem; font-size: 0.9rem; color: var(--dark-text); }
        .num-card p { font-size: 0.78rem; color: #777; margin: 0; }

        .direction-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.8rem; margin: 1.2rem 0 1.8rem; }
        .dir-card { background: #f9f4f4; border: 1px solid #e8d5d5; border-radius: 10px; padding: 1rem; text-align: center; }
        .dir-card .dir-arrow { font-size: 1.6rem; }
        .dir-card h4 { color: var(--primary-color); margin: 0.4rem 0 0.2rem; font-size: 0.9rem; }
        .dir-card p { font-size: 0.78rem; color: #666; margin: 0; }

        /* Stats */
        .stats-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 1.5rem 0; }
        .stat-box { background: linear-gradient(135deg, var(--primary-color), #8b1a20); color: white; border-radius: 12px; padding: 1.2rem; text-align: center; }
        .stat-box .stat-num { font-size: 2.2rem; font-weight: 800; }
        .stat-box p { margin: 0; font-size: 0.85rem; opacity: 0.9; }

        /* Timeline */
        .timeline { list-style: none; padding: 0; position: relative; margin-bottom: 1.5rem; }
        .timeline li { padding-left: 2rem; margin-bottom: 1.2rem; border-left: 3px solid var(--primary-color); position: relative; padding-bottom: 0.5rem; }
        .timeline li::before { content: ""; position: absolute; left: -7px; top: 6px; width: 11px; height: 11px; border-radius: 50%; background: var(--primary-color); }

        /* Bar chart */
        .bar-chart-wrap { background: #fafafa; border: 1px solid #eee; padding: 1.2rem; border-radius: 10px; text-align: center; margin: 1.2rem 0 1.8rem; }
        .bar-chart { height: 170px; display: flex; align-items: flex-end; justify-content: space-around; gap: 10px; padding: 0 1rem; }
        .bar { border-radius: 4px 4px 0 0; }
        .bar-labels { display: flex; justify-content: space-around; padding: 0 1rem; margin-top: 8px; font-size: 0.78rem; font-weight: 700; color: #555; }

        /* Calc box */
        .calc-box { background: #f5f5f5; padding: 1.2rem 1.5rem; border-radius: 10px; font-family: 'Courier New', monospace; font-size: 0.95rem; line-height: 2; margin: 1.2rem 0; border: 1px solid #ddd; }

        /* Tags */
        .tag-list { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 1.5rem; }
        .tag { background: #f0e8e8; color: var(--primary-color); padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.82rem; font-weight: 500; }

        /* CTA */
        .cta-box { background: linear-gradient(135deg, var(--primary-color), #8b1a20); color: white; border-radius: 12px; padding: 1.8rem 2rem; text-align: center; margin-top: 2rem; }
        .cta-box h4 { font-size: 1.3rem; margin-bottom: 0.6rem; }
        .cta-box a { display: inline-block; background: white; color: var(--primary-color); padding: 0.65rem 1.8rem; border-radius: 8px; font-weight: 700; text-decoration: none; margin-top: 0.8rem; }

        /* Back button */
        .back-btn { display: inline-flex; align-items: center; gap: 0.5rem; color: var(--primary-color); font-weight: 600; text-decoration: none; margin-bottom: 1.5rem; font-size: 0.92rem; }
        .back-btn:hover { text-decoration: underline; }

        @media (max-width: 600px) {
            .blog-article-header, .blog-hero-img-wrap, .blog-article-body { padding-left: 1.2rem; padding-right: 1.2rem; }
            .num-grid, .direction-grid, .stats-row { grid-template-columns: repeat(2, 1fr); }
            .blog-detail-title { font-size: 1.5rem; }
        }
    </style>'''

files = [
    'blog-mangal-dosha.html',
    'blog-vastu-tips.html',
    'blog-lal-kitab-financial.html',
    'blog-numerology-life-path.html',
    'blog-kp-astrology.html',
    'blog-student-success.html',
]

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace the full header block (from <div class="header-top"> to </header>)
    content = re.sub(
        r'<div class="header-top">.*?</header>',
        FULL_HEADER,
        content,
        flags=re.DOTALL
    )

    # 2. Replace the old <style> block with the improved styles
    content = re.sub(
        r'<style>.*?</style>',
        IMPROVED_STYLES,
        content,
        count=1,
        flags=re.DOTALL
    )

    # 3. Fix the blog-hero-img: wrap it in blog-hero-img-wrap div and change class
    content = content.replace(
        '<img src=',
        '<div class="blog-hero-img-wrap"><img class="blog-hero-img" src=',
        1
    )
    # Close the wrapper after the img tag
    content = re.sub(
        r'(<img class="blog-hero-img"[^>]+>)\s*(<div class="blog-article-body"|<div class="blog-body")',
        r'\1</div>\n            \2',
        content
    )

    # 4. Replace blog-article-header and blog-body/blog-card classes for consistent structure
    content = content.replace('class="blog-detail-header"', 'class="blog-article-header"')
    content = content.replace('class="blog-detail-content"', 'class="blog-article-body"')
    content = content.replace('class="blog-body"', 'class="blog-article-body"')

    # 5. Remove the old inline hero image style from the img inside detail card
    content = re.sub(
        r'<img src="([^"]+)" alt="([^"]+)" class="blog-hero-img" style="[^"]*">',
        r'<img src="\1" alt="\2" class="blog-hero-img">',
        content
    )

    # 6. Also fix the script tag at the bottom — add search.js
    content = content.replace(
        '<script src="assets/js/navbar.js"></script>',
        '<script src="assets/js/navbar.js"></script>\n    <script src="assets/js/search.js"></script>'
    )

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed: {fname}')
