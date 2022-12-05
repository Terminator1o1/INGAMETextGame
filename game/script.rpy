# The script of the game goes in this file.
init:
    $ annie_alive = True
    define flash = Fade(0.1, 0.0, 0.2, color="#fff")
    define scene_trans = Fade(0.2, 0.0, 0.2, color="#000000")
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define RJ_i = Character("You (left)")
define RJ = Character("You")
define G = Character("Gabe")
define G_i = Character("Gabe (right)")
define C = Character("Chloe")
define R = Character("Richard")
define R_i = Character("Richard (right)")
define A = Character("Annie")
define M = Character("Mo")
define QM = Character("???")
define Sleeper = Character("Sleeper")

# The game starts here.

label start:
    $ timer_range = 0
    $ timer_jump = 0
    # $ text3 = "Text 3 - emergency, action required, intentionally prolonging the text to make sure this garbage actually works"

    show bg forest_stream
    stop music
    
    #play audio "forest.mp3" volume 0.1
   # play audio "birds.mp3" volume 0.8

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

    
    
    "You feel a hand on your shoulder. The bird on your mind flies away."

    show rick_full at left
    show gabe_full at right

    G_i "Dad?"

    RJ_i "What's up, Gabe?"

    G "You ok? You said we needed to stay focused, and then sorta spaced out."

    "You're focused. Of course you are. You're a Cryfman."

    RJ "Just listenin' for the stream, pal. Let's keep going."

    hide rick_full at left
    hide gabe_full at right

    "The stream comes into view. It's quiet, whispering."

    "Your footsteps are grating and blunt in comparison."

    "Should you gather up the water, or take the perimeter?"
    "Sleepers aren't dumb. They'll be waiting for us here."
    "But... if you're taking the perimeter, you won't be able to keep an eye on Gabe."

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

        show rick_full at left
        show gabe_full at right

        RJ "Gabe, go to the perimeter, won't you?"

        G "... *nod*"

        hide rick_full at left
        hide gabe_full at right
    
        "You reach down into the water, throwing the occasional glance behind you."

        "Decisions, decisions."

        "You idiot. Chloe would've sent him to take the water. And Dad..."

        "You shake your head." 

        "{i}Just get the damn water.{/i}"

        $ local_text = "You begin filling the bucket with water"

        $ halftime = (len(local_text) / 40) * 10
        $ timer_jump1 =  "dialogue2"
        show screen soCheap

        "[local_text]"

        hide screen soCheap
        jump dialogue2

    label perimeter:

        show rick_full at left
        show gabe_full at right

        RJ "I'll take the perimeter. Get the water, won't you?"

        G "... I'll call if I see anything."

        hide rick_full at left
        hide gabe_full at right

        "As you move away from Gabe and the stream, you can't help but think."

        "{i}Why did you do that?{/i}"

        "You look back at him, your boy, crouched over the water."

        "And then away. "

        "{i}Keep your eye on the ball.{/i}"

        $ local_text = "You widen your stride and take a breath. Those monsters won't"

        $ halftime = (len(local_text) / 40) * 10
        $ timer_jump1 =  "dialogue2"
        show screen soCheap

        "[local_text]"

        hide screen soCheap
        jump dialogue2

label dialogue2:
    stop audio
    
    play sound "scream.mp3"

    "You hear a scream behind you. You whirl."

    "And before you know it, you're running."

    "Gabe's now two meters away, and he's fighting a losing battle."

    "The Sleeper is muscular and a few centimeters taller than you."

    "Like all Sleepers, its gray skin is dotted with goosebumps. "

    play sound "zombies.mp3"

    "Behind it, a horde roars."

    "They planned this...!"

    "And they're approaching. Fast. Are these the Sprinters you've heard about?"

    show rick_full

    RJ "GABE!!"

    hide rick_full
    
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
            "{i}Don't be a pussy, Junior.{/i} You need to move. You need to move. You need to move."

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

        show rick_full at left
        show gabe_full at right        

        G "DAAAAAADD!"

        RJ "KICK IT! KICK IT HARDER!"

        hide rick_full at left
        hide gabe_full at right

        "You're doing your best to pull the damn thing off. "

        "... must've been a bodybuilder before it turned."

        show rick_full

        RJ "Rrrraaahhh!"

        hide rick_full

        "Somehow, you throw it off. Gabe's already on his feet."

        jump dialogue3

    label pullOut:
        "You reach under Gabe's shoulders and pull."

        show gabe_full

        G "DAAAAD! IT... WON'T... GET OFF!"

        hide gabe_full

        "You just pull harder."

        show gabe_full

        G "Aah-!"

        hide gabe_full

        "You hear a popping sound from Gabe."

        "The sleeper must be just as surprised as you are, because it stops grasping at him for a moment.."

        "You're frozen. Nothing moves."

        show gabe_full

        G "Dad! Come ON!"

        hide gabe_full

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

    play music "crunch.mp3"
    show bg forest_running

    "You're running. "

    "It's just you two and your footsteps, crunching over the red and brown leaves."

    show gabe_full

    G "Dad! Huff - huff - maybe when we get back we can trap them at the station and find a - huff - new place to stay!"

    G "You've heard the - huff - rumors about Sleepers in - hck - hordes! Less focused!"

    $ local_text = "So then we ca"

    $ halftime = (len("Gabe: " + local_text) / 40) * 10
    $ timer_jump1 =  "dialogue3_1"
    show screen soCheap

    G "[local_text]"

    hide screen soCheap
    jump dialogue3_1

    label dialogue3_1:

        stop sound

        hide gabe_full

        show gabe_full at right
        show rick_full at left

        RJ "Gabe, what the hell?"

        G "Dad..!"

        RJ "You've got to keep your eyes open! We talked about this!"

        hide gabe_full at right
        hide rick_full at left

        "Gabe's arms keep pumping, but he looks down."

        show gabe_full at right
        show rick_full at left

        RJ " ... alright?"

        G "..."

        RJ "Alright?!"

        G "..."

        G "... yes, dad."

        hide gabe_full at right
        hide rick_full at left

        "And then it's just the sound of foot-fall again."

        "Why are you mad at him? {i}You{/i} screwed up."

        "You don't look over your shoulder all the way back. The guilt is already enough to think about."
        
        "Your lungs are on fire as the gas station comes back into view."

        "The familiar convenience-store logo, long-since run down, fills you with hollow comfort."

        stop sound
        stop music
        show bg gas_station_outside with scene_trans

        show chloe_full

        C "Rick!"

        C "*gasp*"

        C "Gabe! Are you alright?"

        hide chloe_full

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
            "We need... get to roof...":
                hide screen countdown
                hide screen soCheap
                jump roof

        label horde:

            show chloe_full

            C "Hah??"

            hide chloe_full

            "You grab her by the shoulders."

            show rick_full at left
            show chloe_full at right

            RJ "Chloe... I... the horde... they have Sprinters!"

            $ local_text = "I'll get your dad. One sec- "

            $ halftime = (len("Chloe: " + local_text) / 40) * 10
            $ timer_jump1 =  "horde1"
            show screen soCheap

            C "[local_text]"

            hide screen soCheap
            jump horde1

            label horde1:

                hide rick_full at left
                hide chloe_full at right

                "She doesn't even need to turn around."

                jump dialogue4

        label roof:
            "She nods."

            "God. You don't deserve her. Thank God for that woman."

            "Chloe throws Gabe's arm over her shoulder and begins to retreat to the decrepit gas station you call home."

            "But she bumps into someone."

            jump dialogue4

label dialogue4:

    show rick_full at left
    show richard_full at right

    R_i "Junior. You idiot."

    RJ "..."

    R "I could've told your goddamn daughter to go."

    R "Tch. I mean, seriously? Taking that long and attracting a horde? How amateur can you be?"

    RJ "..."

    hide rick_full at left
    hide richard_full at right

    "He turns his head and looks back at everyone else."

    #(We see the scene outside the gas station. Gabe is leaned against a wall. Annie is with Mo near the door.)

    # contorted face sprite for dad

    show rick_full at left
    show richard_full at right

    R "We don't have time for this. Let your woman and I fortify the front." 

    R "Maybe won't screw more up if your {i}kids{/i} keep an eye on you."

    RJ "..."

    R "Alright?"

    hide rick_full at left
    hide richard_full at right

    $ time = 10
    $ timer_range = 10
    $ timer_jump = 'no_response'
    show screen countdown

    menu:
        "Alright":
            hide screen countdown
            jump alright
        "...":
            hide screen countdown
            jump no_response 

    label alright:

        show richard_full

        R "Good."

        hide richard_full

        jump dialogue5

    label no_response:

        show rick_full at left
        show richard_full at right

        R "{i}Alright?!{/i}"

        RJ "..."
        
        RJ "... yes, dad."

        R "...Good."

        hide rick_full at left
        hide richard_full at right  

        jump dialogue5

label dialogue5:

    show richard_full

    R "Maybe you'll be safer with them watching you."

    hide richard_full

    $ time = 100
    $ timer_range = 100
    $ timer_jump = 'walking_inside'
    show screen countdown

    menu:
        "Gabe's idea":

            hide screen countdown

            "You look towards Chloe, who meets your gaze. Then, back at Dad."

            show rick_full at left
            show richard_full at right

            RJ "You know what? No. Dad, I saw the Sprinter horde. You've heard the rumors, right?"

            RJ "We need to go. Let me help you prepare a trap for them. Chloe's better with the kids anyway."

            R "Don't be a {i}pussy{/i}, Junior! You're my Richard! You should know better! We need to defend our home!"

            RJ "Get it straight, dad. You're {i}Richard{/i}, I'm {i}Rick{/i}, and {i}I{/i} saw the horde."

            hide rick_full at left
            hide richard_full at right

            "He waits a moment, and then nods."

            show richard_full

            R "Alright, then. Where was this decisiveness before? Let's get a move on!"

            hide richard_full

            jump inside_with_richard

        "Prepare the kids":

            hide screen countdown

            jump walking_inside

label walking_inside:

    "You nod your head and head towards Annie and Mo.."

    "Annie jumps towards you as you approach. She smells of dirt and ketchup."

    show rick_full

    RJ "Hey, pumpkin."

    A "Daddy..."

    RJ "You doin' alright?"

    A "..."

    A  "Yes, sir!" #(straightening, hitting a salute)

    hide rick_full

    "You turn to Mortimer, who has a red stain by his mouth."

    show rick_full

    RJ "Mo, kiddo. Don't go finishing all the chips while daddy's gone, now!"

    hide rick_full

    M "Hehehe! They're all in my tummy, having a paaarttyyy!"

    "You chuckle. Mo, sweet Mo... No hesitations with this one."

    "You cradle tiny Mo in one hand and hold Annie in the other as you begin walking inside. Chloe and your dad are hard at work nailing planks to the front windows."

    "You notice Annie nervously looking out to where you came from in the forest."

    #define timer

    $ time = 100
    $ timer_range = 100
    $ timer_jump = 'kiddo'
    show screen countdown

    menu:
        "Annie, don't worry, I'm here.":
        
            hide screen countdown

            "Annie looks up at Mo, in your arm. Then at her your father - her grandfather - working inside."

            A "Pop-pop seems worried, dad."

            $ time = 100
            $ timer_range = 100
            $ timer_jump = 'annie_whats_wrong'
            show screen countdown

            #define timer

            menu:
                "But I'm here with you now, sweetie... Don't worry.":

                    hide screen countdown

                    "She looks hesitant."

                    show rick_full

                    RJ "You need to conserve your strength. It's like I always say."

                    A " 'Stop worrying, so you can get your siesta.' I know, dad."

                    RJ "Exactly. We'll make it through this if we stay optimistic. Then we can all have our siestas."

                    hide rick_full


                    "Annie smiles a small smile, and she grips your hand tighter as you walk inside together."


                    "Annie smiles a small smile, and she grips your hand tighter as you walk inside together."

                    jump sleepers_catch_up_outside

                "Annie, look at me.":

                    hide screen countdown

                    "Annie looks up at you. You notice how dirty her overalls are. All of a sudden. Mo seems heavier."

                    show rick_full

                    RJ "Kiddo, I saw you taking care of your little brother earlier. How did that make you feel?"

                    A "... like mommy?"

                    RJ "That's right. Like mommy. She's strong, right? And that's how I feel when I take care of you. You make me stronger."

                    A "..."

                    RJ "So don't worry. Let me take care of you now, ok?"

                    hide rick_full

                    "Annie takes a breath and broadens her shoulders as the convenience store's doors slide open."

                    jump sleepers_catch_up_outside

            label annie_whats_wrong:

                "Annie, what's wrong?"

                "She looks up at you. Why's she trying to pull a tough face?"

                show rick_full

                RJ "Annie, talk to me."

                A "Pop-pop says I need to be tough. You aren't making it easy."

                hide rick_full

                "You suck air between your teeth too hard. You get a chill for a moment."

                show rick_full

                RJ "Kiddo, you don't have to do anything. Being afraid isn't bad. Lemme put it this way..."

                RJ "Imagine you scraped your knee, but you didn't feel any pain. You'd keep walkin' and walkin'."

                A "... I get it, dad. I wouldn't realize that something's wrong."

                RJ "It's more than that. If Mo were to scrape his knee, you wouldn't get it. You'd be a robot who'd turned off their human side. You see?"

                hide rick_full

                "Annie looks down."

                show rick_full

                RJ "You've done nothing wrong, Annie. Just think about it."

                hide rick_full

                "She just takes a breath and broadens her shoulders as the convenience store's doors slide open."

                jump sleepers_catch_up_outside


        "Kiddo...":

            hide countdown
            jump kiddo

    label kiddo:

        "Annie looks at you with surprisingly cold eyes and sniffles. With a sharp nod, she continues up ahead of you."

        "For a moment, you see dad in her sharp features."

        "You linger, unsure what to say to the dad in Annie. No... the Annie in Annie."

        "But your chance has passed. You follow her inside."

        jump sleepers_catch_up_outside

label sleepers_catch_up_outside:

    "The doors begin to slide open, revealing Gabe against the wall, watching Chloe and dad nailing boards to the windows and getting firearms out of storage cabinets."

    "His gaze is distant. You can't help but notice the film of sweat glazing his forehead."

    "And that he's clutching his leg."

    "You have to ask about it. It's what's best. But in front of Annie and Mo...?"

    $ time = 100
    $ timer_range = 100
    $ timer_jump = 'sleepers_catch_up_outside_1'
    show screen countdown

    menu:
        "Gabe... you're leg. What happened.":
            hide countdown
            jump sleepers_catch_up_outside_1
        "...":
            hide countdown
            jump sleepers_catch_up_outside_1

    label sleepers_catch_up_outside_1:

        "He doesn't answer."

        "He doesn't have time to, either. His head suddenly perks up, and he's pushing off the wall to gain balance."

        "The way he's moving makes his foot looks like it fell asleep. But he's able to shake it off."

        "You don't have to wonder why - a familiar rumbling sound hits you. Sleepers are coming from every direction."

        $ time = 100
        $ timer_range = 100
        $ timer_jump = 'cant_move'
        show screen countdown

        menu:
            "Everyone! Get further inside!":

                hide countdown

                "Gabe moved towards the door, and is still there."

                show rick_full at left
                show gabe_full at right

                RJ "Gabe, what're you doing?"

                G "..."

                hide rick_full at left
                hide gabe_full at right

                "His eyes look glossy. He's leaning against the door."

                show rick_ful

                RJ "Oh, god... Gabe!"

                "You look around. With a twinge of envy you see Annie's run into dad's arms, and Mo's with Chloe. A crashing sound forces you around."

                "Stones litter the floor. Sleepers are on the doors. Gabe still won't move."

                $ time = 20
                $ timer_range = 20
                $ timer_jump = 'grab_gabe'
                show screen countdown

                menu:
                    "Grab gabe and go":

                        hide countdown
                        jump grab_gabe

                    "Jump away":

                        hide countdown

                        "It's an instinctive reaction. Pussy. You can't keep his voice out of your mind."

                        "You find yourself a few meters away when Gabe's body is pulled into the throng."

                        C "GABE!"

                        "You meet the rest of the family, who are nearing the fire escape to regroup. Annie, who began to follow you, now meets you halfway."

                        jump kids_sacrificed


                label grab_gabe:

                    "You lunge towards Gabe."

                    show rick_full

                    RJ "Come ON, kiddo! We need to go!"

                    hide rick_full

                    "You can't keep the desperation out of your voice. Gabe won't budge, only sagging further to the floor."

                    "Arms close in. It's surprisingly sudden."

                    jump pull_gabe_up

            "...":

                hide countdown
                jump cant_move

        label cant_move:

            "You don't seem to be able to move. Everything feels muffled and far away."

            "You glimpse Annie running past you towards Gabe."

            "just managed to pull Gabe halfway through the doors. But the Sprinters are on her."

            "Things come in snippets."

            "Annie's pulled back outside into the crowd. Gabe watches, and is pulled in himself."

            "Your dad's hysterical expression, up in your face. Gabe's hand, the only thing left of him now."

            "Dad leaving you with one final disappointed expression. But there's genuine sorrow in his eyes, somewhere."

            "As he'd always remind you, you tend to daydream, so maybe you're just imagining it."

            jump death



                




label inside_with_richard:

    show bg gas_station_interior with scene_trans
    "Inside, you gather some boards and begin nailing."

    play sound "punch.mp3"
    with flash

    "Suddenly you're on your back and your face is stinging. The concrete is hard and cold on your back."

    show rick_full at left
    show richard_full at right

    R "I mean {i}seriously{/i}, Junior! You need to keep your eyes open."

    RJ "Obviously I didn't try to, dad."

    R "Oh, so you didn't {i}try{/i} to. That solves it."

    RJ "..."

    R "Don't look at me with that dumb face. Stop daydreaming, Rick."

    R "Most people grow out of that teenager stuff. Doubt. Being groggy all the time. Hungry all the time."

    hide rick_full at left
    hide richard_full at right

    "..."

    $ time = 15
    $ timer_range = 15
    $ timer_jump = 'inside_with_richard_1'
    show screen countdown

    menu:
        "Don't talk to me that way you abusive piece of shit. Do you have any idea how intolerable you are? How intolerable you sound? If it weren't for Gabe I'd have shoved my foot so far down your throat it'd come out the other GODDAMN END":

            hide screen countdown

            "Your throat is burning. Where did that come from?"

            "That felt good. "

            "That felt horrible."

            "Your dad's face suddenly looks twenty years older."

            show richard_full

            R "..."

            R "Just get your shit together, son."

            hide richard_full

            jump inside_with_richard_1

    label inside_with_richard_1:

        show richard_full

        R "..."

        R "...We don't have time for this. Get off your ass."

        hide richard_full

        $ time = 100
        $ timer_range = 100
        $ timer_jump = 'glare'
        show screen countdown

        menu:
            "Climb to your feet":

                hide screen countdown

                show richard_full

                R "*sigh* At least you can listen to reason. Maybe I did raise a half-decent man."

                hide richard_full

                jump inside_with_richard_2

            "Glare at him":

                hide screen countdown
                jump glare
        
        label glare:

            "Your dad is nearly seventy, but somehow, he feels immortal."

            "Like he'll never go away."

            "His eyes are unwavering. You can't win this."

            "It doesn't matter what you choose."

            "It'll always end up the same way."

            show richard_full

            R "I raised you better than this."

            R "Get going to your wife and eldest, son. Maybe they'll be able to take care of you."

            hide richard_full

            jump inside_with_richard_2

    label inside_with_richard_2:

        "Then, it's just you two, pulling together fireworks and various canisters of gas, pulling tripwires tight."

        "Neither of you says anything for a time. Leaves have blown in, and you can taste the cold fall air."

        "At some point, you catch his dissapointed eye - his gaze is hard and tired."

        $ time = 100
        $ halftime = time / 2
        $ timer_range = 100
        $ timer_jump = 'trap'
        $ timer_jump1 = 'inside_with_richard_2_updated_menu'
        show screen countdown
        show screen soCheap

        menu:
            "Dad... talk to me. You're treating me like I'm Gabe's age.":
                hide screen countdown
                hide screen soCheap
                jump default_richard_answer
            "Say nothing":
                hide screen countdown
                hide screen soCheap

                "Suddenly, a sound breaks out behind you-!"

                jump trap

        label inside_with_richard_2_updated_menu:
            menu:
                "Dad... talk to me. You're treating me like I'm Gabe's age.":
                    hide screen countdown
                    hide screen soCheap
                    jump default_richard_answer
                "Say nothing":
                    hide screen countdown
                    hide screen soCheap

                    "Suddenly, a sound breaks out behind you-!"

                    jump trap

                "What's wrong? I know things aren't easy...":
                     hide screen countdown
                     hide screen soCheap
                     jump default_richard_answer

        label default_richard_answer:

            show richard_full

            R "..."

            $ local_text = "Rick, I-"

            $ halftime = (len("Richard: " + local_text) / 40) * 10
            $ timer_jump1 =  "trap"
            show screen soCheap

            R "[local_text]"

            hide screen soCheap
            jump trap

    label trap:

        hide richard_full

        "Chloe runs in cradling Mo in one hand and pulling Annie along in another."

        show rick_full at left
        show chloe_full at right

        C "Rick! The horde - it's here!"

        RJ "What!?"

        C "We need to... we have to...get out of here!"

        hide rick_full at left
        hide chloe_full at right

        "A thumping sounds from the door. You swivel, ready to face the enemy, when..."

        show gabe_full

        G "Dad! Grandpa! Someone! SOMEONE!"

        hide gabe_full

        "Gabe's face screams at you, muffled behind the sliding-door entrance. The stones he's throwing at it have gotten your attention, but not as much as the horde, or his sagging left leg."

        "He couldn't have gotten injured at the river and still run all the way back... Could he?"

        "What to do? {i}What to do??{/i}"

        $ time = 100
        $ halftime = time / 4
        $ timer_range = 100
        $ timer_jump = 'horde_approach'
        $ timer_jump1 = 'trap_menu_updated'
        show screen countdown
        show screen soCheap

        menu:
            "Run to Gabe???":
                hide screen countdown
                hide screen soCheap
                jump death
            "Panic":
                hide screen countdown
                hide screen soCheap
                jump horde_approach
            "Gather up the family?":
                hide screen countdown
                hide screen soCheap
                jump horde_approach

        label trap_menu_updated:

            hide screen soCheap

            $ halftime = 25
            $ timer_jump1 = 'trap_menu_updated_1'
            show screen soCheap

            menu:
                "Run to Gabe???":
                    hide screen countdown
                    hide screen soCheap
                    jump death
                "Panic":
                    hide screen countdown
                    hide screen soCheap
                    jump horde_approach
                "Gather up the family?":
                    hide screen countdown
                    hide screen soCheap
                    jump horde_approach
                "Panic":
                    hide screen countdown
                    hide screen soCheap
                    jump horde_approach 

        label trap_menu_updated_1:

            menu:
                "Run to Gabe???":
                    hide screen countdown
                    hide screen soCheap
                    jump death
                "Panic":
                    hide screen countdown
                    hide screen soCheap
                    jump horde_approach
                "Gather up the family?":
                    hide screen countdown
                    hide screen soCheap
                    jump horde_approach
                "Panic":
                    hide screen countdown
                    hide screen soCheap
                    jump horde_approach
                "???":
                    hide screen countdown
                    hide screen soCheap
                    jump horde_approach

label horde_approach:

    show richard_full

    R "Rick, don't just stand there! Chloe said it - the horde's right there! You wanted to get away, so let's get away!"

    hide richard_full

    M "Daaadddyyyy!"

    $ time = 100
    $ timer_range = 100
    $ timer_jump = 'horde_approach_wait'
    show screen countdown

    menu:
        "But... Gabe!":

            hide screen countdown

            show rick_full at left
            show richard_full at right

            R "Screw Gabe! We need to leave!"

            RJ "Dad?!"

            R "The dolt's not going to make it to the door on that leg."

            R "Maybe if I'd raised him he wouldn't have come out a pussy like you! Now let's {i}go!{/i}"

            hide rick_full at left
            hide richard_full at right

            "You stammer for a moment, but there isn't even time for that. Annie's on the move."

            jump annie_dash

        "... fine!":

            hide screen countdown

            "You reach for Annie and Chloe, ready to push them behind the makeshift bomb you and Dad created."

            "But Annie's not there."

            jump annie_dash

    label horde_approach_wait:

        show richard_full

        R "Oh, to hell with it!"

        hide richard_full
        
        "Dad grabs Annie and Chloe, who brings Mo with her."

        "Stunned, you stand there. Dad comes back and drags you along to the back."

        "You feel incompetent, but you girl's got other plans."

        jump annie_dash

label annie_dash:

    "Annie's already grasping at the door."

    show gabe_full

    G "Urh - Ann- hck - thank god!"

    A "Gabe! Your leg! It's...gray!"

    G "It's... fine! Just help me get inside!"

    hide gabe_full

    "This is a dream. It's got to be. Even from where you're standing, it's clear that Annie can't contend with the horde's strength. Say something. Do something."

    $ time = 100
    $ timer_range = 100
    $ timer_jump = 'annie_dash_wait'
    show screen countdown

    menu:
        "Help Annie grab Gabe":

            hide screen countdown

            "You run towards Annie - Gabe's struggling to get up. His leg is definitely screwed up."

            show rick_full at left
            show gabe_full at right

            RJ "Gabe! Your leg!"

            G "Later, dad...!"

            hide rick_full at left
            hide gabe_full at right

            "He winces. The horde pulses behind the half-closed doors, jostling itself to get in."

            $ time = 100
            $ timer_range = 100
            $ timer_jump = 'annie_dash_wait'
            show screen countdown

            menu:
                "Pull Gabe up":

                    hide screen countdown
                    jump pull_gabe_up

                    label pull_gabe_up:

                        "You begin to pull Gabe up. As he gets to his feet, Annie puts his arm around her shoulder."

                        jump sleepers

                        label sleepers:

                            QM "Dooooonnnn't let them get away! You twooo, get the doooor!"

                            "You all swivel. This Sleeper is that bodybuilder from the river. Its hand is on Gabe's calf as two others hold the door open."

                            Sleeper "Nothing personal... kiddo..."

                            "Gabe's face slams into the floor as he's pulled back by the leg."

                            $ time = 20
                            $ timer_range = 20
                            $ timer_jump = 'pull_gabe_1'
                            show screen countdown

                            menu:
                                "Pull him back":
                                    hide screen countdown
                                    jump pull_gabe_1

                            label pull_gabe_1:

                                "You aren't fast enough. And Gabe is swallowed up just like that."

                                "And they're on you. And on Annie."

                                "And soon, things aren't so difficult. You wonder what your dad is thinking, but not for long."

                                "You have no energy to resist the crowd of Sleepers, and soon, you're asleep, too."

                                jump death

                "Pull Annie away":

                    hide screen countdown

                    A "Dad! What're you...!"

                    show rick_full

                    RJ "Annie, he's already done for!"

                    hide rick_full
                    
                    "Annie's face threatens to stop you in your tracks. But you have to move. You've committed. For once."

                    $ time = 100
                    $ timer_range = 100
                    $ timer_jump = 'sleepers'
                    show screen countdown

                    menu:
                        "Annie, he's bitten. He's about to sleep.":
                            
                            hide screen countdown
                            jump annie_unsatisfied
                        
                        "Annie, I need to get you out of here first!":

                            hide screen countdown
                            jump annie_unsatisfied

                    label annie_unsatisfied:

                     "Annie grits her teeth and screws up her face, but listens to daddy. You pick her up, all the while wondering..."

                     "Why is it that you make actions and then justify them, and not the other way around?"

                     jump kids_sacrificed


        "...":

            hide screen countdown
            jump annie_dash_wait

            label annie_dash_wait:

                "You don't seem to be able to move. Everything feels muffled and far away."

                "Annie's just managed to pull Gabe halfway through the doors. But the Sprinters are on her."

                "Things come in snippets."

                "Annie's pulled back outside into the crowd. Gabe watches, and is pulled in himself."

                "Your dad's hysterical expression, up in your face. Gabe's hand, the only thing left of him now."

                $ annie_alive = False

                $ time = 100
                $ timer_range = 100
                $ timer_jump = 'annie_dash_wait_wait'
                show screen countdown

                menu:
                    "...":

                        hide screen countdown 
                        jump annie_dash_wait_wait

                    "Shake your head":

                        hide screen countdown

                        "You shake your head and snap out of it. He's right."

                        "{i}Gabe... Annie... Listen to your grandpa. He knows best...{/i}"

                        "Twisting your eyes shut, you run back to where the rest of your family waits, huddled by the fire escape."

                        "You don't hear any footsteps behind you. Not from the preoccupied Sleepers, and not from your children."

                        jump kids_sacrificed

                label annie_dash_wait_wait:

                        "He's right. You're a wuss. Gabe's a wuss. But is it really your fault?"

                        "Probably. Probably..."

                        "You feel him trying to drag you away. Hear his voice..."

                        show richard_full

                        R "Don't freeze up on me, son...!"

                        hide richard_full

                        "Why would he say that?"

                        "... oh, right. Didn't he love you? Apparently. Then why did he beat you? Chastise your every move?"


label kids_sacrificed:

    if annie_alive:
        "You find Chloe, Dad, and Mo at the back. Annie runs to her mother."
    else:
        "You find Chloe, Dad, and Mo at the back."

    "Seeing you arrive, Chloe locks eyes with you and gives her your signature telepathic nod."

    "She begins to push open the fire escape - and twenty fingers emerge from the other side."

    show chloe_full

    C "Ahhhssshhitshitshit!"

    hide chloe_full

    "She backpedals from those twenty fingers, connected to four arms and the two Sleepers they belong to."

    "A skinny Sleeper reaches towards her as a tiny one lunges through the doorway at Dad."

    $ time = 100
    $ timer_range = 100
    $ timer_jump = 'skinny_wait'
    show screen countdown

    menu:
        "Kick the skinny one":

            hide screen countdown

            "You lift your foot as close to your chest as you can and let it rip."

            "WHAM! As your heel makes contact, you feel a surge of energy flow through you."

            show rick_full

            RJ "RRRAHHH!"

            hide rick_full

            "The skinny Sleeper is clutching its chest, its breathing ragged. You're already running towards Chloe."

            show rick_full at left
            show chloe_full at right

            RJ "Chloe?"

            C "I'm good. Let's get to the side exit, people! The Sleepers coming through the front will be taken care of by the bomb!"

            hide rick_full at left
            hide chloe_full at right

            " {i}‘Fuck!'{/i} "

            "Ok, good. Dad's alright."

            if annie_alive:

                "You spot Annie with her arms around Mo. They're both shivering, looking at the decapitated Sleeper dad's ax took care of."

                "You drag Annie behind you, bringing Mo in tow."
            else:
                 "You spot Mo. He's both shivering, looking at the decapitated Sleeper dad's ax took care of."

                 "You put out your hand to drag him along."

            show rick_full

            RJ "Who had the side-door key!?"

            hide rick_full

            "You're getting dangerously close to the door when you realize: Gabe did. You screech to a halt."
            
            $ time = 100
            $ timer_range = 100
            $ timer_jump = 'door_wait'
            show screen countdown

            menu:
                "Alright, everyone upstairs!":

                    hide screen countdown

                    "You all run to the roof. Your heart feels like it'll leap out of your chest, but when you look at dad, you feel... in control."

                    play sound "fire_works.mp3"

                    "As you run, you hear explosions go off behind you - firecrackers and smoke fill the air."

                    "Maybe things will work out!"

                    "With a pang of guilt, you remember Gabe. It was his idea - the idea you would've gone with. Did you only have confidence in it because it let you seem confident in front of Dad?"

                    #(change background to roof)

                    jump just_got_to_roof

                "Dad, what do we do?":

                    hide screen countdown

                    show richard_full

                    R "We need to get high! Figure out a plan!"

                    hide richard_full
                    
                    "He's already dragging Chloe up with him. You follow him, but your heart is still on the first floor?"

                    "Why couldn't you be the one to take her hand? You shake the thoughts from your head."

                    play sound "fire_works.mp3"

                    "As you run, you hear explosions go off behind you - firecrackers and smoke fill the air."

                    jump just_got_to_roof

            label door_wait:

                "There's a scream behind you. Looking around, it's clear - Mo's nowhere to be found. You dash back down."

                jump keep_moving_towards_mo

        "Run towards Dad":

            hide screen countdown
            jump skinny_wait

    label skinny_wait:

        "You run towards Dad."

        "Ugh. Like old times. When the kids at school would make fun of you and you'd only have him to take cover with."

        "But you'd still do it. Even though it meant he, too, would ridicule you for running home to daddy."

        "And now, too, you look backwards only after your instinctive drive wears off."

        if annie_alive:

            "Wordlessly, Chloe holds onto Annie, trying to stave off the Sleepers."
        else:
            "Wordless, Chloe swats at the Sleepers to no avail."

        "And you can't do anything but watch now. This... is too much."

        "You look back at Dad."

        "Being stuck with him for the rest of the apocalypse... Even your Stockholm syndrome isn't that bad."

        "And so you sit walk towards Chloe, letting yourself fall asleep in her arms for one final time."

        return


label just_got_to_roof:

    play sound "wind.wav"

    "The cold air stings your eyes. Wind blows by your ears, and for a moment, everything is quiet."

    "Of course, it can't last."

    show chloe_full

    C "Where is he? Where's Mo?!"

    hide chloe_full

    "You look around. Sure enough, he isn't anywhere. It'll only take a second to go back down..."

    stop sound 

    $ time = 100
    $ timer_range = 100
    $ timer_jump = 'make_plan'
    show screen countdown

    menu:
        "Go back down":

            hide screen countdown

            "You're already back down the ladder. Of course you'd get Mo. Of course you would - he's your son!"

            $ time = 100
            $ timer_range = 100
            $ timer_jump = 'go_back_down_wait'
            show screen countdown

            menu:
                "Keep moving":

                    hide screen countdown
                    jump keep_moving_towards_mo

            label go_back_down_wait:

                "Mo is taken before your eyes."

                "Before you can even process how stuck in place you are, how in shock you are, you feel hands on your shoulders."

                "And things aren't so clear from that point, but when you come to, you're on the roof..."

                "And dad's towering over you."

                R "..on! Come {i}on{/i}, Rick!"

                "You struggle to your feet."

                jump roof_encounter_start


            label keep_moving_towards_mo:

                "No. No time to be thinking about that."

                "You turn around. Sure enough, Mo's huddled in a corner. His face is buried between his knees. Smoke is everywhere."

                show rick_full

                RJ "Mo! Come here, Mo!"


                hide rick_full

                M "Hah- Daddy!"

                $ local_text = "He begins running towards you"

                $ halftime = (len(local_text) / 40) * 10
                $ timer_jump1 =  "backhand_menu"
                show screen soCheap

                "[local_text]"

                hide screen soCheap
                jump backhand_menu

                label backhand_menu:

                    #(switch to a Sleeper mid-leap towards you)

                    $ time = 20
                    $ timer_range = 20
                    $ timer_jump = 'backhand_menu_wait'
                    show screen countdown

                    menu:
                        "Backhand the shape in front of you":

                            hide screen countdown

                            play sound "punch.mp3"

                            "WHAM"

                            "It's like your fist moved on its own."

                            "The Sleeper has a new dent in its face. And you're gone."

                            "Back on the roof with Mo in hand, you're met with the same cold winds. Somehow, you made that work...!"

                            show chloe_full at left
                            show richard_full at right

                            C "Mo! Mo, my boy..."

                            R "Come here, kiddo. Where were you, ya little rascal?"

                            hide chloe_full at left
                            hide richard_full at right

                            "Tears of exhausted victory flow. You're all able to forget the situation for a moment."

                            $ mo_saved = True

                            jump roof_encounter_start

                    label backhand_menu_wait:

                        "What were you expecting?"

                        "You don't move in time. The Sleeper is on you."

                        "Somewhere, Mo is screaming. But when you seem him next, it's because his foot is in your mouth."

                        "Maybe this is another one of your daydreams..?"

                        return


        "Stay and make a plan":

            hide screen countdown
            jump make_plan

    label make_plan:

        "There's no time. Somehow, you turn the key to your heart. You've left someone behind."
        "You feel it lock shut with a resounding and painful thud."
        "SOmething else, shuts, too:"

        jump roof_encounter_start

label roof_encounter_start:

    play sound "keys.wav"
    show bg roof_main

    "You close the ladder hatch and it locks automatically. The keys were lost along with Gabe, so you should have a few minutes to think."

    if mo_saved and annie_alive :
        "Chloe is with Annie and Mo, cradling them from the world."
    elif mo_saved and not annie_alive:
        "Chloe is with Mo, cradling him from the world."
    elif not mo_saved and annie_alive:
        "Chloe is with Annie, cradling her from the world."
    else:
        "Chloe has her arms wrapped around herself, trying to cradle herself in this harsh reality."

    "Richard's looking at you. His eyes are still cold, but they're tired. He's tired. Old."

    show richard_full

    R "Rick. The horde can't get us from here, but I'm outta ideas. This was you and your son's brilliant plan, and he's gone now to boot, so I'll ask you: what now?"

    hide richard_full

    "Chloe looks up at you."

    show chloe_full at right
    show rick_full at left

    C "Rick, we can't continue with Gabe's plan. Like he said, hordes are more distracted - if your bomb took any of them out, the survivors'll be more independent."

    RJ "I..."

    C "Maybe we could try for a simple distraction. We take my pack and throw it into the car down below. The glass could give us a few seconds."

    if annie_alive:
        A "Mom... where are we gonna go?"

        C "Ann..."

    RJ "We'll have to make a break for it by jumping into the foliage out back. There's no other way down other than the ladder."

    hide chloe_full at right
    hide rick_full at left

    "Dad slams his fist on the metal roof."

    show richard_full

    R "This was supposed to be our home! Our last chance! And you... "

    hide richard_full

    "He looks up at you."

    $ time = 20
    $ timer_range = 20
    $ timer_jump = 'jangling_keys'
    show screen countdown

    menu:
        "Dad... We have to get going.":

            hide screen countdown

            "You're about to open your mouth to say something, but you don't get the chance."

            jump jangling_keys

        "You can't possibly be blaming this on me.":

            hide screen countdown

            "You're about to open your mouth to say something, but you don't get the chance."

            jump jangling_keys

        "Look away":

            hide screen countdown

            "Why's he making things more complicated? This is already a shitstorm."

            jump jangling_keys

        "...":
            hide screen countdown
            jump jangling_keys

label jangling_keys:

    play sound "keys.wav"
    "A rattling sounds behind you. You know that noise."

    "It's the jangling of keys."
    
    "And again, you turn, expecting to see the enemy, but again, something else is there instead."

    #(show Gabe, now a Sleeper, emerging from the hatch)

    "Again, it's Gabe."

    show gabe_full

    G "Daaaaddd.... We... need to ruunnn...."

    hide gabe_full

    $ time = 100
    $ halftime = time / 3
    $ timer_range = 100
    $ timer_jump = 'sleepers_come_up'
    $ timer_jump1 = 'jangling_keys_menu_updated'
    show screen countdown
    show screen soCheap

    menu:
        "Do something":
            hide screen soCheap
            hide screen countdown
            jump act_to_sleeper_gave

    label jangling_keys_menu_updated:

        hide screen soCheap

        $ halftime = time / 6
        $ timer_jump1 = 'jangling_keys_menu_updated_1'

        show screen soCheap

        menu:
            "Do something":
                hide screen soCheap
                hide screen countdown
                jump act_to_sleeper_gave
            "Move. Your. Feet.":
                hide screen soCheap
                hide screen countdown
                jump act_to_sleeper_gave

    label jangling_keys_menu_updated_1:

        menu:
            "Do something":
                hide screen soCheap
                hide screen countdown
                jump act_to_sleeper_gave
            "Move. Your. Feet.":
                hide screen soCheap
                hide screen countdown
                jump act_to_sleeper_gave
            "Say something. Anything.":
                hide screen soCheap
                hide screen countdown
                jump sleepers_come_up

label act_to_sleeper_gave:
    
    "Your voice sounds like gravel sliding out of you."

    show rick_full

    RJ "G-gabe?"

    hide rick_full

    "Your eyes slide over the goosebumps on his freshly-gray skin."

    if annie_alive:
        A "D-daddy! Why is Gabe... why..."

    show richard_full at left
    show gabe_full at right

    R "{i}Richard!{/i} He's {i}dead!{/i} Get a hold of yourself!"

    #(bring Richard into the shot - now it's Gabe on your right and Richard on your left)

    "But you know that he isn't really dead. This isn't a zombie movie."

    "His eyes still have light in them."

    "He can still talk. Run."

    "He's basically just a groggy, very hungry person."

    hide gabe_full at right
    show chloe_full at right

    C "He... looks like himself..."

    R "He's in the early stages! Of course he's still himself!"

    hide richard_full at left
    hide chloe_full at right

    "You look at Dad."

    $ time = 100
    $ timer_range = 100
    $ timer_jump = 'sleeper_gave_wait'
    show screen countdown

    menu:
        "If you want to go so badly then leave.":

            hide screen countdown

            "Something about seeing Gabe like that makes things very clear."

            show rick_full at left
            show richard_full at right

            RJ "Why are you here? Seriously."

            R "..."

            RJ "Cat's got your tongue? Satisfied that your grandson's dead, just so you can tell me I screwed up? That I wasn't you enough?"

            R "...!" #(about to say something)

            hide rick_full at left
            hide richard_full at right

            jump sleepers_over_edge

        "What do you want me to say?":

            hide screen countdown

            show richard_full

            R "I don't want you to say anything. I just..."

            hide richard_full

            "His glance jumps to Gabe."

            show chloe_full

            C "Guys!"

            hide chloe_full

            "Your gaze falls on her. She's bristling, her mouth open to say something."

            jump sleepers_over_edge

    label sleeper_gave_wait:

        "Chloe takes a step towards you."

        show chloe_full

        C "Rick, let's get going. Don't let him keep us."

        hide chloe_full

        jump chloe_snatched

label sleepers_over_edge:

    play sound "metal_crash.mp3"

    "Over the edge of the roof, a forest of fingers springs up. Hands grip one another and Sleepers vault themselves over the edge."

    "They're right behind Chloe. A rumbling comes from the corner of your vision..."

    "... and Gabe is pushed out of the way as the bodybuilder, face mutilated and missing a shoulder, emerges from the ladder hatch."

    "There are seconds now. Sleepers from the roof-edge. Sleepers from the ladder."

    $ time = 25
    $ timer_range = 25
    $ timer_jump = 'sleepers_over_edge_wait'
    show screen countdown

    menu:
        "Grab Chloe and jump":

            hide screen countdown

            "It's suddenly so clear, looking at Gabe. Your Gabe."

            "Dad's poisoned you. Work, work, work. Do more, do it now."

            "What a disappointment. He isn't me."

            "And then you doubt. So he shouts more. And you learn to hate what you're most sure of."

            "And then you're never really awake. And you can't even appreciate it."

            "That piece of you was coming out through Gabe. And you were so poisoned by Dad that you still followed the instinct to cull it."

            "And now Gabe's asleep, and he can't appreciate it, either."

            "You run towards Chloe and reach for her hand. You see Dad follow suit."

            "And as you leap into the bushes, not knowing what they'll do to break your fall, you can feel Gabe's eyes on your back."

            "And that in his final waking moments, he can be proud of his dad of acting of his own accord."

            return

        "Tackle Dad":

            hide screen countdown

            "You can't believe this. How {i}dare{/i} he!?"

            "You slam into him."

            show rick_full

            RJ "Is {i}this{/i} what you wanted? Look, I'm taking the initiative! I'm macho!"

            RJ "Yeah, what I taught Gabe was wrong, because that's all you {i}gave{/i} me!"

            hide rick_full
            show chloe_full

            C "God damn it, Rick!"

            hide chloe_full

            "Her voice is far away. Your vision is red."

            "Gray, bumpy hands enter your vision. They're smothering Dad."

            $ time = 20
            $ timer_range = 20
            $ timer_jump = 'rick_on_richard_death'
            show screen countdown

            menu:
                "Punch":

                    hide screen countdown

                    play sound "punch.mp3"

                    "You swing your first"

                    jump tackle_dad_1

            label tackle_dad_1:

                "Now they're trying to smother you. But you keep lashing out. Your eyes are closed, but your fists don't stop moving."

                $ time = 20
                $ timer_range = 20
                $ timer_jump = 'rick_on_richard_death'
                show screen countdown

                menu:
                    "Punch":

                        hide screen countdown

                        play sound "punch.mp3"

                        "You swing your first"

                        jump tackle_dad_2

            label tackle_dad_2:

                "It doesn't seem to be helping. With every swipe, you feel yourself getting further from something important."

                "You were looking at Gabe just a second ago, and for some reason, you felt like you were looking in a mirror."

                "You're just becoming your old man."

                "The rage just builds. Things wouldn't have ended up any differently if you'd have just abided by who he wanted you to be."

                $ time = 20
                $ timer_range = 20
                $ timer_jump = 'rick_on_richard_death'
                show screen countdown

                menu:
                    "Punch":

                        hide screen countdown

                        play sound "punch.mp3"

                        "You swing your first"

                        jump rick_on_richard_death

            label rick_on_richard_death:

                "That relaxed expression Gabe wore a moment ago... in a strange way, that was you."

                "You feel tears rolling down your face."

                "Even with the shit that you passed down to him from dad, he managed to keep himself."

                "Or maybe it's just that it took him Turning to overcome both of your bullcrap..."

                "Hah... even now, you're indecisive as all get out."

                "That sucks."

                return

    label sleepers_over_edge_wait:

        "You freeze up. Out of the corner of your eye, you see Gabe approaching you."

        "Screams ring out all around you. Chloe. Annie."

        "In front of you, Dad's face is unwavering, but wrought with pain."

        "He turns and runs, finally taking your suggestion and flinging himself off the roof."

        "Arms slowly close around you."

        show gabe_full

        G "Daaaadd..... I am so... tired... of grandpa...."

        hide gabe_full

        "You can't help but laugh."

        show rick_full

        RJ "I feel like we understand each other better than ever, son."

        hide rick_full

        "You close your eyes and cradle your chin in his shoulder as he does the same."

        "His back is rough, but you can ignore it. This is father-son bonding."

        "Maybe Gabe is more like you than you thought. It's a shame that it took you this long to accept that you aren't Dad."

        "At least you can both have that siesta now."

        jump death

label chloe_snatched:

    "Over the edge of the roof, a forest of fingers springs up. Hands grip one another and Sleepers vault themselves over the edge."

    "They were right behind Chloe. A rumbling comes from the corner of your vision..."

    "... and Gabe is pushed out of the way as the bodybuilder, face mutilated and missing a shoulder, emerges from the ladder hatch."

    "How could you have missed that?! Keep your eyes open, you dolt!"
    if annie_alive:
        "Chloe and Annie are pulled down over the edge."
    else:
        "Chloe is pulled down over the edge."



    $ time = 100
    $ timer_range = 100
    $ timer_jump = 'sleepers_over_edge_wait'
    show screen countdown

    menu:
        "Run Over":

            hide screen countdown
            "# TODO unfinished"
            #TODO - timing thingy where they get pulled one by one

        "Jump into bushes":

            hide screen countdown

            "This is your only chance."

            "... at least, that's what you tell yourself after your body starts moving."

            "You aren't quite sure what you just did."

            "It was automatic and so fast that you're still processing it, watching your thoughts go by as the edge of the roof races underneath you."

            "A familiar grunt and another sound of metal crunching under a jumping person tell you that your dad had a similar reaction."

            "You haven't even hit the ground and you're already wishing that you'd have just stayed up there."

            "It would've probably been easier than living out the rest of the apocalypse with the piece of you that you wish would just go away."

            return

            






    





        

 




        








  

    













   


    

                




















            
















    








label death:

    "You died"

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
