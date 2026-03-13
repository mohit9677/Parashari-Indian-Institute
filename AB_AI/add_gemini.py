import glob

# 1. Update Mega Dropdown Box in all HTML files
html_files = glob.glob('*.html')
for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        
        # Add to the end of the Courses Dropdown Menu
        target_li = '<li class="dropdown-item"><a href="mentorship.html">1-on-1 Mentorship</a></li>'
        new_li = '            <li class="dropdown-item"><a href="gemini-jyotish.html">Gemini Jyotish</a></li>'
        
        # Some files might have slightly different spacing, but usually the target_li works.
        if target_li in new_content and new_li not in new_content:
            new_content = new_content.replace(
                target_li, 
                target_li + '\n' + new_li
            )
            
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated Navigation in {filepath}")
            
    except Exception as e:
        print(f"ERROR processing {filepath}: {e}")

# 2. Add to fee-structure.html Crash Course Section
fee_file = 'fee-structure.html'
try:
    with open(fee_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Desktop List Injection
    target_desktop = """                  <div class="course-box">
                    <div class="course-header">
                      <span class="course-name">15. Feng Shui</span>
                      <i class="fas fa-chevron-down course-arrow"></i>
                    </div>
                    <div class="course-details">
                      <span class="course-price"><del style="color:#999;font-size:0.85em;margin-right:5px;">₹3,999</del>
                        <strong style="color:#d32f2f;">₹2,999</strong> <span class="discount-text">(with 25% discount)</span></span>
                      <a href="feng-shui.html" class="btn btn-primary btn-sm enroll-btn" style="padding: 4px 10px; font-size: 0.8em;">Enroll Now</a>
                    </div>
                  </div>"""
                  
    gemini_desktop = """
                  <div class="course-box">
                    <div class="course-header">
                      <span class="course-name">16. Gemini Jyotish</span>
                      <i class="fas fa-chevron-down course-arrow"></i>
                    </div>
                    <div class="course-details">
                      <span class="course-price"><del style="color:#999;font-size:0.85em;margin-right:5px;">₹3,999</del>
                        <strong style="color:#d32f2f;">₹2,999</strong> <span class="discount-text">(with 25% discount)</span></span>
                      <a href="gemini-jyotish.html" class="btn btn-primary btn-sm enroll-btn" style="padding: 4px 10px; font-size: 0.8em;">Enroll Now</a>
                    </div>
                  </div>"""
                  
    if target_desktop in content and gemini_desktop not in content:
        content = content.replace(target_desktop, target_desktop + gemini_desktop)

    # Mobile List Injection
    target_mobile = '<li>Tarot Reading</li>\n          </ul>'
    gemini_mobile = '<li>Tarot Reading</li>\n            <li>Gemini Jyotish</li>\n          </ul>'
    
    if target_mobile in content:
        content = content.replace(target_mobile, gemini_mobile)
        
    with open(fee_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Crash Course Section in fee-structure.html")

except Exception as e:
    print(f"ERROR updating fee-structure.html: {e}")
