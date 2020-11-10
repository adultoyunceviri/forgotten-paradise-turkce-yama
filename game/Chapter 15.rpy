label startch15:
    scene black
    with fasterfadein
    "A few days later..."
    eli talk "\"I've done everythin' in my power, [mc]...\""
    
    scene ch15 camp 1
    eli talk "\"It's all up to you now...\""
    eli talk "\"You have to fight.\""
    
    scene ch15 camp 2
    "..."
    "... ..."
    "... ... ..."
    scene ch15 camp 3
    with vpunch
    "You feel a sudden rush and open your eyes in shock."
    
    mc ctalk "\"Hahh...Hahh...Hahh...\""
    
    scene ch15 camp 4
    with dissolve
    mc ctalk2 "\"E..li?\""
    eli talk "\"Welcome back, [mc].\""
    eli talk "\"You had me worried there for a second.\""
    mc ctalk3 "\"So it worked?\""
    eli talk "\"Of course~! Who do you think I am?\""
    mc ctalk "\"But you... have to pay the price now...\""
    mc ctalk2 "\"I wish... you could stay here. You will be more than welcome.\""
    eli talk "\"'Tis fine. Besides... do you think I won't be spoiled by da Queen he'self? She be showering me with stuff.\""
    eli talk "\"I might even get a title. Be yo' superior and stuff.\""
    mc ctalk2 "\"Haha... That sounds nice.\""
    
    scene ch15 camp 5
    with fasterfadein
    eli talk "\"Listen, [mc]...\""
    eli talk "\"I have somethin' to tell ya.\""
    mc ctalk2 "\"What is it?\""
    eli talk "\"I had a vision.\""
    eli talk "\"In that vision, I saw your path going in different directions.\""
    eli talk "\"There was a portal on top of a mountain, which connects your old planet and this one.\""
    scene ch15 camp 6
    mc ctalk3 "\"What... like a wormhole?\""
    eli talk "\"Worm...hole?\""
    mc ctalk2 "\"It's like a tunnel...\""
    scene ch15 camp 5
    eli talk "\"Yes. Like a tunnel! Going through it you won't be able to influence you' choices as it has already happened.\""
    eli talk "\"Unless something unexpected happens to disturb that reality, you be havin' no free will.\""
    mc ctalk3 "\"Well, damn.\""
    eli talk "\"It's up to you. On da way there you will also be able to contact your crew on your ship.\""
    mc ctalk2 "\"What? Really?\""
    eli talk "\"Yes. That's what I saw.\""
    mc ctalk "\"That's great news!\""
    mc ctalk2 "\"I lost contact the moment I landed here. I hope everything is ok there.\""
    eli talk "\"That be all I can tell you. Your destiny is still in yo' hands.\""
    scene ch15 camp 6
    mc ctalk3 "\"Thank you, Eli. For everything...\""
    mc ctalk2 "\"Without you I wouldn't be alive now.\""
    scene ch15 camp 5
    eli talk "\"Don't mention it. 'Tis was a pleasure helping you.\""
    "Eli starts to leave."
    $ quick_menu = False
    menu:
        "Hug her":
            $ quick_menu = True
            scene ch15 camp 7
            with sshake
            "You embrace Elisande in a warm hug."
            mc ctalk "\"You come and visit, you hear?\""
            mc ctalk2 "\"You always have a place here.\""
            eli talk "\"Thank you, [mc]. I will be comin' to visit you, don't worry.\""
            scene black
            with fasterfadein
            "You let her go and watch as she leaves and rides off."
            scene ch15 camp 8
            with Dissolve(1)
            "You leave the house and make your way out."
            jump ch15camp1
            
        "Go outside":
            $ quick_menu = True
            scene ch15 camp 8
            "As Elisande leaves you make your way out of the house."
            jump ch15camp1
            
            
label ch15camp1:
    scene black
    with fasterfadein
    "Meanwhile..."
    
    scene ch15 cell 1
    dany talk "\"Open the cell!\""
    
    scene ch15 cell 2
    with vpunch
    "Aurora looks at Dany scared."
    dany talk "\"Don't worry. I am not here to hurt you or anything like that.\""
    scene ch15 cell 3
    dany talk "\"In fact, I am here to tell you that you are free.\""
    aur nudetalk "\"I am.... free?\""
    dany talk "\"Yes! You are.\""
    dany talk "\"I never intended to keep you prisoner. I needed to study you and your baby, but since you refused to cooperate...\""
    dany talk "\"Anyway... That's behind us now. And from today you are absolutely free.\""
    
    scene ch15 cell 4
    aur nudetalk "\"Baby...\""
    aur nudetalk "\"I WANT MY BABY!\""
    
    scene ch15 cell 5
    dany talk "\"Of course. Your baby will be waiting for you, alongside provisions and new clothes.\""
    
    dany talk "\"But before you go...I have a proposition for you.\""
    dany talk "\"You are free to go wherever you want, but I am offering you a house and shelter here in my kingdom.\""
    dany talk "\"The choice is up to you.\""
    
    scene ch15 cell 6
    aur nudetalk "Stay here with promise of free food and shelter..."
    aur nudetalk "Or travel and meet up with [mc]?"
    $ quick_menu = False
    
    menu:
        "Take your chances and stay here":
            $ quick_menu = True
            $ ch15_aurora_leave = False
            scene ch15 cell 7
            aur nudetalk "\"I have decided.\""
            aur nudetalk "\"...I will stay here.\""
            scene ch15 cell 5
            with sshake
            dany talk "\"Excellent! You will not regret it.\""
            jump ch15camp2
            
        "Go and find [mc]":
            $ quick_menu = True
            $ ch15_aurora_leave = True
            scene ch15 cell 7
            aur nudetalk "\"I have decided.\""
            aur nudetalk "\"I will take my chances out there.\""
            scene ch15 cell 5
            dany talk "\"That's fine. Let's go, I will lead you to your baby.\""
            jump ch15camp2
            
label ch15camp2:
    scene ch15 camp 9
    with fasterfadein
    "You leave the house and the first one to notice you is Ingrid."
    ingrid talk "\"[mc]?!\""
    ingrid talk "\"[mc]!\""
    
    scene ch15 camp 11
    ingrid talk "\"I am so glad you are back!\""
    mc ctalk2 "\"Hehe. I am glad to be back too.\""
    scene ch15 camp 10
    with sshake
    ingrid talk "\"LUNA! [mc] is awake!\""
    scene ch15 camp 11
    with dissolve
    ingrid talk "\"Sorry about that, but Luna told me she needed to talk with you as soon as you wake up.\""
    ingrid talk "\"I will catch up with you later, okay? I will let you talk with Luna.\""
    mc ctalk "\"Sure, Ingrid. Thanks!\""
    scene ch15 camp 12
    with fasterfadein
    "As Ingrid leaves, Ivy comes to talk with you."
    ivy talk "\"So...\""
    ivy talk "\"I owe you an apology.\""
    mc ctalk "\"There's no need for that, Ivy. I understand your concern.\""
    
    scene ch15 camp 13
    with sshake
    ivy talk "\"Please. Let me finish.\""
    ivy talk "\"You saved Luna and you were tortured over nothing. I was close to doing something terrible as well.\""
    ivy talk "\"I just want you to know that you have my full support to stay here, together wth your people.\""
    mc ctalk2 "\"Thank you, Ivy. I really appreciate that.\""
    
    scene ch15 camp 14
    ivy talk "\"And... I can also provide my 'services' as a thank you.\""
    ivy talk "\"I am sure you will be satisfied.\""
    ivy talk "\"Let me know later.\""
    "Before you can answer Luna interrupts your conversation."
    
    scene ch15 camp 15
    luna talk "\"Hey, [mc]! I am really glad to see you awake!\""
    luna talk "\"We have a lot to discuss.\""
    luna talk "\"Please, come inside.\""
    
    scene ch15 camp 16
    with pushleft
    
    "Luna gestures you to follow her."
    
    $ quick_menu = False
    scene ch15 camp 17 with fadein:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(3, hard=True)
    pause
    $ quick_menu = True
    "As you enter, you are greeted by Luna sitting on her chair."
    with dissolve
    scene ch15 camp 18
    with fasterfadein
    luna talk "\"I am really glad you were able to recover, [mc].\""
    luna talk "\"We need to have some serious discussion now.\""
    luna talk "\"You've already proven yourself more than once to be our ally.\""
    luna talk "\"You are more than welcome to stay here.\""
    luna talk "\"I am guessing you will want to contact your people and bring them here as well?\""
    mc ctalk "\"That's correct. I came alone for the solo purpose of making sure it's safe enough.\""
    luna talk "\"That's fine... but can we trust them? It took us a long time to make sure you are who you are.\""
    mc ctalk2 "\"There were a few problems... and some other stuff that happened. But I can say they can be trusted. And if not, I will be here to put things in order.\""
    mc ctalk3 "\"I've been with these people for... way too long now. And it's okay if you feel threatened by the unknown. I will just leave and we will find some other place to call home on this planet.\""
    luna talk "\"No. Trust goes both ways. I do trust you. That means if you trust them, they are welcome as well.\""
    mc ctalk "\"Thank you.\""
    luna talk "\"You will be leaving to contact them?\""
    mc ctalk "\"Yeah. First thing in the morning.\""
    
    scene ch15 camp 19
    luna talk "\"Good. So... As a reward for everything you've done for us...\""
    luna talk "\"You can pick a partner to keep you company tonight.\""
    luna talk "\"Every single girl you've met so far specializes in certain 'techniques'.\""
    luna talk "\"Mira can bring you great pleasure, and her back ASSets are quite something from what I heard.\""
    luna talk "\"It's no secret that Ingrid likes you and will give you great pleasure in bed.\""
    luna talk "\"Ivy is very good with her feet and tease.\""
    luna talk "\"Who would you like to be with?\""
    $ quick_menu = False
    
    menu:
        "You":
            $ quick_menu = True
            $ch15_luna_sex = True
            $ch15_mira_sex = False
            $ch15_ingrid_sex = False
            $ch15_invy_sex = False
            $ch15_nobody_sex = False
            
            scene ch15 camp 18
            mc ctalk "\"You.\""
            luna talk "\"Me?? I don't think I mentioned myself in that list.\""
            mc ctalk2 "\"Is that a no then?\""
            luna talk "\"Heh. It's a yes.\""
            jump ch15luna1
            
        "Mira":
            $ quick_menu = True
            $ch15_luna_sex = False
            $ch15_mira_sex = True
            $ch15_ingrid_sex = False
            $ch15_invy_sex = False
            $ch15_nobody_sex = False
            scene ch15 camp 18
            mc ctalk2 "\"I'd be interested in getting to know Mira a bit better...\""
            luna talk "\"Mira, hmm? Excellent choice.\""
            scene ch15 camp 20
            with fasterfadein
            "Luna gets up and opens the door."
            luna talk "\"I will call her now. Stay here.\""
            jump ch15mira1
            
        "Ingrid":
            $ quick_menu = True
            $ch15_luna_sex = False
            $ch15_mira_sex = False
            $ch15_ingrid_sex = True
            $ch15_invy_sex = False
            $ch15_nobody_sex = False
            scene ch15 camp 18
            mc ctalk2 "\"Ingrid is my choice...\""
            luna talk "\"Ingrid, hmm? Excellent choice.\""
            scene ch15 camp 20
            with fasterfadein
            "Luna gets up and opens the door."
            luna talk "\"I will call her now. Stay here.\""
            jump ch15ingrid1
            
        "Ivy":
            $ quick_menu = True
            $ch15_luna_sex = False
            $ch15_mira_sex = False
            $ch15_ingrid_sex = False
            $ch15_invy_sex = True
            $ch15_nobody_sex = False
            scene ch15 camp 18
            mc ctalk2 "\"I'd like to see what Ivy has to offer...\""
            luna talk "\"Ivy, hmm? Excellent choice.\""
            scene ch15 camp 20
            with fasterfadein
            "Luna gets up and opens the door."
            luna talk "\"I will call her now. Stay here.\""
            jump ch15ivy1
            
        "Nobody":
            $ quick_menu = True
            $ch15_luna_sex = False
            $ch15_mira_sex = False
            $ch15_ingrid_sex = False
            $ch15_invy_sex = False
            $ch15_nobody_sex = True
            scene ch15 camp 18
            mc ctalk2 "\"Actually I prefer to rest tonight. A long travel is ahead of me and I wish to rest as much as possible.\""
            luna talk "\"Ah. Of course... I will let you rest.\""
            scene ch15 camp 20
            with fasterfadein
            "Luna gets up."
            luna talk "\"Have a good rest, [mc]. And I hope everything goes smoothly tomorrow!\""
            jump ch15aftersex
            
            
            
            
label ch15luna1:
    scene ch15 camp 21
    "Luna gets up and goes to the door."
    luna talk "\"We'll need some privacy. Hehe.\""
    
    scene ch15 camp kiss 0
    with fasterfadein
    luna talk "\"Now, come here.\""
    "You and Luna start exchanging saliva from your french kisses..."
    
    #anim
    show screen ch15_luna_kiss
    $ quick_menu = False
    $ renpy.show("ch15_luna_kiss")
    $ renpy.pause(12, hard=True)
    
    label ch15_luna_kiss:
    $ quick_menu = True
    hide screen ch15_luna_kiss
    luna talk "\"Such a good *Mmmmhh* kisser.\""
    
    scene ch15 camp luna 2
    with sshake
    luna talk "\"Mmmmmhhh...\""
    luna talk "\"I can feel your hard rod through your pants~\""
    luna talk "\"Already this hard, are we?\""
    
    scene ch15 camp luna 1
    "Luna takes out your cock."
    
    luna talk "\"Mmm.\""
    luna talk "\"I can't wait any longer.\""
    luna talk "\"Put it in me.\""
    
    #anim
    show screen ch15_luna_sex
    with fasterfadein
    $ quick_menu = False
    $ renpy.show("ch15_luna_sex")
    $ renpy.pause(12, hard=True)
    
    label ch15_luna_sex:
    $ quick_menu = True
    hide screen ch15_luna_sex
    luna talk "\"Ahh~ yessss~~\""
    luna talk "\"Hnnnnnn~! Pound me like the bitch I am~!\""
    mc ctalk "\"Ahh... I am getting close...\""
    luna talk "\"Hahh.. Cum~! Cum in me~!\""
    
    $ quick_menu = False
    scene white
    with Dissolve(1)
    pause 1
    scene ch15 camp luna 3
    with Dissolve(1)
    scene white
    with Dissolve(1)
    pause 1
    scene ch15 camp luna 3
    with Dissolve(1)
    $ quick_menu = True
    
    mc ctalk2 "\"Hahh..Hahh....Ahh...\""
    
    scene ch15 camp luna 4
    with sshake
    "You take your cock out of her hole and cum starts leaking out."
    luna talk "\"Wow. You really messed me up down there.\""
    luna talk "\"Mmm...\""
    mc ctalk3 "\"Sorry. I might have overdone it.\""
    luna talk "\"It's fine, it's fine.\""
    luna talk "\"If we are lucky we might grow additional member in our camp~\""
    mc cthinking "Does she mean... a baby?"
    mc cthinking "I... wouldn't mind that."
    
    scene black
    with Dissolve(1)
    "You go to bed sometime later..."
    
    jump ch15aftersex
    
    
    
label ch15mira1:
    scene ch15 camp 22
    with dissolve
    "And just like that she leaves."
    
    scene ch15 camp 22
    with fadein
    "A few minutes later you hear the door open again."
    
    scene ch15 camp mira 1
    with dissolve
    mira talk "\"[mc]? I am glad you picked me~\""
    mira talk "\"Let's not lose any time. Come here~\""
    
    scene ch15 camp mira 2
    with sshake
    "As you get closer to Mira, she quickly takes your cock out."
    "She starts to gently stroke your dick."
    mira talk "\"Mmm, you're a big boy, I remember now.\""
    mira talk "\"I had quite the enjoyment 'torturing' you when we captured you.\""
    mira talk "\"But it wasn't much of a torture for you, was it?\""
    mira talk "\"Looked like you enjoyed it. You have quite the stamina.\""
    mira talk "\"But today you will worship me...\""
    
    scene ch15 camp mira 3
    mira talk "\"And more specifically -- my ass.\""
    "Mira bends down and tells you to help her undress..."
    "You happily oblige."
    
    scene ch15 camp mira 4
    with dissolve
    mira talk "\"Mmmhm... That's much better.\""
    mira talk "\"Now, be a good boy and clean my ass up~\""
    
    scene ch15 camp mira 5
    with dissolve
    "You happily oblige again and start eating her ass out."
    mc ctalk "\"Mmmhh... *Slurp*, *Succ*, *Kiss*\""
    mira talk "\"Ahhh... yesss... That's the spot~!\""
    mira talk "\"Put your tongue deep in there.\""
    mira talk "\"Lick everything clean~\""
    
    scene ch15 camp mira 6
    mira talk "\"Ahh, Ahh!! AHH~!\""
    mira talk "\"Yes, Yes! Don't stop.\""
    with sshake
    mira talk "\"Eat it!\""
    mira talk "\"Eat my sweaty ass!\""
    with sshake
    with sshake
    mira talk "\"I am almost there.\""
    mira talk "\"Ahh...\""
    
    $ quick_menu = False
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch15 camp mira 7
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch15 camp mira 7
    with Dissolve(1)
    
    $ quick_menu = True
    mira talk "\"Aghhhh!!\""
    "You feel her shake as she climax."
    mc ctalk "\"Now it's my turn.\""
    
    scene ch15 camp mira 8
    "As you say that you start grinding between her ass cheeks."
    "Feeling close to cumming yourself, you don't hold back and finish right on top of her ass."
    
    $ quick_menu = False
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch15 camp mira 9
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch15 camp mira 9
    with Dissolve(1)
    
    $ quick_menu = True
    
    "You cum and splash her back full of cum."
    mira talk "\"Ah. That was really nice, [mc].\""
    mira talk "\"I will go clean and leave you to rest.\""
    mc ctalk "\"Yeah, it was great. Thank you, Mira.\""
    
    scene black
    
    "You go to bed a bit later..."
    
    jump ch15aftersex
    
    
label ch15ingrid1:
    scene ch15 camp 22
    with dissolve
    "And just like that she leaves."
    
    scene ch15 camp ingrid 1
    with fadein
    "A few minutes later you hear the door open again."
    ingrid talk2 "\"[mc]~!\""
    ingrid talk2 "\"Luna said you asked for me to share a bed tonight...\""
    mc ctalk "\"Hehe. That's right.\""
    
    scene ch15 camp ingrid 2
    with fasterfadein
    ingrid talk2 "\"Let's not waste any time then.\""
    ingrid talk2 "\"Undress and prepare for me on the bed.\""
    mc ctalk2 "\"Yes, ma'am.\""
    
    scene ch15 camp ingrid 3
    with fasterfadein
    "You do as your told and lie naked on the sheets."
    ingrid talk3 "\"Mm. I wanted to do this with you for so long.\""
    
    scene ch15 camp ingrid 4
    with fasterfadein
    ingrid talk3 "\"You have no idea how horny I am right now.\""
    "She doesn't even need to say it. You can feel her wet pussy grinding against your dick."
    ingrid talk3 "\"Now, put it in me. Shove your hard cock in my dirty pussy!\""
    
    #anim
    show screen ch15_ingrid_sex
    $ quick_menu = False
    $ renpy.show("ch15_ingrid_sex")
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(12, hard=True)
    
    label ch15_ingrid_sex:
    $ quick_menu = True
    hide screen ch15_ingrid_sex
    ingrid talk3 "\"Hahhh... Hnnnn...\""
    mc nudetalk "\"I am about to... cum....Hahh...\""
    ingrid talk3 "\"Cum! Put a baby in me!\""
    
    "Hearing that puts you over the edge and you start cumming."
    
    $ quick_menu = False
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch15 camp ingrid 6
    with Dissolve(1)
    scene white
    
    with Dissolve(1)
    pause 1
    
    scene ch15 camp ingrid 6
    with Dissolve(1)
    
    $ quick_menu = True
    mc nudetalk "\"Hahh...Hahh...\""
    
    $ quick_menu = False
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch15 camp ingrid 7
    with Dissolve(1)
    $ quick_menu = True
    "You take your cock out of her messy pussy."
    ingrid talk3 "\"Hahh... I can feel your seed in me.\""
    ingrid talk3 "\"I will definitely get pregnant with that much semen in my fertile pussy.\""
    
    scene ch15 camp ingrid 8
    with fasterfadein
    ingrid talk3 "\"That was really nice.\""
    mc nudetalk2 "\"Yeah, it was.\""
    ingrid talk3 "\"I love you.\""
    "You didn't expect to hear that..."
    $ quick_menu = False
    
    menu:
        "Say you love her back":
            $ quick_menu = True
            mc nudetalk2 "\"I love you too, Ingrid.\""
            ingrid talk3 "\"I am so glad to hear you say that.\""
            ingrid talk3 "\"Once you get back we have to pick a name for our child.\""
            mc nudetalk2 "\"Yeah, for sure. Let's get some rest now.\""
            ingrid talk3 "\"Yeah.\""
            scene black
            with Dissolve(1)
            "Not long after you both fall asleep."
            
            jump ch15aftersex
        "Don't":
            $ quick_menu = True
            mc nudetalk3 "\"Let's get some rest.\""
            ingrid talk3 "\"Yeah...\""
            
            scene black
            with Dissolve(1)
            "Not long after you both fall asleep."
            
            jump ch15aftersex
            
    
    
    
    
label ch15ivy1:
    scene ch15 camp 22
    with dissolve
    "And just like that she leaves."
    
    scene ch15 camp ivy 1
    with fadein
    "A few minutes later you hear the door open again."
    
    ivy talk "\"Hehe. I knew you'd pick me.\""
    ivy talk "\"You picked the best girl for sure.\""
    ivy talk "\"Today I will let you get off from the fantasy of having me...\""
    ivy talk "\"I will tease you with my feet and you will cum in no time. Let's start, lie down on the floor.\""
    
    scene ch15 camp ivy 4
    with fasterfadein
    "You do as your told and Ivy follows and sits on top of your crotch, teasing your cock with her ass through your pants."
    ivy talk "\"There. That's what you wanted, right? My feet, in your face.\""
    
    scene ch15 camp ivy 2
    ivy talk "\"You like them?\""
    ivy talk "\"Looks like you're speechless.\""
    ivy talk "\"You have my permission to lick them clean~\""
    
    scene ch15 camp ivy 3
    mc ctalk "\"*Lick*,*Slurp*,*Kiss*\""
    
    ivy talk "\"Ahh. Yess. Clean them both.\""
    ivy talk "\"Suck each of my toes clean.\""
    
    scene ch15 camp ivy 4
    with sshake
    ivy talk "\"I can feel your dick trying to escape.\""
    ivy talk "\"Must be painful to be trapped there while my feet and ass are so close~\""
    ivy talk "\"Doesn't matter though, keep licking~\""
    
    scene ch15 camp ivy 5
    with sshake
    ivy talk "\"Mmm. Just like that, my good puppy.\""
    mc ctalk2 "\"*Slurp*, *Suck*\""
    
    $ quick_menu = False
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch15 camp ivy 6
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch15 camp ivy 6
    with Dissolve(1)
    
    $ quick_menu = True
    ivy talk "\"Oh... my... did you just??\""
    
    with sshake
    ivy talk "\"HAHAHA! You did.\""
    ivy talk "\"And quite a lot too. Are you trying to get me pregnant through my panties?\""
    
    scene ch15 camp ivy 7
    ivy talk "\"So naughty.\""
    ivy talk "\"But I should really clean up. I don't want to get pregnant like this, hahaha.\""
    ivy talk "\"Cya later, [mc].\""
    
    scene black
    with fasterfadein
    
    "Shortly after you decide to go to sleep."
    
    jump ch15aftersex
    
    
label ch15aftersex:
    if ch11_saved_ruby:
        jump ch15morning1
    else:
        with fasterfadein
        scene meanwhile
        $ quick_menu = False
        $ renpy.pause(2, hard=True)
        with fasterfadeout
        scene ch15 paradise 1
        with fadein
        $ quick_menu = True
        
        stop music fadeout 5.0
        play music "music/Ambient Thriller Motif.mp3" fadein 10.0
        "\"Coordinates set...\""
        "\"Latitude: Set, Longitude: Set, Distortion: Set\""
        "\"Automatic pilot set on...\""
        
        scene ch15 paradise 2
        with vpunch
        "\"Opening door...\""
        
        scene ch15 paradise 3
        ad thinking "Time to leave this cursed ship."
        ad thinking "Mother thinks she can keep me here like one of her other human slaves..."
        ad thinking "Trying to hide the truth about my father and where he is."
        
        scene ch15 paradise 4
        ad thinking2 "Well, that is not going to happen."
        ad thinking2 "I will go and find him myself."
        ad thinking2 "I already have a pretty good idea where to start looking."
        
        scene ch15 paradise 5
        with sshake
        "*Door opens*"
        ad thinking2 "What the..."
        
        scene ch15 paradise 6
        with vpunch
        qm alientalk "\"[ad]!? Where do you think you are going?!\""
        qm alientalk "\"Did you think I wouldn't find out? Me? Your own mother?\""
        
        scene ch15 paradise 7
        with sshake
        ad talk2 "\"I am leaving, Mother!\""
        ad talk2 "\"You can do whatever the hell you plan on doing on this ship, but without me.\""
        ad talk2 "\"I am going to find father.\""
        
        scene ch15 paradise 8
        with vpunch
        qm alientalk "\"You are not going anywhere without my permission!\""
        qm alientalk "\"You will do exactly as you are told! You hear me?\""
        
        scene ch15 paradise 9
        with sshake
        qm alientalk "\"This is your final warning. Next time you will be severely punished.\""
        qm alientalk "\"AM I CLEAR?!\""
        
        scene ch15 paradise 10
        with vpunch
        "With a swift turn, [ad] stabs her mother through her heart."
        ad talk2 "\"Yes, mother.\""
        ad talk2 "\"Crystal clear.\""
        
        scene ch15 paradise 11
        with sshake
        "Purple blood starts spilling everywhere."
        qm alientalk "\"Y-You...\""
        
        scene ch15 paradise 12
        with sshake
        qm alientalk "\"Why...\""
        ad talk2 "\"It's time for you to rest, Mother.\""
        
        scene ch15 paradise 13
        with vpunch
        ad talk2 "\"You were too lost in your own fantasy here.\""
        ad talk2 "\"And I don't want to be dragged down with you...\""
        ad talk2 "\"It's your own fault this happened.\""
        
        scene ch15 paradise 14
        with fasterfadein
        ad thinking2 "Wait for me, Father..."
        
        scene ch15 paradise 15
        ad thinking2 "I am on my way."
        
        scene black
        with Dissolve(1)
        pause 1
        stop music fadeout 5.0
        play music "music/Eastern Thought.mp3" fadein 10.0
        
        jump ch15morning1
        
label ch15morning1:
    scene ch15 camp 23
    with Dissolve(1)

    "The next morning comes and you prepare to leave for your journey to the mountains."
    "Mira opens the gate for you."
    
    scene ch15 camp 24
    mira talk "\"Safe journey, [mc]! We will be expecting your return!\""
    mc ctalk2 "\"Thank you, Mira!\""
    
    scene black
    with Dissolve(1)
    pause 1
    if ch11_saved_ruby:
        jump ch15mountain1
    else:
        stop music fadeout 5.0
        play music "music/Ambient Thriller Motif.mp3" fadein 10.0
        "Meanwhile on Paradise..."
        "Lexa found the corpse of the Alien Mother dead on the floor..."
        "After seeing [ad] had left, she quickly went to wake everyone and release the prisoners."
        "She found Ruby's body lying on the floor and her first thought was getting an expert on the case and the only reasonable choice was Jane."

        scene ch15 paradise 16
        with Dissolve(1)
        l aangry "\"Jane, quickly I need your help. It's an emergency!\""
        j nudetalk "\"Whoa, hold on a second.\""
        j nudetalk2 "\"What happened?\""
        l aangry "\"I will explain on the way. We have no time to lose, [mc] might be in danger.\""
        j nudetalk "\"O-Okay. Lead the way.\""

        scene black
        with Dissolve(1)
        "Lexa explains the situation in detail to Jane as they make their way to Ruby's body..."

        scene ch15 paradise 17
        with Dissolve(1)
        "..."
        l atalk "\"Is it bad?\""
        j nudetalk2 "\"Well... Hard to say, but I think I will be able to fix her up.\""
        l atalk "\"We need to be quick though! [mc] is in danger!\""
        j nudetalk "\"I know you care about [mc] a lot, but you need to let me work.\""
        l atalk "\"Right... I will give you space.\""
        j nudetalk2 "\"Thank you.\""

        scene black
        with Dissolve(1)
        pause 1

        scene ch15 arrival 1
        with Dissolve(1)

        stop music fadeout 5.0
        play music "music/Eastern Thought.mp3" fadein 10.0

        eli thinking "Ugh... always be hatin' to gather my stuff when I move."
        eli thinking "At least I won't be needin' to move again."
        eli thinking "Da Queen really enjoyed my company hmm... Hehe. I guess I don't need to use my magic charm all da time."

        "Elisande hears a loud sound from a distant engine..."

        scene ch15 arrival 3
        eli thinking "What in the Goddess' name is this now?"
        eli thinking "A meteorite?"
        
        $ quick_menu = False
        scene ch15 arrival 4
        with sshake
        $ renpy.pause(1, hard=True)
        with sshake

        scene ch15 arrival 5
        with vpunch
        $ renpy.pause(1, hard=True)

        scene ch15 arrival 6
        with sshake
        $ renpy.pause(2, hard=True)

        scene ch15 arrival 7
        with fasterfadein

        stop music fadeout 5.0
        play music "music/Ambient Thriller Motif.mp3" fadein 10.0
        
        $ quick_menu = True
        ad thinking2 "A little bit of a bumpy ride..."
        ad thinking2 "But I made it in one piece."

        scene ch15 arrival 8
        with fasterfadein
        $ renpy.pause(1, hard=True)

        scene ch15 arrival 9
        with sshake
        "[ad] jumps and starts swimming towards the shore."

        $ quick_menu = False
        scene ch15 arrival 10 with fade:
            subpixel True
            yalign 1.0
            linear 7.0 yalign 0.0000001
        $ renpy.pause(3, hard=True)
        pause
        with dissolve
        $ quick_menu = True

        scene ch15 arrival 11
        with dissolve
        ad thinking3 "Time to do some interrogation..."
        "[ad] starts moving towards Elisande."

        scene ch15 arrival 12
        with fasterfadein
        eli talk "\"Hey, ya' okay? Were you da one that crashed?\""
        ad talk3 "\"Shut up, bitch. I will ask the questions.\""

        scene ch15 arrival 13
        with sshake
        "[ad] pulls out her knife."
        eli talk "\"Take it easy...\""
        eli talk "\"What do ya want?\""

        ad talk3 "\"I know someone visited you recently.\""
        eli talk "\"I get many visitors.\""
        ad talk3 "\"[mc] is his name.\""

        scene ch15 arrival 14
        eli thinking "[mc]?? Is this be his...."
        eli thinking "She doesn't look very friendly..."
        eli thinking "What should I do..."
        $ quick_menu = False
        
        menu:
            "Try and distract her to buy [mc] some time":
                $ quick_menu = True
                $ch15_ad_distract = True
                eli thinking "I should be buyin' him as much time as possible."
                scene ch15 arrival 15
                eli talk "\"Come. Sit down. We have much do discuss.\""
                eli talk "\"I am sure you be curious about this world. I can tell you off the bat that the mask you be wearin' is no longer needed.\""
                stop music fadeout 5.0
                play music "music/Eastern Thought.mp3" fadein 10.0
                scene black
                with Dissolve(1)
                pause 1
                jump ch15mountain1
            "Tell her the truth and [mc]'s location":
                $ quick_menu = True
                $ch15_ad_distract = False
                eli thinking "I don't think she be fallin' for my bullshit."
                scene ch15 arrival 15
                eli talk "\"Come, then. I will tell you what you want to know.\""
                stop music fadeout 5.0
                play music "music/Eastern Thought.mp3" fadein 10.0
                scene black
                with Dissolve(1)
                pause 1
                jump ch15mountain1
            
label ch15mountain1:
    scene ch15 mountain 1
    "A few hours later you finally reached the designated spot where Elisande told you to go."
    "You stop to catch your breath before trying to see if the communication signal works."
    
    scene ch15 mountain 2
    with dissolve
    mc ctalk2 "\"This [mc]. Do you copy, Ruby?\""
    mc ctalk2 "\"I repeat, this is [mc]! Do you copy?\""
    "..."
    "... ..."
    "... ... ..."
    scene ch15 mountain 3
    with vpunch
    mc ctalk3 "\"Fuck! I can't reach them...\""
    "..."
    r ttalk "\"[mc]...I copy.\""
    
    scene ch15 mountain 5
    with vpunch
    mc ctalk2 "\"YES!\""
    mc ctalk "\"You can hear me, Ruby?!\""
    
    scene ch15 mountain 2
    r ttalk2 "\"Loud and clear.\""
    mc ctalk2 "\"You have no idea how glad I am to hear that.\""
    
    if ch11_saved_ruby:
        r ttalk2 "\"I was starting to get worried something happened to you.\""
        mc ctalk "\"A lot of stuff happened, but that's a long story.\""
        mc ctalk2 "\"I am glad I finally reached you. I can tell you I found good people that will take us in.\""
        r ttalk "\"That's great to hear, Commander.\""
        mc ctalk3 "\"Do you still have the coordiinates of my capsule landing location?\""
        r ttalk2 "\"I believe so, yes.\""
        mc ctalk "\"Great. I want you to tell Jane to land the ship near there.\""
        mc ctalk2 "\"Once you start getting close to the ground you will spot the camp. It's not that far off. Land near.\""
        r ttalk "\"Copy that.\""
        mc ctalk "\"Well, that's it, I guess. I will see you sometime tomorrow!\""
        r ttalk2 "\"Understood. Ruby out.\""
        
        scene ch15 mountain 5
        mc cthinking "Fuck! I am so happy I managed to contact them!"
        mc cthinking "Now, I gotta check that 'portal' Elisande mentioned. It's on my way as well."
        jump ch15portal1
    else:
        mc ctalk "\"Everything okay?\""
        r ttalk "\"No. Not really, Commander.\""
        r ttalk2 "\"A lot happened here while you were gone.\""
        mc ctalk2 "\"What happened? Is everyone okay?\""
        
        scene black
        with Dissolve(1)
        "Ruby fills you in on what happened."
        scene ch15 mountain 2
        with Dissolve(1)
        mc ctalk2 "\"This is insane... How did I miss that...and she is my daughter...?\""
        r ttalk "\"We are safe now, but she is headed your way. Be cautious.\""
        mc ctalk "\"Thank you, Ruby. I will be.\""
        mc ctalk2 "\"I will deal with her, but you should start heading this way as well.\""
        mc ctalk "\"Do you still have the coordiinates of my capsule landing location?\""
        r ttalk "\"Yes.\""
        mc ctalk2 "\"Great. I want you to tell Jane to land the ship near there.\""
        mc ctalk2 "\"Once you start getting close to the ground you will spot the camp. It's not that far off. Land near.\""
        r ttalk "\"Copy that.\""
        mc ctalk "\"Well, that's it, I guess. I will see you sometime tomorrow!\""
        r ttalk2 "\"Understood. Ruby out.\""
        scene ch15 mountain 3
        mc cthinking "Fuck! I am so happy I managed to contact them!"
        mc cthinking "But I can't believe all of that happened.\""
        mc cthinking "Now, I gotta check that 'portal' Elisande mentioned. It's on my way as well."
        jump ch15portal1
        
label ch15portal1:
    scene black
    with Dissolve(1)
    "A few hours later you finally reach the top."
    scene ch15 portal 1
    with Dissolve(1)
    mc cthinking "The sun has started to go down. Not good.\""
    $ quick_menu = False
    
    menu:
        "Look ahead":
            jump ch15portal2
            
label ch15portal2:
    scene ch15 portal 2
    $ quick_menu = True
    "You look ahead and see a very large structure."
    mc cthinking "This has to be what Elisande was talking about."
    
    scene ch15 portal 4
    with fasterfadein
    "You move in to inspect it closer."
    mc cthinking "But... it doesn't seem active."
    $ quick_menu = False
    
    menu:
        "Try to touch it":
            jump ch15portal3
            
label ch15portal3:
    scene ch15 portal 5 
    $ quick_menu = True
    "You try and feel the portal..."
    scene ch15 portal 6
    with dissolve
    "But as your hand gets closer it starts to materialize into something..."
    
    $ quick_menu = False
    scene ch15 portal 7 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(3, hard=True)
    pause
    with dissolve
    $ quick_menu = True
    
    scene ch15 portal 8
    with dissolve
    "You scratch your head as the portal opens up in front of you."
    mc cthinking "What do I make of this now?"
    mc cthinking "Elisande said it will only open to me. It's connected to Earth, before all of this happenned..."

    if ch11_saved_ruby:
        mc cthinking "That would mean if I walk through now I will be back there! Like none of this happened!"
        mc cthinking "Like it was all just a bad dream."
        mc cthinking "Can I make this commitment though? I don't know what awaits me on the other side..."
        mc cthinking "Elisande also mentioned that everything that happened will happen as it's meant to, no matter what."
        mc cthinking "But she also said there is a way to break the cycle and my choice is valid..."
        mc cthinking "Something is pulling me towards that portal, but my intuition is telling me to stay here."
        $ quick_menu = False
        
        menu:
            "Go through the portal":
                $ quick_menu = True
                $ch15_enter_portal = True
                scene ch15 portal 9
                mc cthinking "Screw it."
                scene ch15 portal 10
                with sshake
                "As you begin to move through, you notice your hands disappear..."
                scene ch15 portal 11
                with sshake
                "And slowly the rest of your body too..."
                scene ch15 portal 12
                "Until you are gone completely."
                scene ch15 portal 13
                with fasterfadein
                "The portal entrance dematerializes the moment you enter through..."
                jump ch15end1
                
            "Leave":
                $ quick_menu = True
                $ch15_enter_portal = False
                scene ch15 portal 3
                with fasterfadein
                mc cthinking "No. This is not my destiny."
                mc cthinking "I have people who rely on me. I have to go back."
                jump ch15end2
                
    else:
        "As you are about to make a choice you hear something behind you..."
        if ch15_ad_distract:
            stop music fadeout 5.0
            play music "music/Ambient Thriller Motif.mp3" fadein 10.0
            scene ch15 portal 14
            with sshake
            "Approaching footsteps getting closer..."
            
            scene ch15 portal 15
            "With a sudden stop, you turn around..."
            mc ctalk2 "\"Who goes there?\""
            
            scene ch15 portal 16
            with sshake
            
            mc ctalk "\"Y-You are...\""
            
            scene ch15 portal 17
            ad talk "\"I am [ad].\""
            ad talk "\"Your daughter.\""
            scene ch15 portal 16
            with sshake
            mc ctalk2 "\"My... daughter.\""
            scene ch15 portal 17
            ad talk "\"You probably didn't know I existed.\""
            ad talk "\"Mother kept it a secret.\""
            ad talk "\"But she is gone now.\""
            ad talk "\"I came here to find you!\""
            
            scene ch15 portal 18
            with sshake
            "You move your hand closer to her cheeks."
            
            scene ch15 portal 19
            with dissolve
            ad talk "\"Hnnnnn...\""
            
            scene ch15 portal 20
            mc ctalk "\"How did you find me?\""
            ad talk "\"Well... I followed your path.\""
            ad talk "\"Your ship has pretty good system to track down people here, you know?\""
            
            scene ch15 portal 21
            ad talk "\"I saw you visited that woman near the sea.\""
            mc cthinking "Elisande?"
            scene ch15 portal 22
            with sshake
            ad talk "\"She wasn't being very cooperative...\""
            scene ch15 portal 23
            with sshake
            ad talk "\"So she left me no choice...\""
            scene ch15 portal 24
            with sshake
            "[ad] starts taking something out of the bag."
            
            scene ch15 portal 25
            with sshake
            ad talk "\"I had to get the truth out of her and punish her for trying to keep me away from you.\""
            
            scene ch15 portal 26
            with sshake
            ad talk "\"And I did.\""
            
            scene ch15 portal 27
            with vpunch
            ad talk "\"She got what she deserved.\""
            
            scene ch15 portal 28
            with vpunch
            mc cunhappy "\"N-NO! WHAT DID YOU DO?!\""
            mc cunhappy "\"Y-You killed her...\""
            mc cunhappy "\"You murdered my friend...\""
            
            scene ch15 portal 29
            ad talk "\"I...I thought this would please you.\""
            ad talk "\"I... I am sorry.\""
            
            scene ch15 portal 30
            with vpunch
            mc cunhappy "\"'SORRY'?!\""
            mc cunhappy "\"I can't believe this!\""
            scene ch15 portal 31
            with sshake
            mc cthinking "This is too much for me to deal with..."
            mc cthinking "What do I do now..."
            mc cthinking "I have two options..."
            mc cthinking "Either go through the portal with her or..."
            mc cthinking "Or do what is necessary..."
            mc cthinking "There is no third option... I can't go back with her to my people."
            mc cthinking "They will never accept her. Not after what she has done."
            $ quick_menu = False
            menu:
                "Trick her and kill her":
                    $ quick_menu = True
                    scene ch15 portal 32
                    mc ctalk3 "\"We need to bury her. She doesn't deserve this.\""
                    scene ch15 portal 41
                    with fasterfadein
                    mc ctalk2 "\"The only way is for us to go through this portal together.\""
                    mc ctalk "\"There is nothing for us back here.\""
                    scene ch15 portal 42
                    ad talk "\"Oh? This is so interesting.\""
                    ad talk "\"The world is so mysterious.\""
                    
                    scene ch15 portal 43
                    ad talk "\"I am excited to travel through with you, Father.\""
                    scene ch15 portal 44
                    ad talk "\"What about you, Father? Are you exci--\""
                    scene ch15 portal 45
                    with sshake
                    ad talk "\"Hey!! What is this?\""
                    ad talk "\"What are you doing?!\""
                    mc ctalk3 "\"I am sorry. It has to be done...\""
                    
                    scene ch15 portal 46
                    with vpunch
                    mc ctalk2 "\"AAAAAAA~!\""
                    ad talk "\"Aghhh!\""
                    
                    scene ch15 portal 47
                    with sshake
                    ad talk "\"AAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHH!!!!!\""
                    
                    scene ch15 portal 48
                    with dissolve
                    "It takes only a few moments for her screams to fade away."
                    
                    scene ch15 portal 8
                    with fasterfadein
                    "After some time you try and gather your thoughts and figure out what to do next..."
                    
                    mc cthinking "If I walk through this portal I will be back there on Earth! Like none of this happened!"
                    mc cthinking "Elisande will be alive. [ad] won't be born and I won't have to think of what I have done..."
                    mc cthinking "Like it was just a bad dream."
                    mc cthinking "Can I make this commitment though? I don't know what awaits me on the other side..."
                    mc cthinking "Elisande also mentioned that everything that happened will happen as it's meant to, no matter what."
                    mc cthinking "But she also said there is a way to break the cycle and my choice is valid..."
                    mc cthinking "Something is pulling me towards that portal, but my intuition is telling me to stay here."
                    $ quick_menu = False
                    menu:
                        "Go through the portal":
                            $ch15_enter_portal = True
                            $ quick_menu = True
                            scene ch15 portal 9
                            mc cthinking "Screw it."
                            scene ch15 portal 10
                            with sshake
                            "As you begin to move through, you notice your hands disappear..."
                            scene ch15 portal 11
                            with sshake
                            "And slowly the rest of your body too..."
                            scene ch15 portal 12
                            "Until you are gone completely."
                            scene ch15 portal 13
                            with fasterfadein
                            "The portal entrance dematerializes the moment you enter through..."
                            jump ch15end1
                            
                        "Leave":
                            $ch15_enter_portal = False
                            $ quick_menu = True
                            scene ch15 portal 3
                            with fasterfadein
                            mc cthinking "No. This is not my destiny."
                            mc cthinking "I still have people who rely on me. I have to go back."
                            jump ch15end2
                            
                            
                "Go through the portal with her":
                    $ quick_menu = True
                    mc cthinking "I have decided. She is still my daughter. My flesh and blood."
                    mc cthinking "She might be naive, because no one taught her otherwise. I will be the parent she needs. That way this doesn't ever happen again."
                    scene ch15 portal 32
                    mc ctalk3 "\"We need to bury her. She doesn't deserve this.\""
                    
                    scene ch15 portal 41
                    with fasterfadein
                    mc ctalk "\"This is what we have to do now...\""
                    mc ctalk2 "\"This is a portal to another world, a world where we can both live together.\""
                    mc ctalk "\"We have nothing left for us here, so this is our only option.\""
                    
                    scene ch15 portal 33
                    with dissolve
                    ad talk "\"A portal to another world?\""
                    ad talk "\"Sounds so mysterious!\""
                    
                    scene ch15 portal 34
                    with sshake
                    ad talk "\"I am ready, Father.\""
                    "[ad] brushes her hand towards yours."
                    $ quick_menu = False
                    menu:
                        "Hold hands":
                            jump ch15end3

        else:
            stop music fadeout 5.0
            play music "music/Ambient Thriller Motif.mp3" fadein 10.0
            
            scene ch15 portal 38
            with sshake
            "Approaching footsteps getting closer..."
            
            scene ch15 portal 39
            "With a sudden stop, you turn around..."
            mc ctalk2 "\"Who goes there?\""
            
            scene ch15 portal 16
            with sshake
            
            mc ctalk "\"Y-You are...\""
            
            scene ch15 portal 17
            ad talk "\"I am [ad].\""
            ad talk "\"Your daughter.\""
            scene ch15 portal 16
            with sshake
            mc ctalk2 "\"My... daughter.\""
            scene ch15 portal 17
            ad talk "\"You probably didn't know I existed.\""
            ad talk "\"Mother kept it a secret.\""
            ad talk "\"But she is gone now.\""
            ad talk "\"I came here to find you!\""
            
            scene ch15 portal 18
            with sshake
            "You move your hand closer to her cheeks."
            
            scene ch15 portal 19
            with dissolve
            ad talk "\"Hnnnnn...\""
            
            scene ch15 portal 20
            mc ctalk "\"How did you find me?\""
            ad talk "\"Well... I followed your path.\""
            ad talk "\"Your ship has pretty good system to track down people here, you know?\""
            
            scene ch15 portal 21
            ad talk "\"I saw you visited that woman near the sea.\""
            mc cthinking "Elisande?"
            ad talk "\"She told me where to find you.\""
            ad talk "\"I was ready to do very mean things to her, but she didn't waste my time and gave me valuable information, so I let her go.\""
            scene ch15 portal 40
            mc cthinking "Thank god..."
            with dissolve
            mc ctalk "\"That's good. You did good letting her go.\""
            ad talk "\"Father is happy with me?\""
            mc ctalk2 "\"Yes, I am.\""
            mc cthinking "But what do I do now..."
            mc cthinking "I have two options..."
            mc cthinking "Either go through the portal with her or..."
            mc cthinking "Or do what is necessary..."
            mc cthinking "There is no third option... I can't go back with her to my people."
            mc cthinking "They will never accept her. Not after what she has done to them and who her mother was."
            $ quick_menu = False
            menu:
                "Trick her and kill her":
                    $ quick_menu = True
                    mc cthinking "It has to be done..."
                    scene ch15 portal 4
                    with dissolve
                    mc ctalk2 "\"The only way is for us to go through this portal together.\""
                    mc ctalk "\"There is nothing for us back here.\""
                    scene ch15 portal 42
                    ad talk "\"Oh? This is so interesting.\""
                    ad talk "\"The world is so mysterious.\""
                    
                    scene ch15 portal 43
                    ad talk "\"I am excited to travel through with you, Father.\""
                    scene ch15 portal 44
                    ad talk "\"What about you, Father? Are you exci--\""
                    scene ch15 portal 45
                    with sshake
                    ad talk "\"Hey!! What is this?\""
                    ad talk "\"What are you doing?!\""
                    mc ctalk3 "\"I am sorry. It has to be done...\""
                    
                    scene ch15 portal 46
                    with vpunch
                    mc ctalk2 "\"AAAAAAA~!\""
                    ad talk "\"Aghhh!\""
                    
                    scene ch15 portal 47
                    with sshake
                    ad talk "\"AAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHH!!!!!\""
                    
                    scene ch15 portal 48
                    with dissolve
                    "It takes only a few moments for her screams to fade away."
                    
                    scene ch15 portal 8
                    with fasterfadein
                    "After some time you try and gather your thoughts and figure out what to do next..."
                    
                    mc cthinking "If I walk through this portal I will be back there on Earth! Like none of this happened!"
                    mc cthinking "[ad] won't be born and I won't have to think of what I have done..."
                    mc cthinking "Like it was just a bad dream."
                    mc cthinking "Can I make this commitment though? I don't know what awaits me on the other side..."
                    mc cthinking "Elisande also mentioned that everything that happened will happen as it's meant to, no matter what."
                    mc cthinking "But she also said there is a way to break the cycle and my choice is valid..."
                    mc cthinking "Something is pulling me towards that portal, but my intuition is telling me to stay here."
                    $ quick_menu = False
                    menu:
                        "Go through the portal":
                            $ quick_menu = True
                            $ch15_enter_portal = True
                            scene ch15 portal 9
                            mc cthinking "Screw it."
                            scene ch15 portal 10
                            with sshake
                            "As you begin to move through, you notice your hands disappear..."
                            scene ch15 portal 11
                            with sshake
                            "And slowly the rest of your body too..."
                            scene ch15 portal 12
                            "Until you are gone completely."
                            scene ch15 portal 13
                            with fasterfadein
                            "The portal entrance dematerializes the moment you enter through..."
                            jump ch15end1
                            
                        "Leave":
                            $ quick_menu = True
                            $ch15_enter_portal = False
                            scene ch15 portal 3
                            with fasterfadein
                            mc cthinking "No. This is not my destiny."
                            mc cthinking "I still have people who rely on me. I have to go back."
                            jump ch15end2
                            
                            
                "Go through the portal with her":
                    $ quick_menu = True
                    mc cthinking "I have decided. She is still my daughter. My flesh and blood."
                    mc cthinking "She might be naive, because no one taught her otherwise. I will be the parent she needs."
                    scene ch15 portal 41
                    with dissolve
                    mc ctalk "\"This is what we have to do now...\""
                    mc ctalk2 "\"This is a portal to another world, a world where we can both live together.\""
                    mc ctalk "\"We have nothing left for us here, so this is our only option.\""
                    
                    scene ch15 portal 33
                    with dissolve
                    ad talk "\"A portal to another world?\""
                    ad talk "\"Sounds so mysterious!\""
                    
                    scene ch15 portal 34
                    with sshake
                    ad talk "\"I am ready, Father.\""
                    "[ad] brushes her hand towards yours."
                    $ quick_menu = False
                    menu:
                        "Hold hands":
                            jump ch15end3
            
            
label ch15end3:
    scene ch15 portal 35
    with sshake
    $ quick_menu = True
    "You grab her hand and hold her tightly."
    mc ctalk "\"Whatever happens...\""
    mc ctalk2 "\"Do not let go of my hand, you hear me?\""
    ad talk "\"Yes, Father.\""
    
    scene ch15 portal 36
    with sshake
    mc ctalk "\"Let's go.\""
    "After saying that you both take a step forward through the portal."
    
    scene ch15 portal 37
    with dissolve
    "And you both disappear into the abyss."
    
    scene black
    with Dissolve(1)
    pause 3
    
    "You feel at peace."
    "Like nothing matters."
    "'Is this what 'death' feels like?' You think."
    pause 1
    "Just as you were accepting your fate, you start to feel an intense push--"
    
    with vpunch
    
    scene ch15 portal 49
    with Dissolve(1)
    pause 1
    
    with vpunch
    
    scene ch15 portal 50
    with Dissolve(1)
    with vpunch
    ad talk "\"Ahhh~!\""
    mc ctalk "\"Agh!\""
    
    scene ch15 portal 51
    with Dissolve(1)
    with vpunch
    mc ctalk "\"Ah! Shit... are you okay, [ad]?\""
    ad talk "\"Yes... I think so.\""
    
    scene ch15 portal 52
    with Dissolve(1)
    with sshake
    "Before you try to understand what happeneed, a bright light starts shining behind you."
    
    ad talk "\"AHHH!\""
    mc ctalk "\"Aghhh!\""
    with vpunch
    
    scene white
    with Dissolve(1)
    pause 3
    
    with fadein
    scene afewmonthslater
    $ quick_menu = False
    $ renpy.pause(2, hard=True)
    with fasterfadeout
    scene ch15 mc ad end 1
    with fadein
    $ quick_menu = True

    stop music fadeout 5.0
    play music "music/Spread the Word.mp3" fadein 10.0
    
    "A few months pass since then."
    
    "You try and keep [ad] under the radar as much as possible until everything has blown away."
    
    "You got a rental repair watch store that extends to your own personal apartment."
    
    "The world seems the same to you, but different at the same time."
    
    scene ch15 mc ad end 2
    with fasterfadein
    
    "Elisande mentioned that everything will happen exactly the same..."
    "It's the same world, but different somehow."
    "A parallel universe or something else all together?"
    
    "As you continue to walk down the street you hear a nearby stranger talk."
    
    qm empty "\"Wow. They really are something else.\""
    qm empty "\"Being on Paradise must be a dream!\""
    
    "You stop and go to the nearby booth."
    
    scene ch15 mc ad end 3
    with fasterfadein
    
    mc wtalk3 "\"One newspaper, please.\""
    
    scene ch15 mc ad end 4
    with sshake
    
    "You pick up the newspaper and start heading back."
    
    scene ch15 mc ad end 5
    with dissolve
    mc wtalk3 "So... the planet is still intact. They've been there for longer than what it took for the apocalypse to happen last time."
    mc wtalk3 "I think this confirms it. We are safe."
    
    scene ch15 mc ad end 6
    with fasterfadein
    
    mc wtalk3 "\"Hey, Pijo. How was your post today?\""
    "..."
    mc wtalk3 "\"I see. Well, keep up the good work.\""
    "You reply back to the snowman and enter."
    
    scene ch15 mc ad end 7
    with fasterfadein
    mc wtalk3 "\"Ah, home! Sweet home!\""
    
    mc wtalk3 "\"I AM BACK!\""
    "..."
    scene ch15 mc ad end 8
    with dissolve
    mc wtalk4 "Weird."
    mc wtalk4 "That has never happened before. Way too quiet."
    
    scene ch15 mc ad end 9
    with fasterfadein
    "You make your way down the living room."
    mc wtalk4 "\"[ad]?\""
    
    scene ch15 mc ad end 10
    with sshake
    ad pyjtalk "\"Dad? Hey! Welcome home!\""
    
    $ quick_menu = False
    scene ch15 mc ad end 11 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(3, hard=True)
    pause
    with dissolve
    $ quick_menu = True
    mc wtalk4 "\"Why didn't you answer earlier when I called? I got worried.\""
    ad pyjtalk "\"Sorry, Dad. I didn't hear you come in.\""
    mc wtalk4 "\"Don't give your old man a heart attack like that.\""
    ad pyjtalk "\"Te-hee. Sorry.\""
    mc wtalk4 "\"Look how tall you've grown. I have to stand on my toes now.\""
    ad pyjtalk "\"Yeah~! I have~\""
    ad pyjtalk "\"How was outside? What did you do?\""
    
    scene ch15 mc ad end 12
    with dissolve
    mc wtalk4 "\"I got you your favorite food -- hot dog!\""
    ad pyjtalk "\"Really? Yay!\""
    
    scene ch15 mc ad end 13
    with dissolve
    mc wtalk4 "\"You should eat it before it gets cold.\""
    ad pyjtalk "\"Later! First tell meee --\""
    ad pyjtalk "\"How was outside???\""
    mc wtalk4 "\"Very white.\""
    scene ch15 mc ad end 14
    with dissolve
    ad pyjtalk "\"Hahaha!\""
    ad pyjtalk "\"Come and sit next to me and tell me more about it.\""
    
    scene ch15 mc ad end 15
    with fasterfadein
    "You sit next to [ad]."
    mc wtalk4 "\"Well. I might have some good news.\""
    ad pyjtalk "\"Really? Really???\""
    scene ch15 mc ad end 16
    with sshake
    "[ad] lies down and puts her head in your lap."
    mc wtalk4 "\"Yup. It seems you will be able to go outside starting in a few days.\""
    ad pyjtalk "\"No more hiding?!\""
    mc wtalk4 "\"No more hiding.\""
    ad pyjtalk "\"YAYYYYYYY!\""
    ad pyjtalk "\"I will be able to decorate Pijo even further!\""
    ad pyjtalk "\"How is he doing?\""
    mc wtalk4 "\"He is very well.\""
    mc wtalk4 "\"Takes his job very seriously.\""
    ad pyjtalk "\"Hehe.\""
    
    scene ch15 mc ad end 17
    with dissolve
    "'This is fine' you think."
    "It's not the life you expected, but you gave someone a future, where a future didn't seem likely."
    "You stop and think about what could have happened, but it's all getting more faint with each passing day."
    "You have a new life together with your daughter and you are happy with everything you have."
    
    ad pyjtalk "\"I love you, Dad.\""
    mc wtalk4 "\"I love you too, sweetie.\""
    $ persistent.change = "End 3"

    scene ending 4
    with fadein
    $ quick_menu = False
    pause 1.5
    $ quick_menu = True
    voidstar talk "\"{size=+10}Congratulations{/size} on reaching one of the multiple endings the game has to offer!\""
    voidstar talk "\"Many thanks to my patrons and supporters throughout the 2 years of development. This game was made possible thanks to all of you.\""
    voidstar talk "\"Thanks to everyone who spread the word about the game and kept the community going! You all rock!\""
    voidstar talk "\"For more news and updates about future projects, follow me on my {a=https://www.patreon.com/VoidStar}{color=#FF6600}Patreon{/color}{/a}.\""
    
    jump thanks
    
    #End4
                                            
    
    
    


label ch15end1:
    scene black
    with fasterfadein
    "You don't feel anything..."
    "You are at complete peace."
    "Just as you were accepting your fate you felt intense push--"
    
    with vpunch
    
    scene ch15 portal 53
    with Dissolve(1)
    pause 1
    
    with vpunch
    
    scene ch15 portal 54
    with vpunch
    mc ctalk "\"Aaaahgghh!!\""
    
    scene ch15 portal 55
    with vpunch
    mc ctalk2 "\"What the hel--\""
    
    scene ch15 portal 56
    with sshake
    "Before you try to understand what happeneed, a bright light starts shining behind you."
    
    mc ctalk3 "\"Agghhh!\""
    with vpunch
    
    scene white
    with Dissolve(1)
    pause 1
    
    with fasterfadein
    scene afewmonthslater
    $ quick_menu = False
    $ renpy.pause(2, hard=True)
    with fasterfadeout
    scene ch15 mc alt end 1
    with fadein
    $ quick_menu = True
    
    stop music fadeout 5.0
    play music "music/Spread the Word.mp3" fadein 10.0
    
    mc wtalk1 "We are finally here."
    mc wtalk1 "In the end, she was right."
    mc wtalk1 "Hah..."
    
    scene ch15 mc alt end 2
    with fasterfadein
    mc wtalk1 "Nothing I did mattered."
    mc wtalk1 "The timeline is already written and I am just a puppet."
    scene ch15 mc alt end 3
    mc wtalk1 "It's time."
    
    scene ch15 mc alt end 4
    with sshake
    "You quickly put on your disguise."
    "Few moments later you hear footsteps getting closer to your apartment and a few seconds later someone comes in..."

    $ quick_menu = False
    scene ch15 mc alt end 5 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(3, hard=True)
    pause
    with dissolve
    $ quick_menu = True
    
    l utalk "\"You are the 'customer'?\""
    
    scene ch15 mc alt end 6
    with dissolve
    mc wtalk2 "\"That's correct.\""
    
    l utalk "\"Let's get to business.\""
    l utalk "\"Did you bring the money?\""
    
    scene ch15 mc alt end 7
    mc wtalk2 "\"It's right here.\""
    l utalk "\"Good.\""
    l utalk "\"Show me.\""
    
    scene ch15 mc alt end 8
    with sshake
    "You open the briefcase."
    l utalk "\"Hmm...\""
    
    scene ch15 mc alt end 9
    l utalk "\"It seems to be missing half of what we agreed upon.\""
    
    scene ch15 mc alt end 10
    mc wtalk2 "\"You will get the other half when the job is done.\""
    mc wtalk2 "\"I believe that's fair.\""
    mc wtalk2 "\"I kept my word so far.\""
    
    l utalk "\"Yes, you did. You must understand my profession however.\""
    l utalk "\"If I don't get the other half, I WILL come for you. And blood will be spilled.\""
    
    mc wtalk2 "\"I am well aware of that. No need to worry. I have the other half and it will be yours when the job is done.\""
    
    l utalk "\"Good.\""
    
    mc wtalk2 "\"The pill?\""
    
    scene ch15 mc alt end 11
    with fasterfadein
    l utalk "\"This pill cost me a lot of trouble to get.\""
    l utalk "\"Hope it was worth it.\""
    
    scene ch15 mc alt end 12
    with dissolve
    mc wtalk2 "\"It will be worth it.\""
    
    scene ch15 mc alt end 13
    "Lexa turns around."
    l utalk "\"Now, with all that said...\""
    
    scene ch15 mc alt end 14
    with dissolve
    l cangry2 "\"You will excuse me as I have a ship to catch.\""
    mc wtalk2 "\"Safe journey.\""
    l cangry2 "\"Journey? It won't be a journey. I will be back in no time.\""
    mc wtalk2 "\"Of course...\""
    
    scene ch15 mc alt end 15
    with dissolve
    l cangry2 "\"We meet here in exactly a week from now.\""
    l cangry2 "\"Have the rest of the money ready.\""
    mc wtalk2 "\"Sure.\""
    
    scene ch15 mc alt end 16
    with dissolve
    "After saying that she leaves."
    
    scene ch15 mc alt end 17
    with vpunch
    
    mc wtalk2 "..."
    mc wtalk2 "She thought she'd see the other half, but the truth is there is no other half..."
    mc wtalk2 "The last of my savings, the life savings for my daughters education and support."
    mc wtalk2 "Not that it matters now."
    
    scene ch15 mc alt end 18
    with fadein
    "You leave the apartment and go outside through the alleyway."
    "As you walk down, you notice a familiar face."
    
    scene ch15 mc alt end 19
    with dissolve
    mc wtalk2 "It's Jane!"
    mc wtalk2 "And she looks sad..."
    mc wtalk2 "I know what is about to happen too..."
    
    with vpunch
    mc wtalk2 "FUCK!"
    
    scene ch15 mc alt end 20
    with vpunch
    mc wtalk2 "I can't do anything..."
    mc wtalk2 "I am unable to change the past..."
    mc wtalk2 "I am sorry Jane..."
    mc wtalk2 "I am sorry everyone. I let you down."
    
    scene ch15 mc alt end 21
    with fasterfadein
    "You continue walking down the street until you get to a spot on the street near the alleyway."
    
    scene ch15 mc alt end 22
    with fasterfadein
    mc wtalk2 "So, this is it..."
    mc wtalk2 "Not long left now..."
    
    scene ch15 mc alt end 23
    with dissolve
    mc wtalk2 "What keeps me going is the thought that..."
    mc wtalk2 "Somewhere out there... Everyone made it safely to Ingrid, Luna, Mira and Ivy."
    mc wtalk2 "No matter what happens to me now. They will live their lives as they were meant to."
    $ persistent.change = "End 1"

    scene ending 3
    with fadein
    $ quick_menu = False
    pause 1.5
    $ quick_menu = True
    voidstar talk "\"{size=+10}Congratulations{/size} on reaching one of the multiple endings the game has to offer!\""
    voidstar talk "\"Many thanks to my patrons and supporters throughout the 2 years of development. This game was made possible thanks to all of you.\""
    voidstar talk "\"Thanks to everyone who spread the word about the game and kept the community going! You all rock!\""
    voidstar talk "\"For more news and updates about future projects, follow me on my {a=https://www.patreon.com/VoidStar}{color=#FF6600}Patreon{/color}{/a}\""
    
    jump thanks
    #End1
    
label ch15end2:
    scene black
    with fasterfadein
    
    stop music fadeout 5.0
    play music "music/Spread the Word.mp3" fadein 10.0
    
    "You return back and on the next day you come outside the gates..."
    
    $ quick_menu = False
    scene ch15 end 1
    with Dissolve(1)
    $ renpy.pause(1, hard=True)
    
    scene ch15 end 2
    with sshake
    $ quick_menu = True
    "Ingrid opens the gates and patiently awaits for the new members."
    
    scene ch15 end 3
    with fasterfadein
    mc cthinking "This is definitely them."
    mc cthinking "They are coming!"
    
    $ quick_menu = False
    scene ch15 end 5
    with sshake
    $ renpy.pause(1, hard=True)
    with sshake
    $ renpy.pause(1, hard=True)
    
    scene ch15 end 4
    with fasterfadein
    $ quick_menu = True
    mc cthinking "They are getting close."
    mc cthinking "About to land!"
    
    scene ch15 end 6
    with vpunch
    mc ctalk "\"Agh!\""
    
    scene ch15 end 7
    with fadein
    pause 1
    "The ship successfuly lands."
    
    scene ch15 end 8
    with fasterfadein
    "Moments later a platform with staircase is extended."
    
    scene ch15 end 9
    with dissolve
    "First one to come out is Ruby."
    
    scene ch15 end 10
    with fasterfadein
    r ttalk "\"Commander.\""
    mc ctalk "\"Ruby! Glad to see you!\""
    r ttalk2 "\"Likewise, Commander.\""
    mc ctalk2 "\"Please, just [mc] is fine. No need for such formalities anymore.\""
    r ttalk "\"Understood...[mc].\""
    mc ctalk "\"You can make your way inside. They are expecting you.\""
    r ttalk "\"Thank you. On my way.\""
    
    scene ch15 end 11
    with dissolve
    "As Ruby leaves you watch for the next member to come out..."
    
    scene ch15 end 12
    with dissolve
    "Victor comes up next."
    
    v observing "\"Very cool, [mc]. You are like some sort of a superhero, huh!\""
    mc ctalk "\"Well, not really, but... I like the sound of that.\""
    v talk "\"Haha. Well, where do I go?\""
    mc ctalk2 "\"Right behind me, they are expecting you.\""
    v observing "\"Gotcha.\""
    
    $ quick_menu = False
    scene ch15 end 11
    with dissolve
    pause 1
    
    scene ch15 end 13
    with dissolve
    $ quick_menu = True
    "Melisa comes in next."
    m talk "\"[mc]. You've outdone yourself.\""
    mc ctalk "\"Hehe.\""
    m talk2 "\"But not telling the rest of us about it was foolish! To say the least.\""
    m talk "\"Still... I am very happy you are okay.\""
    
    if ch9_melisa_sex:
        scene ch15 end 14
        with dissolve
        m talk2 "\"You know...\""
        m talk2 "\"I hope you have a room next to me...\""
        m talk "\"I am sure we can keep each other company and you can tell me all about your... adventures.\""
        mc ctalk "\"We will be close by, hehe.\""
        m talk2 "\"Mmhm, good.\""
        m talk "\"Going now, pretty boy.\""
    else:
        m talk "\"Well, I will make my way towards those pretty amazons behind you I suppose?\""
        mc ctalk2 "\"That's right.\""
        
    $ quick_menu = False
    scene ch15 end 11
    with dissolve
    pause 1
    
    scene ch15 end 15
    with dissolve
    $ quick_menu = True
    "Jack comes in after."
    jack talk "\"[mc].\""
    mc ctalk "\"Jack.\""
    "..."
    jack talk "\"I guess I should start, huh?\""
    jack talk2 "\"Listen... I owe you an apology.\""
    jack talk "\"I know it's probably too late for that now, but...You have to understand I didn't mean for all of this to happen.\""
    jack talk2 "\"I was just a bodyguard. That's all.\""
    jack talk "\"This went south way too fast.\""
    jack talk2 "\"Everything is messed up...\""
    jack talk "\"But we have a chance at living normal lives again... thanks to you.\""
    
    scene ch15 end 16
    jack talk "\"So, thank you.\""
    "Jack extends his arm forward."
    $ quick_menu = False
    
    menu:
        "Handshake":
            $ quick_menu = True
            $ch15_forgive_jack = True
            scene ch15 end 17
            mc ctalk2 "\"It's fine, Jack.\""
            mc ctalk "\"We all make mistakes.\""
            mc ctalk2 "\"I believe we should all get second chances. What matters is...\""
            mc ctalk "\"What we do with those second chances.\""
            jack talk2 "\"I agree wholeheartedly.\""
            mc ctalk2 "\"Good. You can start your redemption by helping this new place right behind me.\""
            jack talk "\"Got it, [mc]. I will do my best.\""
        "Refuse":
            $ quick_menu = True
            $ch15_forgive_jack = False
            scene ch15 end 15
            with vpunch
            mc ctalk "\"A bit too late for that now, Jack.\""
            mc ctalk2 "\"You can join the others, but you will be kept under strict watch.\""
            jack talk "\"I... understand. Thank you, [mc].\""

scene ch15 end 18
with fasterfadein
"Next one that comes over is Jane."

j pouty "\"You know I am mad at you right?\""
mc ctalk "\"Ehhh? For what?\""
j pouty "\"You risked your life without telling us.\""
j pouty "\"I expected more from you.\""
mc ctalk2 "\"I am sorry, Jane.\""
mc ctalk "\"I couldn't risk more casualties.\""
j talk "\"Fine. You get away with it. But just this once.\""
j talk2 "\"Don't ever do this again.\""
mc ctalk2 "\"Hehe. I promise.\""
j talk "\"Good~\""

if ch10_jane_bj:
    scene ch15 end 19
    with dissolve
    j talk2 "\"And you better show me how sorry you are starting later tonight.\""
    j talk "\"Otherwise I couldn't be sure.\""
    
    scene ch15 end 20
    with dissolve
    j talk "\"And I will need to check by connecting our naked bodies. That way I know you are not lying.\""
    mc ctalk "\"I am game for that, hehe.\""
    j talk2 "\"Good~ I expect you tonight.\""
    
else:
    j talk2 "\"I am going to join the others now.\""
    mc ctalk "\"Yeah, go ahead.\""

scene ch15 end 31
with fasterfadein
"Chloe comes next."
chloe talk "\"Well, shit.\""
chloe talk "\"I really thought I was going to wake up, but I guess this is no dream, huh?\""
chloe talk2 "\"Such a fucked up situation, dude.\""
mc ctalk2 "\"Yeah, it sure is.\""
chloe talk "\"At least, thanks to you, we are able to make the best of it.\""

if ch10_chloe_sex:
    $chloe_love = True
    scene ch15 end 32
    with sshake
    chloe talk "\"I think a thank you is in order.\""
    chloe talk2 "\"You were really nice with me on the ship.\""
    chloe talk "\"If you want to continue our 'friends' with 'benefits' relationship, then seek me out.\""
    chloe talk2 "\"I am always game to go down with you.\""
    mc ctalk "\"Yeah, for sure, Chloe.\""
    chloe talk "\"Alright then, later.\""
else:
    $chloe_love = False
    chloe talk "\"Well, I guess this is my life now.\""
    chloe talk2 "\"Gonna go and see what's what, later.\""
    
scene ch15 end 21
with fasterfadein
l atalk "\"[mc]... I was worried sick...\""
if ch11_saved_ruby:
    mc ctalk "\"I am sorry, Lex... Are you okay? Did they hurt you?\""
    l atalk "\"I am a tough person... You know that better than anyone...\""
    l atalk "\"It doesn't matter now, I want to forget about it. I am glad I am here, together with you.\""
else:
    mc ctalk "\"Sorry, Lex. I had to do it without telling anyone. I had to keep you all safe.\""
    l atalk "\"I understand... I am not mad at you. I will support you in whatever you do.\""
    l atalk "\"I am so glad to be here, together with you.\""

l atalk "\"Quite the journey, huh?\""
mc ctalk2 "\"Yeah! I'd say.\""

if ch10_lexa_fj:
    scene ch15 end 22
    with dissolve
    l atalk "\"Since we are here now...\""
    l atalk "\"Have you made your choice... for a partner?\""
    l atalk "\"Do you see me as one?\""
    $ quick_menu = False
    menu:
        "I want us to be together":
            $ quick_menu = True
            $ch15_lexa_love = True
            mc ctalk "\"Yes. I'd like for us to be together.\""
            l atalk "\"Mmm. My lover.\""
            l atalk "\"[mc], do we have a house there? Just for the two of us?\""
            mc ctalk2 "\"Not sure, but I will make sure we get one.\""
            l atalk "\"Good. I am going, because I will jump on you and start fucking out in the open.\""
            mc ctalk "\"Yeaaah. I think that's the best to do for now.\""
            jump ch15end2x1
        "No":
            $ quick_menu = True
            $ch15_lexa_love = False
            scene ch15 end 21
            with sshake
            mc ctalk "\"No, sorry, Lexa. I don't see it happening.\""
            l atalk "\"I.. I see... I understand. We walk different paths.\""
            l atalk "\"It was nice whatever we had... while it lasted.\""
            l atalk "\"I will see you at camp.\""
            jump ch15end2x1
            
elif fuck_lexa_cell:
    scene ch15 end 22
    with dissolve
    l atalk "\"Since we are here now...\""
    l atalk "\"Have you made your choice... for a partner?\""
    l atalk "\"Do you see me as one?\""
    $ quick_menu = False
    menu:
        "I want us to be together":
            $ quick_menu = True
            $ch15_lexa_love = True
            mc ctalk "\"Yes. I'd like for us to be together.\""
            l atalk "\"Mmm. My lover.\""
            l atalk "\"[mc], do we have a house there? Just for the two of us?\""
            mc ctalk2 "\"Not sure, but I will make sure we get one.\""
            l atalk "\"Good. I am going, because I will jump on you and start fucking out in the open.\""
            mc ctalk "\"Yeaaah. I think that's the best to do for now.\""
            jump ch15end2x1
        "No":
            $ quick_menu = True
            $ch15_lexa_love = False
            scene ch15 end 21
            with sshake
            mc ctalk "\"No, sorry, Lexa. I don't see it happening.\""
            l atalk "\"I.. I see... I understand. We walk different paths.\""
            l atalk "\"It was nice whatever we had... while it lasted.\""
            l atalk "\"I will see you at camp.\""
            jump ch15end2x1
            
elif showers_lexa_sex:
    scene ch15 end 22
    with dissolve
    l atalk "\"Since we are here now...\""
    l atalk "\"Have you made your choice... for a partner?\""
    l atalk "\"Do you see me as one?\""
    $ quick_menu = False
    menu:
        "I want us to be together":
            $ quick_menu = True
            $ch15_lexa_love = True
            mc ctalk "\"Yes. I'd like for us to be together.\""
            l atalk "\"Mmm. My lover.\""
            l atalk "\"[mc], do we have a house there? Just for the two of us?\""
            mc ctalk2 "\"Not sure, but I will make sure we get one.\""
            l atalk "\"Good. I am going, because I will jump on you and start fucking out in the open.\""
            mc ctalk "\"Yeaaah. I think that's the best to do for now.\""
            jump ch15end2x1
        "No":
            $ quick_menu = True
            $ch15_lexa_love = False
            scene ch15 end 21
            with sshake
            mc ctalk "\"No, sorry, Lexa. I don't see it happening.\""
            l atalk "\"I.. I see... I understand. We walk different paths.\""
            l atalk "\"It was nice whatever we had... while it lasted.\""
            l atalk "\"I will see you at camp.\""
            jump ch15end2x1

else:
    $ch15_lexa_love = False
    l atalk "\"Well... I will be going now. There are other people coming after me.\""
    jump ch15end2x1

label ch15end2x1:
    scene ch15 end 23
    with fasterfadein
    "The next one is your wife, Cassandra."
    "She looks a bit shaken up as she stands there and starts to talk."
    
    if persistent.show_ntr:
        cass ptalk "\"[mc]... I ...\""
        cass ptalk "\"I ...\""
        "You figure out what she is trying to say."
        mc ctalk "\"You remember now? You have your memories back?\""
        cass ptalk "\"Yeah. I do...\""
        cass ptalk "\"What I've done...\""
        mc ctalk2 "\"You can't blame yourself... You didn't know.\""
        cass ptalk "\"But I slept... and...\""
        mc ctalk "\"I know everything.\""
        cass ptalk "\"Then...\""
        cass ptalk "\"That means... you don't want me anymore...\""
        $ quick_menu = False
        menu:
            "Forgive her and take her back":
                $ quick_menu = True
                $ch15_cass_forgive = True
                $ch15_cass_ntr = False
                $ch15_cass_breakup = False
                mc ctalk "\"It's fine. I forgive you.\""
                scene ch15 end 24
                with dissolve
                cass ptalk "\"Y-You do?\""
                cass ptalk "\"After knowing everything I've done?\""
                mc ctalk2 "\"Yes.\""
                
                scene ch15 end 25
                with dissolve
                cass ptalk "\"Thank you so much, honey.\""
                cass ptalk "\"I will never leave you.\""
                mc ctalk2 "\"Me too, babe, me too...\""
                jump ch15end2x2
            
            "Tell her to continue seeing Andre":
                $ quick_menu = True
                $ch15_cass_ntr = True
                $ch15_cass_breakup = False
                $ch15_cass_forgive = False
                mc ctalk "\"I forgive you... but I want you to do something for me.\""
                cass ptalk "\"Of course! Anything!\""
                
                mc ctalk2 "\"Continue seeing Andre... And keep giving me all the details.\""
                cass pthinking "\"Wait... you... what...\""
                scene ch15 end 24
                with dissolve
                cass pthinking "\"You understand what you just said?\""
                
                mc ctalk2 "\"Absolutely.\""
                
                scene ch15 end 25
                with dissolve
                cass ptalk "\"I didn't know you were like that, honey.\""
                cass ptalk "\"If that's what you truly want I will be more than happy to do so for you.\""
                jump ch15end2x2
                
            "Say it's over":
                $ quick_menu = True
                $ch15_cass_forgive = False
                $ch15_cass_breakup = True
                $ch15_cass_forgive = False
                
                mc ctalk "\"It's over between us.\""
                mc ctalk "\"We both get a new start, separately.\""
                cass ptalk "\"I understand...\""
                scene ch15 end 11
                with dissolve
                "She leaves and moves towards the others."
                jump ch15end2x2
    else:
        $ quick_menu = True
        cass ptalk "\"[mc]... I ...\""
        cass ptalk "\"I ...\""
        "You figure out what she is trying to say."
        mc ctalk "\"You remember now? You have your memories back?\""
        cass ptalk "\"Yeah. I do...\""
        cass ptalk "\"Please... [mc]. Forgive me...\""
        cass ptalk "\"I don't want to lose you or the girls...\""
        $ quick_menu = False
        menu:
            "Forgive her and take her back":
                $ quick_menu = True
                $ch15_cass_forgive = True
                $ch15_cass_ntr = False
                $ch15_cass_breakup = False
                mc ctalk "\"It's fine. I forgive you.\""
                scene ch15 end 24
                with dissolve
                cass ptalk "\"Y-You do?\""
                cass ptalk "\"After knowing everything I've done?\""
                mc ctalk2 "\"Yes.\""
                
                scene ch15 end 25
                with dissolve
                cass ptalk "\"Thank you so much, honey.\""
                cass ptalk "\"I will never leave you.\""
                mc ctalk2 "\"Me too, babe, me too...\""
                jump ch15end2x2
            "Say it's over":
                $ quick_menu = True
                $ch15_cass_forgive = False
                $ch15_cass_breakup = True
                $ch15_cass_forgive = False
                
                mc ctalk "\"It's over between us.\""
                mc ctalk "\"We both get a new start, separately.\""
                cass ptalk "\"I understand...\""
                scene ch15 end 11
                with dissolve
                "She leaves and moves towards the others."
                jump ch15end2x2
        
label ch15end2x2:
scene ch15 end 11
with dissolve
"Cassandra leaves and you see Andre making his way towards you."
if persistent.show_ntr:
    scene ch15 end 27
    with dissolve
    "You see Cass and Andre's baby in his arms."
    a talk "\"Hey, [mc].\""
    a talk "\"I hope... there's no hard feelings?\""
    mc ctalk2 "\"It is what it is.\""
    mc ctalk "\"This is a fresh start for everyone. Let's not look back at what we couldn't change.\""
    a talk2 "\"Yeah! Well said.\""
    jump ch15end2x3
else:
    scene ch15 end 26
    with dissolve
    a talk "\"Hey, [mc].\""
    a talk "\"Very fucked up situation, huh?\""
    mc ctalk "\"Yeah, for sure.\""
    a talk2 "\"Thanks to you we can start fresh, I appreciate it.\""
    a talk "\"And I am sorry for everything.\""
    mc ctalk "\"It's a fresh start for everyone. Let's do our best...\""
    a talk "\"Yeah! Well said.\""
    jump ch15end2x3

label ch15end2x3:
    scene ch15 end 28
    with fasterfadein
    "Dahlia comes up next."
    
    d talk "\"My, my, [mc].\""
    d talk2 "\"You are truly something else.\""
    d talk "\"You fight aliens, save damsels in distress, find a new home for everyone.\""
    d talk2 "\"Just wow.\""
    mc ctalk2 "\"Somebody had to do it.\""
    d talk "\"Right. I am glad it was you.\""
    d talk2 "\"You had that aura about you... since the start.\""
    if saved_dahlia_from_edis:
        d talk "\"I am happy to have gone through this journey together with you.\""
        if accept_dahlia_visit:
            scene ch15 end 29
            with dissolve
            "Dahlia turns around to check if there is someone behind her watching."
            
            scene ch15 end 30
            with vpunch
            d talk2 "\"This is yours, whenever you feel like it.\""
            d talk "\"Don't be shy to ask me.\""
            mc ctalk "\"Oh, wow.\""
            mc ctalk2 "\"I will keep it in mind, Dahlia. Thanks.\""
            d talk "\"No, Thank YOU.\""
            d talk "\"I am going now, you have some very excited girls waiting to meet you next.\""
            jump ch15end2x4
        else:
            d talk "If it wasn't for you...I would've been so broken...\""
            d talk2 "\"You have no idea how much I appreciate what you've done.\""
            mc ctalk "\"There is no need to mention it, Dahlia. I'd always help you.\""
            d talk "\"Thank you... truly.\""
            d talk "\"I am going now, you have some very excited girls waiting to meet you next.\""
            jump ch15end2x4
    else:
        d talk "\"I am happy to have gone through this journey together with you.\""
        d talk2 "\"I... I am fucked up forever now, but it is what it is...\""
        d talk "\"Casualties always happen.\""
        mc ctalk "\"I am so sorry for what happened to you, Dahlia.\""
        mc ctalk2 "\"I am sorry I wasn't there for you...\""
        d talk2 "\"Thanks, [mc]. I appreciate it.\""
        d talk "\"You can't save absolutely everyone always.\""
        d talk2 "\"Doing this is more than anyone could have done. So don't feel any guilt about me.\""
        d talk "\"I am going now, you have some very excited girls waiting to meet you next.\""
        jump ch15end2x4
        
label ch15end2x4:
    scene ch15 end 33
    with fasterfadein
    e talk "\"D-DAD!!\""
    z talk "\"*Gasp*\""
    
    scene ch15 end 34
    with vpunch
    "Before you can reply you get hugged by both Zoey and Elyse."
    mc ctalk "\"Woah there.\""
    mc ctalk2 "\"Go easy on your old man.\""
    
    e talk2 "\"Dad... I am so happy to see you again.\""
    mc ctalk2 "\"Me too, girls, me too.\""
    z talk2 "\"You fought aliens and creatures?!\""
    mc ctalk "\"I did, yeah.\""
    z talk "\"Woah! Cool!\""
    e talk "\"Tell us all about it!\""
    mc ctalk "\"Sure, let's head inside.\""
    
    scene ch15 end 35
    with fasterfadein
    e talk2 "\"Come on, you two, hurry up!\""
    mc ctalk "\"We are coming!\""
    
    scene ch15 end 36
    with dissolve
    z talk "\"Dad? What is it?\""
    
    if ch15_aurora_leave:
        mc ctalk2 "\"Go ahead, honey.\""
        mc ctalk "\"I will meet you inside in a bit, okay?\""
        z talk2 "\"Okay, Dad.\""
        scene ch15 end 39
        with dissolve
        mc cthinking "Is that...?"
        
        scene ch15 end 40
        with dissolve
        "You look at the horizon and see Aurora coming your way."
        mc cthinking "Oh my...It is!"
        
        scene ch15 end 41
        with fasterfadein
        mc ctalk "\"Aurora!\""
        aur ctalk "\"Hi, [mc].\""
        mc ctalk2 "\"They freed you?\""
        aur ctalk "\"Yeah!\""
        mc ctalk "\"So it worked...\""
        aur ctalk "\"I knew it! It was thanks to you that I got freed.\""
        mc ctalk2 "\"Well... partially. Someone else did most of the work.\""
        mc ctalk "\"I am just glad it worked.\""
        aur ctalk "\"Yeah... me too.\""
        
        scene ch15 end 42
        mc ctalk "\"Who is this little fella?\""
        aur ctalk "\"It's my baby boy.\""
        mc ctalk "\"He is cute. Does he have a name yet?\""
        aur ctalk "\"Yeah, he does.\""
        aur ctalk "\"[mc].\""
        
        scene ch15 end 43
        mc ctalk2 "\"I am honored.\""
        mc ctalk "\"How did you find us?\""
        aur ctalk "\"They gave me a lot of food,water,horse and a map.\""
        aur ctalk "\"I also asked for you and they pointed me towards this direction.\""
        mc ctalk "\"I am really glad to hear that.\""
        
        scene ch15 end 44
        "As you walk towards the camp you feel accomplished."
        "You managed to do the best you can."
        "Giving hope to these people was all worth it in the end."
        $ persistent.change = "End 2"
     
        scene ending 5
        with fadein
        $ quick_menu = False
        pause 1.5
        $ quick_menu = True
        voidstar talk "\"{size=+10}Congratulations{/size} on reaching one of the multiple endings the game has to offer!\""
        voidstar talk "\"Many thanks to my patrons and supporters throughout the 2 years of development. This game was made possible thanks to all of you.\""
        voidstar talk "\"Thanks to everyone who spread the word about the game and kept the community going! You all rock!\""
        voidstar talk "\"For more news and updates about future projects, follow me on my {a=https://www.patreon.com/VoidStar}{color=#FF6600}Patreon{/color}{/a}.\""

        jump thanks
        
    
    else:
        scene ch15 end 37
        mc ctalk2 "\"Nothing, let's go inside.\""
        z talk "\"Dad...\""
        mc ctalk "\"Yeah?\""
        z talk2 "\"I missed you... a lot.\""
        mc ctalk2 "\"Me too, honey. Me too.\""
        mc ctalk "\"We are never going to be separated again.\""
        z talk "\"Pinky promise?\""
        
        scene ch15 end 38
        mc ctalk "\"Sure, pinky promise!\""
        $ persistent.change = "End 2"
        
        scene ending 5
        with fadein
        $ quick_menu = False
        pause 1.5
        $ quick_menu = True
        voidstar talk "\"{size=+10}Congratulations{/size} on reaching one of the multiple endings the game has to offer!\""
        voidstar talk "\"Many thanks to my patrons and supporters throughout the 2 years of development. This game was made possible thanks to all of you.\""
        voidstar talk "\"Thanks to everyone who spread the word about the game and kept the community going! You all rock!\""
        voidstar talk "\"For more news and updates about future projects, follow me on my {a=https://www.patreon.com/VoidStar}{color=#FF6600}Patreon{/color}{/a}.\""
        
        jump thanks