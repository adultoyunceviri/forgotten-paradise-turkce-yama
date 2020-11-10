label startch14:
    $ luna_romance = 0
    $ ingrid_romance = 0
    scene black
    with fasterfadein
    "A few minutes ago..."
    scene ch14 flashback 1
    with fadein
    eli nudetalk "\"Bind • US • TOGETHER~OH • GREAT ONE\""
    eli nudetalk "\"we are FOREVER your servants in life and DEATH • GREAT ONE\""
    scene ch14 flashback 2
    with vpunch
    eli nudetalk "\"BIND • OUR SOULS TOGETHER\""
    eli nudetalk "\BIND US TOGETHER IN UNITY\""
    scene ch14 flashback 3
    eli nudetalk "\"OH~GREAT ONE • MAKE OUR MINDS ONE! • UNITE US!\""
    scene ch14 flashback 4
    with sshake
    with sshake
    with sshake
    scene black
    with Dissolve(1)
    mc ctalk "\"Uhh...\""
    
    scene ch14 flashback 5
    with Dissolve(1)
    mc ctalk2 "\"Wh--What happened?\""
    
    scene ch14 flashback 6
    with dissolve
    mc ctalk3 "\"Where am I?\""
    qm empty "\"'Tis my mind, [mc].\""
    mc ctalk2 "\"Who said that?\""
    
    scene ch14 flashback 7
    with dissolve
    eli talk "\"Here, take my hand.\""
    
    scene ch14 flashback 8
    with dissolve
    mc ctalk "\"You are...\""
    eli talk "\"You know who I be. You be the one searching fo' me.\""
    mc ctalk3 "\"Elisande...?\""
    eli talk "\"That's right.\""
    
    scene ch14 flashback 9
    with dissolve
    eli talk "\"We have a lot to discuss.\""
    mc ctalk "\"What is this place?\""
    eli talk "\"I don't know an easy way fo' me to say this...\""
    eli talk "\"...There be 2 bad and one good news fo' you.\""
    mc ctalk "\"I am not going to like this, huh?\""
    "..."
    mc ctalk2 "\"Just give it to me straight.\""
    eli talk "\"You were in a very bad shape when you arrived last night. The blade be coated in poison.\""
    eli talk "\"And I do not possess the antidote eitha'.\""
    eli talk "\"So thee' be only one thing I could do...\""
    
    scene ch14 flashback 12
    eli talk "\"In order to slow down the poison, I had to use a spell which was a double edge swo'd.\""
    eli talk "\"It worked to slow down the poison long enough fo' us to find a cure, but it left us with anotha' problem...\""
    mc ctalk "\"Which is...?\""
    eli talk "\"Your soul entered my body and mind.\""
    
    scene ch14 flashback 11
    with sshake
    mc ctalk "\"What? You are joking, right?\""
    eli talk "\"I am afraid not.\""
    eli talk "\"Our minds are interwined now. I can see your memories and you can see mine.\""
    mc ctalk2 "\"So... this place is...\""
    eli talk "\"'Tis part of my own mind, soul or body. However you want to interpret it.\""
    scene ch14 flashback 12
    eli talk "\"That be the first bad thing. The second is that the only cure for this, as far as I know, be located in the same place where you got you' wound to begin with.\""
    eli talk "\"It be kept by da Queen & produced by da Queen. It's a way for her soldiers to do damage with no way to repair or survive it unless she says otherwise.\""
    eli talk "\"Thankfully we have time, that be the good news. Your body is still alive and we can revert this process... if we get the antidote fast enough that is.\""
    
    scene ch14 flashback 11
    mc ctalk "\"I am ready to do whatever it takes.\""
    eli talk "\"Since we be sharing da same body now... it might get a bit weird fo' you.\""
    scene ch14 flashback 12
    eli talk "\"I doubt you've experienced a woman's point of view, so take that into consideration.\""
    eli talk "\"We also have to explain to your friends the situation. I doubt it'd be easy to understand from their eyes.\""
    mc ctalk2 "\"They will understand. We've already seen and experienced some stuff that can't be explained.\""
    eli talk "\"Okay. We will have to leave and infiltrate the Queen's castle immediately. We don't have any time to lose.\""
    eli talk "\"I will let you say farewell to your companions.\""
    
    scene ch14 flashback 10
    mc ctalk3 "\"This is all so crazy to comprehend, but for some reason I feel at peace.\""
    mc ctalk2 "\"Let's do this!\""
    
    scene black
    with Dissolve(1)
    
    scene ch14 camp 1
    with Dissolve(1)
    
    eli talk "I will let you do the talking."

    mc elithinking "Now... Who should I go to first..."
    $ _skipping = False
    $ quick_menu = False
    
    show screen ch14_ingrid_luna_preference
    $ renpy.pause(9999, hard=True)
    


label ch14ingrid:
    $ ch14_ingrid_preference = True
    $ ch14_luna_preference = False
    $ ingrid_romance += 1
    scene ch14 camp 2
    with fasterfadein
    hide screen ch14_ingrid_luna_preference
    
    $ quick_menu = True
    $ _skipping = True

    "You move to Ingrid first and sit by her on the sand."
    "..."
    mc elitalk "\"Hey, Ingrid.\""
    ingrid talk "\"Hey.\""
    ingrid talk "\"Who am I speaking to?\""
    mc elitalk "\"[mc]. I ...\""
    mc elitalk "\"...I know this is a lot to take in, but it's not as weird as it seems to me right now.\""
    mc elitalk "\"The good news is that there is a chance and a way to revert this and get me back in my own body.\""
    scene ch14 camp 3
    
    ingrid talk "\"Yeah?\""
    ingrid talk "\"Just a chance? I don't know if I can trust a total stranger and all of this sounds too crazy for me.\""
    mc elitalk "\"Well, yeah. It is crazy. But I think you already had a good tase of crazy when you found me.\""
    
    scene ch14 camp 5
    ingrid talk "\"That's a good point.\""
    ingrid talk "\"You know the girls around the camp nicknamed you 'Outlander'.\""
    mc elitalk "\"Oh, really?\""
    ingrid talk "\"Yeah. It has a nice ring to it.\""
    
    scene ch14 camp 4
    mc elitalk "\"I like it.\""
    scene ch14 camp 5
    ingrid talk "\"What is your plan now?\""
    scene ch14 camp 4
    mc elitalk "\"We will go back to the capital to retrieve a leaf from a plant that is needed to create the antidote.\""
    scene ch14 camp 5
    ingrid talk "\"Sounds good. When do we leave?\""
    scene ch14 camp 4
    mc elitalk "\"I am sorry, Ingrid. We will be going alone.\""
    mc elitalk "\"They already know your faces and you are wanted.\""
    mc elitalk "\"I also need someone to guard my body until we return.\""
    mc elitalk "\"Can you do that for me?\""
    scene ch14 camp 5
    ingrid talk "\"Yeah...I can do that.\""
    ingrid talk "\"I just want you to come back...\""
    scene ch14 camp 6
    mc elitalk "\"I know.\""
    mc elitalk "\"I will. I promise.\""
    
    
    
    scene ch14 camp 7
    with fasterfadein
    "You go and see Luna."
    mc elitalk "\"Hey.\""
    luna talk "\"Hey yourself.\""
    mc elitalk "\"How are you taking this in?\""
    luna talk "\"I believe we all have our purpose to fulfill.\""
    luna talk "\"Even if we don't know it we are set on a path which we have to walk.\""
    scene ch14 camp 8
    with dissolve
    luna talk "\"The fact that you came from somewhere up there and my people were the ones to find you and then for you to save me...\""
    scene ch14 camp 9
    with pushright
    luna talk "\"It all adds up.\""
    luna talk "\"It's our destiny to be where we are right now.\""
    scene ch14 camp 11
    with dissolve
    mc elitalk "\"It makes sense.\""
    mc elitalk "\"Everything is connected. I don't really understand it fully myself, but...\""
    mc elitalk "\"Everything that has happened to me, my world, my family paved away the path for me to come here and meet you guys.\""
    mc elitalk "\"Me and Elisande are going back to the capital now to get what is needed for the antidote.\""
    mc elitalk "\"I'd like for you guys to guard my body until we come back.\""
    scene ch14 camp 10
    with pushright
    luna talk "\"Of course, [mc]. That's the least we can do.\""
    
    jump ch14camp2
    
label ch14luna:
    $ ch14_luna_preference = True
    $ ch14_ingrid_preference = False
    $ luna_romance += 1
    scene ch14 camp 7
    with fasterfadein
    hide screen ch14_ingrid_luna_preference
    
    $ quick_menu = True
    $ _skipping = True

    "You move to talk to Luna first."
    mc elitalk "\"Hey.\""
    luna talk "\"Hey yourself.\""
    mc elitalk "\"How are you taking this in?\""
    luna talk "\"I believe we all have our purpose to fulfill.\""
    luna talk "\"Even if we don't know it we are set on a path which we have to walk.\""
    scene ch14 camp 8
    with dissolve
    luna talk "\"The fact that you came from somewhere up there and my people were the ones to find you and then for you to save me...\""
    scene ch14 camp 9
    with pushright
    luna talk "\"It all adds up.\""
    luna talk "\"It's our destiny to be where we are right now.\""
    scene ch14 camp 11
    with dissolve
    mc elitalk "\"It makes sense.\""
    mc elitalk "\"Everything is connected. I don't really understand it fully myself, but...\""
    mc elitalk "\"Everything that has happened to me, my world, my family paved away the path for me to come here and meet you guys.\""
    mc elitalk "\"Me and Elisande are going back to the capital now to get what is needed for the antidote.\""
    mc elitalk "\"I'd like for you guys to guard my body until we come back.\""
    scene ch14 camp 10
    with pushright
    luna talk "\"Of course, [mc]. That's the least we can do.\""
    luna talk "\"Be safe, [mc], Elisande.\""
    mc elitalk "\"You too, Luna. I will be back as soon as I can. If something happens and we don't return in two days just run and forget about me.\""
    scene ch14 camp 12
    with pushup
    luna talk "\"You will come back.\""
    luna talk "\"I believe in you.\""
    
    scene ch14 camp 2
    with fasterfadein
    "You go and see Ingrid."
    "..."
    mc elitalk "\"Hey, Ingrid.\""
    ingrid talk "\"Hey.\""
    ingrid talk "\"Who am I speaking to?\""
    mc elitalk "\"[mc]. I ...\""
    mc elitalk "\"...I know this is a lot to take in, but it's not as weird as it seems to me right now.\""
    mc elitalk "\"The good news is that there is a chance and a way to revert this and get me back in my own body.\""
    scene ch14 camp 3
    
    ingrid talk "\"Yeah?\""
    ingrid talk "\"Just a chance? I don't know if I can trust a total stranger and all of this sounds too crazy for me.\""
    mc elitalk "\"Well, yeah. It is crazy. But I think you already had a good tase of crazy when you found me.\""
    
    scene ch14 camp 5
    ingrid talk "\"That's a good point.\""
    ingrid talk "\"You know the girls around the camp nicknamed you 'Outlander'.\""
    mc elitalk "\"Oh, really?\""
    ingrid talk "\"Yeah. It has a nice ring to it.\""
    
    scene ch14 camp 4
    mc elitalk "\"I like it.\""
    scene ch14 camp 5
    ingrid talk "\"What is your plan now?\""
    scene ch14 camp 4
    mc elitalk "\"We will go back to the capital to retrieve a leaf from a plant needed to create the antidote.\""
    scene ch14 camp 5
    ingrid talk "\"Sounds good. When do we leave?\""
    scene ch14 camp 4
    mc elitalk "\"I am sorry, Ingrid. We will be going alone.\""
    mc elitalk "\"They already know your faces and you are wanted.\""
    mc elitalk "\"I also need someone to guard my body until we return.\""
    mc elitalk "\"Can you do that for me?\""
    scene ch14 camp 5
    ingrid talk "\"Yeah...I can do that.\""
    ingrid talk "\"I just want you to come back...\""
    mc elitalk "\"I will. I promise.\""
    
    jump ch14camp2
    
    



label ch14camp2:
    scene ch14 camp 13
    with fadein
    
    mc elitalk "I... I just want to say..."
    mc elitalk "I really appreciate what you are doing for me."
    mc elitalk "Going out of your way to help a complete stranger."

    eli talk "Thank me after I actually save you."
    eli talk "'Tis not going to be a walk in the park."

    scene ch14 camp 14
    with dissolve
    
    mc elitalk "What is the plan?"
    eli talk "To infiltrate the castle and reach the Queen's private quarters."
    mc elitalk "That sounds... hard."
    mc elithinking "How will we reach there?"
    
    eli thinking "Sneaking in will not be an option."
    eli talk "They be already on alert because of you guys."
    eli talk "And I don't be planning to risk my life that way."
    eli talk "There be a guy outside in the suburbs who goes out to scout for potential partner for the Queen."
    eli talk "We will need to be the one who he selects today."
    mc elithinking "The Queen is into girls?"
    eli talk "She be bisexual, yes."
    eli talk "Seducing her and then making our way to her hidden stash will be our only option."
    mc elithinking "Sounds like a decent plan."
    eli talk "Trust me. 'Tis the only way to get you back to your body in time."
    
    
    scene black
    with Dissolve(1)
    
    if ch11_saved_ruby:
        jump ch14town1
    else:
        with fasterfadein
        scene meanwhile
        $ quick_menu = False
        $ renpy.pause(2, hard=True)
        with fasterfadeout
        scene black
        with fadein
        $ quick_menu = True
        
        stop music fadeout 5.0
        play music "music/Ambient Thriller Motif.mp3" fadein 10.0
        
        qm alienntalk "\"Ahhhhhhhhhh~~~~~\""
        qm alienntalk "\"Yesss~~~\""
        qm alienntalk "\"Fuck me harder!\""
        
        scene ch14 lab 1
        with Dissolve(1)
        
        ad thinking "There she goes again..."
        ad thinking "This is the 5th time today..."
        "Moaning continues"
        ad thinking "She refuses to talk to me at all and has me caged on this awful place."
        qm alienntalk "\"Ahhh, Hahhh, Mmmmmmahhh...\""
        

        $ renpy.show("ch14_alien_victor_sex1")
        
        ad thinking "All she does is breed all day..."
        ad thinking "She already gave birth multiple times, but to disfigured creatures..."
        ad thinking "Non-intelligent and grotesque looking."
        ad thinking "...She is trying to procreate more like me."
        ad thinking "But it's obvious none of the males on board are my father."

        scene ch14 lab 3
        with pushleft
        
        ad thinking "She keeps them to experiment on..."
        ad thinking "I bet I would be in there if I didn't resemble a human."
        $ quick_menu = False
        menu:
            "Continue watching your mother have sex":
                jump ch14paradise1
            
            "Leave":
                jump ch14paradise2
                
                
    label ch14paradise1:
        $ quick_menu = True
        scene ch14 lab 4
        with pushright
        qm alienntalk "\"That's right, boy.\""
        qm alienntalk "\"Put your dick deep in me...\""
        qm alienntalk "\"Fuck me!\""
        
        $ renpy.show("ch14_alien_victor_sex2")
        
        qm alienntalk "\"Nng......\n{space=90}Auhaa......\n{space=180}Auugh......\""
        
        qm alienntalk "\"Ungh.....\n{space=90}Phew......\n{space=180}Hahhh......\""
        
        qm alienntalk "\"Nmph......\n{space=90}Ahnn......\n{space=180}Uhnhh......\""
        
        scene ch14 lab 2
        with sshake
        
        v nudetalk "\"Fuck... Ughh.. I am...\""
        
        scene ch14 lab 5
        v nudetalk "\"{size=+10}CUMMING!{/size}\""
        with sshake
        scene white
        with Dissolve(1)
        pause 1
        
        scene ch14 lab 5
        with Dissolve(1)
        
        scene white
        with Dissolve(1)
        pause 1
    
        scene ch14 lab 6
        with Dissolve(1)
        
        v nudetalk "\"Fuck! It hurts!\""
        qm alienntalk "\"Mmmmmmmmmmmmmmm~~\""
        qm alienntalk "\"That's right. Splatter my insides full of your seed.\""
        qm alienntalk "\"Make me a baby!\""
        with sshake
        v nudetalk "\"Ugh!\""
        
        scene ch14 lab 7
        with pushleft
        
        ad thinking "I've seen enough."
        ad thinking "Now is my chance to interrogate her while mother is still busy..."
        jump ch14paradise3
        
    label ch14paradise2:
        $ quick_menu = True
        scene ch14 lab 7
        with pushright
        ad thinking "I've seen enough."
        ad thinking "Now is my chance to interrogate her while mother is still busy..."
        jump ch14paradise3


    label ch14paradise3:
        scene ch14 lab 8
        with fasterfadein
        "..."
        "Door opens."
        scene ch14 lab 9
        with pushright
        
        ad talk "\"Wakey, wakey.\""
        ad talk "\"Time for us to have a chat, my dear.\""
        
        scene ch14 lab 10
        
        l doubt "\"What do you want?!\""
        ad talk "\"Aww. What's with that attitude?\""
        
        scene ch14 lab 11
        with sshake
        ad talk "\"Tell me... who is this [mc] you mentioned earlier?\""
        l doubt "..."
        ad talk "\"Silence is not a valid option.\""
        l talk "\"He is the commander of this ship.\""
        ad talk "\"Is that so?\""
        ad talk "\"And where is he? Where can I find him?\""
        l talk "\"Why the hell do you want to know?\""
        ad talk "\"My mother has been here on this ship for a while.\""
        ad talk "\"I was conceived here not too long ago and I want to know who my father is.\""
        ad talk "\"I know it's not any of the males currently on board since I've compared all the DNA.\""
        ad talk "\"That leaves the mysterious [mc] which I can't find anywhere.\""
        l talk "\"Why don't you go and ask your whore mother?\""
        ad talk "\"Heh. I did ask her. She refuses to tell me because 'it's not my time yet'. So I am taking the initiative into my own hands.\""
        ad talk "\"So? Who and where is he?\""
        
        scene ch14 lab 12
        with vpunch
        l talk "\"*Spit*\""
        l talk "\"Go to hell. I am not telling you anything.\""
        
        scene ch14 lab 13
        with sshake
        "..."
        ad talk "\"Did you just...\""
        
        scene ch14 lab 14
        with vpunch
        ad talk "\"{size=+10}You fucking bitch!{/size}\""
        with sshake
        ad talk "\"You are fucking lucky I am not my mother.\""
        ad talk "\"If it was her, your head would be ripped off in an instant.\""
        
        scene ch14 lab 15
        ad talk "\"You think you are a tough bitch?\""
        ad talk "\"You don't know anything.\""
        ad talk "\"But my patience is running thin, so keep testing it and see what happens.\""
        l talk "\"Do your worse.\""
        
        scene ch14 lab 16
        with dissolve
        ad talk "\"You know... I always admired you.\""
        ad talk "\"You were a really good sparring partner.\""
        scene ch14 lab 17
        ad talk "\"Thanks to you I can defend myself a lot better.\""
        ad talk "\"Of course I accelerated way faster and you are no match to me at this point in time.\""
        scene ch14 lab 18
        ad talk "\"But I still admire you. You never backed down.\""
        ad talk "\"But don't think for a moment that I won't break you in half.\""
        scene ch14 lab 19
        ad talk "\"Your perfect little body.\""
        ad talk "\"It will be a shame if something...happened to it.\""
        
        scene ch14 lab 20
        ad talk "\"We wouldn't want that, right?\""
        ad talk "\"You are still young. But if you continue to piss me off...\""
        ad talk "\"I will shove my hand so far up your cunt that it will come out the other side.\""
        "..."
        "... ..."
        "... ... ..."
        ad talk "\"Yeah? I see.\""
        scene ch14 lab 21
        with pushright
        ad talk "\"Perhaps you won't talk. And it will be a shame to die like that when you have a much better use to me.\""
        ad talk "\"But I am sure one of the little girls will be more than willing to spill their guts as I do this to them.\""
        scene ch14 lab 22
        "..."
        with sshake
        l talk "\"{size=+10}WAIT!{/size}\""
        
        scene ch14 lab 23
        l talk "\"I will talk...\""
        l talk "\"Okay? Just...\""
        
        scene ch14 lab 24
        l talk "\"Just don't hurt them...\""
        l talk "\"I will tell you whatever you want to know...\""
        ad thinking "Heh. I knew you had a weak spot."
        jump ch14town1
        
label ch14town1:
    with fasterfadein
    scene afewhourslater
    $ quick_menu = False
    $ renpy.pause(2, hard=True)
    with fasterfadeout
    scene ch14 town 1
    with fadein
    $ quick_menu = True
    
    stop music fadeout 5.0
    play music "music/Eastern Thought.mp3" fadein 10.0
    
    eli talk "We are here, [mc]."
    
    scene ch14 town 2
    mc elitalk "So..."
    mc elitalk "What now?"
    
    scene ch14 town 3
    with dissolve
    eli talk "Now we need to locate ou' guy. His name be Walter."
    eli talk "He should be aroun' here..."
    
label ch14town2:
    $ _skipping = False
    $ quick_menu = False
    show screen ch14_town_clickable
    $ renpy.pause(9999, hard=True)

    
label ch14woman1:
    $ quick_menu = True
    hide screen ch14_town_clickable
    eli thinking "A woman in dress standing on the stairs."
    eli thinking "Not who we be lookin' for."
    jump ch14town2
        
label ch14woman2:
    $ quick_menu = True
    hide screen ch14_town_clickable
    eli thinking "A girl walking down the street."
    eli thinking "Not who we be lookin' for."
    jump ch14town2
        
label ch14couple:
    $ quick_menu = True
    hide screen ch14_town_clickable
    eli thinking "A couple chatting."
    eli thinking "Neitha' of 'em is our target."
    jump ch14town2
        
label ch14drunk:
    $ quick_menu = True
    hide screen ch14_town_clickable
    eli thinking "A drunk shouting loudly."
    eli thinking "Not who we be lookin' for."
    jump ch14town2
    
label ch14mysterious:
    hide screen ch14_town_clickable
    $ quick_menu = True
    eli thinking "Looks like a mercenary of some sort."
    eli thinking "Not who we be lookin' for."
    jump ch14town2
        
label ch14town3:
    hide screen ch14_town_clickable
    $ quick_menu = True
    $ _skipping = True
    
    scene ch14 town 4
    with fasterfadein
    eli talk "Dat be him!"
    eli talk "He be scouting around and waitin'."
    eli talk "We must get his approval at all costs in order to get to the Queen."
    
    scene ch14 town 5
    with dissolve
    mc elithinking "How do we do that?"
    eli talk "First we be having to get really classy."
    
    scene ch14 town 7
    with dissolve
    eli talk "We need new clothes. The rags on me won't help to charm 'tis fool."
    mc elithinking "By charm you mean..."
    
    scene ch14 town 6
    with pushleft
    eli talk "That's right. We will need to charm our way to the Queen's private quarters through this prick."
    mc elithinking "Oh shit..."
    eli talk "Heh. I did warn you about dealin' with female stuff."
    eli talk "Our best bet be the merchant over there."
    
    scene ch14 town 8
    with dissolve
    eli talk "Let's go before we lose track of our target."
    
    scene ch14 town 12
    with fasterfadein
    
    qm merchanttalk "\"Hello, beautiful lady! Welcome to my store! We have everything you might possibly need in terms of clothes.\""
    qm merchanttalk "\"A fine selection just arrived across the sea. Exotic and pretty just like you!\""
    
    eli talk "My, my... he be charmin'."
    
    scene ch14 town 10
    with pushright
    
    eli thinking "How should we do this, [mc]?"
    eli talk "Try and use a spell on him or wait for a good moment to steal?"

    $ quick_menu = False
    menu:
        "Brainwash him":
            $ quick_menu = True
            $ch14_brainwash = True
            $ch14_steal = False
            mc elitalk "Do a spell on him."
            eli talk "I got it."
            
            scene ch14 town 9
            eli talk "\"Look into my eyes...\""
            "..."
            eli talk "\"I be needin' new clothes. You can provide fo' me, yes?\""
            scene ch14 town 11
            with sshake
            qm merchanttalk "\"A-A-Ahh... Y-Yes.\""
            qm merchanttalk "\"P-Please choose whatever you want. It's on me.\""
            scene ch14 town 14
            with dissolve
            eli talk "\"How generous of you...\""
            eli talk "\"I be likin' this one a lot. Thank you~!\""
            qm merchanttalk "\"M-My pleasure! Please come again!\""
            scene ch14 town 15
            with pushright
            eli talk "\"I might just do that.\""
            eli talk "\"Hahaha-ha.\""
            eli talk "We need to find somewhere to change now."
            jump ch14town4
        "Steal":
            $ quick_menu = True
            $ch14_brainwash = False
            $ch14_steal = True

            mc elitalk "Let's wait a bit and try to steal it."
            eli talk "Sure. I be fast with my hands."
            scene ch14 town 13
            with fadein
            "You wait a bit until the merchant turns his back."
            eli talk "Now be a good time."
            
            scene ch14 town 14
            "You look around and move in very quick and grab the one that caught your eye."
            scene ch14 town 15
            with pushright
            eli talk "Nice and easy."
            eli talk "We need to find somewhere to change now."
            jump ch14town4
    
label ch14town4:
    
    scene ch14 town 16
    eli talk "'Tis be a good spot. Hard for someone to see us change here."
    mc elithinking "You think this will work?"
    
    $ quick_menu = False
    scene ch14 town 17 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(5, hard=True)
    $ quick_menu = True
    
    eli talk "It will work."
    
    $ quick_menu = False
    scene ch14 town 17x with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(6.5, hard=True)
    $ quick_menu = True
    
    scene ch14 town 18
    with fasterfadein
    
    eli talk "But you understand what might be needin' to happen, right?"
    mc elitalk "What?"
    eli talk "He be a pig. He might want more than just a pretty dress."
    
    scene ch14 town 19
    with dissolve
    "You leave the alleyway."
    eli talk "If he does... we have no choice in da matter and have to oblige to his every wish."
    mc elitalk "Why though? Can't you use your 'magic' on him?"
    eli talk "I wish it be that simple. Unfortunately my magic is not guaranteed to work and we can't afford to blow our cover."
    mc elitalk "Fuck. This sucks."
    
    scene ch14 town 20
    with dissolve
    eli talk "You can always stay in da 'dark' and not see anythin' if it comes to dat."
    mc elitalk "That's comforting at least, but you..."
    eli talk "Don't be worryin' 'bout me."
    eli talk "I find satisfaction and pleasure in everythin'."
    
    scene ch14 town 21
    with dissolve
    eli talk "He be alone. Now is da time."
    eli talk "Here we go."
    
    scene ch14 town 22
    with fasterfadein
    "You move closer to Walter."
    walter talk "\"Hmm?\""
    
    $ renpy.show("ch14_walter_eye")
    
    "Walter eyeing you from head to toe, very carefully checking your whole body."
    walter talk "\"Very nice. Turn around."
    
    scene ch14 town 24
    with dissolve
    "Elisande turns around."
    walter talk "\"Mmmm, yes. Excellent curves.\""
    
    scene ch14 town 25
    with dissolve
    "You turn back around."
    eli talk "\"I be here fo' a chance to meet da Queen.\""
    eli talk "\"I hea' the way is through you.\""
    
    scene ch14 town 23
    with dissolve
    
    walter talk "\"You heard right.\""
    walter talk "\"But having curves and a nice body is not enough.\""
    walter talk "\"It takes a bit more if you catch my drift.\""
    
    scene ch14 town 25
    with dissolve
    mc elidresstalk "This bastard..."
    eli dresstalk "\"Yes, 'course. It's only natural for you to be testin' the stock before you present it to da Queen he'self.\""
    
    scene ch14 town 26
    with dissolve
    walter talk "\"That's good. I am glad you understand how this is done.\""
    walter talk "\"I know just the way for us to conduct our 'business'. Follow me.\""
    
    scene ch14 town 27
    with fasterfadein
    "Elisande follows Walter to a secluded alleyway down in the slums..."
    walter talk "\"This will have to do.\""
    "You watch as Walter undresses near the canal..."
    
    scene ch14 town 28
    with dissolve
    "Before you can even say anything he drops his pants dpwm and takes out his cock."
    "..."
    walter talk "\"Now, show me how badly you want to see the Queen.\""
    
    scene ch14 town 29
    with dissolve
    "Elisande kneels down next to Walter."
    mc elidresstalk "Ugh......it reeks...."
    eli dresstalk "Now be the time to black out your view and senses, [mc]."
    eli dresstalk "Unless you don't mind what about to be happenin'"

    $ quick_menu = False
    menu:
        "Watch what happens":
            $ch14_watched_elisande = True
            jump ch14town5
        "Don't":
            $ch14_watched_elisande = False
            jump ch14town6
    
label ch14town5:
    $ quick_menu = True
    scene ch14 handjob
    with dissolve
    "You decide you want to see what happens..."
    eli dresstalk "\"Let's take care of this fella now shall we?\""
    $ quick_menu = False
    show screen ch14_walter_handjob
    $ renpy.show("ch14_walter_handjob")
    $ renpy.pause(12, hard=True)

    label ch14_walter_handjob:
    hide screen ch14_walter_handjob
    
    $ quick_menu = True
    
    scene ch14 blowjob
    with vpunch
    walter nudetalk "\"Now suck me, bitch!\""
    $ quick_menu = False
    show screen ch14_walter_blowjob
    $ renpy.show("ch14_walter_blowjob")
    $ renpy.pause(12, hard=True)

    label ch14_walter_blowjob:
    hide screen ch14_walter_blowjob
    
    $ quick_menu = True
    walter nudetalk "\"Ugh. That's right, bitch. Suck me faster.\""
    
    $ quick_menu = False
    show screen ch14_walter_blowjob2
    $ renpy.show("ch14_walter_blowjob2")
    $ renpy.pause(12, hard=True)

    label ch14_walter_blowjob2:
    hide screen ch14_walter_blowjob2
    $ quick_menu = True
    eli dresstalk "\"*Suck*, *Slurp*, *Succ*...\""
    
    walter nudetalk "\"Ahh...\""
    
    scene ch14 walter cum 1
    with dissolve
    
    walter talk "\"Take it all, whore!\""
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch14 walter cum 1
    with Dissolve(1)
    scene white
    pause 1
    
    scene ch14 walter cum 2
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch14 walter cum 2
    with Dissolve(1)
    
    eli dresstalk "\"*Gulp*, *Gulp*, *Gulp*\""
    "Walter holds Eli's head down, making her gag and swallow most of his semen."
    
    scene ch14 walter cum 3
    with sshake
    "After emptying his balls, he releases her."
    
    scene ch14 walter cum 3
    with sshake
    walter talk "\"Your mouth is such a good fuck hole. I enjoyed it.\""
    
    scene ch14 walter cum 4
    with dissolve
    eli dresstalk "\"... *Cough* So I get to see da Queen now?\""
    walter talk "\"You know what? Sure. You were the best one today.\""
    walter talk "\"I will let the guards know to let you pass.\""
    
    scene ch14 town 30
    with dissolve
    walter talk "\"See ya.\""
    "And just like that the man leaves.\""
    
    scene ch14 town 31
    with dissolve
    mc elidresstalk "One step closer."
    eli dresstalk "Oh? You watched? Didn't expect that."
    eli dresstalk "Did ya enjoy it?"
    mc elidresstalk "Let's just say you are good at what you do."
    eli dresstalk "Hahaha. Good answer."
    eli dresstalk "Let's go now. Da Queen awaits."
    jump ch14town7
    
label ch14town6:
    $ quick_menu = True
    scene black
    with Dissolve(1)
    "You try to block every sound and picture."
    "After a few minutes you hear Elisande call for you."
    eli dresstalk "[mc]? It be over now. It's safe to look."
    
    scene ch14 town 31
    with dissolve
    mc elidresstalk "Shit... I can still feel it."
    eli dresstalk "You will have to endure it a bit longer."
    eli dresstalk "Let's go now. Da Queen awaits."
    jump ch14town7
    
    
    
    
label ch14town7:
    scene ch14 town 32
    with fadein
    "You move to the castle's gates."
    "Immediately the guards stop you from proceeding any futher."
    "You let the guards know you are to meet the Queen on Walter's orders."
    
    scene ch14 town 33
    with dissolve
    "They inspect you for any weapons and start escorting you to the Queen's private quarters."
    
    scene black
    with Dissolve(1)
    pause 1
    
    scene ch14 queen 1
    with fasterfadein
    "The guard takes you to the door and let's you know that he will be outside."
    
    scene ch14 queen 2
    with dissolve
    
    eli dresstalk "Ok, this is it, [mc]."
    eli dresstalk "We gotta be careful now. Please the Queen and then we will have enough time to find da plant."
    eli dresstalk "Will you stay and watch?"
    mc elidresstalk "I have no problem with this sort of thing. Hehe."
    eli dresstalk "Ha. I thought so."
    
    scene ch14 queen 3
    with dissolve
    "You knock on the door."
    "You hear a faint voice from the other side saying 'Come in.'."
    
    scene ch14 queen 4
    with fasterfadein
    "You open the door and enter the Queen's private chamber."
    
    $ quick_menu = False
    scene ch14 queen 5 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(5, hard=True)
    $ quick_menu = True
    
    "You stare at her with your mouth wide open."
    
    scene ch14 queen 6
    with dissolve
    dany gowntalk "\"So, you are the one chosen to entertain me today?\""
    dany gowntalk "\"I like dark skinned girls.\""
    
    scene ch14 queen 7
    with dissolve
    
    eli dresstalk "\"Yes, my Queen.\""
    eli dresstalk "\"It be a pleasure to serve you today.\""
    
    scene ch14 queen 6
    with dissolve
    
    dany gowntalk "\"Good. Well I have a lot of stress on my plate from some recent events...\""
    
    if ch13_chopped_ramsay_head:
        dany gowntalk "\"My commander got decapitated by prisoners.\""
        dany gowntalk "\"I showed weakness and this is what happened.\""
    else:
        dany gowntalk "\"My commander bled through the castle and died in my arms, murdered by prisoners.\""
        dany gowntalk "\"I showed weakness and this is what happened.\""
    
    dany gowntalk "\"Anyway... enough of that. You are here for other reasons.\""
    dany gowntalk "\"Are you experienced in sex?\""
    
    eli dresstalk "\"Yes, Your Grace.\""
    
    scene ch14 queen 8
    with dissolve
    
    dany gowntalk "\"I like your clothing style. But I will like seeing you nude more. Now!\""
    
    eli dresstalk "\"At once, Your Grace.\""
    
    scene ch14 queen 9
    with dissolve
    "You quickly strip down from your clothes."
    dany gowntalk "\"That's good.\""

    dany gowntalk "\"You have such a lovely painted body.\""
    dany gowntalk "\"Very exotic.\""
    
    dany gowntalk "\"Makes me want to worship someone else for a change.\""
    
    scene ch14 queen 10
    with dissolve
    "The Queen quickly puts her mouth on Elisande's breasts and starts suckling her nipples."
    
    dany talk "\"*Suck*, *Suck*, *Shlrup*, *Lick*\""
    
    scene ch14 queen 11
    with dissolve
    eli nudetalk "\"Ahh!\""
    dany talk "\"So *Slurp* delicious.\""
    
    scene ch14 queen 12
    with dissolve
    dany talk "\"Your aroma is so intoxicating.\""
    dany talk "\"Get on the bed and spread those chocolate legs for me!\""
    
    scene ch14 queen 13
    with dissolve
    "Obeying the Queen's demands, Elisande goes on the bed and spreads her legs."
    eli nudetalk "\"This is okay?\""
    dany nudetalk "\"Perfect!\""
    
    scene ch14 queen 14
    with fasterfadein
    "Dany removes her nightgown and reveals her nude body to you."
    dany nudetalk "\"Mmm, I can't wait to taste your bush, you little minx.\""
    

    scene ch14 queen 15
    with sshake
    eli nudetalk "\"I can't wait eit--\""
    with sshake
    eli nudetalk "\"Ahh~!\""
    $ quick_menu = False
    show screen ch14_dany_cunnilingus
    $ renpy.show("ch14_dany_cunnilingus")
    $ renpy.pause(12, hard=True)

    label ch14_dany_cunnilingus:
    hide screen ch14_dany_cunnilingus
    
    $ quick_menu = True
    
    eli nudetalk "\"Ahhh, AHHHHH~!\""
    
    with sshake
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch14 queen 15
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch14 queen 15
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch14 queen 16
    with Dissolve(1)
    
    "With a huge squirt, Elisande splatter the Queen's face with her juice.\""
    dany nudetalk "\"*Slurp*, *Succ*, *Kiss*\""
    
    scene ch14 queen 15
    with dissolve
    
    dany nudetalk "\"Mmm, delicious!\""
    dany nudetalk "\"But we are far from being done.\""

    scene ch14 queen 17
    with fasterfadein
    "You continued having sex doing all sorts of different dirty things to each other."
    
    scene ch14 queen 18
    with dissolve
    "Tasting every bit of each other's juices."

    scene ch14 queen 19
    with fasterfadein
    "Sucking each other's toes."

    scene ch14 queen 20
    with fasterfadein
    "Licking every part of the body for maximum pleasure."
    dany nudetalk "\"Time for you to pleasure me, ok?\""
    
    scene ch14 queen 21
    with fasterfadein
    "And just like that Dany positions herself and pushes her ass in Elisande's face."
    dany nudetalk "\"Eat and clean my ass!\""

    dany nudetalk "\"AHHH~!!\""
    
    scene ch14 queen 21
    with vpunch
    dany nudetalk "\"FUUUUUUUUUUUUUUUUCK!!!!!!\""
    with sshake
    with sshake
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch14 queen 21
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    
    scene ch14 queen 22
    with Dissolve(1)
    "The Queen squirms and squirts right into Elisande's mouth."
    eli nudetalk "\"*Slurp* *Gulp*\""
    
    scene black
    with Dissolve(1)
    pause 1
    
    scene ch14 queen 23
    with fasterfadein
    "Dany faints from the pleasure."
    
    eli nudetalk "\"Hahh, Ahh, Hahh...\""
    mc elinudetalk "Holy shit... this was..."
    eli nudetalk "I know..."
    eli nudetalk "It's good she is out fo' now. We can focus on our main goal."

    scene ch14 queen 24
    with fasterfadein
    eli talk "\"While we be here we next to the Queen, we could kill two birds with one stone.\""
    mc ctalk "\"What do you have in mind?\""
    eli talk "\"Da Queen won't stop searchin' fo' you now that you've done the damage you've done.\""
    eli talk "\"It'd be safer if we--\""
    mc ctalk "\"No... I don't want to kill her like this.\""
    mc ctalk "\"And if we remove her from her position someone else might take over, far, far worse.\""
    eli talk "\"... That be true...\""
    eli talk "\"I was going to suggest to try and conjure a spell on her while she be sleepin'. It could change everythin'.\""
    mc ctalk "\"You can do that? It will be of great help if she left Ingrid and the rest alone.\""
    eli talk "\"Yes. I will do that.\""
    mc ctalk "\"There's one more thing...\""
    eli talk "\"I know already what you want to ask.\""
    eli talk "\"That blue skinned girl. You want to free her.\""
    mc ctalk "\"Yes...\""
    eli talk "\"I will try to add that to the spell on her and make her release her.\""
    eli talk "\"There'd be no way fo' her to escape right now with such a tight security everywhere.\""
    mc ctalk "\"As long as the spell works...\""
    eli talk "\"It will have to work.\""
    eli talk "\"I didn't expect her to faint, so this might be our only chance for the spell of manipulation to work.\""
    mc ctalk "\"Let's do it.\""
    
    
    scene ch14 queen 25
    with dissolve
    "Elisande kneels down next to Dany..."
    "She starts chanting and whispering magical words in the Queen's ear."
    eli nudetalk "\"soteela Fa, Fa lasotee, Solala soteelala someelasotee sosotee soteelaso So so meela meelasolaso meelaso meeteelaso, Solateemee, tee teelaso teelalaso, Meela solatee, lalaso mee, meemeesotee.\""
    eli nudetalk "\"Teemeelasoso tee meela lasodoh meelaso Meela soteela meeteelaso, meela meesolamee, Meelasola solala, meela teelamee, Meela tee soteesolamee teeso lasomee.\""
    eli nudetalk "\"So meela lasomee, lalaso mee, meemeesotee, So meedoh soso teesoso la lalasotee lalatee sola, Tee meesoso, dohla mee! So meelamee teesotee lasosotee solasotee lala, Tee meesoso, dohla mee! Lala Fa Teesosolamee somee, Lasomee latee raysolala lasotee teeteela Sosotee, Sola latee meelasomeetee teeteela Sosotee. Dohteelaso Fa, Someelaso Sorayla, Dohteelaso Tee, Sorayla someelaso!\""
    
    scene ch14 queen 26
    with fasterfadein
    "Elisande finish casting the spell and moves away."
    eli nudetalk "This will have to do."
    eli nudetalk "Now we need to find the plant fo' creating the antidote."
    eli nudetalk "Let's go now, before she wakes up."
    
    scene ch14 queen 27
    with fasterfadein
    "You dress back up and leave the Queen's room and meet the guard outside."
    "You explain to him that the Queen ordered for him to guard her until she is done resting."
    
    "With that you leave and go down the hallway..."
    
label ch14tower:
    scene ch14 queen 28
    with Dissolve(1)
    "You go through many different rooms & corridors and begin to think you are never going to find anything in here."
    
    scene ch14 tower 1
    with fasterfadein
    
    "You begin worrying until you reach a tower of some sort in the north side of the castle."
    
    scene ch14 tower 2
    with dissolve
    "You open the large metal door."
    "..."
    mc elidresstalk "Holy...shit..."
    mc elidresstalk "Look at all of this."
    
    scene ch14 tower 3
    with pushright
    eli dresstalk "We are not here for treasure, [mc]. Don't be forgettin' our main goal."
    
label ch14tower1:
    $ _skipping = False
    $ quick_menu = False
    show screen ch14_tower_clickable
    $ renpy.pause(9999, hard=True)
        
label ch14towergold1:
    hide screen ch14_tower_clickable
    $ quick_menu = True
    eli dresstalk "A large pile of gold."
    eli thinking "Villagers be starvin' while the Queen is hoarding so much money...Bitch."
    jump ch14tower1
        
label ch14towergold2:
    hide screen ch14_tower_clickable
    $ quick_menu = True
    eli dresstalk "A large pile of gold."
    mc elidresstalk "I could literally swim in there."
    jump ch14tower1
        
label ch14vase:
    hide screen ch14_tower_clickable
    $ quick_menu = True
    eli dresstalk "A vase full of jewelry, diamonds and gold chains."
    mc elidresstalk "They won't notice if one thing is missing."
    eli dresstalk "Don't even think about it."
    jump ch14tower1
    
label ch14goblet:
    hide screen ch14_tower_clickable
    $ quick_menu = True
    eli dresstalk "A golden goblet on display."
    eli dresstalk "Looks very expensive."
    jump ch14tower1  
    
label ch14tower2:
    hide screen ch14_tower_clickable
    $ quick_menu = True
    $ _skipping = True
    
    scene ch14 tower 4x
    with dissolve
    eli dresstalk "I see it!"
    eli dresstalk "This be it!"
    
    scene ch14 tower 4
    with dissolve
    "You move closer to inspect it."
    eli dresstalk "Gettin' a single leaf should do da work!"
    mc elidresstalk "Let's grab this and get da hell outta h---"
    with sshake
    mc elidresstalk "W-What was that?!"
    with vpunch
    
    scene ch14 tower 5
    with sshake
    "A loud rumble stops you in your tracks."
    
    mc elidresstalk "Oh...my..."
    
    scene ch14 tower 6
    with dissolve
    "You slowly move your head up to see."
    
    
    scene ch14 tower 7
    with vpunch
    qm reddragon "\"{size=+12}GROOWWRR!! SCREEEEEEEECH~!\""
    with sshake
    with sshake
    
    scene ch14 tower 8
    with sshake
    "A very large and armored red dragon looms over Elisande's head..."
    "The loud roar from the beast shakes up the whole tower."
    
    scene ch14 tower 9
    with dissolve
    eli dresstalk "Don't... be movin'... a muscle..."
    
    scene ch14 tower 10
    with dissolve
    "The dragon moves his head close to Elisande's face."
    eli dresstalk "\"Ugh...\""
    
    scene ch14 tower 11
    with dissolve
    "He takes out his tongue and licks your whole face."
    mc elidresstalk "What is he... doing..."
    
    scene ch14 tower 12
    with dissolve
    eli dresstalk "We must have the scent of the Queen on us."
    eli dresstalk "Perhaps that be the only reason he hasn't eaten us yet..."
    mc elidresstalk "How do we get out of this situation now..."
    
    scene ch14 tower 13
    with fasterfadein
    "While contemplating your own doom, you hear the door behind you open."
    
    mc elidresstalk "Oh. Thank the Gods! I hope we can get out of this situation somehow."
    
    scene ch14 tower 15
    with dissolve
    dany talk "\"Well, well, well...\""
    dany talk "\"What do we have here?\""
    
    dany talk "\"You leave my chambers without my order, you tell my guard a lie and you wonder around my castle without my permission?\""
    dany talk "\"You know I execute people for way less than that.\""
    
    scene ch14 tower 14
    with dissolve
    mc elidresstalk "This is bad."
    mc elidresstalk "Let me handle this situation. I've interacted with her before and know her a little bit."
    eli dresstalk "Okay. If you are sure, go for it."
    
    
    scene ch14 tower 17
    with dissolve
    mc elidresstalk "\"I am sorry, okay?\""
    mc elidresstalk "\"I know how this looks, but I am trying to save someone.\""
    
    scene ch14 tower 16
    with dissolve
    dany talk "\"Save someone?\""
    with sshake
    dany talk "\"By stealing my treasure?!\""
    
    scene ch14 tower 17
    with dissolve
    
    mc elidresstalk "\"N-No! I wasn't going to steal any of your gold.\""
    mc elidresstalk "\"I need this here for an antidote for a poison.\""
    mc elidresstalk "\"It can't be found anywhere else in the kingdom and time is short.\""
    
    scene ch14 tower 16
    with dissolve
    dany talk "\"Antidote? You mean...\""
    dany talk "\"One of my guards did something to someone you know?\""
    
    scene ch14 tower 17
    with dissolve
    mc elidresstalk "\"Yes, my Queen... It's the only way to save the person's life.\""
    
    scene ch14 tower 16
    with dissolve
    dany talk "\"Either way, you should've asked me first.\""
    "..."
    
    scene ch14 tower 17
    with dissolve
    mc elidresstalk "\"I know I should have...\""
    mc elidresstalk "\"I was just scared you might refuse.\""
    
    scene ch14 tower 19
    with dissolve
    "..."
    dany talk "\"You know what?\""
    dany talk "\"I am feeling merciful today.\""
    dany talk "\"And you did bring me a lot of pleasure, so much so that I fainted.\""
    dany talk "\"I will let you keep your life.\""
    
    scene ch14 tower 21
    with dissolve
    mc elidresstalk "\"T-Thank you, your Grace!\""
    "..."
    mc elidresstalk "\"A-And...t-the antidote?\""
    
    scene ch14 tower 19
    with dissolve
    dany talk "\"I will let you have it...\""
    dany talk "\"On one condition.\""
    
    scene ch14 tower 20
    with dissolve
    mc elidresstalk "\"W-What is it?\""
    
    scene ch14 tower 18
    with dissolve
    dany talk "\"You will move in here with me. I will get you a room next to me and we can keep each other company.\""
    dany talk "\"Since I enjoyed our time together quite a bit.\""
    dany talk "\"So? What do you say?\""

    $ quick_menu = False
    scene ch14 tower 20
    with dissolve
    menu:
        "Accept and pledge Elisande's body to her":
            $ ch14_elisande_body_pledged = True
            $ quick_menu = True
            mc elidresstalk "I can't let you become her slave..."
            mc elidresstalk "This is going way out of hand."
            mc elidresstalk "We shoul--\""
            eli dresstalk "It's fine, [mc]."
            eli dresstalk "We came to do one job and we be finishing that job."
            eli dresstalk "And it wasn't as bad as you might think fo' me."
            jump ch14tower3
            
        "Refuse":
            $ ch14_elisande_body_pledged = False
            jump ch14elibodyending
            

label ch14tower3:
    eli dresstalk "\"I accept your offer.\""
    
    scene ch14 tower 19
    with dissolve
    dany talk "\"Great!\""
    dany talk "\"We will have a lot of good moments together, my dear.\""
    dany talk "\"I was looking for a partner for a long time. But let's see where our relationship takes us.\""
    
    scene ch14 tower 20
    with dissolve
    dany talk "\"Now, I will let you take the antidote to your friend to save his life...\""
    dany talk "\"I expect you to come back in a fortnight.\""

    eli dresstalk "\"Thanks and I will.\""
    
    scene ch14 tower 22
    with dissolve
    "You take a leaf from the plant and make your way out of there."
    
    jump startch15
            
label ch14elibodyending:
    $ quick_menu = True
    scene ch14 tower 21
    with dissolve
    mc elidresstalk "\"No. I will have to refuse that offer...your Grace.\""
    mc elidresstalk "\"I can't pledge myself like that.\""
    
    scene ch14 tower 21
    with sshake
    dany talk "\"Really now?\""
    dany talk "\"I expected more cooperation, considering your position right now.\""
    dany talk "\"But that's fine. I am a woman of my word. I will spare your life. But don't ever show your face around here ever again or I will have you executed on the spot.\""
    dany talk "\"Understand me?\""
    
    scene ch14 tower 16
    with dissolve
    mc elidresstalk "\"Yes... your Grace.\""
    dany talk "\"Good. Now get out of here.\""
    
    scene ch14 tower 22
    with dissolve
    "You leave the castle and make your way back..."
    
    scene ch14 ending 1
    with fadein
    "Luna and Ingrid were at the beach where you last saw them, anticipating your return."

    
    scene ch14 ending 2
    with dissolve
    "You explain the situation to Luna and Ingrid..."
    "The mixed feelings were very obvious."
    "Some were dissapointed and angry."
    "Others more understandable and supportive."
    
    scene black
    with Dissolve(1)
    scene ch14 ending 3
    with fasterfadein
    "Some weeks pass since then and you begin to feel more home than ever before with Elisande."
    
    scene ch14 ending 4
    with fasterfadein
    "Your old body eventually died out. You had a funeral for yourself with no name on the tombstone."
    "To you it just feels like an old shell at this point. Like a snake that shed it's skin."
    "You've accepted your new body and Elisande has accepted you."
    
    if ch14_ingrid_preference:
        scene ch14 ending 5
        with fasterfadein
        "You also found love."
        "It was hard at fisrt for Ingrid, but she eventually accepted your new body and co-partner."
        
        scene ch14 ending 6
        with fasterfadein
        "You spend more time with Ingrid and the feelings become mutual not only for you, but for Elisande as well."
        
        scene ch14 ending 7
        with fasterfadein
        "After some time you gave up on any way to communicate with Paradise and your old crew."
        "You were secretly hoping they were still out there, but at this point in time you were home."
        
        scene ending 2
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
        scene ch14 ending 8
        with fasterfadein
        "You also found love."
        "Luna accepted you and Elisande and was open to the relationship from the start."
        
        scene ch14 ending 9
        with fasterfadein
        "You spend more time with Luna and the feelings become mutual not only for you, but for Elisande as well."
        
        scene ch14 ending 10
        with fasterfadein
        "After some time you gave up on any way to communicate with Paradise and your old crew."
        "You were secretly hoping they were still out there, but at this point in time you were home."
        
        scene ending 2
        with fadein
        $ quick_menu = False
        pause 1.5
        $ quick_menu = True
        voidstar talk "\"{size=+10}Congratulations{/size} on reaching one of the multiple endings the game has to offer!\""
        voidstar talk "\"Many thanks to my patrons and supporters throughout the 2 years of development. This game was made possible thanks to all of you.\""
        voidstar talk "\"Thanks to everyone who spread the word about the game and kept the community going! You all rock!\""
        voidstar talk "\"For more news and updates about future projects, follow me on my {a=https://www.patreon.com/VoidStar}{color=#FF6600}Patreon{/color}{/a}\""
        
        jump thanks
