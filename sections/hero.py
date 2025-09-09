from nicegui import ui

def render():
    # Navbar
    with ui.element("nav").classes("flex flex-row justify-between bg-white items-center p-4 w-full fixed left-0 top-0 py-10 px-20 z-50 shadow-md"):  # Added padding and vertical alignment
        # Logo
        ui.label("LOGO").classes("text-black text-2xl font-bold")  # Added styling to the logo

        # Navlinks
        navlinks = [
            {"title": "Home", "path": "/"},
            {"title": "Menu", "path": "/"},
            {"title": "Gallery", "path": "/"},
            {"title": "About", "path": "/"},
            {"title": "Blog", "path": "/"},
            {"title": "Contact", "path": "/"},
        ]

        # Navigation links with spacing
        with ui.row().classes("space-x-3"):  # Added spacing between links
            for item in navlinks:
                ui.link(item["title"], item["path"]).classes(
                    "no-underline uppercase text-lg hover:underline text-black font-bold"  # Added hover effect and text size
                )

        # Socials (icons)
        with ui.row().classes("space-x-4 text-xl text-center text-black"):  # Added spacing and text size
            ui.html('<i class="fa-brands fa-facebook-f"></i>')
            ui.html('<i class="fa-brands fa-instagram"></i>')
            ui.html('<i class="fa-brands fa-x-twitter"></i>')

    # Hero Section (Big Container)
    with ui.element("div").classes("w-screen h-screen relative pt-[100px]"):  # Added padding-top to prevent overlap with navbar
        with ui.element("div").style(
            "background-image:url('/assets/hero.jpg'); background-size: cover; background-position: center; background-color: #000000;"  # Added fallback background color
        ).classes("flex flex-col bg-cover bg-center w-full h-full justify-center items-center"):
            # Ensure the hero text and button are centered
            with ui.element("div").classes("text-white font-bold text-center flex flex-col items-center justify-center bg-black/50  h-full w-full"):
                ui.label("Welcome to").classes("text-4xl mb-0 pb-0")
                with ui.element("div").classes("flex flex-row"):
                    ui.html("<h1>NL</h1>").classes("text-7xl uppercase text-orange-600")
                    ui.html("<h1>Eatery</h1>").classes("text-7xl uppercase text-white ml-4")
                ui.button("Look Menu", color="orange-600").classes("rounded-full w-[120px]")

# Initialize the app
ui.run()
