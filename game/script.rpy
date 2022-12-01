# The script of the game goes in this file.
python:
    import math
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define RJ = Character("You")
define G = Character("Gabe")
define C = Character("Chloe")

# The game starts here.

label start:
    $ timer_range = 0
    $ timer_jump = 0
    # $ text3 = "Text 3 - emergency, action required, intentionally prolonging the text to make sure this garbage actually works"

    "You hear birds chirping..."

    "What kind is that? Chickadee? Robin? You aren't sure."

    $ time = 100
    $ timer_range = 100
    $ timer_jump = 'dialogue1'
    show screen countdown

    menu:
        "Chickadee":
            hide screen countdown
            jump dialogue1
        "Robin":
            hide screen countdown
            jump dialogue1
    

label dialogue1:
    
    "You feel a hand on your shoulder."

    "[G]: Dad?"

    "[RJ]: What's up, Gabe?"

    "[G]: You ok? You said we needed to stay focused, and then sorta spaced out."

    "You're focused. Of course you are. You're a Cryfman."

    "[RJ]: Just listenin' for the stream, pal. Let's keep going."

    "The stream comes into view. It's quiet, whispering."

    "Your footsteps are grating and blunt in comparison."

    "Should Gabe gather up the water? Sleepers aren't dumb. They'll be waiting for us here."

    "But then... if he's taking the perimeter, you won't be able to keep an eye on him..."

    $ time = 100
    $ timer_range = 100
    $ timer_jump = 'dialogue2'
    show screen countdown

    menu:
        "Water":
           hide screen countdown
           jump water
        "Perimeter":
            hide screen countdown
            jump perimeter

    label water:

        "[RJ]: Gabe, gather the water, won't you?"

        "[G]: ... *nod*."
    
        "You reach down into the water, throwing the occasional glance behind you."

        "Decisions, decisions."

        "You idiot. You sent your son to take the perimeter?"

        "Chloe would've sent him to take the water. And Dad..."

        "You shake your head." 

        "{i}Just get the damn water.{/i}"

        $ local_text = "You begin filling the bucket with water"

        $ halftime = (len(local_text) / 40) * 10
        $ timer_jump1 =  "dialogue2"
        show screen soCheap

        "[local_text]"

    label perimeter:

        "[RJ]: Gabe, take the perimeter, won't you?"

        "[G]: ... I'll call if I see anything."

        "As you move away from Gabe and the stream, you can't help but think."

        "Why did you do that?"

        "You look back at him, your boy, crouched over the water."

        "And then away. "

        "{i}Keep your eye on the ball.{/i}"

        $ local_text = "You widen your stride and take a breath. Those monsters won't"

        $ halftime = (len(local_text) / 40) * 10
        $ timer_jump1 =  "dialogue2"
        show screen soCheap

        "[local_text]"

label dialogue2:

    "You hear a scream behind you."

    "You whirl."

    "And before you know it, you're running."

    "Suddenly, Gabe's two meters away, and he's fighting a losing battle."

    "The Sleeper is muscular and a few centimeters taller than you."

    "Like all Sleepers, its gray skin is dotted with goosebumps. "

    "Behind it, a horde roars."

    "They planned this...!"

    "And they're approaching. Fast. Are these the Sprinters you've heard about?"

    "RJ GABE!!"
    
    $ time = 100
    $ halftime = time / 3
    $ timer_range = 100
    $ timer_jump = 'death'
    $ timer_jump1 = 'dialogue2UpdatedMenu'
    show screen countdown
    show screen soCheap

    menu:
        "Drag the Sleeper off of him":
            hide screen countdown
            hide screen soCheap
            jump dragSleeper
        "Pull him out":
            hide screen countdown
            hide screen soCheap
            jump pullOut

    label dialogue2UpdatedMenu:
        menu:
            "{i}Don't be a pussy, Richard.{/i} You need to move. You need to move. You need to move."

            "Drag the Sleeper off of him":
                hide screen countdown
                hide screen soCheap
                jump dragSleeper
            "Pull him out":
                hide screen countdown
                hide screen soCheap
                jump pullOut
            "Keep pussying out":
                hide screen countdown
                hide screen soCheap
                jump pussyOut

    label dragSleeper:
        "You reach behind the Sleeper. It smells like death."

        G "DAAAAAADD!"

        RJ "KICK IT! KICK IT HARDER!"

        "You're doing your best to pull the damn thing off. "

        "... must've been a bodybuilder before it turned."

        RJ "Rrrraaahhh!"

        "Somehow, you throw it off. Gabe's already on his feet."

        jump dialogue3

    label pullOut:
        "You reach under Gabe's shoulders and pull."

        "[G]: DAAAAD! IT... WON'T... GET OFF!"

        "You just pull harder."

        "[G]: Aah-!"

        "You hear a popping sound from Gabe."

        "The sleeper must be just as surprised as you are, because it stops grasping at him for a moment.."

        "You're frozen. Nothing moves."

        "[G]: Dad! Come ON!"

        "You're right behind him."

        jump dialogue3

    label pussyOut:
        "You're frozen. You can't move."

        "Time seems to slow. Gabe disappears in front of you. The sleeper's large, muscular hands tear at his flesh like the beak of a crow."

        "It mumbles to itself. It smiles. Why wouldn't it? It finally found food."

        "But still, you just watch. "

        "Even when it finishes Gabe off, you just watch."

        "Even when it steps up towards you, you just watch."

        "And even when it looks you dead in the eyes and reaches towards you, looking almost sympathetic, all you can do is just watch."

        jump death

label dialogue3:

    "You're running. "

    "It's just you two and your footsteps, crunching over the red and brown leaves."

    G "Dad! Huff - huff - maybe when we get back we can lure them to the station and find a - huff - new place to stay!"

    G "You've heard the - huff - rumors about Sleepers in - hck - hordes! Less focused!"

    $ local_text = "So-"

    $ halftime = (len("Gabe: " + local_text) / 40) * 10
    $ timer_jump1 =  "dialogue3_1"
    show screen soCheap

    G "[local_text]"

    label dialogue3_1:

        RJ "Gabe, what the hell?"

        G "Dad..!"

        RJ "You've got to keep your eyes open! We talked about this!"

        "Gabe's arms keep pumping, but he looks down."

        RJ " ... alright?"

        G "..."

        RJ "Alright?!"

        G "..."

        G "... yes, dad."

        "Why are you mad at him? You screwed up. You weren't careful enough. "

        "How is it that you {i}always{/i} make the wrong decisions?"

        "And then it's just the sound of foot-fall again. You don't look over your shoulder all the way back."
        
        "Your lungs are on fire as the gas station comes back into view."

        "The familiar convenience-store logo, long-since run down, fills you with hollow comfort."

        C "Rick!"

        C "*gasp*"

        C "Gabe! Are you alright?"

        "The words seem to stick to your throat."

        $ time = 100
        $ halftime = (2 * time) / 3
        $ timer_range = 100
        $ timer_jump = 'dialogue4'
        $ timer_jump1 = 'dialogue4'
        show screen countdown
        show screen soCheap

        menu:
            "Chloe... No time... A horde...":
                hide screen countdown
                hide screen soCheap
                jump horde
            "We need... to roof...":
                hide screen countdown
                hide screen soCheap
                jump roof

        label horde:
            C "Hah??"

            "You grab her by the shoulders."

            RJ "Chloe... I... the horde... they have Sprinters!"

            $ local_text = "I'll get your dad. One sec- "

            $ halftime = (len("Chloe: " + local_text) / 40) * 10
            $ timer_jump1 =  "horde_1"
            show screen soCheap

            C "[local_text]"

            label horde1:

                "She doesn't even need to turn around."

                jump dialogue4

        label roof:
            "She nods."

            "God. You don't deserve her. Thank God for that woman."

            "Chloe throws Gabe's arm over her shoulder and begins to retreat to the decrepit gas station you call home."

            "But she bumps into someone."

            jump dialogue4

label dialogue4:

    "Bro chill i haven't gotten here yet. boolean boolean"





    








label death:

    "You die"

    return 

    # scene bg room

    # "Text 1 - intro to theme"

    # "Text 2 - events"

    # $ halftime = (len(text3) / 30) * 10
    # $ timer_jump1 =  "testLabel"
    # show screen soCheap

    # "[text3]"

    # $ time = 100
    # $ halftime = 50
    # $ timer_range = 100
    # $ timer_jump = 'defaultRadio'
    # $ timer_jump1 = 'updatedFirstMenu'
    # show screen countdown
    # show screen soCheap

    # menu:
    #     "Radio back to the radio station":
    #         hide screen countdown
    #         jump radio
    #     "Run back to alarm the family faster.":
    #         hide screen countdown
    #         jump run

    # label testLabel:
    #     hide screen soCheap
    #     "Wau"

    # label updatedFirstMenu:
    #     menu:
    #         "Radio back to the radio station":
    #             hide screen countdown
    #             hide screen soCheap
    #             jump radio
    #         "Run back to alarm the family faster.":
    #             hide screen countdown
    #             hide screen soCheap
    #             jump run
    #         "Let AJ decide":
    #             hide screen countdown
    #             hide screen soCheap
    #             jump defaultRadio

    # label defaultRadio:
    #     "Text 1 - AJ takes the radio to inform the family"
        
    #     jump radio

    # label radio:
    #     "Complete path"
    
    # label run:
    #     "Text 1, explain the scenario"

    #     "Text 2, present the decisions"

    #     menu:
    #         "Listen to Richard":
    #             jump fight
    #         "Listen to Beth":
    #             jump flee
    #         "Go to the roof":
    #             jump roof

    # label fight:
    #     "Text 1 - "

    # label flee:
    #     ""
    
    # label roof:
    #     ""

    




    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
        # This is to fade the bar in and out, and is only required once in your script

    screen countdown:
        timer 0.1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump(timer_jump)])
        bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.
    
    screen soCheap:
        timer 0.1 repeat True action If(halftime > 0.3, true=SetVariable('halftime', halftime - 1), false=[Hide('soCheap'), Jump(timer_jump1)])

    # screen countdown:
    #     timer 0.1 repeat True action If(math.floor(time/300), 0==[print(0), Hide('countdown'), Jump(timer_jump)], 
    #                                                      1==[print(1), Jump(timer_jump)],
    #                                                      2==[print(2), SetVariable('time', time - 1)])
    #     bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

    return
