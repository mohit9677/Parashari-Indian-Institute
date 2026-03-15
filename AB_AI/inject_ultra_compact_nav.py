import os
import re

cwd = r"d:\ParashariTeam\AB_AI"
navbar_css_path = os.path.join(cwd, 'assets/css/navbar.css')

html_snippet = """
  <!-- Mobile Ultra-Compact Navbar Buttons -->
  <div class="mobile-navbar-actions">
    <a href="#" class="mobile-placement-btn" title="100% Placement Support">100%</a>
    <div class="mobile-tiny-cta">
      <a href="login.html" class="btn btn-outline mobile-tiny-btn">Login</a>
      <a href="register.html" class="btn btn-primary mobile-tiny-btn">Reg</a>
    </div>
  </div>
"""

css_snippet = """
/* Ultra-Compact Mobile Navbar Overrides */
.mobile-navbar-actions {
  display: none;
}
@media (max-width: 1150px) {
  .navbar {
    display: flex !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 5px 10px !important;
    gap: 4px !important;
    height: 60px !important; /* Force tight height */
    min-height: 60px !important;
  }
  .logo {
    flex-shrink: 0;
  }
  .mobile-logo {
    max-height: 38px !important; /* Shrink logo slightly to fit */
    width: auto;
  }
  .mobile-navbar-actions {
    display: flex;
    flex: 1;
    align-items: center;
    justify-content: flex-end;
    gap: 4px;
    margin: 0 4px;
  }
  .mobile-placement-btn {
    background: linear-gradient(135deg, #c8960c, #8b4513);
    color: white !important;
    font-size: 11px;
    font-weight: 800;
    padding: 4px 6px;
    border-radius: 4px;
    text-decoration: none;
    white-space: nowrap;
    margin-right: auto; /* Pushes login/reg to the right */
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    letter-spacing: 0.5px;
  }
  .mobile-tiny-cta {
    display: flex;
    gap: 3px;
  }
  .mobile-tiny-btn {
    font-size: 10px !important;
    padding: 4px 6px !important;
    white-space: nowrap !important;
    line-height: 1 !important;
    min-width: 0 !important;
    height: 24px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
  }
  .hamburger {
    margin-left: 0 !important;
    padding: 4px !important;
    gap: 4px !important;
    transform: scale(0.85); /* Shrink hamburger slightly */
  }
}
"""

def inject_mobile_navbar():
    # 1. Inject CSS into navbar.css
    with open(navbar_css_path, 'r', encoding='utf-8') as f:
        navbar_css = f.read()
        
    if "/* Ultra-Compact Mobile Navbar Overrides */" not in navbar_css:
        with open(navbar_css_path, 'a', encoding='utf-8') as f:
            f.write("\n" + css_snippet)
        print("CSS injected into navbar.css")
    else:
        print("CSS already present.")

    # 2. Inject HTML into all .html files
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    if "<!-- Mobile Ultra-Compact Navbar Buttons -->" not in content:
                        # Find the hamburger and insert right before it
                        # Hamburger looks like <button class="hamburger" id="hamburger"> or just <button class="hamburger"
                        
                        # Use regex to find the hamburger within <nav class="navbar">
                        pattern = re.compile(r'(<button class="hamburger"[^>]*>)')
                        new_content = pattern.sub(html_snippet + r'\1', content, count=1)
                        
                        if new_content != content:
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            print(f"Injected HTML into {file}")
                except Exception as e:
                    print(f"Failed to process {file}: {e}")

if __name__ == "__main__":
    inject_mobile_navbar()
