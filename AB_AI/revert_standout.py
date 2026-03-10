import codecs

with codecs.open('courses.html', 'r', 'utf-8') as f:
    html = f.read()

standout_start = html.find('<h2 class="card-section-title">Why Our Courses Stand Out</h2>')
if standout_start != -1:
    grid_start = html.find('<div class="grid grid-3 grid-gap-2">', standout_start)
    if grid_start != -1:
        next_section = html.find('<h2 class="card-section-title">Student Categories</h2>', grid_start)
        grid_end = html.rfind('</div>', grid_start, next_section)
        grid_end = html.rfind('</div>', grid_start, grid_end)

        if next_section != -1 and grid_end != -1:
            new_grid = '''<div class="grid grid-3 grid-gap-2">
        <div class="premium-gold-card card-auto p-4 text-center" data-animate>
          <div class="mb-1">
            <img src="https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=100&h=100&fit=crop"
              alt="Curriculum" class="img-circle" style="width: 80px; height: 80px; margin: 0 auto; object-fit: cover;">
          </div>
          <h4 class="color-primary">Comprehensive Curriculum</h4>
          <p class="card-small-text">Covering fundamentals to advanced topics with practical applications and case
            studies.</p>
        </div>
        <div class="premium-gold-card card-auto p-4 text-center" data-animate>
          <div class="mb-1">
            <img src="https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=100&h=100&fit=crop" alt="Faculty"
              class="img-circle" style="width: 80px; height: 80px; margin: 0 auto; object-fit: cover;">
          </div>
          <h4 class="color-primary">Expert Faculty</h4>
          <p class="card-small-text">Learn from practitioners with 20+ years of experience in their respective fields.
          </p>
        </div>
        <div class="premium-gold-card card-auto p-4 text-center" data-animate>
          <div class="mb-1">
            <img src="https://images.unsplash.com/photo-1567427018141-0584cfcbf1b8?w=100&h=100&fit=crop"
              alt="Recognition" class="img-circle"
              style="width: 80px; height: 80px; margin: 0 auto; object-fit: cover;">
          </div>
          <h4 class="color-primary">Industry Recognition</h4>
          <p class="card-small-text">Certificates valued by employers and recognized by international astrological
            bodies.</p>
        </div>
        <div class="premium-gold-card card-auto p-4 text-center" data-animate>
          <div class="mb-1">
            <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=100&h=100&fit=crop" alt="Flexible"
              class="img-circle" style="width: 80px; height: 80px; margin: 0 auto; object-fit: cover;">
          </div>
          <h4 class="color-primary">Flexible Learning</h4>
          <p class="card-small-text">Online and offline classes available to suit your schedule and preferences.</p>
        </div>
        <div class="premium-gold-card card-auto p-4 text-center" data-animate>
          <div class="mb-1">
            <img src="https://images.unsplash.com/photo-1521791136064-7986c2920216?w=100&h=100&fit=crop" alt="Career"
              class="img-circle" style="width: 80px; height: 80px; margin: 0 auto; object-fit: cover;">
          </div>
          <h4 class="color-primary">Career Support</h4>
          <p class="card-small-text">Placement assistance, mentoring, and professional networking opportunities.</p>
        </div>
        <div class="premium-gold-card card-auto p-4 text-center" data-animate>
          <div class="mb-1">
            <img src="https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=100&h=100&fit=crop" alt="Lifetime"
              class="img-circle" style="width: 80px; height: 80px; margin: 0 auto; object-fit: cover;">
          </div>
          <h4 class="color-primary">Lifetime Access</h4>
          <p class="card-small-text">Access course materials and community for continuous learning after graduation.</p>
        </div>
      </div>'''
            
            new_html = html[:grid_start] + new_grid + '\n    ' + html[grid_end:]
            with codecs.open('courses.html', 'w', 'utf-8') as f:
                f.write(new_html)
            print("Successfully reverted 'Why Our Courses Stand Out' cards.")
        else:
            print("Could not find the end of the section.", grid_end, next_section)
    else:
        print("Could not find grid_start")
else:
    print("Could not find section title")
