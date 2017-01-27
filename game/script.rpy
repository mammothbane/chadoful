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

    image jacq_ron normal = 'jacq_ron.png'
    image hanna_garrick normal = 'hanna_garrick.png'

    image bg death = 'you_died.png'
    image bg black = 'black_screen.png'
    image bg knowledge = 'knowledge_is_power.jpg'

    $ left_offset = Position(xpos=0.1, xanchor=0, ypos=0.5, yanchor=0.5)
    $ right_offset = Position(xpos=0.9, xanchor=0.999, ypos=0.5, yanchor=0.5)
    $ center_vert = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

init offset = 100
init python:
    jacqRon = True

label start:
    scene bg knowledge # todo: update

    $ charName = 'Me'
    show player normal at left_offset
    player 'Wow, I can\'t believe they let an average girl like me transfer into Chadbourne house.'
    player "It's a co-op, so it's uber exclusive!" # todo: umlaut
    player "I just hope everyone in the house will like me. It's the middle of the year already..."
    player "But I'm not going to let that stop me from pursuing my dreams of being the best housing coordinator in Wood Neighborhood!"

    show nico normal at right_offset
    nico 'Welcome to Chadbourne! You must be our new housing coordinator.'
    nico "What's your name again?"

    python:
        charName = renpy.input('What is your name?').strip()
        if not charName:
            charName = 'Kat'

    nico "Wow, '[charName]', what a nice name!"
    nico "I have a feeling that we're going to get along well."
    nico "Let me add you to--"
    $ renpy.pause(2)

    # join snrp groupme

    nico "That's us! SNRP, or {b}S{/b}ick-{b}N{/b}asty {b}R{/b}edwood {b}P{/b}onchos!"
    nico "Feel free to like someone's message or post a meme!"
    nico "...that's all anyone ever does."

    # nico picks up bags

    nico "I'll just drop your bags in your room?"

    player "\[Wow, he's {i}so nice{/i}, and he's carrying my bags for me~~!!\]"
    player "\[What could this mean?!\]"

    # play alarm sound

    menu:
        'Great! Can you show me around?':
            $ jacqRon = False
            jump nicoRoom1
        'Huh?! What\'s that sound?':
            hide nico with dissolve
            $ renpy.pause(0.7) # door open/close

            show jacq_ron normal at right_offset with dissolve

            ron "Oh, hi, you're [charName], right?"
            jacq "We've been so excited to meet you!"
            $ renpy.pause(1.2)
            jacq "Want to join us for yoga?"
            ron "Jacq~~, I thought this was {i}our{/i} thing!"
            player "\[Huh, are they..? No way, that seems pretty platonic to me.\]"
            jacq "Actually, you look pretty tired. You must want to get some sleep."
            jacq "But you should come play board games with us tonight! We'll send a GroupMe message when we're starting."
            ron "Well, bye!"

            hide jacq_ron
            jump boardGamesNap


label nicoRoom1:
    # todo: bags carried should scale with number of trophies carried; nico makes a comment about heavy bags

    scene bg knowledge # todo: update
    show player normal at left_offset with dissolve
    show nico normal at right_offset with dissolve

    nico "Welcome to your new room!"
    player "\[Isn't this... the attic?\]"
    # muffled crash
    nico "Don't be too alarmed; they're just doing construction in one of the downstairs rooms."
    nico "You see, some... events... occurred before you came."
    nico "But no need to worry about that! Your first priority should be meeting everyone in this house."
    nico "We're having a board game night this evening. You should come!"
    nico "But you must be exhausted from carrying all these bags around. And here I am. Talking."

    menu:
        "Yep.":
            nico "...well. You must want to get some shuteye!"
            player "Yep."
            nico "...I can take a hint. See you tonight, I guess... I'll post in the GroupMe when we're starting."
            hide nico with dissolve
            player "Yikes. Maybe I shouldn't have been so blunt. Something to remember, I guess."
            player "Now for a well-deserved nap."
            jump boardGamesNap

        "No, go on...":
            # increase nico longwinded
            nico "I can't believe they let someone transfer into Chadbourne House in the middle of the year."
            nico "I didn't even know there was an attic!"
            player "\[I wish I could just take a nap, but that would be rude...\]"
            nico "Wow, that view is amazing!"
            nico "And it's so huge up here. Do you want to play a board game?"
            player "..."
            nico "Well, great, I'll just start setting up for Lords of Waterdeep."
            nico "So, in order to play this game..."
            # set player to sleeping
            player "Zzzz..."
            nico "[charName], you too!?"
            hide nico with dissolve
            jump boardGamesNap

label boardGamesNap:
    scene bg black with fade
    $ renpy.pause(3)
    # groupme sound

    scene bg knowledge with fade # in room
    # show groupme with explanatory messages
    show player normal at left_offset with dissolve

    "GROUPME STUFF HAPPENS HERE"

    scene bg knowledge with fade # common room
    # more scene intro?

    "So I guess these are the people I'll be living with this year."
    show nico normal at center_vert with dissolve
    "There's Nico. Is he really always this talkative?"
    hide nico with dissolve

    show ron normal at center_vert with dissolve
    "Ron flirts with {i}everyone{/i}."
    hide ron with dissolve

    show ariel normal at center_vert with dissolve
    "Here's Ariel. I wonder what happened... She looks so sad."
    hide ariel with dissolve

    show hanna normal at center_vert with dissolve
    "Hanna, I think. Everyone calls her 'Fleemlord', but I don't think that's her actual name."
    hide hanna with dissolve

    show garrick normal at center_vert with dissolve
    "Garrick and Hanna are definitely together. Does he ever stop eating..?"
    hide garrick with dissolve

    # gurren lagann theme blares loudly

    show jacq normal at center_vert with dissolve
    "Jacq's been awfully quiet. I think some of these anime references are flying over her head."
    hide jacq with dissolve

    show dh normal at center_vert with dissolve
    "DH..."

    hide dh with dissolve

    "But I thought there was one more person in this house..."

    $ renpy.pause(1)

    # knock at the door
    # crashbar sounds

    show nathan normal at center_vert with dissolve
    "Nathan's swipe doesn't work. He technically doesn't live here, but I can turn a blind eye."
