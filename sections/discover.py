from nicegui import ui

def render():
    with ui.element('div') \
        .style('background-image: url("/assets/DM2.jpg"); background-position: center 0%;') \
        .classes('relative h-[400px] w-screen bg-cover bg-center bg-no-repeat md:bg-fixed overflow-hidden flex flex-col items-center justify-center'):
        ui.element('div').classes('absolute inset-0 bg-black/65')  # overlay for opacity 
        ui.label('Discover').classes('text-white text-center text-4xl font-bold drop-shadow-lg font-montserrat')
        ui.html('<h1> NL Eatery </h1>').classes('text-white text-center text-6xl font-bold drop-shadow-lg font-montserrat uppercase')