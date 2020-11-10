label startch11:
    scene twohundredyearslater
    with fadein
    $ renpy.pause(2, hard=True)

    scene black
    with fadein
    
    "..."
    qm empty "\"[mc]...\""
    "... ..."
    qm empty "\"We are waiting for you...\""
    "... ... ..."
    "\"Initializing pod opening sequence...\""
    scene ch11cryo1
    with fasterfadein
    "\"20 percent complete...\""
    "..."
    scene ch11cryo2
    with dissolve
    "\"60 percent complete...\""
    "..."
    scene ch11cryo3
    with dissolve
    "\"100 percent complete..\""
    scene ch11cryo4
    "\"Opening sequence complete...opening pod.\""
    mc nudetalk3 "\"*Gasp*\""
    "You take a deep breath before the pod opens up."
    scene ch11cryo5
    with dissolve
    r ttalk "\"Take it slow, [mc].\""
    "You hear a familiar voice..."
    r ttalk2 "\"How are you feeling?\""
    scene ch11cryo6
    with dissolve
    "You sit up."
    mc nudetalk2 "\"I feel like a shit...\""
    scene ch11cryo7
    with dissolve
    "You look at the floor and notice Ruby's feet..."
    "It may have been 200 years, but you remember she used to wear boots."
    mc nudethinking "Weird..."
    mc nudetalk3 "\"I assume everything is fine?\""
    r ttalk "\"I did as you instructed me, [mc].\""
    r ttalk2 "\"We have arrived at our destination.\""
    scene ch11cryo8
    with dissolve
    mc nudetalk "\"Really? That's great news, Ruby!\""
    mc nudetalk2 "\"There is no time to waste then. I must prepare and go down there.\""
    r ttalk "\"You are going down there?\""
    mc nudetalk "\"Of course. That is why I instructed you to wake me and only me, so that I make sure everything is okay for everyone else to come.\""
    mc nudetalk3 "\"We don't know if the natives are hostile or not, so we need to be careful.\""
    r ttalk2 "\"I understand. But what if something happens to you down there?\""
    mc nudetalk2 "\"Don't worry. I will be careful. It is the only way. And if something does happen to me you will wake up Jane and let her know.\""
    mc nudetalk "\"Now... I really need to take a shower.\""
    r ttalk "\"Of course, [mc].\""
    jump ch11showers1

    
    
label ch11showers1:
    scene ch11shower1
    with fasterfadein
    mc nudethinking "Ah, it feels so good to take a shower after so much time being stuck in there..."
    mc nudethinking "Ruby seems different...somehow."
    mc nudethinking "I can't really tell how however..."
    
    scene ch11shower2
    with dissolve
    "Your thoughts got interrupted when you hear the door to the showers open and hear footsteps approaching..."
    mc nudetalk "\"Huh? Ruby is that you?\""
    
    $ quick_menu = False
    scene ch11shower3 with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 7.0 yalign 0.0000001
    pause
    with dissolve
    $ quick_menu = True
    scene ch11shower4
    with fasterfadein
    
    mc nudetalk2 "\"What are you doing?\""
    
    r nudettalk "\"I thought you might need to release some stress after so many years.\""
    r nudettalk2 "\"Don't you think so?\""
    
    scene ch11shower5
    with dissolve
    
    r nudettalk "\"Hmmmm. It seems your friend down there agrees.\""
    mc nudetalk3 "\"Ruby, I...\""
    
    scene ch11shower6
    with vpunch
    
    r nudettalk2 "\"Shhh. Just put it in my pussy.\""
    r nudettalk "\"Come on. I know you need it.\""
    $ quick_menu = False
    menu:
        "Fuck her":
            $ quick_menu = True
            jump ch11showers2

label ch11showers2:
    scene ch11showers
    with flash
    mc nudethinking "She feels really different inside..."
    mc nudethinking "Feels very slimy and as if she is eating my dick up... wow..."
    
    $ quick_menu = False
    show screen ch11_ruby_fuck
    $ renpy.show("ch11_ruby_fuck")
    $ renpy.transition(Dissolve(1))
    $ renpy.pause(12, hard=True)

label ch11_ruby_fuck:
    hide screen ch11_ruby_fuck
    $ quick_menu = True
    r nudettalk2 "\"Ahh~ yess. Fuck me.\""
    r nudettalk "\"Fuck me faster and harder.\""
    
    $ quick_menu = False
    show screen ch11_ruby_fuck2
    $ renpy.show("ch11_ruby_fuck2")
    $ renpy.transition(Dissolve(1))
    $ renpy.pause(12, hard=True)

label ch11_ruby_fuck2:
    hide screen ch11_ruby_fuck2
    
    $ quick_menu = True
    mc nudepleasure "\"Fuck! It feels so good.\""
    r nudettalk "\"Mmm~ Yesssss~\""
    mc nudepleasure "I don't remember her moaning and doing stuff like this. But I am not complaining..."
    mc nudetalk2 "\"It feels way too good after such a long time...\""
    mc nudetalk "\"I am getting close...\""
    r nudettalk2 "\"Make sure you finish inside me!\""
    scene ch11showercum1
    with flash
    mc nudepleasure2 "\"Ahh!\""
    scene ch11showercum2
    with flash
    with flash
    with flash
    with flash
    scene ch11showercum3
    with flash
    mc nudepleasure "\"Ahhhh. So good.\""
    scene ch11shower7
    with dissolve
    "As semen starts dripping from Ruby's pussy she stands up."
    "You watch as she scoopes the semen back in her pussy instead of letting it drip..."
    mc nudethinking "Weird..."
    scene black
    with dissolve
    "You don't pay much attention and move to your room and dress up."
    jump ch11room1
    
label ch11room1:
    scene ch11room1
    with fasterfadein
    mc thinking "I feel refreshed enough... should I just prepare and go down or to check the ship before that?"
    $ quick_menu = False
    menu:
        "Explore the ship":
            $ quick_menu = True
            $ ch11_saved_ruby = True
            mc thinking "Ruby was acting a little strange..."
            mc thinking "I have to make sure everything is fine."
            scene ch11room2
            with fasterfadein
            "You leave and make your way down the hallway."
            jump ch11explore
        "Prepare and go down":
            $ quick_menu = True
            $ ch11_saved_ruby = False
            mc thinking "I am overthinking. Everything is fine. Let's prepare and go down."
            scene ch11room2
            with fasterfadein
            "You leave and make your way down the hallway."
            jump ch11leaving

label ch11explore:
    scene ch11cc1
    with fasterfadein
    "You go to the command center to check on the cameras throughout the ship."
    scene ch11cc2
    with dissolve
    mc thinking "Okay... let's see here..."
    $ quick_menu = False
    menu:
        "Check for damage":
            $ quick_menu = True
            mc thinking "No system damage or errors..."
    mc thinking "I should check the cameras."
    $ quick_menu = False
    menu:
        "Check cameras":
            $ quick_menu = True
            jump ch11cc1
            
label ch11cc1:
    scene ch11medcam
    with fasterfadein
    mc thinking "Everything seems fine here."
    scene ch11airlockcam
    with fasterfadein
    mc thinking "Next."
    scene ch11citadelcam
    with fasterfadein
    "You go through a few more until..."
    scene ch11engcam
    with vpunch
    mc shocked "What?"
    with vpunch
    
    scene ch11engcam2
    with vpunch
    "You zoom in."
    
    mc shocked "Wait what is this?!"
    mc shocked "Ruby?"
    
    scene ch11cc3
    with fasterfadein
    
    mc shocked "What happened? I just saw her a few minutes ago..."
    
    scene ch11cc4
    with dissolve
    
    mc thinking "Wait... does that mean..."
    
    scene ch11cc5
    with dissolve
    
    r ttalk "\"[mc]? Something wrong?\""
    "Shivers run down your spine as you hear that voice and look at the camera at the same time."
    mc shocked "Oh God..."
    
    scene ch11cc6
    with vpunch
    
    mc talk2 "\"You tell me, imposter.\""
    r ttalk2 "\"What could you possibly mean by that? It's me, Ruby.\""
    mc talk3 "\"Stop playing games. I saw the cameras.\""
    mc talk "\"What the hell have you done to Ruby?\""
    
    scene ch11cc7
    with dissolve
    
    r ttalk "\"So you found out. Pity. I really wanted to play along our little roleplaying game we had going there.\""
    r ttalk2 "\"I guess I have to show my real self now.\""
    
    scene ch11cc8
    with dissolve
    
    "As the fake Ruby says that she grabs her head as it starts pulsing and pulsing with bright light..."
    scene ch11cc8
    with vpunch
    scene ch11cc9
    with vpunch
    scene ch11cc8
    with vpunch
    scene ch11cc9
    with vpunch
    
    mc shocked "\"What the hell are you?!\""
    
    scene ch11cc10
    with dissolve
    $ renpy.pause(2, hard=True)
    scene ch11cc11
    with flash
    "From her head..."
    scene ch11cc12
    with flash
    "And her arms..."
    
    scene ch11cc13
    with flash
    "To her feet changing..."
    
    $ quick_menu = False
    scene ch11cc15 with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 8.0 yalign 0.0001
    pause
    with fasterfadein
    $ quick_menu = True
    
    "Until she has fully transformed."

    scene ch11cc14
    with fasterfadein
    
    "You just stand there in shock... but also a bit of fear, as a very tall alien stands in front of you on your own ship."
    
    mc talk2 "\"What the hell do you want?\""
    qm alientalk "\"What... I want...?\""
    mc thinking "That translation device is really coming in handy..."
    
    scene ch11cc16
    with vpunch
    "The tall alien begins to remove Ruby's dress from her body."
    qm alienntalk "\"I want to remove this from my body to begin with...\""
    qm alienntalk "\"I can't stand it.\""
    
    $ quick_menu = False
    scene ch11cc17 with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 8.0 yalign 0.00001
    pause
    $ quick_menu = True
    
    scene ch11cc18
    with fasterfadein
    
    qm alienntalk "\"That's much better... don't you think so?\""
    "She looks at you with her large pinkish eyes."
    
    scene ch11cc19
    with dissolve
    mc talk "\"I am fine with my clothes on, thank you very much.\""
    qm alienntalk "\"Hmm...\""
    qm alienntalk "\"How boring. I guess I just have to force you out of them then.\""
    
    scene ch11cc20
    with dissolve
    
    "You remember there is a gun placed under the desk."
    mc thinking "This could be my chance. I need to eliminate her..."
    mc thinking "Who knows what she can do."
    $ quick_menu = False
    menu:
        "Grab the gun":
            $ quick_menu = True
            jump ch11cc2
            
label ch11cc2:
        
        scene ch11cc21
        with vpunch
        "You pick up the gun and aim at her instantly fast."
        mc talk "\"I am sorry, but I don't take any chances with invaders on this ship.\""
        
        menu:
            "Shoot":
                jump ch11cc3
    
label ch11cc3:
    scene ch11cc22
    with vpunch
    "You fire a shot directly at her..."
    scene ch11cc23
    with vpunch
    "However, her body bends in an unnatural way... Being able to completely dodge your shot and pass through her."
    scene ch11cc24
    with dissolve
    mc shocked "\"N-No way!\""
    
    scene ch11cc25
    with vpunch
    "Before you can even react she claws your face really hard."
    mc shocked2 "\"Aaaghhh!\""
    
    scene ch11cc26
    with vpunch
    mc thinking "She is unhumanly strong... what the hell..."
    
    scene ch11cc27
    with dissolve
    "As you look forward you spot the gun which you just dropped next to the Alien's feet."
    qm alienntalk "\"[mc]?\""
    
    scene ch11cc42
    with dissolve
    qm alienntalk "\"Look at me [mc].\""
    mc talk "Fuck... it's so creepy that she knows my name and everything from Ruby."
    qm alienntalk "\"Look directly into my eyes, [mc].\""
    qm alienntalk "\"I promise, everything will be fine if you do that.\""
    $ quick_menu = False
    menu:
        "Look at her eyes as she demands":
            $ quick_menu = True
            jump ch11manipulationend
        "Go for the gun":
            $ quick_menu = True
            jump ch11goreend
        "Tackle her instead":
            $ quick_menu = True
            jump ch11killalien

label ch11manipulationend:
    scene ch11cc43
    with fasterfadein
    "You look directly at her eyes..."
    mc shocked "\"W-What the...\""
    scene ch11cc44
    with flash
    "Before you can even think about reverting your eyes away, it's already too late."
    qm alienntalk "\"That's it, my pet.\""
    qm alienntalk "\"Now worship your new Queen.\""
    
    scene ch11cc45
    with fasterfadein
    "Without saying a word you go down on your knees and start caressing her leg."
    "You grab her foot and feel her smooth alien skin on your hand."
    qm alienntalk "\"That's it, my pet.\""
    
    scene ch11cc46
    with dissolve
    "You begin to lick her toes one by one."
    "You don't feel disgusted."
    "In fact you feel very little outside of the pleasure you get from your new master letting you worship her."
    scene ch11cc47
    with dissolve
    "You lick through her feet savoring the taste."
    qm alienntalk "\"Good job~ my new pet. Now undress and lie down on the floor.\""
    qm alienntalk "\"You deserve a reward for being such a good boy.\""
    
    scene ch11cc48
    with flash
    "You don't hesitate at all and do as you are being told."
    "The tall Alien sits on your face and you start munhcing on her genitalia down below."
    "A very odd, but satisfying taste fills your mouth as her juices start to flow down."
    
    scene black
    with fasterfadein
    "Time passes and you remain a faithful servant to the unknown Alien that boarded your ship."
    "You feel pride to be selected as her personal toy and to be able to serve her every need."
    
    scene ch11cc49
    with fasterfadein
    "She keeps you close to her on a leash and you breed every day..."
    "You completely forget your goal to humanity or the other passengers on Paradise."
    "Your only goal in life becomes to please your new Queen."
    
    $ quick_menu = False
    scene ending 1
    with fadein
    $ quick_menu = False
    pause 1.5
    $ quick_menu = True
    voidstar talk "\"{size=+10}Congratulations{/size} on reaching one of the multiple endings the game has to offer!\""
    voidstar talk "\"Many thanks to my patrons and supporters throughout the 2 years of development. This game was made possible thanks to all of you.\""
    voidstar talk "\"Thanks to everyone who spread the word about the game and kept the community going! You all rock!\""
    voidstar talk "\"For more news and updates about future projects, follow me on my {a=https://www.patreon.com/VoidStar}{color=#FF6600}Patreon{/color}{/a}.\""
    
    jump thanks
     
    
label ch11goreend:
    mc talk "\"Like hell I will!\""
    scene ch11cc28
    with hpunch
    mc talk2 "\"I will end you right now!\""
    "You move to grab the weapon on the ground..."
    
    scene ch11cc29
    with flash
    qm alienntalk "\"Wrong choice.\""
    "And before you can even realize what was happening..."
    
    scene ch11cc30
    with flash
    "The Alien strikes through your hand cutting it clean in half."
    scene ch11cc30
    with vpunch
    with vpunch
    mc shocked "\"{size=+10}AAAAAAAAAAAAAAAAAAAAAGHHHH!!!{/size}\""
    with vpunch
    scene ch11cc31
    with vpunch
    "You fall to the ground, looking at the pool of blood left by your arm."
    mc shocked "\"Aghh.....\""
    
    scene ch11cc32
    with dissolve
    qm alienntalk "\"You had a choice and no matter what you chose, I would've been fine with it.\""
    qm alienntalk "\"Now, I will enjoy the moment of devouring every part of you...\""
    with vpunch
    
    scene ch11cc33
    with dissolve
    qm alienntalk "\"Let's remove these clothes...\""
    qm alienntalk "\"You won't be needing them anymore.\""
    with vpunch
    
    scene ch11cc34
    with vpunch
    mc nudeshocked2 "\"Fuck you!\""
    "You try and swing a punch at her with your left arm..."
    "Too slow and weak however... to affect her in time."
    qm alienntalk "\"You still struggle?\""
    qm alienntalk "\"If you don't stop I will cut off all your limbs.\""
    qm alienntalk "\"Let me enjoy this or you will die in a lot of pain.\""
    qm alienntalk "\"Now for your shaft here...\""
    "She places her hand on your cock and start stroking it"
    qm alienntalk "\"It will fill me up like it did earlier in the shower room.\""
    
    mc nudeshocked2 "\"{size=+10}Like hell I will get hard from you, you ugly bitch!{/size}\""
    
    scene ch11cc35
    with vpunch
    
    "You take a look at her and you shock yourself at what you are seeing..."
    
    mc nudeshocked "W-What the fuck is this!!!"
    mc nudeshocked2 "She has... teeth there... it's drooling..."
    mc nudeshocked "Oh my god!!!"
    
    scene ch11cc36
    with vpunch
    
    qm alienntalk "\"Ahhh~\""
    mc nudeshocked "\"No!!\""
    mc nudeshocked2 "Why am I getting hard...FUCK it hurts!"
    
    scene ch11cc38
    with flash
    "Your protests are in vain as you slide in and out of her..."
    "Her smoothness and her tightness makes you erect in no time."
    "She squeezes you and it doesn't take you long to cum at all."
    
    with flash
    
    with flash
    
    scene ch11cc39
    with flash
    with flash
    with flash
    "You cum in her... filling her with blood and semen at the same time."
    
    scene ch11cc37
    with flash
    qm alienntalk "\"{size=+10}Ahhhh~ I can feel you filling me up.{/size}\""
    qm alienntalk "\"You chose wisely not to struggle more.\""
    qm alienntalk "\"And now I shall reward you...\""
    
    scene ch11cc40
    with vpunch
    qm alienntalk "\"With a swift death!\""
    "You watch as she opens her mouth in an enourmous size... also growing her teeth sharper."
    
    scene ch11cc41
    with vpunch
    qm alienntalk "\"{size=+10}DIE!{/size}\""
    mc nudeshocked2 "\"{size=+10}AGHHHH!{/size}\""
    
    "She begins biting off your head... you feel the pain for the first few seconds until your vision fades away and you pass out from blood loss..."
    scene black
    with fadein
    "Your journey ends here... Only God knows what will await the remaining passengers of Paradise once the Alien has her way with them..."
    "One by one..."
    
    $ quick_menu = False
    scene gameover3
    with fasterfadein
    $ renpy.pause(5, hard=True)
    jump thanks
    
    
    
label ch11killalien:
    $ ch11_kill_alien = True
    scene ch11cc50
    with vpunch
    "Before thinking twice you charge forward head first and tackle her to the ground..."
    mc shocked "\"Like hell I am doing that!\""
    with vpunch
    
    scene ch11cc51
    with vpunch
    "It leaves you with enough time to grab the gun and aim straight at her again."
    qm alienntalk "\"Hey... let's talk about this.\""
    mc talk "\"There is nothing to talk about.\""
    mc talk2 "\"You should have never entered this ship or touched any of my friends!\""
    $ quick_menu = False
    menu:
        "Charge up your gun":
            jump ch11killalien2
            
label ch11killalien2:
    scene ch11cc52
    with dissolve
    $ quick_menu = True
    "You begin to charge a large amount of power in the gun."
    mc talk "\"Dodge this, bitch.\""
    qm alienntalk "\"Wait.... No!!!\""
    $ quick_menu = False
    menu:
        "Blow her head off":
            jump ch11killalien3
            
label ch11killalien3:
    scene ch11cc53
    with flash
    with vpunch
    $ quick_menu = True
    "You fire such a powerful shot that goes right through her fingers and absolutely deletes her head off."
    with vpunch
    "Purple blood flying everywhere..."
    scene ch11cc54
    with vpunch
    "As her still warm body falls on the cold floor, emotionless."
    mc talk "\"You messed with the wrong people.\""
    mc talk "I am in big shit now though..."
    mc thinking "I have to try and take care of Ruby..."
    jump ch11medbay
    
label ch11medbay:
    scene ch11medbay1
    with fasterfadein
    "You picked up Ruby and carried her to the medical room."
    mc talk "\"Please, Ruby. I need you.\""
    mc talk "\"Please... don't be gone forever.\""
    
    scene ch11medbay2
    with dissolve
    "You place her gently on the bed."
    mc thinking "I have to figure what is actually wrong with her... if I can somehow repair her..."
    mc thinking "There has to be some information somewhere... in some book."
    $ quick_menu = False
    menu:
        "Search how to repair Ruby":
            jump ch11medbay2
            
label ch11medbay2:
    scene black
    with fadein
    $ quick_menu = True
    "After a few hours of research through various books in both Melisa and Jane's personal belongings..."
    "You found a circuit that is replaceable at the back of Ruby's head. You checked and saw that it matched the damaged area."
    
    scene ch11medbay3
    with fasterfadein
    "You begin the repairs immediately..."
    "With lots of wishful thinking you finish in a few hours time..."
    
    scene ch11medbay4
    with dissolve
    mc talk "\"Come on, Ruby... I've done everything I can.\""
    mc talk2 "\"Please...\""
    "..."
    mc talk "\"I need you...\""
    
    scene ch11medbay5
    with dissolve
    "As you were about to give up all hope she opens her eyes."
    
    r nudettalk "\"[mc]...?\""
    
    with vpunch
    mc shocked "\"{size=+10}RUBY!{/size}\""
    
    scene ch11medbay6
    with vpunch
    
    mc talk3 "\"I thought I lost you for a moment...\""
    mc talk2 "\"I am really glad you woke up. I couldn't proceed with this mission without you.\""
    
    scene ch11medbay7
    with dissolve
    
    r nudettalk "\"I can't feel the presence of the Alien form, does that mean you disposed of her?\""
    mc talk "\"Yes. She is gone for good.\""
    r nudettalk2 "\"I am really sorry, Commander.\""
    r nudettalk "\"As soon as I learned of the Alien form that invaded our ship, I went straight to wake you up.\""
    r nudettalk2 "\"But before I could do that she knocked me out by pulling my circuit out.\""
    mc talk2 "\"You do not need to apologize for anything, Ruby.\""
    mc talk "\"It's dealt with.\""
    mc talk2 "\"Make sure everything is fine with you. I've bought you clean suit to wear... since that thing used yours.\""
    r nudettalk "\"Thank you, [mc].\""
    mc talk "\"Meet me at the airpod once you're ready. I need to leave as soon as possible.\""
    
    jump ch11leaving2
    
    
    
label ch11leaving:
    with fasterfadein
    scene afewhourslater
    $ quick_menu = False
    pause 2.5
    with fasterfadeout
    jump ch11leaving2

label ch11leaving2:
    scene ch11pod1
    $ quick_menu = True
    with fadein
    stop music fadeout 5.0
    
    play music "music/Quest for Glory.mp3" fadein 10.0
    "You meet with Ruby at the escape pod like instructed."
    mc talk "\"This is important, Ruby. I aim to land at a place with water, but also not that far away from land.\""
    mc talk2 "\"I need to scout the area and see if it's secure enough for me to signal you to wake everyone else up.\""
    mc talk "\"You MUST wait for my signal, okay?\""
    
    r ttalk "\"I understand, [mc].\""
    
    mc talk "\"Okay. I leave the activation and coordinates to you.\""
    
    scene ch11pod2
    with dissolve
    "Ruby proceeds to activate various things on the console..."
    "\"Coordinates set...\""
    "\"Latitude: -30.03681, Longitude: 112.94856, Distortion: 1.33\""
    "\"Automatic pilot set on...\""
    "\"Opening door...\""
    
    scene ch11pod3
    with vpunch
    "The door to your capsule opens."
    
    scene ch11pod4
    with dissolve
    
    r ttalk "\"It's all ready and prepared for you, [mc].\""
    r ttalk2 "\"Are you sure you want to do this?\""
    mc talk2 "\"I have no other choice. I can't risk anyone else.\""
    mc talk "\"Leave this to me. We can communicate and I will let you know once it's safe.\""
    mc talk2 "\"Watch my coordinates and what happens, Ruby. In case I can't communicate to you for some reason look for a signal of some sort.\""
    r ttalk "\"I understand, [mc]. Godspeed.\""
    $ quick_menu = False
    menu:
        "Enter the pod":
            jump ch11leaving3

label ch11leaving3:
    scene ch11pod5
    with fasterfadein
    $ quick_menu = True
    "You enter the pod."
    mc thinking "Okay, let's do this."
    scene ch11pod6
    with vpunch
    "The door behind you shuts tight."
    "\"Capsule door secure...\""
    "\"Leaving sequence started.\""
    "\"Countdown initiated.\""
    "\"9...8...7...6...5...4...\""
    "\"3...\""
    with vpunch
    "\"2...\""
    with vpunch
    "\"1...\""
    with vpunch
    "\"Lift off!\""
    scene ch11pod8
    with vpunch
    with vpunch
    with vpunch
    "\"Launch successful!\""
    "\"Destination set.\""
    "\"ETA 3 hours.\""
    jump ch11leaving4

label ch11leaving4:
    scene ch11pod9
    with dissolve
    mc thinking "It looks really comfy here I gotta say."
    mc thinking "Now everyone is counting on me."
    mc thinking "I must do this for all of us."
    mc thinking "For a better future."
    
    if ch11_saved_ruby:
        jump ch11leaving4x
    else:
        scene ch11cc55
        with fadein
        qm alientalk "\"Ahh... [mc]... I miss you already.\""
        qm alientalk "\"Our baby misses you.\""
        qm alientalk "\"It will grow lonely without it's dad around...\""
        qm alientalk "\"But we have enough entertainment around us to keep us busy...\""
        jump ch11leaving4x
    
    
    
label ch11leaving4x:
    scene black
    with fasterfadein
    "After an hour or so the capsule starts to shake and a blinking red light goes off inside."
    
    scene ch11pod13
    with vpunch
    
    "\"{size=+10}WARNING! Unstable gravitational pull.{/size}\""
    mc shocked "\"What the hell?!\""
    "\"{size=+10}WARNING! Mass system failure.{/size}\""
     
    "\"{size=+10}Expected coordinates malfunction. Emergency landing set to Latitude: 8.43169, Longitude: 40.76637, Distortion: 1.02{/size}\""
    
    mc shocked2 "\"Oh no. This is really bad.\""
    
    scene ch11pod10
    with vpunch
    "\"Parachute deployed.\""
    mc talk "\"That is good at least.\""
    
    scene ch11pod12
    with vpunch
    "\"{size=+10}Parachute malfunction! Error! *Beep* *Beep* *Beep*{/size}\""
    
    mc shocked "\"What th---\""
    
    with vpunch
    
    scene ch11pod14
    with vpunch
    
    mc shocked2 "\"{size=+10}AGHHH!{/size}\""
    with vpunch
    
    with vpunch
    
    scene ch11pod15
    with vpunch
    "\"{size=+10}WARNING!.... WARNING!...{/size}\""
    
    scene ch11pod11
    with fasterfadein
    qm miratalk "\"Are you seeing this?\""
    qm ingridtalk "\"I am.\""
    qm miratalk "\"What in the Goddess' name is this?\""
    qm ingridtalk "\"Whatever it might be, we need to investigate.\""
    qm ingridtalk "\"Go and investigate, Mira and report back.\""
    mira talk "\"Yes, Ingrid.\""
    
    scene ch11pod16
    with fasterfadein
    with vpunch
    "\"{size=+10}WARNING! CRITICAL FAILURE!{/size}\""
    "\"{size=+10}IMPACT IN 3...{/size}\""
    "\"{size=+10}2...{/size}\""
    "\"{size=+10}1...{/size}\""
    jump ch11leaving5

label ch11leaving5:
    scene ch11pod17
    with vpunch
    "The capsule hits the earth and even though it was softened by the parachute for the little time it was opened it still hit the ground hard."
    
    "..."
    
    scene ch11pod18
    with dissolve
    "\"Y----Y---You hav--e r-reached you--r d--d--estin--ation.\""
    "\"T-Thank you f-----or usin--g Para---dise Express.\""
    
        
    scene black
    with fadein
    
    qm aavatalk "\"[mc]...\""
    qm aavatalk2 "\"[mc].......\""
    
    scene ch11cryodream2
    with fasterfadein
    qm aavatalk "\"Come to me... [mc]...\""
    qm aavatalk2 "\"Come...\""
    if breed_with_alien_queen:
        scene ch11cryodream3
        with fasterfadein
        qm aavatalk2 "\"Come see our grown child, [mc].\""
        qm aavatalk "\"It's already so big... it pleases mommy very much.\""
        qm aavatalk2 "\"You can tell, can't you? Whose gens this baby has?\""
        qm aavatalk "\"That's right, [mc]... Deep inside you you know.\""
        scene ch11cryodream1
        with fasterfadein
        qm aavatalk2 "\"Come find me... we will be one big family again.\""
        qm aavatalk "\"Us and all of our children.\""
        jump ch11leaving6
    else:
        scene ch11cryodream3
        with fasterfadein
        qm aavatalk "\"I've had so many children. [mc].\""
        qm aavatalk2 "\"They are all eager to meet you and so am I.\""
        qm aavatalk "\"I've heard so much about you.\""
        scene ch11cryodream1
        with fasterfadein
        qm aavatalk "\"Come find me so you can experience what pleasure really is.\""
        qm aavatalk2 "\"And we can start one big family together...\""
        jump ch11leaving6
        
label ch11leaving6:
    scene ch11pod19
    with fasterfadein
    mira talk "\"Hello?\""
    mira talk "\"Anyone there!? Show yourself.\""
    
    scene ch11pod20
    with fasterfadein
    mira talk "\"Hey you? You alive?\""
    "..."
    "Soft breathing can be heard from [mc]'s nose."
    mira talk "He seems alive. Ingrid would want to question him."
    
    scene ch11pod21
    with dissolve
    mira talk "\"Come on, you're coming with me.\""
    mc sleep "..."
    jump ch11camp1
    
label ch11camp1:
    scene ch11camp1
    with fasterfadein
    
    mira talk "\"Hey, Ivy. Tell Ingrid I captured someone suspicious.\""
    ivy talk "\"Is it a spy? Does he have anything to do with Luna's disappearance!?\""
    mira talk "\"I don't know yet. He is unconscious. But I will get answers from him.\""
    
    scene ch11camp2
    with fasterfadein
    
    mira talk "\"Down you go.\""
    
    scene black
    with fadein
    "A couple of minutes later..."
    pause 2.0

    scene ch11camp3
    with vpunch
    mira talk "\"Wake up!\""
    mira talk "\"You slept enough.\""
    
    scene ch11camp4
    with vpunch
    mc nudetalk3 "\"...What??\""
    mc nudetalk2 "\"Where am I?\""
    mc nudetalk "\"I remember the malfunction and... I crashed down...\""
    mc nudetalk2 "\"You saved me?\""
    
    scene ch11camp5
    with dissolve
    mira talk "\"We will be asking the questions, not you.\""
    mira talk "\"You got that?\""
    
    mc nudetalk "\"Yes...\""
    
    mira talk "\"Now answer the questions:\""
    mira talk "\"Are you a spy?\""
    
    mc nudetalk2 "\"What? No.\""
    
    mira talk "\"Do you have anything to do with Luna's disappearance?\""
    
    mc nudetalk "\"No?! I don't even know who that is.\""
    
    mira talk "\"Who are your people? What is your story?\""
    
    mc nudetalk "\"That is a bit complicated to answer...And you wouldn't believe me anyway.\""
    
    mira talk "\"We have all night. Talk.\""
    
    scene ch11camp6
    with dissolve
    
    mc nudetalk2 "\"Well... it will sound crazy, but...\""
    mc nudetalk "\"Me and my family got elected for a space travel and we went to space in a ship called 'Paradise' from a different planet than this one... very far away...
    The planet got destroyed and we embarked on a journey to find a new home which took us 200 years to get here, we had to battle a lot of different obstacles along the way and had a lot of
    hardships.\""
    mc nudetalk2 "\"I decided to land on this planet alone since I don't want to jeopardize the lives of the few people that survived that apocalypse back at my home planet and my capsule malfunctioned and here I am.\""
    
    mira talk "\"...\""
    mc nudetalk2 "\"I know it sounds crazy, but it's the truth. I don't want any enemies here. I am looking for a home for my own people.\""
    mira talk "\"...\""
    scene ch11camp5
    with dissolve
    mira talk "\"Do you by any chance live in the woods?\""
    mc nudetalk3 "\"What? No. Why?\""
    mira talk "\"Perhaps you've eaten something which has messed up your brain too much.\""
    mc nudetalk2 "\"Well... I told you you wouldn't believe me.\""
    
    mira talk "\"I will be back.\""
    "With that the girl leaves the tent you're being held in."
    
    scene ch11camp8
    with dissolve
    mc nudetalk "What the fuck did I get myself into?!"
    mc nudetalk "What a mess..."
    
    scene ch11camp9
    with vpunch
    mc nudetalk "I can't move an inch."
    mc nudetalk "They really are barbarian women... I shouldn't even dare mess with them."
    
    scene ch11camp8
    with dissolve
    mc nudetalk3 "\"Ruby? Ruby! Can you hear me?!\""
    mc nudetalk2 "\"Hello?\""
    mc nudetalk3 "\"Ruby!\""
    
    scene ch11camp7
    with dissolve
    mc nudetalk "Damn. The communication device got messed up as well."
    mc nudetalk "This can't get any worse..."
    
    jump ch11camp2

label ch11camp2:
    scene ch11camp10
    with dissolve
    ivy talk "\"You might bullshit them, but you can't bullshit me.\""
    ivy talk "\"I will make you talk.\""
    ivy talk "\"One way or another.\""
    mc nudetalk2 "\"Listen... I am not lying!\""
    
    scene ch11camp11
    with vpunch
    ivy talk "\"Think carefully before you answer.\""
    ivy talk "\"You really don't want to find out how good I am with a knife.\""
    ivy talk "\"I will make a necklace out of your testicles.\""
    
    scene ch11camp12
    with vpunch
    ivy talk "\"Are you sure you don't want to change your story?\""
    mc nudeshocked "\"Please! I will tell you whatever you want... Just please...\""
    ivy talk "\"Hmph. Wrong answer.\""
    mc nudeshocked2 "\"{size=+10}NO!{/size}\""
    ingrid talk "\"{size=+10}Ivy!{/size}\""
    
    scene ch11camp13
    with vpunch
    
    ingrid talk "\"He won't be useful to us dead.\""
    ivy talk "\"He is just bullshitting us, Ingrid!\""
    ivy talk "\"Probably wasting our time so that he can cover his people further.\""
    ingrid talk "\"Either way. I will get the truth out of him tonight.\""
    
    scene ch11camp14
    with dissolve
    $ persistent.change = "New world"
    ingrid talk "\"First he will go through the Seventh Primal Torture.\""
    ingrid talk "\"And then we will proceed with the interrogation on his story further.\""
    ingrid talk "\"So you better buckle up because it will be a long, wild night.\""
    jump startch12
