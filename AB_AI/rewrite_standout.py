import re
import codecs

with codecs.open('courses.html', 'r', 'utf-8') as f:
    html = f.read()

standout_start = html.find('<h2 class="card-section-title">Why Our Courses Stand Out</h2>')
if standout_start != -1:
    grid_start = html.find('<div class="grid grid-3 grid-gap-2">', standout_start)
    if grid_start != -1:
        # Search for the next section to know where the grid ends
        next_section = html.find('<h2 class="card-section-title">Student Categories</h2>', grid_start)
        # Find the closing tag of the <div class="container"> before the next section
        grid_end = html.rfind('</div>', grid_start, next_section)
        # Go back one more to close the grid
        grid_end = html.rfind('</div>', grid_start, grid_end)

        if next_section != -1 and grid_end != -1:
            new_grid = '''<div class="grid grid-3 grid-gap-2">
        <div class="highlights-card" data-animate style="height: 350px;">
          <img src="https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=800&h=600&fit=crop" style="object-fit:cover; width:100%; height:100%; border-radius: 12px;" alt="Curriculum">
          <div class="highlights-overlay">
            <h4>Comprehensive Curriculum</h4>
            <p>Covering fundamentals to advanced topics with practical applications and case studies.</p>
          </div>
        </div>

        <div class="highlights-card" data-animate style="height: 350px;">
          <img src="https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=800&h=600&fit=crop" style="object-fit:cover; width:100%; height:100%; border-radius: 12px;" alt="Faculty">
          <div class="highlights-overlay">
            <h4>Expert Faculty</h4>
            <p>Learn from practitioners with 20+ years of experience in their respective fields.</p>
          </div>
        </div>

        <div class="highlights-card" data-animate style="height: 350px;">
          <img src="https://images.unsplash.com/photo-1567427018141-0584cfcbf1b8?w=800&h=600&fit=crop" style="object-fit:cover; width:100%; height:100%; border-radius: 12px;" alt="Recognition">
          <div class="highlights-overlay">
            <h4>Industry Recognition</h4>
            <p>Certificates valued by employers and recognized by international astrological bodies.</p>
          </div>
        </div>

        <div class="highlights-card" data-animate style="height: 350px;">
          <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&h=600&fit=crop" style="object-fit:cover; width:100%; height:100%; border-radius: 12px;" alt="Flexible">
          <div class="highlights-overlay">
            <h4>Flexible Learning</h4>
            <p>Online and offline classes available to suit your schedule and preferences.</p>
          </div>
        </div>

        <div class="highlights-card" data-animate style="height: 350px;">
          <img src="https://images.unsplash.com/photo-1521791136064-7986c2920216?w=800&h=600&fit=crop" style="object-fit:cover; width:100%; height:100%; border-radius: 12px;" alt="Career">
          <div class="highlights-overlay">
            <h4>Career Support</h4>
            <p>Placement assistance, mentoring, and professional networking opportunities.</p>
          </div>
        </div>

        <div class="highlights-card" data-animate style="height: 350px;">
          <img src="https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800&h=600&fit=crop" style="object-fit:cover; width:100%; height:100%; border-radius: 12px;" alt="Lifetime">
          <div class="highlights-overlay">
            <h4>Lifetime Access</h4>
            <p>Access course materials and community for continuous learning after graduation.</p>
          </div>
        </div>
      </div>'''
            
            new_html = html[:grid_start] + new_grid + '\n    ' + html[grid_end:]
            with codecs.open('courses.html', 'w', 'utf-8') as f:
                f.write(new_html)
            print("Successfully redesigned 'Why Our Courses Stand Out' cards.")
        else:
            print("Could not find the end of the section.", grid_end, next_section)
    else:
        print("Could not find grid_start")
else:
    print("Could not find section title")
