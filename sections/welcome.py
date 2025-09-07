from nicegui import ui

def render():
    with ui.element().classes('flex justify-between w-screen h-screen p-0 mt-0').style('background-color: #efefef'):
        
        with ui.element("div").classes('flex flex-col justify-center items-center w-1/2 h-full p-10'):
           ui.label('Italian Restaurant').classes('text-2xl font-bold italic font-montserrat')
           ui.label('WELCOME').classes('text-6xl font-semibold mt-2 font-montserrat')
           ui.html('Donec quis lorem nulla. Nunc eu hate me. Morbi nec lobortis est. Sed <br>fringilla, nunc sed imperdiet lacinia, nisl ante egestas mi, ac facilesis <br>ligula sem id neque.') \
                .classes('mt-4 text-center font-montserrat leading-relaxed')
           ui.link("OUR STORY").classes("no-underline mt-6 text-gray-800 hover:text-red-600 transition-colors duration-300 font-montserrat")
        
        with ui.element("div").classes("flex justify-center items-center w-1/2 h-full"):
            ui.image('assets/welcome.jpg').classes("rounded-lg w-[400px] h-[400px] object-cover p-4 ml-10 transition-transform duration-300 hover:scale-110")


ui.run()
