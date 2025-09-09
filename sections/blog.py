from nicegui import ui

# Only round the image; keep the card square
ui.add_head_html('''
<style>
.image-rounded { border-radius: 12px; overflow: hidden; }

/* Hover zoom-out effect */
.card-zoom-out .image-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transform: scale(1.08);           /* start slightly zoomed in */
    transition: transform 400ms ease;  /* smooth animation */
    will-change: transform;
    display: block;
}
.card-zoom-out:hover .image-wrapper img {
    transform: scale(1.00);           /* zoom out on hover */
}
</style>
''')

def render():
    with ui.element("section").classes("w-full py-16 bg-white"):
        # headings
        # with ui.element("div").classes("text-center mb-12"):
            # ui.label("Latest News").classes("font-lobster italic text-orange-500 text-2xl")
            # ui.label("THE BLOG").classes("text-4xl font-bold text-black mt-2")

        # blog cards container
        with ui.row().classes("justify-center gap-8 flex-wrap px-6"):
            blogs = [
                {
                    "image": ('/assets/M3.1.jpg'),
                    "title": "Romantic Restaurant",
                    "desc": "Phasellus lorem enim, luctus ut velit eget, convallis egestas eros.",
                },
                {
                    "image": ('/assets/M3.2.jpg'),
                    "title": "Delicious Food",
                    "desc": "Duis elementum, risus sit amet lobortis nunc justo condimentum ligula, vitae feugiat.",
                },
                {
                    "image": ('/assets/M3.3.jpg'),
                    "title": "Red Wines You Love",
                    "desc": "Sed ornare ligula eget tortor tempor, quis porta tellus dictum.",
                },
            ]

            for blog in blogs:
                with ui.element("div").classes(
                    "w-[320px] bg-white"
                ):
                    # image (rounded only here)
                    with ui.element("div").classes("image-wrapper image-rounded relative w-full").style("height: 200px;"):
                        ui.image(blog["image"]).classes(
    "w-full h-full object-cover transition-transform duration-500 ease-out hover:scale-110"
)

                    # content
                    with ui.element("div").classes("p-4 flex flex-col flex-1"):
                        ui.label(blog["title"]).classes("text-lg font-bold text-gray-900 mb-2 uppercase")
                        ui.label(blog["desc"]).classes("text-sm text-gray-600 mb-4 leading-relaxed")
                        ui.link("learn more →", "#").classes(
                            "mt-auto text-xs tracking-widest uppercase text-gray-700 hover:text-orange-500 no-underline"
                        )


ui.run()