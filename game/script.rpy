init:
    define dh = Character('DH')
    define teague = Character('Teague')
    define hanna = Character('Hanna')
    define ariel = Character('Ariel')
    define nathan = Character('Nathan')
    define garrick = Character('Garrick')
    define nico = Character('Nico')
    define jacq = Character('Jacq')
    define ron = Character('Ron')
    define player = Character('[charName]')

    image dh normal = 'dh.png'
    image teague normal = 'teague.png'
    image hanna normal = 'hanna.png'
    image ariel normal = 'ariel.png'
    image nathan normal = 'nathan.png'
    image garrick normal = 'garrick.png'
    image nico normal = 'nico.png'
    image jacq normal = 'jacq.png'
    image ron normal = 'ron.png'
    image player normal = 'player.png'

    image bg death = 'you_died.png'
    image bg black = 'black_screen.png'
    image bg knowledge = 'knowledge_is_power.jpg'

    $ left_offset = Position(xpos=0.1, xanchor=0, ypos=0.5, yanchor=0.5)
    $ right_offset = Position(xpos=0.9, xanchor=0.999, ypos=0.5, yanchor=0.5)

init offset = 100

label start:
    scene bg knowledge

    python:
        charName = renpy.input('What is your name?').strip()
        if not charName:
            charName = 'Kat'

    show player normal at left_offset with dissolve
    player 'Da fuq?'

    show dh normal at right_offset with dissolve
    dh 'we lost'

    scene bg death with fade
    $ renpy.pause(3)

    show bg black with fade

    return
