from nicegui import ui, app

def render():
    # Big Container
    with ui.element("div").style(
        "background-image:url(/assets/hero.jpg); background-size: cover; background-position: center;"  # Improved styling
    ).classes("h-screen w-screen flex flex-col bg-cover bg-center justify-center items-center"):  # Added background-size and background-position

        # Navbar
        with ui.element("nav").classes("flex flex-row justify-between items-center p-4 w-full fixed left-0 top-0 py-10 px-20"):  # Added padding and vertical alignment
            # Logo
            ui.label("LOGO").classes("text-white text-2xl font-bold")  # Added styling to the logo

            # Navlinks
            navlinks = [
                {"title": "Home", "path": "/"},
                {"title": "Menu", "path": "/"},
                {"title": "Gallery", "path": "/"},
                {"title": "About", "path": "/"},
                {"title": "Blog", "path": "/"},
                {"title": "Contact", "path": "/"},
            ]

            with ui.row().classes("space-x-3"):  # Added spacing between links
                for item in navlinks:
                    ui.link(item["title"], item["path"]).classes(
                        "no-underline uppercase text-lg hover:underline text-white font-bold"  # Added hover effect and text size
                    )

            # Socials
            with ui.row().classes("space-x-4 text-xl text-white"):  # Added spacing and text size
                ui.html('<i class="fa-brands fa-facebook-f"></i>')
                ui.html('<i class="fa-brands fa-instagram"></i>')
                ui.html('<i class="fa-brands fa-x-twitter"></i>')

        # text 
        with ui.element("div").classes("text-white font-bold text-center"):
            ui.label("Welcome to").classes("text-4xl mb-0 pb-0")
            # ui.html("<h1> NL Eatry </h1>").classes("text-7xl Uppercase")
            with ui.element("div").classes("flex flex-row"):
                ui.html("<h1>NL</h1>").classes("text-7xl uppercase text-orange-600")
                ui.html("<h1>Eatry</h1>").classes("text-7xl uppercase text-white  ml-4")
            ui.button("Look Menu", color="orange-600").classes("px-4 py-2 rounded-2xl")
    

ui.run()