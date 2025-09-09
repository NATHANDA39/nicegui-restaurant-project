from nicegui import app, ui
from sections import blog, hero, welcome, menu, discover

# Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

# Load Font Awesome for social icons 

ui.add_head_html('''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css" integrity="sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw==" crossorigin="anonymous" referrerpolicy="no-referrer" />''')

# Load google font
ui.add_head_html('''
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <style>
        .font-montserrat { font-family: "Montserrat", sans-serif; }
    </style>
''')


ui.add_head_html('<link rel="stylesheet" href="/assets/reset.css"/>')

hero.render()
welcome.render()
discover.render()
blog.render()
menu.render()



ui.run()