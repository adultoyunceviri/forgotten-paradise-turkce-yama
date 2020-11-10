label startch6:
    
with fadein
scene black
mc thinking "I should get a shower before going..."
"You already memorize the route to the showers, so it doesn't take you long to reach it."

scene mcchangingforshower
$ renpy.transition(Dissolve(1))
$ renpy.pause(2, hard=True)
with dissolve
"You take off your clothes and put them in the lockers next to you."

scene mctowelonlockers 
with dissolve

mc nudethinking "Seeing Cassandra again would be really nice... even though I learned what I learned we are still married and lived together for many years..."
mc nudethinking "Zoey being there is just another reason for me to go..."

if sex_with_elyse:
    mc nudethinking "First Elyse trying to seduce me in the pool.... and then...Zoey..."
    if mc_zoey_sex:
        jump ch6z1
    else:
        jump ch6z2
elif mc_zoey_sex:
    jump ch6z1
else:
    
    mc nudethinking "I wonder if she will be pissed that I refused her last time... I hope not."
    jump ch6z2

label ch6z1:
if zoey_cum_inside:
    
    mc nudethinking "I don't even want to remember the fact that I came inside her..."
    
elif zoey_cum_outside:
    
    mc nudethinking "The fact that I've fucked her doesn't give me any comfort... but at least I held myself from cumming inside her..."

label ch6z2:

mc nudethinking "And last but not least Dahlia. She is one hell of a beauty and she seems to fancy me somewhat."

mc nudethinking "Time to get that shower. I don't want to be very late..."

scene mcabouttotakeashower
with fadein

"As you make your way in to the showers you notice there is someone else taking one..."

mc nudethinking "Someone else is here?"

qm "\"Hnnh... Mm..Hahh.....\""
"You stand still for a second and hear soft moaning coming from the shower cabin next to you."

mc nudethinking "Ohoh... Should I take a peek?"

$ quick_menu = False

menu:
    "Take a peek":
        $ quick_menu = True
        scene mcpeekingonelyse0
        $ spy_elyse_shower_caught = True
        with dissolve
        "Your curiousity takes the better of you and you decide to take a slight peek."
        "The voice becomes more clear as you move closer."
        
        scene mcpeekingonelyse1
        with dissolve
        
        e nudepleasure "\"Mmm...\""
        
        scene showerselyseanim12
        with dissolve
        
        e nudepleasure "\"Pha...Hmmh...\""
        
        mc nudethinking "Elyse?? And she is masturbating..."
        
        scene elyseshowernoticesyou0
        with dissolve
        "You just stand there stunned at what you're seeing."
        
        scene elyseshowernoticesyou1
        with dissolve
        "Before you can even realize she notices you peeking at her..."
        e nudesad "\"Huh!?\""
        mc nudethinking "Oh shi--"
        
        scene elysecomingoutshowerangry
        with dissolve
        
        "In a burst of rage she storms out of the shower..."
        
        e nudetalk "\"What the fuck are you doing?\""
        e nudetalk "\"Peeking on other people's showers?!\""
        mc nudetalk3 "\"I --\""
        e nudetalk "\"Fucking pervert.\""
        
        "Elyse leaves after throwing quite a few insults..."

        if sex_with_elyse:
            scene black
            with dissolve
            mc nudeshocked2 "I guess she doesn't remember anything from the other day when we actually... nevermind..."
        else:
            scene black
            with dissolve
            mc nudeshocked2 "God... this was really embarrassing..."
        
        scene mctakingrobeoffshower
        with fadein
        
        "You go in the last shower cabin and remove your towel."
        $ quick_menu = False
        menu:
            "Shower":
                jump ch6shower
        label ch6shower:
        $ quick_menu = True
        scene mcrobeoffshowers2
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(2, hard=True)
        with dissolve
        
        scene mccominginlockerstochange
        with fadein
        
        "You take your shower and go back to the changing rooms and hear some noise coming from around the corner..."
        mc nudethinking "Elyse is still here? Changing?"
        

        mc nudethinking "She was so angry earlier... I wonder if it's even a good idea to check..."
        $ quick_menu = False
        menu:
            "Check":
                $ quick_menu = True
                mc nudethinking "Fuck it. Can't go any worse than before..."
                jump janelockers
        
        
        
        
    "Play it safe and don't":
        $ quick_menu = True
        $ spy_elyse_shower_caught = False
        
        scene mctakingrobeoffshower
        with fadein
        
        mc nudethinking "Better not try anything stupid that will get me in trouble."
        mc nudethinking "Not worth i--"
        qm "\"Mmmmhh...Haa...\""
        
        scene mcrobeoffshowers
        with dissolve
        
        "You remove your towel, but the moaning continues..."
        
        mc nudethinking "Fuck, it's driving me nuts. Maybe there is another way to see what is happening up there without getting spotted."
        
        scene mcclimbingshowerwall
        with dissolve
        
        mc nudethinking "Should I do it? Climb the showers and check from above?"
        
        $ quick_menu = False
        
        menu:
            "Climb and spy from above":
                $ quick_menu = True
                $ spy_elyse_shower = True
                scene mcpeeksonelyse
                with fadein
                "The curiousity takes the better of you and you begin to climb the shower cabin."
                "As you reach the top you see the cause of the moaning..."
                
                scene mccumstopofelyseshower
                with dissolve
                
                mc nudetalk3 "Elyse... masturbating right now..."
                "The fact you are spying on someone pleasuring themselves and the fact you could be caught makes you way too excited as you continue to watch her..."
                
                $ quick_menu = False
                show screen elyse_masturb_shower
                $ renpy.show("elyse_masturb_shower")
                $ renpy.transition(Dissolve(1))
                $ renpy.pause(12, hard=True)

                label elyse_masturb_shower:
                hide screen elyse_masturb_shower
                
                scene elysecumming1
                with dissolve
                
                $ quick_menu = True
                "You watch her until she gets up and begin to spasm... looking as she is about to cum."
                
                $ quick_menu = False
                
                menu:
                    "Jack off":
                        $ quick_menu = True
                        scene mcmasturbtopshowers00
                        with dissolve
                        "This alone is enough for you to start rubbing one out right above her..."
                        
                        $ quick_menu = False
                        show screen mc_jacks_on_top_shower
                        $ renpy.show("mc_jacks_on_top_shower")
                        $ renpy.transition(Dissolve(1))
                        $ renpy.pause(12, hard=True)

                        label mc_jacks_on_top_shower:
                        hide screen mc_jacks_on_top_shower
                        
                        scene mcmasturbtopshowerscum1
                        with dissolve
                        
                        $ quick_menu = True
                        "Soon you feel that you're reaching your limit..."
                        
                        $ quick_menu = False
                        
                        menu:
                            "Cum":
                                $ quick_menu = True
                                mc nudepleasure "Oh, sweet mother of go...d!!"
                                scene mcmasturbtopshowerscum2
                                with flash
                                scene mcmasturbtopshowerscum2
                                with flash
                                scene mcmasturbtopshowerscum2
                                with flash
                                $ renpy.pause(1, hard=True)
                                scene elysecumming2
                                with dissolve
                                "You cum right above Elyse... Some of your cum hitting the floor, but some splattering on her hair, chest and face without her noticing from the water dripping."
                                scene mcclimbingshowerwall
                                with dissolve
                                
                                "Satisfied you climb back down and take your shower..."
                                scene mcrobeoffshowers2
                                with dissolve
                                "It doesn't take more than a minute or two after you turn on your shower to hear Elyse turning hers off and leaving."
                                
                                scene mccominginlockerstochange
                                with fadein
                                
                                "You take your shower and go back to the changing rooms and hear some noise coming from around the corner..."
                                mc nudethinking "Elyse is still here? Changing?"
                                
                                $ quick_menu = False
                                
                                menu:
                                    "Check":
                                        $ quick_menu = True
                                        mc nudethinking "Can't really get in trouble for coming in here now."
                                        jump janelockers


            
            "Don't":
                $ quick_menu = True
                $ spy_elyse_shower = False
                mc nudethinking "Nah... I really shouldn't be doing stuff like this. Especially from above where there would be no excuse if I get caught."
                scene mccominginlockerstochange
                with dissolve
                "You take your shower and go back to the changing rooms and hear some noise coming from around the corner..."
                mc nudethinking "Someone is still here?"
                
                $ quick_menu = False
                
                menu:
                    "Check":
                        $ quick_menu = True
                        mc nudethinking "Can't really get in trouble for coming in here now."
                        jump janelockers
                
        
label janelockers:
scene mccominginlockerstochange2
with dissolve

"You turn around the corner only to find a familiar face there..."

$ quick_menu = False

scene janeportraitlockers with fade:
    subpixel True
    yalign 1.0
    pause 2.0
    linear 7.0 yalign 0.0
pause

$ quick_menu = True

"She is just sitting there... completely naked..."

#group lockers
if shower_jane_group:
    j nudetalk "\"Oh, [mc]? We have a habbit of meeting in the showers now it seems.\""
    mc nudetalk "\"Hi, Jane. Shower meetings with you are never dull, so I am totally fine with that.\""
    j nudeyummy "\"Oh, yeah? Well, we can't have this one be dull either.\""
    j nudeyummy "\"Come closer...\""
    
    $ quick_menu = False
    
    menu:
        "Come closer":
            $ quick_menu = True
            scene lockersmcmovescloser
            with dissolve
            "You say to yourself 'why the heck not' and move in closer to Jane."
            scene janelockersfondlesbreasts
            with dissolve
            j nudetalk "\"So, mister. What would it be? Blowjob or titty fuck?\""
            $ quick_menu = False
            menu:
                "Blowjob":
                    $ quick_menu = True
                    $ lockers_jane_tits = False
                    $ lockers_jane_blowjob = True
                    mc nudetalk3 "\"Your mouth, please.\""
                    j nudeyummy "\"My mouth, huh? I will show you what heaven feels like.\""
                    "Her nude body and her dirty language gets you hard in no time."
                    mc nudetalk "\"Ahh...\""
                    scene janelockersbj00
                    with dissolve
                    j nudetalk2 "\"Already got you hard. This won't take long.\""
                    
                    $ quick_menu = False
                    show screen jane_lockers_blowjob6
                    $ renpy.show("jane_lockers_blowjob6")
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(12, hard=True)

                    label jane_lockers_blowjob6:
                    hide screen jane_lockers_blowjob6
                    
                    $ quick_menu = True
                    mc nudepleasure "\"Fuck... getting close...\""
                    
                    j nudeblow "\"*Buhh* Mmmh! Spray it *Gah* inside *Ghh* my mouth *Buh*\""
                    
                    "Her sloppy sounds while talking with your cock in her mouth is all you needed to push you over the edge..."
                    
                    scene janelockersbjcum1
                    with flash
                    scene janelockersbjcum1
                    with flash
                    scene janelockersbjcum1
                    with flash
                    
                    mc nudepleasure "\"Aaahh~\""
                    j nudepleasure1 "\"*Gulp* *Gulp* *Gulp*\""
                    
                    "Jane tries to swallow as much as she can, but your load is too much for her and she spills some out of her mouth."
                    
                    scene janelockersbjcum2
                    with flash
                    
                    j nudepleasure1 "\"*Slurp*\""
                    j nudeskeptical "\"Fuck, baby... you will drawn me in your cum.\""
                    
                    scene black
                    with fadein
                    
                    "She cleans herself and you both sit back on the bench."
                    
                    scene lockersmcjanesitting
                    with fadein
                    
                    j nudetalk "\"I guess I drained you before the party has started, huh?\""
                    
                    mc nudetalk3 "\"Hahaha. I regenerate fast.\""
                    
                    j nudetalk2 "\"Oh, yeah? You ready for round two then?\""
                    
                    mc nudetalk2 "\"Wait, now?\""
                    
                    j nudetalk "\"I wish. I have to go and you will be late, so some other time we will continue where we left off.\""
                    
                    mc nudetalk "\"No complains here.\""
                    
                    j nudetalk2 "\"Go, go now, before I change my mind.\""
                    
                    "You both say goodbye to each other and part ways for now as you dress back up and leave for Andre's room."
                    scene mcchangingforshower
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(2, hard=True)
                    with dissolve
                    
                    jump andrecassroom
                    
                    
                "Titty fuck":
                    $ quick_menu = True
                    $ lockers_jane_blowjob = False
                    $ lockers_jane_tits = True
                    mc nudetalk3 "\"Your breasts, please.\""
                    j nudeyummy "\"My tits, huh? Prepare to be squished by my pretty tits.\""
                    "Her nude body and her dirty language gets you hard in no time."
                    mc nudetalk "\"Ahh...\""
                    scene janelockersboobjob00
                    with dissolve
                    j nudetalk2 "\"Already got you hard. This won't take long.\""
                    
                    $ quick_menu = False
                    show screen jane_lockers_boobjob6
                    $ renpy.show("jane_lockers_boobjob6")
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(12, hard=True)

                    label jane_lockers_boobjob6:
                    hide screen jane_lockers_boobjob6
                    
                    $ quick_menu = True
                    mc nudepleasure "\"Fuck... getting close...\""
                    
                    j nudepleasure2 "\"Hahh...Spray them. Spray my slutty tits.\""
                    
                    "The sound her tits make as they bounce up and down from my cock and her dirty talking pushed you over the edge..."
                    
                    scene lockersjanecummingbreasts1
                    with flash
                    scene lockersjanecummingbreasts1
                    with flash
                    scene lockersjanecummingbreasts1
                    with flash
                    
                    mc nudepleasure "\"Hahh, aah~\""
                    scene lockersjanecummingbreasts2
                    with dissolve
                    j nudepleasure1 "\"Spray me, baby. Yess~\""
                    
                    "Jane seems mesmerized from all the cum. Her expression is saying this is pure joy for her."
                    
                    scene lockersjanecummingbreasts3
                    with dissolve
                    
                    j nudepleasure1 "\"Mmm.\""
                    j nudeskeptical "\"Fuck, baby... I won't need a shower after this.\""
                    
                    scene black
                    with fadein
                    
                    "She cleans herself and you both sit back on the bench."
                    
                    scene lockersmcjanesitting
                    with fadein
                    
                    j nudetalk "\"I guess I drained you before the party has started, huh?\""
                    
                    mc nudetalk3 "\"Hahaha. I regenerate fast.\""
                    
                    j nudetalk2 "\"Oh, yeah? You ready for round two then?\""
                    
                    mc nudetalk2 "\"Wait, now?\""
                    
                    j nudetalk "\"I wish. I have to go and you will be late, so some other time we will continue where we left off.\""
                    
                    mc nudetalk "\"No complains here.\""
                    
                    j nudetalk2 "\"Go, go now, before I change my mind.\""
                    
                    "You both say goodbye to each other and part ways for now as you dress back up and leave for Andre's room."
                    scene mcchangingforshower
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(2, hard=True)
                    with dissolve
                    
                    jump andrecassroom
        "Say you're in a hurry":
            $ quick_menu = True
            scene lockersmcjanesitting
            with dissolve
            mc nudetalk2 "\"Sorry, Jane, but I am in a hurry actually. I was invited to Andre's room for some social gathering.\""
            j nudeyummy "\"Oh, yeah? I bet you two are going to fuck all the other women in there.\""
            mc nudetalk3 "\"Haha. We'll see. Actually I thought you'd be there too.\""
            j nudetalk2 "\"I wish I could come, but I need to take a shower and do a routine check on the ship. It will take quite some time.\""
            mc nudetalk3 "\"I see, keep us safe!\""
            j nudetalk "\"Hey! Don't even doubt me. I will keep this baby running as smoothly as it has so far.\""
            scene black
            with fadein
            "You chat for a little while longer and you both part ways. You dress back up and leave for Andre's room."
            
            scene mcchangingforshower
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(2, hard=True)
            with dissolve
            
            jump andrecassroom
            
            
#no look lockers
elif jane_shower_nolook:
    j nudetalk "\"Oh, [mc]? We ended up meeting in the showers anyway, this time only the two of us.\""
    mc nudetalk3 "\"Haha, yeah it seems so.\""
    j nudetalk2 "\"No Andre for you to worry about... sharing with.\""
    j nudeyummy "\"How about you come closer...\""
    
    $ quick_menu = False
    
    menu:
        "Come closer":
            $ quick_menu = True
            scene lockersmcmovescloser
            with dissolve
            "You say to yourself 'why the heck not' and move in closer to Jane."
            scene janelockersfondlesbreasts
            with dissolve
            j nudetalk "\"So, mister. What would it be? Blowjob or titty fuck?\""
            
            $ quick_menu = False
            
            menu:
                "Blowjob":
                    $ quick_menu = True
                    $ lockers_jane_tits = False
                    $ lockers_jane_blowjob = True
                    mc nudetalk3 "\"Your mouth, please.\""
                    j nudeyummy "\"My mouth, huh? You were dying to feel my mouth last time when Andre fucked my brains out?\""
                    mc nudetalk "\"Ahh...\""
                    scene janelockersbj00
                    with dissolve
                    j nudetalk2 "\"Already got you hard. This won't take long.\""
                    
                    $ quick_menu = False
                    show screen jane_lockers_blowjob5
                    $ renpy.show("jane_lockers_blowjob5")
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(12, hard=True)

                    label jane_lockers_blowjob5:
                    hide screen jane_lockers_blowjob5
                    
                    $ quick_menu = True
                    mc nudepleasure "\"Fuck... getting close...\""
                    
                    j nudeblow "\"*Buhh* Mmmh! Spray it *Gah* inside *Ghh* my mouth *Buh*\""
                    
                    "Her sloppy sounds while talking with your cock in her mouth is all you needed to push you over the edge..."
                    
                    scene janelockersbjcum1
                    with flash
                    scene janelockersbjcum1
                    with flash
                    scene janelockersbjcum1
                    with flash
                    
                    mc nudepleasure "\"Aaahh~\""
                    j nudepleasure1 "\"*Gulp* *Gulp* *Gulp*\""
                    
                    "Jane tries to swallow as much as she can, but your load is too much for her and she spills some out of her mouth."
                    
                    scene janelockersbjcum2
                    with flash
                    
                    j nudepleasure1 "\"*Slurp*\""
                    j nudeskeptical "\"Fuck, baby... you will drawn me in your cum.\""
                    
                    scene black
                    with fadein
                    
                    "She cleans herself and you both sit back on the bench."
                    
                    scene lockersmcjanesitting
                    with fadein
                    
                    j nudetalk "\"I guess I drained you before the party has started, huh?\""
                    
                    mc nudetalk3 "\"Hahaha. I regenerate fast.\""
                    
                    j nudetalk2 "\"Oh, yeah? You ready for round two then?\""
                    
                    mc nudetalk2 "\"Wait, now?\""
                    
                    j nudetalk "\"I wish. I have to go and you will be late, so some other time we will continue where we left off.\""
                    
                    mc nudetalk "\"No complains here.\""
                    
                    j nudetalk2 "\"Go, go now, before I change my mind.\""
                    
                    "You both say goodbye to each other and part ways for now as you dress back up and leave for Andre's room."
                    scene mcchangingforshower
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(2, hard=True)
                    with dissolve
                    
                    jump andrecassroom
                    
                    
                "Titty fuck":
                    $ quick_menu = True
                    $ lockers_jane_blowjob = False
                    $ lockers_jane_tits = True
                    mc nudetalk3 "\"Your breasts, please.\""
                    j nudeyummy "\"My tits, huh? You were dying to feel them last time when Andre fucked every inch of my body?\""
                    mc nudetalk "\"Ahh...\""
                    scene janelockersboobjob00
                    with dissolve
                    j nudetalk2 "\"Already got you hard. This won't take long.\""
                    
                    $ quick_menu = False
                    show screen jane_lockers_boobjob5
                    $ renpy.show("jane_lockers_boobjob5")
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(12, hard=True)

                    label jane_lockers_boobjob5:
                    hide screen jane_lockers_boobjob5
                    
                    $ quick_menu = True
                    mc nudepleasure "\"Fuck... getting close...\""
                    
                    j nudepleasure2 "\"Hahh...Spray them. Spray my slutty tits.\""
                    
                    "The sound her tits make as they bounce up and down from my cock and her dirty talking pushed you over the edge..."
                    
                    scene lockersjanecummingbreasts1
                    with flash
                    scene lockersjanecummingbreasts1
                    with flash
                    scene lockersjanecummingbreasts1
                    with flash
                    
                    mc nudepleasure "\"Hahh, aah~\""
                    scene lockersjanecummingbreasts2
                    with dissolve
                    j nudepleasure1 "\"Spray me, baby. Yess~\""
                    
                    "Jane seems mesmerized from all the cum. Her expression is saying this is pure joy for her."
                    
                    scene lockersjanecummingbreasts3
                    with dissolve
                    
                    j nudepleasure1 "\"Mmm.\""
                    j nudeskeptical "\"Fuck, baby... I won't need a shower after this.\""
                    
                    scene black
                    with fadein
                    
                    "She cleans herself and you both sit back on the bench."
                    
                    scene lockersmcjanesitting
                    with fadein
                    
                    j nudetalk "\"I guess I drained you before the party has started, huh?\""
                    
                    mc nudetalk3 "\"Hahaha. I regenerate fast.\""
                    
                    j nudetalk2 "\"Oh, yeah? You ready for round two then?\""
                    
                    mc nudetalk2 "\"Wait, now?\""
                    
                    j nudetalk "\"I wish. I have to go and you will be late, so some other time we will continue where we left off.\""
                    
                    mc nudetalk "\"No complains here.\""
                    
                    j nudetalk2 "\"Go, go now, before I change my mind.\""
                    
                    "You both say goodbye to each other and part ways for now as you dress back up and leave for Andre's room."
                    scene mcchangingforshower
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(2, hard=True)
                    with dissolve
                    
                    jump andrecassroom
        "Say you're in a hurry":
            $ quick_menu = True
            scene lockersmcjanesitting
            with dissolve
            mc nudetalk2 "\"Sorry, Jane, but I am in a hurry actually. I was invited to Andre's room for some social gathering.\""
            j nudeyummy "\"Oh, yeah? You accepted the invite from the man who fucked me instead of you? Interesting...\""
            mc nudetalk3 "\"Uhhh... Yeah, I guess...Actually I thought you'd be there too.\""
            j nudetalk2 "\"Sorry, haha. I am just teasing you. I wish I could come, but I need to take a shower and do a routine check on the ship. It will take quite some time.\""
            mc nudetalk3 "\"I see, keep us safe!\""
            j nudetalk "\"Hey! Don't even doubt me. I will keep this baby running as smoothly as it has so far.\""
            scene black
            with fadein
            "You chat for a little while longer and you both part ways. You dress back up and leave for Andre's room."
            
            scene mcchangingforshower
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(2, hard=True)
            with dissolve
            
            jump andrecassroom



elif jane_dinner:
    j nudetalk "\"Oh, [mc]? We ended up meeting in the showers anyway, this time only the two of us.\""
    mc nudetalk3 "\"Haha, yeah it seems so.\""
    j nudetalk2 "\"No Andre for you to worry about... sharing with.\""
    j nudeyummy "\"How about you come closer...\""
    
    $ quick_menu = False
    
    menu:
        "Come closer":
            $ quick_menu = True
            scene lockersmcmovescloser
            with dissolve
            "You say to yourself 'why the heck not' and move in closer to Jane."
            scene janelockersfondlesbreasts
            with dissolve
            j nudetalk "\"So, mister. What would it be? Blowjob or titty fuck?\""
            
            $ quick_menu = False
            
            menu:
                "Blowjob":
                    $ quick_menu = True
                    $ lockers_jane_tits = False
                    $ lockers_jane_blowjob = True
                    mc nudetalk3 "\"Your mouth, please.\""
                    j nudeyummy "\"My mouth, huh? You didn't get to my mouth last time, but now I will give you even more pleasure as a compensation.\""
                    mc nudetalk "\"Ahh...\""
                    scene janelockersbj00
                    with dissolve
                    j nudetalk2 "\"Already got you hard. Mmm...\""
                    
                    $ quick_menu = False
                    show screen jane_lockers_blowjob4
                    $ renpy.show("jane_lockers_blowjob4")
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(12, hard=True)

                    label jane_lockers_blowjob4:
                    hide screen jane_lockers_blowjob4
                    
                    $ quick_menu = True
                    mc nudepleasure "\"Fuck... getting close...\""
                    
                    j nudeblow "\"*Buhh* Mmmh! Spray it *Gah* inside *Ghh* my mouth *Buh*\""
                    
                    "Her sloppy sounds while talking with your cock in her mouth is all you needed to push you over the edge..."
                    
                    scene janelockersbjcum1
                    with flash
                    scene janelockersbjcum1
                    with flash
                    scene janelockersbjcum1
                    with flash
                    
                    mc nudepleasure "\"Aaahh~\""
                    j nudepleasure1 "\"*Gulp* *Gulp* *Gulp*\""
                    
                    "Jane tries to swallow as much as she can, but your load is too much for her and she spills some out of her mouth."
                    
                    scene janelockersbjcum2
                    with flash
                    
                    j nudepleasure1 "\"*Slurp*\""
                    j nudeskeptical "\"Fuck, baby... you will drawn me in your cum.\""
                    
                    scene black
                    with fadein
                    
                    "She cleans herself and you both sit back on the bench."
                    
                    scene lockersmcjanesitting
                    with fadein
                    
                    j nudetalk "\"I guess I drained you before the party has started, huh?\""
                    
                    mc nudetalk3 "\"Hahaha. I regenerate fast.\""
                    
                    j nudetalk2 "\"Oh, yeah? You ready for round two then?\""
                    
                    mc nudetalk2 "\"Wait, now?\""
                    
                    j nudetalk "\"I wish. I have to go and you will be late, so some other time we will continue where we left off.\""
                    
                    mc nudetalk "\"No complains here.\""
                    
                    j nudetalk2 "\"Go, go now, before I change my mind.\""
                    
                    "You both say goodbye to each other and part ways for now as you dress back up and leave for Andre's room."
                    scene mcchangingforshower
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(2, hard=True)
                    with dissolve
                    
                    jump andrecassroom
                    
                    
                "Titty fuck":
                    $ quick_menu = True
                    $ lockers_jane_blowjob = False
                    $ lockers_jane_tits = True
                    mc nudetalk3 "\"Your breasts, please.\""
                    j nudeyummy "\"My tits, huh? We didn't get to them last time, but now I will give you even more pleasure as a compensation.\""
                    mc nudetalk "\"Ahh...\""
                    scene janelockersboobjob00
                    with dissolve
                    j nudetalk2 "\"Already got you hard. Mmm...\""
                    
                    $ quick_menu = False
                    show screen jane_lockers_boobjob4
                    $ renpy.show("jane_lockers_boobjob4")
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(12, hard=True)

                    label jane_lockers_boobjob4:
                    hide screen jane_lockers_boobjob4
                    
                    $ quick_menu = True
                    mc nudepleasure "\"Fuck... getting close...\""
                    
                    j nudepleasure2 "\"Hahh...Spray them. Spray my slutty tits.\""
                    
                    "The sound her tits make as they bounce up and down from my cock and her dirty talking pushed you over the edge..."
                    
                    scene lockersjanecummingbreasts1
                    with flash
                    scene lockersjanecummingbreasts1
                    with flash
                    scene lockersjanecummingbreasts1
                    with flash
                    
                    mc nudepleasure "\"Hahh, aah~\""
                    scene lockersjanecummingbreasts2
                    with dissolve
                    j nudepleasure1 "\"Spray me, baby. Yess~\""
                    
                    "Jane seems mesmerized from all the cum. Her expression is saying this is pure joy for her."
                    
                    scene lockersjanecummingbreasts3
                    with dissolve
                    
                    j nudepleasure1 "\"Mmm.\""
                    j nudeskeptical "\"Fuck, baby... I won't need a shower after this.\""
                    
                    scene black
                    with fadein
                    
                    "She cleans herself and you both sit back on the bench."
                    
                    scene lockersmcjanesitting
                    with fadein
                    
                    j nudetalk "\"I guess I drained you before the party has started, huh?\""
                    
                    mc nudetalk3 "\"Hahaha. I regenerate fast.\""
                    
                    j nudetalk2 "\"Oh, yeah? You ready for round two then?\""
                    
                    mc nudetalk2 "\"Wait, now?\""
                    
                    j nudetalk "\"I wish. I have to go and you will be late, so some other time we will continue where we left off.\""
                    
                    mc nudetalk "\"No complains here.\""
                    
                    j nudetalk2 "\"Go, go now, before I change my mind.\""
                    
                    "You both say goodbye to each other and part ways for now as you dress back up and leave for Andre's room."
                    scene mcchangingforshower
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(2, hard=True)
                    with dissolve
                    
                    jump andrecassroom
                    
        "Say you're in a hurry":
            $ quick_menu = True
            scene lockersmcjanesitting
            with dissolve
            mc nudetalk2 "\"Sorry, Jane, but I am in a hurry actually. I was invited to Andre's room for some social gathering.\""
            j nudeyummy "\"Oh, yeah? Don't break too many hearts there.\""
            mc nudetalk3 "\"Haha. I will try not to. Actually I thought you'd be there too.\""
            j nudetalk2 "\"I wish I could come, but I need to take a shower and do a routine check on the ship. It will take quite some time.\""
            mc nudetalk3 "\"I see, keep us safe!\""
            j nudetalk "\"Hey! Don't even doubt me. I will keep this baby running as smoothly as it has so far.\""
            scene black
            with fadein
            "You chat for a little while longer and you both part ways. You dress back up and leave for Andre's room."
            
            scene mcchangingforshower
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(2, hard=True)
            with dissolve
            
            jump andrecassroom
    


#solo blowjob lockers
elif solo_jane_shower_face:
    j nudetalk "\"Oh, [mc]? We have a habbit of meeting in the showers now it seems.\""
    mc nudetalk "\"Hi, Jane. Shower meetings with you are never dull, so I am totally fine with that.\""
    j nudeyummy "\"Oh, yeah? Well, we can't have this one be dull either.\""
    j nudeyummy "\"Come closer...\""
    
    $ quick_menu = False
    
    menu:
        "Come closer":
            $ quick_menu = True
            scene lockersmcmovescloser
            with dissolve
            "You say to yourself 'why the heck not' and move in closer to Jane."
            scene janelockersfondlesbreasts
            with dissolve
            j nudetalk "\"So, mister. What would it be? Blowjob or titty fuck?\""
            $ quick_menu = False
            menu:
                "Blowjob":
                    $ quick_menu = True
                    $ lockers_jane_tits = False
                    $ lockers_jane_blowjob = True
                    mc nudetalk3 "\"Your mouth, please.\""
                    j nudeyummy "\"My mouth, huh? You really got a liking for my mouth it seems. I will make you feel what heaven is like again.\""
                    "Her nude body and her dirty language gets you hard in no time."
                    mc nudetalk "\"Ahh...\""
                    scene janelockersbj00
                    with dissolve
                    j nudetalk2 "\"Already got you hard. This won't take long.\""
                    
                    $ quick_menu = False
                    show screen jane_lockers_blowjob3
                    $ renpy.show("jane_lockers_blowjob3")
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(12, hard=True)

                    label jane_lockers_blowjob3:
                    hide screen jane_lockers_blowjob3
                    
                    $ quick_menu = True
                    mc nudepleasure "\"Fuck... getting close...\""
                    
                    j nudeblow "\"*Buhh* Mmmh! Spray it *Gah* inside *Ghh* my mouth *Buh*\""
                    
                    "Her sloppy sounds while talking with your cock in her mouth is all you needed to push you over the edge..."
                    
                    scene janelockersbjcum1
                    with flash
                    scene janelockersbjcum1
                    with flash
                    scene janelockersbjcum1
                    with flash
                    
                    mc nudepleasure "\"Aaahh~\""
                    j nudepleasure1 "\"*Gulp* *Gulp* *Gulp*\""
                    
                    "Jane tries to swallow as much as she can, but your load is too much for her and she spills some out of her mouth."
                    
                    scene janelockersbjcum2
                    with flash
                    
                    j nudepleasure1 "\"*Slurp*\""
                    j nudeskeptical "\"Fuck, baby... you will drawn me in your cum.\""
                    
                    scene black
                    with fadein
                    
                    "She cleans herself and you both sit back on the bench."
                    
                    scene lockersmcjanesitting
                    with fadein
                    
                    j nudetalk "\"I guess I drained you before the party has started, huh?\""
                    
                    mc nudetalk3 "\"Hahaha. I regenerate fast.\""
                    
                    j nudetalk2 "\"Oh, yeah? You ready for round two then?\""
                    
                    mc nudetalk2 "\"Wait, now?\""
                    
                    j nudetalk "\"I wish. I have to go and you will be late, so some other time we will continue where we left off.\""
                    
                    mc nudetalk "\"No complains here.\""
                    
                    j nudetalk2 "\"Go, go now, before I change my mind.\""
                    
                    "You both say goodbye to each other and part ways for now as you dress back up and leave for Andre's room."
                    scene mcchangingforshower
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(2, hard=True)
                    with dissolve
                    
                    jump andrecassroom
                    
                    
                "Titty fuck":
                    $ quick_menu = True
                    $ lockers_jane_blowjob = False
                    $ lockers_jane_tits = True
                    mc nudetalk3 "\"Your breasts, please.\""
                    j nudeyummy "\"My tits, huh? I see you're marking your territory on each part of my body.\""
                    "Her nude body and her dirty language gets you hard in no time."
                    mc nudetalk "\"Ahh...\""
                    scene janelockersboobjob00
                    with dissolve
                    j nudetalk2 "\"Already got you hard. This won't take long.\""
                    
                    $ quick_menu = False
                    show screen jane_lockers_boobjob3
                    $ renpy.show("jane_lockers_boobjob3")
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(12, hard=True)

                    label jane_lockers_boobjob3:
                    hide screen jane_lockers_boobjob3
                    
                    $ quick_menu = True
                    mc nudepleasure "\"Fuck... getting close...\""
                    
                    j nudepleasure2 "\"Hahh...Spray them. Spray my slutty tits.\""
                    
                    "The sound her tits make as they bounce up and down from my cock and her dirty talking pushed you over the edge..."
                    
                    scene lockersjanecummingbreasts1
                    with flash
                    scene lockersjanecummingbreasts1
                    with flash
                    scene lockersjanecummingbreasts1
                    with flash
                    
                    mc nudepleasure "\"Hahh, aah~\""
                    scene lockersjanecummingbreasts2
                    with dissolve
                    j nudepleasure1 "\"Spray me, baby. Yess~\""
                    
                    "Jane seems mesmerized from all the cum. Her expression is saying this is pure joy for her."
                    
                    scene lockersjanecummingbreasts3
                    with dissolve
                    
                    j nudepleasure1 "\"Mmm.\""
                    j nudeskeptical "\"Fuck, baby... I won't need a shower after this.\""
                    
                    scene black
                    with fadein
                    
                    "She cleans herself and you both sit back on the bench."
                    
                    scene lockersmcjanesitting
                    with fadein
                    
                    j nudetalk "\"I guess I drained you before the party has started, huh?\""
                    
                    mc nudetalk3 "\"Hahaha. I regenerate fast.\""
                    
                    j nudetalk2 "\"Oh, yeah? You ready for round two then?\""
                    
                    mc nudetalk2 "\"Wait, now?\""
                    
                    j nudetalk "\"I wish. I have to go and you will be late, so some other time we will continue where we left off.\""
                    
                    mc nudetalk "\"No complains here.\""
                    
                    j nudetalk2 "\"Go, go now, before I change my mind.\""
                    
                    "You both say goodbye to each other and part ways for now as you dress back up and leave for Andre's room."
                    scene mcchangingforshower
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(2, hard=True)
                    with dissolve
                    
                    jump andrecassroom
        "Say you're in a hurry":
            $ quick_menu = True
            scene lockersmcjanesitting
            with dissolve
            mc nudetalk2 "\"Sorry, Jane, but I am in a hurry actually. I was invited to Andre's room for some social gathering.\""
            j nudeyummy "\"Oh, yeah? I bet you are going to conquer all other women he has targeted and take them for yourself.\""
            mc nudetalk3 "\"Haha. We'll see. Actually I thought you'd be there too.\""
            j nudetalk2 "\"I wish I could come, but I need to take a shower and do a routine check on the ship. It will take quite some time.\""
            mc nudetalk3 "\"I see, keep us safe!\""
            j nudetalk "\"Hey! Don't even doubt me. I will keep this baby running as smoothly as it has so far.\""
            scene black
            with fadein
            "You chat for a little while longer and you both part ways. You dress back up and leave for Andre's room."
            
            scene mcchangingforshower
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(2, hard=True)
            with dissolve
            
            jump andrecassroom
    
#solo breasts lockers
elif solo_jane_shower_breasts:
    j nudetalk "\"Oh, [mc]? We have a habbit of meeting in the showers now it seems.\""
    mc nudetalk "\"Hi, Jane. Shower meetings with you are never dull, so I am totally fine with that.\""
    j nudeyummy "\"Oh, yeah? Well, we can't have this one be dull either.\""
    j nudeyummy "\"Come closer...\""
    
    $ quick_menu = False
    
    menu:
        "Come closer":
            $ quick_menu = True
            scene lockersmcmovescloser
            with dissolve
            "You say to yourself 'why the heck not' and move in closer to Jane."
            scene janelockersfondlesbreasts
            with dissolve
            j nudetalk "\"So, mister. What would it be? Blowjob or titty fuck?\""
            
            $ quick_menu = False
            
            menu:
                "Blowjob":
                    $ quick_menu = True
                    $ lockers_jane_tits = False
                    $ lockers_jane_blowjob = True
                    mc nudetalk3 "\"Your mouth, please.\""
                    j nudeyummy "\"My mouth, huh? Last time was my breasts. I see you like to explore each part of my body.\""
                    "Her nude body and her dirty language gets you hard in no time."
                    mc nudetalk "\"Ahh...\""
                    scene janelockersbj00
                    with dissolve
                    j nudetalk2 "\"Already got you hard. This won't take long.\""
                    
                    $ quick_menu = False
                    show screen jane_lockers_blowjob2
                    $ renpy.show("jane_lockers_blowjob2")
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(12, hard=True)

                    label jane_lockers_blowjob2:
                    hide screen jane_lockers_blowjob2
                    
                    $ quick_menu = True
                    mc nudepleasure "\"Fuck... getting close...\""
                    
                    j nudeblow "\"*Buhh* Mmmh! Spray it *Gah* inside *Ghh* my mouth *Buh*\""
                    
                    "Her sloppy sounds while talking with your cock in her mouth is all you needed to push you over the edge..."
                    
                    scene janelockersbjcum1
                    with flash
                    scene janelockersbjcum1
                    with flash
                    scene janelockersbjcum1
                    with flash
                    
                    mc nudepleasure "\"Aaahh~\""
                    j nudepleasure1 "\"*Gulp* *Gulp* *Gulp*\""
                    
                    "Jane tries to swallow as much as she can, but your load is too much for her and she spills some out of her mouth."
                    
                    scene janelockersbjcum2
                    with flash
                    
                    j nudepleasure1 "\"*Slurp*\""
                    j nudeskeptical "\"Fuck, baby... you will drawn me in your cum.\""
                    
                    scene black
                    with fadein
                    
                    "She cleans herself and you both sit back on the bench."
                    
                    scene lockersmcjanesitting
                    with fadein
                    
                    j nudetalk "\"I guess I drained you before the party has started, huh?\""
                    
                    mc nudetalk3 "\"Hahaha. I regenerate fast.\""
                    
                    j nudetalk2 "\"Oh, yeah? You ready for round two then?\""
                    
                    mc nudetalk2 "\"Wait, now?\""
                    
                    j nudetalk "\"I wish. I have to go and you will be late, so some other time we will continue where we left off.\""
                    
                    mc nudetalk "\"No complains here.\""
                    
                    j nudetalk2 "\"Go, go now, before I change my mind.\""
                    
                    "You both say goodbye to each other and part ways for now as you dress back up and leave for Andre's room."
                    scene mcchangingforshower
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(2, hard=True)
                    with dissolve
                    
                    jump andrecassroom
                    
                    
                "Titty fuck":
                    $ quick_menu = True
                    $ lockers_jane_blowjob = False
                    $ lockers_jane_tits = True
                    mc nudetalk3 "\"Your breasts, please.\""
                    j nudeyummy "\"My tits, huh? You really like my tits, huh?\""
                    "Her nude body and her dirty language gets you hard in no time."
                    mc nudetalk "\"Ahh...\""
                    scene janelockersboobjob00
                    with dissolve
                    j nudetalk2 "\"Already got you hard. This won't take long.\""
                    
                    $ quick_menu = False
                    show screen jane_lockers_boobjob2
                    $ renpy.show("jane_lockers_boobjob2")
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(12, hard=True)

                    label jane_lockers_boobjob2:
                    hide screen jane_lockers_boobjob2
                    
                    $ quick_menu = True
                    mc nudepleasure "\"Fuck... getting close...\""
                    
                    j nudepleasure2 "\"Hahh...Spray them. Spray my slutty tits.\""
                    
                    "The sound her tits make as they bounce up and down from my cock and her dirty talking pushed you over the edge..."
                    
                    scene lockersjanecummingbreasts1
                    with flash
                    scene lockersjanecummingbreasts1
                    with flash
                    scene lockersjanecummingbreasts1
                    with flash
                    
                    mc nudepleasure "\"Hahh, aah~\""
                    scene lockersjanecummingbreasts2
                    with dissolve
                    j nudepleasure1 "\"Spray me, baby. Yess~\""
                    
                    "Jane seems mesmerized from all the cum. Her expression is saying this is pure joy for her."
                    
                    scene lockersjanecummingbreasts3
                    with dissolve
                    
                    j nudepleasure1 "\"Mmm.\""
                    j nudeskeptical "\"Fuck, baby... I won't need a shower after this.\""
                    
                    scene black
                    with fadein
                    
                    "She cleans herself and you both sit back on the bench."
                    
                    scene lockersmcjanesitting
                    with fadein
                    
                    j nudetalk "\"I guess I drained you before the party has started, huh?\""
                    
                    mc nudetalk3 "\"Hahaha. I regenerate fast.\""
                    
                    j nudetalk2 "\"Oh, yeah? You ready for round two then?\""
                    
                    mc nudetalk2 "\"Wait, now?\""
                    
                    j nudetalk "\"I wish. I have to go and you will be late, so some other time we will continue where we left off.\""
                    
                    mc nudetalk "\"No complains here.\""
                    
                    j nudetalk2 "\"Go, go now, before I change my mind.\""
                    
                    "You both say goodbye to each other and part ways for now as you dress back up and leave for Andre's room."
                    scene mcchangingforshower
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(2, hard=True)
                    with dissolve
                    
                    jump andrecassroom
        "Say you're in a hurry":
            $ quick_menu = True
            scene lockersmcjanesitting
            with dissolve
            mc nudetalk2 "\"Sorry, Jane, but I am in a hurry actually. I was invited to Andre's room for some social gathering.\""
            j nudeyummy "\"Oh, yeah? I bet you are going to conquer all other women he has targeted and take them for yourself.\""
            mc nudetalk3 "\"Haha. We'll see. Actually I thought you'd be there too.\""
            j nudetalk2 "\"I wish I could come, but I need to take a shower and do a routine check on the ship. It will take quite some time.\""
            mc nudetalk3 "\"I see, keep us safe!\""
            j nudetalk "\"Hey! Don't even doubt me. I will keep this baby running as smoothly as it has so far.\""
            scene black
            with fadein
            "You chat for a little while longer and you both part ways. You dress back up and leave for Andre's room."
            
            scene mcchangingforshower
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(2, hard=True)
            with dissolve
            
            jump andrecassroom
    
#ntr lockers
elif ntr_jane_shower:
    j nudetalk "\"Oh, [mc]? We ended up meeting in the showers anyway, this time only the two of us.\""
    mc nudetalk3 "\"Haha, yeah it seems so.\""
    j nudetalk2 "\"No Andre for you to worry about... sharing with.\""
    j nudeyummy "\"How about you come closer...\""
    
    $ quick_menu = False
    
    menu:
        "Come closer":
            $ quick_menu = True
            scene lockersmcmovescloser
            with dissolve
            "You say to yourself 'why the heck not' and move in closer to Jane."
            scene janelockersfondlesbreasts
            with dissolve
            j nudetalk "\"So, mister. What would it be? Blowjob or titty fuck?\""
            
            $ quick_menu = False
            
            menu:
                "Blowjob":
                    $ quick_menu = True
                    $ lockers_jane_tits = False
                    $ lockers_jane_blowjob = True
                    mc nudetalk3 "\"Your mouth, please.\""
                    j nudeyummy "\"My mouth, huh? You were dying to feel my mouth last time when Andre fucked my brains out?\""
                    mc nudetalk "\"Ahh...\""
                    scene janelockersbj00
                    with dissolve
                    j nudetalk2 "\"Already got you hard. This won't take long.\""
                    
                    $ quick_menu = False
                    show screen jane_lockers_blowjob
                    $ renpy.show("jane_lockers_blowjob")
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(12, hard=True)

                    label jane_lockers_blowjob:
                    hide screen jane_lockers_blowjob
                    
                    $ quick_menu = True
                    mc nudepleasure "\"Fuck... getting close...\""
                    
                    j nudeblow "\"*Buhh* Mmmh! Spray it *Gah* inside *Ghh* my mouth *Buh*\""
                    
                    "Her sloppy sounds while talking with your cock in her mouth is all you needed to push you over the edge..."
                    
                    scene janelockersbjcum1
                    with flash
                    scene janelockersbjcum1
                    with flash
                    scene janelockersbjcum1
                    with flash
                    
                    mc nudepleasure "\"Aaahh~\""
                    j nudepleasure1 "\"*Gulp* *Gulp* *Gulp*\""
                    
                    "Jane tries to swallow as much as she can, but your load is too much for her and she spills some out of her mouth."
                    
                    scene janelockersbjcum2
                    with flash
                    
                    j nudepleasure1 "\"*Slurp*\""
                    j nudeskeptical "\"Fuck, baby... you will drawn me in your cum.\""
                    
                    scene black
                    with fadein
                    
                    "She cleans herself and you both sit back on the bench."
                    
                    scene lockersmcjanesitting
                    with fadein
                    
                    j nudetalk "\"I guess I drained you before the party has started, huh?\""
                    
                    mc nudetalk3 "\"Hahaha. I regenerate fast.\""
                    
                    j nudetalk2 "\"Oh, yeah? You ready for round two then?\""
                    
                    mc nudetalk2 "\"Wait, now?\""
                    
                    j nudetalk "\"I wish. I have to go and you will be late, so some other time we will continue where we left off.\""
                    
                    mc nudetalk "\"No complains here.\""
                    
                    j nudetalk2 "\"Go, go now, before I change my mind.\""
                    
                    "You both say goodbye to each other and part ways for now as you dress back up and leave for Andre's room."
                    scene mcchangingforshower
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(2, hard=True)
                    with dissolve
                    
                    jump andrecassroom
                    
                    
                "Titty fuck":
                    $ quick_menu = True
                    $ lockers_jane_blowjob = False
                    $ lockers_jane_tits = True
                    mc nudetalk3 "\"Your breasts, please.\""
                    j nudeyummy "\"My tits, huh? You were dying to feel them last time when Andre fucked every inch of my body?\""
                    mc nudetalk "\"Ahh...\""
                    scene janelockersboobjob00
                    with dissolve
                    j nudetalk2 "\"Already got you hard. This won't take long.\""
                    
                    $ quick_menu = False
                    show screen jane_lockers_boobjob
                    $ renpy.show("jane_lockers_boobjob")
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(12, hard=True)

                    label jane_lockers_boobjob:
                    hide screen jane_lockers_boobjob
                    
                    $ quick_menu = True
                    mc nudepleasure "\"Fuck... getting close...\""
                    
                    j nudepleasure2 "\"Hahh...Spray them. Spray my slutty tits.\""
                    
                    "The sound her tits make as they bounce up and down from my cock and her dirty talking pushed you over the edge..."
                    
                    scene lockersjanecummingbreasts1
                    with flash
                    scene lockersjanecummingbreasts1
                    with flash
                    scene lockersjanecummingbreasts1
                    with flash
                    
                    mc nudepleasure "\"Hahh, aah~\""
                    scene lockersjanecummingbreasts2
                    with dissolve
                    j nudepleasure1 "\"Spray me, baby. Yess~\""
                    
                    "Jane seems mesmerized from all the cum. Her expression is saying this is pure joy for her."
                    
                    scene lockersjanecummingbreasts3
                    with dissolve
                    
                    j nudepleasure1 "\"Mmm.\""
                    j nudeskeptical "\"Fuck, baby... I won't need a shower after this.\""
                    
                    scene black
                    with fadein
                    
                    "She cleans herself and you both sit back on the bench."
                    
                    scene lockersmcjanesitting
                    with fadein
                    
                    j nudetalk "\"I guess I drained you before the party has started, huh?\""
                    
                    mc nudetalk3 "\"Hahaha. I regenerate fast.\""
                    
                    j nudetalk2 "\"Oh, yeah? You ready for round two then?\""
                    
                    mc nudetalk2 "\"Wait, now?\""
                    
                    j nudetalk "\"I wish. I have to go and you will be late, so some other time we will continue where we left off.\""
                    
                    mc nudetalk "\"No complains here.\""
                    
                    j nudetalk2 "\"Go, go now, before I change my mind.\""
                    
                    "You both say goodbye to each other and part ways for now as you dress back up and leave for Andre's room."
                    scene mcchangingforshower
                    $ renpy.transition(Dissolve(1))
                    $ renpy.pause(2, hard=True)
                    with dissolve
                    
                    jump andrecassroom
        "Say you're in a hurry":
            $ quick_menu = True
            scene lockersmcjanesitting
            with dissolve
            mc nudetalk2 "\"Sorry, Jane, but I am in a hurry actually. I was invited to Andre's room for some social gathering.\""
            j nudeyummy "\"Oh, yeah? You accepted the invite from the man who fucked me instead of you? Interesting...\""
            mc nudetalk3 "\"Uhhh... Yeah, I guess...Actually I thought you'd be there too.\""
            j nudetalk2 "\"Sorry, haha. I am just teasing you. I wish I could come, but I need to take a shower and do a routine check on the ship. It will take quite some time.\""
            mc nudetalk3 "\"I see, keep us safe!\""
            j nudetalk "\"Hey! Don't even doubt me. I will keep this baby running as smoothly as it has so far.\""
            scene black
            with fadein
            "You chat for a little while longer and you both part ways. You dress back up and leave for Andre's room."
            
            scene mcchangingforshower
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(2, hard=True)
            with dissolve
            
            jump andrecassroom
            
label andrecassroom:
    
scene mcwalkingclosertoandreroom
with dissolve

mc thinking "This has to be it."

mc thinking "Let's see..."

scene andreroomsitting0
with dissolve

cass considering "\"Andre, you sure [mc] is coming?\""

v talk "\"It's been quite a while, maybe the guy is lost. We should send a search party.\""

scene zoeytabletfeet
with dissolve
z pleased "\"Hahaha. That would be fun.\""

v talk "\"We can split in teams of two, me and Zoey on the same team.\""

scene andreroomsitting0
with dissolve

d talk "\"Give him a break. He will be here. Also how will teams of two work when we are 5 people, smart ass?\""

v talk "\"Oh someone has the hots for [mc]!\""

d talk2 "\"Ugh, whatever, kid.\""

a shirttalk "\"He will be here, people, relax.\""

v talk "\"I say 5 more minutes and we all start having fun without him.\""

d talk "\"What's your definiton of fun anyway?\""

a shirttalk "\"Shh. The door is opening. This must be him.\""

scene mccominginandresroom
with dissolve

"The door opens and you walk through to spot everyone gathered around in a very pretty room with a double bed."

if mc_zoey_sex:
    scene zoeytabletfeetwink
    with dissolve
    "Zoey spots you and winks at you... I guess she won't forget what happened before so easily..."

else:
    scene zoeytabletfeet
    with dissolve
    "You spot Zoey with a tablet in her hand... This room has everything someone could want."
    
"Your eyes, however, glue on the one person of interest in the room -- your wife Cassandra."
$ quick_menu = False
scene cassandraportraitandreroom with fade:
    subpixel True
    yalign 1.0
    pause 2.0
    linear 7.0 yalign 0.0
pause
$ quick_menu = True
"She looks as beautiful as ever you think..."
"As you were lost in your thoughts you were abruptly brought back to reality..."

scene andrecloseupseeingmcenter
with dissolve

a shirttalk2 "\"[mc]! I knew you'd make it, man. Come on up.\""
"Andre gestures you to join them on the bed and you quickly go up."

scene mcclimbsbed
with dissolve

"You climb on the bed, but your eyesight doesn't leave Cassandra's face. She is so gorgeous you think to yourself..."

d talk "\"Nice for you to join us, [mc].\""

mc talk3 "\"Thank you, Dahlia. Sorry if I was late.\""

v talk "\"Just a tiny bit, dude, but no worries.\""

a shirttalk "\"Hey it's all good, [mc]. You said you might be late.\""

d talk2 "\"Pass me that shit, Andre.\""

mc talk2 "\"You guys already drinking?\""

a shirttalk2 "\"Yeah, it's quite strong, but the taste is divine.\""

"Cassandra seems to be staring back at you. You wonder if she could be remembering any of her feelings back towards you..."

scene everyonelookingatzoey
with dissolve

a shirttalk2 "\"Come on, Zoey. Did you just come to play on the tablet? Come join us.\""

v talk "\"Hey don't drink it all!\'"

d angry2 "\"Hmph.\""

z talk "\"Ahh, fine! But I will finish this level later.\""

scene zoeyperspective
with dissolve

a shirttalk2 "\"Sure you can finish it. I will even give you the tablet. I have better things to do than playing on it.\""

"Zoey jumps from the chair and quickly hops on the bed next to you."

z talk2 "\"What's better than playing games?\""

a shirttalk2 "\"One day you will find out.\""

a shirttalk "\"Aaanyway, now that we are all here...\""

scene zoeysitsonbed
with dissolve

a shirttalk2 "\"Why not play a casual game of truth or dare?\""

v talk "\"Oh I love that shit!\""

a shirttalk "\"Oh, yeah? Well, since I am the host it's only fair that I do the first truth or dare choice and this one is for you all...\"" 

a shirttalk2 "\"Only Zoey has her shoes off, so the rest of you take them off as well!\""

v talk "\"Huh? That's easy enough...\""

scene black
with fadein

"And so everyone removed their shoes as instructed."

scene victorpointsatbottle
with dissolve

v talk "\"Hey I was kidding when I said don't drink it all, but now I am afraid you actually might. Pass the bottle, Dahlia!\""

d talk2 "\"Little kids shouldn't drink alcohol, you know?\""

v talk "\"Hey!\""

a shirttalk "\"Hahaha, stop teasing him, Dahlia.\""

d talk "\"Alright, fine.\""

d talk2 "\"This is actually really strong stuff, Andre.\""

a shirttalk2 "\"Indeed it is. I have a few more bottles laying around. Only the world's finest on Paradise, right?\""

d talk "\"Riiight.\""

scene andretalkstoyou
with dissolve

a shirttalk "\"So, [mc]. Truth or Dare?\""
mc talk3 "\"What? Why am I going first?\""
a shirttalk2 "\"You arrived last, so you go first! It's only fair.\""
v talk "\"True,true!\""
mc talk2 "\"Fine... truth then.\""
a shirttalk2 "\"I will go easy on you.\""
a shirttalk "\"Okay we all know we have 3 amazingly beautiful girls here tonight, but which one is your personal favorite? And you don't have to answer, just look at her for a moment and that will enough.\""
mc thinking "That's not easy at all..."

$ quick_menu = False

menu:
    "Take a quick look at Cassandra":
        $ quick_menu = True
        $ looked_at_cass = True
        $ looked_at_zoey = False
        $ looked_at_dahlia = False
        scene cassupclose
        with dissolve
        "You take a really swift peek and almost nobody seem to have noticed who you looked at."
        jump andreroomafterlooking
        
    "Take a quick look at Dahlia":
        $ quick_menu = True
        $ looked_at_cass = False
        $ looked_at_zoey = False
        $ looked_at_dahlia = True
        scene dahliaupclose
        with dissolve
        "You take a really swift peek and almost nobody seem to have noticed who you looked at."
        jump andreroomafterlooking

    "Take a quick look at Zoey":
        $ quick_menu = True
        $ looked_at_cass = False
        $ looked_at_zoey = True
        $ looked_at_dahlia = False
        scene zoeyupclose
        with dissolve
        "You take a really swift peek and almost nobody seem to have noticed who you looked at."
        jump andreroomafterlooking

label andreroomafterlooking:
scene victordrinking
with fadein
v talk "\"Woah, what was that? I didn't even see.\""
d talk2 "\"Neither did I honestly. Must be the alcohol.\""
v talk "\"Cheater.\""
mc talk2 "\"Hey that's not my problem. I did look at someone. You just didn't pay good enough attention.\""
v talk "\"Bah, whatever. Here.\""
scene mclookingatbottle
with dissolve
"Victor passes you the bottle."
v talk "\"You will drink at least, right?\""

mc thinking "What should I do? Is it wise to willingly drink when a truth or dare game is going on?"

$ quick_menu = False

menu:
    "Drink":
        $ quick_menu = True
        $ andre_room_drunk = True
        scene mcdrinkingbottle
        with dissolve
        "You say fuck it and start chogging it like water."
        v talk "\"Nice. Leave some for Zoey too!\""
        scene mcpassingthebottle3
        with dissolve
        mc thinking "Is he...trying to get her drunk?"
        mc thinking "Anyway... I can't say anything in this situation. She will have to make the choice herself to drink or not."
        scene mcpassingthebottle
        with dissolve
        mc thinking "More than half the bottle is already gone... and this is some strong stuff..."
        "You pass the bottle to Zoey."
        jump afterandreroombottle
    "Pass it on":
        $ quick_menu = True
        $ andre_room_drunk = False
        mc talk3 "\"Hey thanks, but no thanks. I will skip for now.\""
        a shirttalk2 "\"I see what your next dare will be, [mc]! Hahaha. You won't stay sober tonight.\""
        mc thinking "He is probably right, but at least I will try not to help myself get wasted."
        scene mcpassingthebottle
        with dissolve
        "You pass the bottle towards Zoey hoping she refuses..."
        jump afterandreroombottle
        
label afterandreroombottle:
scene mcpassingthebottle4
with dissolve
"She didn't even hesitate and started drinking as well."

scene black
with fadein
"It didn't take long until the game of truth or dare went in full motion with more and more dares..."
scene zoeykissesvictor
with dissolve
"They got more and more sexual as time went by and as more alcohol was ingested."
if persistent.show_ntr:
    scene cassandrecloseup
    with fadein
    a shirttalk2 "\"What kind of easy dare is that? French kiss the most beautiful girl here?\""
    a shirttalk2 "\"Give me an actual challenge.\""
    scene cassandrecloseup2
    with dissolve
    cass yummy "\"Oh... For a moment there I thought you were going to choose someone else.\""
    a shirttalk "\"There is no one else when you are here, darling. You know that.\""
    scene cassandrecloseup3
    with flash
    cass talk "\"Mmmhh, mmmm~~\""
    cass yummy "\"*Slurp* Mmh~\""
    "They continue to kiss for what seems to be a good 3 minutes before they finally break."
    scene cassandrecloseup4
    with dissolve
    a shirttalk2 "\"Tastes like strawberries. I am one lucky son of a bitch.\""
    
scene black
with fadein
"Things got even more wild..."
scene dahliaflashes
with fadein
d talk2 "\"What? You want me to flash someone of my choosing my tits? That's embarrassing... but fine.\""
d talk "\"It's just tits... don't think about it too much....\""

scene dahliaflashes2
with dissolve
"Dahlia quickly turns towards you and drops her tits out for everyone to see, but she keeps her stare directly at you."
scene dahliaflashes3
with dissolve
d talk2 "\"Fuck that's embarrassing..."

scene black
with fadein
if andre_room_drunk:
    "As time went by I started to get very drunk and was barely holding up..."
    "The last thing I remember before fainting was..."
    jump andreroombeforefaint
else:
    "The game went from truth and dare to dare and dare... I was eventually dared to drink alcohol, but at least I was feeling a little bit better than the others."
    jump andreroomtipsy
    
label andreroombeforefaint:
scene zoeyfeetindahliasface1
with fadein
z happy "\"I told you I'd break you, Dahlia. There is no way in hell you--\""
scene zoeyfeetindahliasface2
with vpunch
d talk2 "\"You thought wrong.\""
z talk2 "\"Wait.. what are you doing? Stop it.\""
d talk "\"Stop what? I am actually going to enjoy this.\""
scene zoeyfeetindahliasface3
with dissolve
z talk "\"Whaa-- you seriousss?\""
d talk2 "\"Absolutely, baby.\""
d talk "\"Did you think something like this would get me out of the game?\""
z talk "\"I...\""
d talk2 "\"Quite the opposite actually.\""
scene zoeyfeetindahliasface6
with dissolve
"Dahlia starts slurping on a few of Zoey's toes one by one tasting it with her tongue..."
d talk "\"*Slurp* *Slurp* *Slurp*\""
d talk "\"Mmm.\""
scene zoeyfeetindahliasface4
with dissolve
"Then she puts all her toes all at once inside her mouth."
z pleasure "\"Eeeeeeeeeeee--\""
z pleasure "\"That tickles.\""
d talk2 "\"*Slurp* Mmmh *Slurp*\""
scene zoeyfeetindahliasface5
with dissolve
"Dahlia starts slurping on Zoey's toes even harder... saliva starting to form and drop beneath her mouth."
d talk "\"Sho...tash--ty... *slurp*\""
scene zoeypovdahlialicking
with dissolve
z flirting "\"Hey, hey okay! You win the dare. You can stop now...\""
z desire "\"Hahahah...stop it please!\""
scene zoeypovdahlialickingpassout1
with dissolve
d talk "\"...\""
scene zoeypovdahlialickingpassout2
with dissolve
z happy "\"...\""
scene zoeypovdahlialickingpassout3
with dissolve
z flirting "\"...\""

jump afterandreroomdrunk
label afterandreroomdrunk:
scene black
with fadein
"..."
"... ..."
"... ... ..."
scene mcwakesupdrunk
with vpunch
mc thinking "God... the headache..."

if persistent.show_ntr:
    $ andre_room_drunk_ntr = True
    mc thinking "My eyes are still blurry... what is happening?"
    scene andrefucksdahliacassblurred
    with dissolve
    "It takes you a few moments to focus your eyes enough to get a better visual..."
    scene andrefucksdahliacass
    with fadein
    a shirttalk "\"Don't fight girls, there is enough for both of you.\""
    a shirttalk2 "\"I will provide even for those who are unable to at the moment, hehehe.\""
    scene black
    with fadein
    "It doesn't take you long and you pass out again..."
    scene victorfuckszoeyblurred
    with fadein
    "Only to wake up to another image right before your eyes..."
    v talk "\"Fuck. You're so hot. I love you.\""
    z pleasure "\"Hnngh... Mmmmh...Hahh...\""
    scene victorfuckszoey
    with fadein
    z pleasure "\"Yessh... Hnn... Ahh...Mmm...\""
    "The image before your eyes doesn't make you feel better at all..."
    "You stand up to leave..."
    jump afterandreroom
else:
    mc thinking "I need to leave ..."
    "You stand up to leave..."
    jump afterandreroom

label andreroomtipsy:
scene zoeyfeetindahliasface1
with fadein
z happy "\"I told you I'd break you, Dahlia. There is no way in hell you--\""
scene zoeyfeetindahliasface2
with vpunch
d talk2 "\"You thought wrong.\""
z talk2 "\"Wait.. what are you doing? Stop it.\""
d talk "\"Stop what? I am actually going to enjoy this.\""
scene zoeyfeetindahliasface3
with dissolve
z talk "\"Whaa-- you seriousss?\""
d talk2 "\"Absolutely, baby.\""
d talk "\"Did you think something like this would get me out of the game?\""
z talk "\"I...\""
d talk2 "\"Quite the opposite actually.\""
scene zoeyfeetindahliasface6
with dissolve
"Dahlia starts slurping on a few of Zoey's toes one by one tasting it with her tongue..."
d talk "\"*Slurp* *Slurp* *Slurp*\""
d talk "\"Mmm.\""
scene zoeyfeetindahliasface4
with dissolve
"Then she puts all her toes all at once inside her mouth."
z pleasure "\"Eeeeeeeeeeee--\""
z pleasure "\"That tickles.\""
d talk2 "\"*Slurp* Mmmh *Slurp*\""
scene zoeyfeetindahliasface5
with dissolve
"Dahlia starts slurping on Zoey's toes even harder... saliva starting to form and drop beneath her mouth."
d talk "\"Sho...tash--ty... *slurp*\""
scene zoeypovdahlialicking
with dissolve
z flirting "\"Hey, hey okay! You win the dare. You can stop now...\""
z desire "\"Hahahah...stop it please!\""
scene black
with fadein


if looked_at_cass:
    with fasterfadein
    scene sometimelater
    $ quick_menu = False
    pause 2.5
    with fasterfadeout

    scene mcfuckscass0x
    with fasterfadein
    $ quick_menu = True
    a shirttalk2 "\"Come on, [mc]. Don't be shy. Only the three of us are awake right now.\""
    a shirttalk "\"I saw you looking at Cass earlier, don't lie. I might be drunk, but I still remember.\""
    a shirttalk2 "\"Come on. Fuck her. She wants it too.\""
    
    "You look around you and everyone except yourself Cass and Andre seem to be passed out..."
    "You feel tipsy, but you also see that look in Cassandra's eyes where you know she actually wants it..."
    
    $ quick_menu = False
    
    menu:
        "Fuck her":
            $ quick_menu = True
            $ andre_room_fucked_cass = True
            $ andre_room_fucked_zoey = False
            $ andre_room_fucked_dahlia = False
            mc thinking "Fuck it. She is my wife. I might as well enjoy this."
            scene mcfuckscass0
            with dissolve
            "You get on top of Cassandra and take your cock out of your zipper..."
            "It takes you a few moments to accurately penetrate her... but eventually you hit the motherload."
            
            $ quick_menu = False
            show screen andre_room_cass_fuck
            $ renpy.show("andre_room_cass_fuck")
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(12, hard=True)

            label andre_room_cass_fuck:
            hide screen andre_room_cass_fuck
            
            $ quick_menu = True
            
            mc pleasure "Fuck... getting close..."
            
            scene mccummingoncass
            with flash
            scene mccummingoncass
            with flash
            scene mccummingoncass
            with flash
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(1, hard=True)
            scene mccummingoncass2
            with dissolve
            "It doesn't take long for you to spray your wife's belly with hot jizz..."
            "You quickly say your goodbyes and leave before you pass out."
            jump afterandreroom
        
        
    

elif looked_at_zoey:
    with fasterfadein
    scene sometimelater
    $ quick_menu = False
    pause 2.5
    with fasterfadeout

    scene mcfuckszoey0
    with fasterfadein
    $ quick_menu = True
    
    a shirttalk "\"Come on, man. You can't lie to me.\""
    a shirttalk2 "\"I saw you looking at her earlier.\""
    a shirttalk "\"Wait... I got it!\""
    a shirttalk2 "\"Let me give you a hand...\""
    
    scene mcfuckszoey1
    with dissolve
    a shirttalk "\"Hey, Zoey? You still here with us?\""
    scene zoeylaying
    a shirttalk2 "\"Zooo~~ooo~~eee~y...\""
    z flirting "\"Hmmm...\""
    scene zoeylaying2
    with dissolve
    z desire "\"What's up?\""
    a shirttalk "\"Your last dare of the night!\""
    z happy "\"What's the *hic* dare?\""
    a shirttalk2 "\"Really simple...\""
    a shirttalk "\"...Get [mc] here to fuck you and you are the winner!\""
    z desire "\"That's too *hic* easy.\""
    z flirting "\"I know how to use my woman parts *hic*.\""
    scene mcfuckszoey3
    with fadein
    "Zoey quickly takes off her shorts and spread herself for you..."
    z happy "\"Well?\""
    $ quick_menu = False
    menu:
        "Fuck her":
            $ quick_menu = True
            $ andre_room_fucked_cass = False
            $ andre_room_fucked_zoey = True
            $ andre_room_fucked_dahlia = False
            scene andreroommcfuckszoey0
            with dissolve
            "She is way too inviting for you to decline..."
            $ quick_menu = False
            show screen andre_room_zoey_fuck
            $ renpy.show("andre_room_zoey_fuck")
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(12, hard=True)

            label andre_room_zoey_fuck:
            hide screen andre_room_zoey_fuck
            $ quick_menu = True
            
            mc pleasure "Fuck... almost there..."
            
            scene mccumminginsidezoey
            with flash
            scene mccumminginsidezoey
            with flash
            scene mccumminginsidezoey
            with flash
            "You couldn't hold it any longer and explode inside her..."
            scene black
            with fadein
            "You say your goodbyes with Zoey and Andre and quickly stumble out of the room."
            jump afterandreroom
            
    

else:
    with fasterfadein
    scene sometimelater
    $ quick_menu = False
    pause 2.5
    with fasterfadeout

    scene mcfucksdahlia0
    with fasterfadein
    $ quick_menu = True
    a shirttalk "\"I saw you staring at her earlier. Come on.\""
    a shirttalk2 "\"Look at how inviting she is. She also flashed you earlier.\""
    a shirttalk "\"You really going to pass on that?\""
    scene mcfucksdahlia1
    with dissolve
    a shirttalk2 "\"Come on, look at her...\""
    
    scene mcbeforefucingdahlia
    with dissolve
    
    a shirttalk "\"You would be missing out big time!\""
    
    $ quick_menu = False
    
    menu:
        "Fuck her mouth":
            $ quick_menu = True
            $ andre_room_fucked_cass = False
            $ andre_room_fucked_zoey = False
            $ andre_room_fucked_dahlia = True
            scene mcbeforefucingdahlia2
            with dissolve
            "You take off your pants and put your cock in front of her..."
            d talk2 "\"Mmm... is this for me?\""
            d talk "\"Well, don't mind if I do!\""
            
            $ quick_menu = False
            show screen dahlia_andre_room_blowjob
            $ renpy.show("dahlia_andre_room_blowjob")
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(12, hard=True)

            label dahlia_andre_room_blowjob:
            hide screen dahlia_andre_room_blowjob
            
            $ quick_menu = True
            mc pleasure "\"I'm about to...\""
            
            $ quick_menu = False
            
            menu:
                "Cum":
                    $ quick_menu = True
                    scene mcfuckingdahliasthroatcum
                    with flash
                    scene mcfuckingdahliasthroatcum
                    with flash
                    scene mcfuckingdahliasthroatcum
                    with flash
                    mc pleasure "\"Aaahh~\""
                    "Dahlia gulps whatever semen she can..."
                    scene black
                    with fadein
                    "You say your goodbyes and stumble out of the room..."
                    jump afterandreroom
        


label afterandreroom:
scene afterandreroom
with fadein
mc thinking "Fuck... I drank way too much..."

jump yourroomafterparty

jump endofch6
#---------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------------------


label endofch6:

with fadein
scene tobecontinued
$ quick_menu = False
$ renpy.pause(2.5, hard=True)
with fasterfadeout

scene black
with fasterfadein
$ quick_menu = True
$ mpause()
voidstar talk "\"Thank you so much for playing the current version (0.6) of Forgotten Paradise!\""
voidstar talk "\"This is all the time I had to develop the game, but make sure to check all the routes possible as there are quite a few ones in this version.\""
voidstar talk "\"If you'd like to support the game and follow the development, then please do that at my Patreon: https://www.patreon.com/Vo1dStar\""
voidstar talk "\"Even a single dollar helps. Thank you for believing in me and see you in the next version~!\""

jump thanks

#---------------------------------------------------------------------------------------------------------------------------------------------------