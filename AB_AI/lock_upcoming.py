import re
with open('upcoming-courses.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_str = '<div class="grid-responsive grid-gap-2">'
# Find the start of grid
grid_start = html.find(start_str)
# Find the end of grid (the closing div)
grid_end = html.find('</div>\n    </div>\n  </section>', grid_start)
if grid_end == -1: grid_end = html.find('</section>', grid_start)

locked_html = """
        <div class="card premium-gold-card text-center" style="grid-column: 1 / -1; padding: 4rem 2rem;">
          <div style="font-size: 4rem; color: #D4AF37; margin-bottom: 1rem;">🔒</div>
          <h3 class="color-primary" style="font-size: 2rem; margin-bottom: 1rem;">All Courses Are Now Available</h3>
          <p class="card-small-text" style="font-size: 1.1rem; max-width: 600px; margin: 0 auto 2rem;">
            We currently do not have any locked or upcoming courses. All 21 of our specialized Vedic Science and Astrology certification programs are fully available for enrollment right now!
          </p>
          <a href="courses.html" class="btn btn-primary btn-lg">View Available Courses</a>
        </div>
"""

new_html = html[:grid_start + len(start_str)] + '\n' + locked_html + '      ' + html[grid_end:]

# also change "Upcoming Programs" text
new_html = new_html.replace('Prepare for our specialized certification programs starting soon', 'Explore all our currently active programs')
new_html = new_html.replace('<h2 class="card-section-title">Upcoming Programs</h2>', '<h2 class="card-section-title">Programs Access</h2>')
new_html = new_html.replace('<h2>Upcoming Programs</h2>', '<h2>Programs Access</h2>')

with open('upcoming-courses.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print("upcoming-courses.html updated successfully.")
