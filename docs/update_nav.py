import os
import re

nav_template = '''      <aside class="nav">
        <h2>Table of Contents</h2>
        
        <h3>Getting Started</h3>
        <ul>
          <li><a href="01-introduction.html">1. Introduction</a></li>
          <li><a href="02-installation.html">2. Installation</a></li>
          <li><a href="03-data.html">3. Data and Logs</a></li>
        </ul>
        
        <h3>Core Concepts</h3>
        <ul>
          <li><a href="04-pipeline.html">4. The Pipeline</a></li>
          <li><a href="05-models.html">5. Model Architecture</a></li>
        </ul>
        
        <h3>Running DeepSentry</h3>
        <ul>
          <li><a href="06-config.html">6. Configuration</a></li>
          <li><a href="07-live.html">7. Live Monitoring</a></li>
        </ul>
        
        <h3>Reference & Support</h3>
        <ul>
          <li><a href="08-reference.html">8. API Reference</a></li>
          <li><a href="09-troubleshooting.html">9. Troubleshooting</a></li>
        </ul>
        
        <h3>Advanced & Production</h3>
        <ul>
          <li><a href="10-advanced.html">10. Advanced Topics</a></li>
          <li><a href="11-examples.html">11. Examples & Use Cases</a></li>
          <li><a href="12-production.html">12. Production Best Practices</a></li>
        </ul>
        
        <h2>Quick Links</h2>
        <div class="small">
          <div><a href="index.html">Start page</a></div>
          <div><a href="../README.md">README.md</a></div>
          <div><a href="../Dockerfile">Dockerfile</a></div>
          <div><a href="../LICENSE">MIT License</a></div>
        </div>
      </aside>'''

# Map to mark current chapter
chapter_names = {
  '04': '4. The Pipeline',
  '05': '5. Model Architecture',
  '06': '6. Configuration',
  '07': '7. Live Monitoring',
  '08': '8. API Reference',
  '09': '9. Troubleshooting',
  '10': '10. Advanced Topics',
  '11': '11. Examples & Use Cases',
  '12': '12. Production Best Practices',
}

files = ['04-pipeline.html', '05-models.html', '06-config.html', '07-live.html', 
         '08-reference.html', '09-troubleshooting.html', '10-advanced.html', '11-examples.html', '12-production.html']

for fname in files:
  with open(fname, 'r') as f:
    content = f.read()
  
  # Extract chapter number
  chap_num = fname[:2]
  
  # Create nav with strong tag on current chapter
  chap_name = chapter_names.get(chap_num, '')
  nav = nav_template.replace(f'href="{chap_num[0:2]}-', f'href="{chap_num}-')
  
  if chap_name and f'>{chap_name}<' in nav:
    nav = nav.replace(f'>{chap_name}<', f'><strong>{chap_name}</strong><')
  
  # Replace old nav with new nav
  content_new = re.sub(
    r'<aside class="nav">.*?</aside>',
    nav,
    content,
    flags=re.DOTALL,
    count=1
  )
  
  with open(fname, 'w') as f:
    f.write(content_new)
  
  print(f"Updated {fname}")

print("Done!")
