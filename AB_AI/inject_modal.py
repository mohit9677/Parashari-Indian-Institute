import os

cwd = r"d:\ParashariTeam\AB_AI"

# 1. Append CSS to main.css
css_to_add = """
/* Quick View Modal Styles */
.quick-view-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(4px);
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
}

.quick-view-overlay.show {
  opacity: 1;
  pointer-events: auto;
}

.quick-view-modal {
  background: #1a1005; 
  border: 1px solid rgba(255, 215, 0, 0.4);
  border-radius: 12px;
  width: 90%;
  max-width: 480px; 
  padding: 0;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.8), 0 0 20px rgba(255, 215, 0, 0.2);
  transform: translateY(20px) scale(0.95);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  overflow: hidden;
  position: relative;
  display: flex;
  flex-direction: column;
}

.quick-view-overlay.show .quick-view-modal {
  transform: translateY(0) scale(1);
}

.qv-close {
  position: absolute;
  top: 15px;
  right: 15px;
  cursor: pointer;
  color: #fff;
  font-size: 1.5rem;
  z-index: 10;
  background: rgba(0,0,0,0.5);
  border-radius: 50%;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s, color 0.2s;
}

.qv-close:hover {
  background: #FFD700;
  color: #000;
}

.qv-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-bottom: 2px solid rgba(255, 215, 0, 0.3);
}

.qv-body {
  padding: 24px;
}

.qv-title {
  color: #FFD700;
  font-size: 1.5rem;
  margin-bottom: 12px;
  font-weight: 700;
  line-height: 1.2;
}

.qv-desc {
  color: #eaeaea;
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 0;
}

.qv-landscape-bar {
  background: linear-gradient(90deg, #2a1b0a 0%, #170d02 100%);
  border-top: 1px solid rgba(255, 215, 0, 0.3);
  padding: 16px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom-left-radius: 12px;
  border-bottom-right-radius: 12px;
}

.qv-prices {
  display: flex;
  flex-direction: column;
}

.qv-old-price {
  color: #999;
  font-size: 0.9rem;
  text-decoration: line-through;
  margin-bottom: -2px;
}

.qv-new-price {
  color: #FFD700;
  font-size: 1.7rem;
  font-weight: bold;
}

.qv-enroll-btn {
  background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
  color: #000 !important;
  border: none;
  padding: 12px 28px;
  border-radius: 8px;
  font-weight: bold;
  font-size: 1.15rem;
  cursor: pointer;
  text-decoration: none;
  transition: transform 0.2s, box-shadow 0.2s;
  display: inline-block;
  box-shadow: 0 4px 10px rgba(255, 165, 0, 0.3);
}

.qv-enroll-btn:hover {
  transform: translateY(-2px) scale(1.03);
  box-shadow: 0 6px 15px rgba(255, 215, 0, 0.5);
  color: #000 !important;
}
"""

css_file = os.path.join(cwd, 'assets/css/main.css')
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

if ".quick-view-modal" not in css_content:
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write(css_to_add)
    print("Added CSS to main.css")
else:
    print("CSS already exists in main.css")


# 2. Add Modal HTML and JS to courses.html and index.html
modal_html = """
  <!-- QUICK VIEW MODAL STRUCTURE -->
  <div id="quickViewOverlay" class="quick-view-overlay">
    <div class="quick-view-modal">
      <div class="qv-close" id="qvClose"><i class="fa-solid fa-xmark"></i></div>
      <img src="" id="qvImage" class="qv-image" alt="Course Image">
      <div class="qv-body">
        <h3 id="qvTitle" class="qv-title">Course Title</h3>
        <p id="qvDesc" class="qv-desc">Course Description</p>
      </div>
      <div class="qv-landscape-bar">
        <div class="qv-prices">
          <span id="qvOldPrice" class="qv-old-price">₹3,999</span>
          <span id="qvNewPrice" class="qv-new-price">₹2,999</span>
        </div>
        <a href="#" id="qvEnrollBtn" class="qv-enroll-btn">Enroll Now</a>
      </div>
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', function () {
      const overlay = document.getElementById('quickViewOverlay');
      if (!overlay) return;
      
      const closeBtn = document.getElementById('qvClose');
      const qvImage = document.getElementById('qvImage');
      const qvTitle = document.getElementById('qvTitle');
      const qvDesc = document.getElementById('qvDesc');
      const qvOldPrice = document.getElementById('qvOldPrice');
      const qvNewPrice = document.getElementById('qvNewPrice');
      const qvEnrollBtn = document.getElementById('qvEnrollBtn');

      closeBtn.addEventListener('click', () => {
        overlay.classList.remove('show');
      });

      overlay.addEventListener('click', (e) => {
        if (e.target === overlay) overlay.classList.remove('show');
      });

      document.body.addEventListener('click', function(e) {
        const btn = e.target.closest('.learn-more');
        if (!btn) return;

        // Try standard card first
        let card = btn.closest('.premium-gold-card');
        if (!card) card = btn.closest('.card'); // For index.html
        if (!card) return;

        const category = card.getAttribute('data-category');
        if (category === 'Crash Course') {
          e.preventDefault(); 
          
          let imgEl = card.querySelector('.card-image');
          let titleEl = card.querySelector('.card-title');
          let descEl = card.querySelector('p'); // Fallback to 'p' tag if '.course-desc-text' not found
          let descElSpecific = card.querySelector('.course-desc-text');
          let delEl = card.querySelector('del');
          let strongEl = card.querySelector('strong');

          if (imgEl && titleEl && (descElSpecific || descEl) && delEl && strongEl) {
            qvImage.src = imgEl.src;
            qvTitle.innerText = titleEl.innerText;
            qvDesc.innerText = descElSpecific ? descElSpecific.innerText : descEl.innerText;
            qvOldPrice.innerText = delEl.innerText;
            qvNewPrice.innerText = strongEl.innerText;
            
            qvEnrollBtn.href = btn.getAttribute('href');
            overlay.classList.add('show');
          }
        }
      });
    });
  </script>
"""

html_files = ['courses.html', 'index.html']

for html_file in html_files:
    filepath = os.path.join(cwd, html_file)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "id=\"quickViewOverlay\"" not in content:
            # Inject right before </body> or </html>
            if "</body>" in content:
                new_content = content.replace("</body>", modal_html + "\n</body>")
            elif "</html>" in content:
                new_content = content.replace("</html>", modal_html + "\n</html>")
            else:
                new_content = content + "\n" + modal_html
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added modal HTML to {html_file}")
        else:
            print(f"Modal already exists in {html_file}")
