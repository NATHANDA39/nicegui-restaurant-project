from nicegui import app, ui
from sections import hero, welcome 

# Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

# Load Font Awesome for social icons 

ui.add_head_html('''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css" integrity="sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw==" crossorigin="anonymous" referrerpolicy="no-referrer" />''')

ui.add_head_html('<link rel="stylesheet" href="/assets/reset.css"/>')

hero.render()
# welcome.render()

ui.run()