label startch12:
    scene black
    with fasterfadein
    "A few minutes pass and one of the girls comes back with a cup."
    
    scene ch12camp3
    with dissolve
    
    ivy talk "\"...\""
    ivy talk "\"Come on, drink.\""
    ivy talk "\"If I wanted to kill you I wouldn't waste my time with poison.\""
    ivy talk "\"This will be all the hydration you will be getting for the night and believe me you will need it.\""
    $ quick_menu = False
    menu:
        "Drink":
            jump ch12camp1
            
label ch12camp1:
    $ quick_menu = True
    scene ch12camp4
    with dissolve
    "You open your mouth."
    mc nudethinking "She is right. If she wanted to kill me why bother with this?"
    
    scene ch12camp5
    with dissolve
    "\"*Gulp*, *Gulp*, *Gulp*\""
    
    scene ch12camp3
    with fasterfadein
    "You drink the everything you were given."
    ivy talk "\"Good boy. Now wait patiently.\""
    
    scene ch12camp6
    with dissolve
    "You try to overhear the conversation, but can barely hear what they are talking about..."
    "You do hear a few sentences though..."
    
    ingrid talk "\"...So he drank it all down?...\""
    ivy talk "\"Every last drop.\""
    ingrid talk "\"Should be any moment now...\""
    
    mc nudethinking "What the fuck are they saying?"
    "You feel your cock twitch all of sudden."
    
    scene ch12erection
    with dissolve
    $ quick_menu = False
    $ renpy.show("ch12_mc_erection")
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(3, hard=True)

label ch12_mc_erection:
    $ quick_menu = True
    scene ch12camp7
    with dissolve
    
    mc nudeshocked "\"Whoa,whoa,whoa!\""
    mc nudetalk2 "\"What the fuck is happening?\""
    mc nudeshocked "\"What the fuck did you give me?\""
    ivy talk "\"Water, of course. But with something extra.\""
  
    scene ch12camp9
    with dissolve
    
    "You look up and see the girl already undressed."
    ivy talk "\"You probably thought we'd beat the truth out of you.\""
    ivy talk "\"We have a much better system in place here.\""
    ivy talk "\"We will ride you until sunrise and until your cock starts to hurt from all the fucking you are going to receive.\""
    
    scene ch12footjob
    with dissolve
    ivy talk "\"You might enjoy this at first, but your enjoyment will soon fade away.\""
    
    show screen ch12_ivy_fj
    $ quick_menu = False
    $ renpy.show("ch12_ivy_fj")
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(12, hard=True)

label ch12_ivy_fj:
    hide screen ch12_ivy_fj
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch12campcum1
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch12campcum1
    with Dissolve(1)
    $ quick_menu = True
    "Just as you came another girl entered the tent."
    
    scene ch12camp1
    with dissolve
    
    "Your cock was still rock hard."
    
    scene ch12camp2
    with dissolve
    
    "The girl positions herself on top of you..."
    "And guides your penis towards her holes."
    
    show screen ch12_girl_sex
    $ quick_menu = False
    $ renpy.show("ch12_girl_sex")
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(12, hard=True)

label ch12_girl_sex:
    hide screen ch12_girl_sex
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch12campcum2
    with Dissolve(1)

    scene white
    with Dissolve(1)
    pause 1
    
    scene ch12campcum2
    with Dissolve(1)
    $ quick_menu = True
    "The girls know what they are doing and they keep making you cum..."
    "The drug seems super effective too as it keeps your dick hard no matter how many times you came."
    
    scene ch12camp10
    with fasterfadein
    ivy talk "\"Fuck. You still don't want to talk?\""
    ivy talk "\"You're more resilient than I thought.\""
    
    scene ch12camp11
    with dissolve
    ivy talk "\"I am done for tonight, send in the next one.\""
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch12campcum3
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch12campcum3
    with Dissolve(1)
    
    "You kept cumming all night until your balls were completely empty..."
    "Your dick felt sore, but they kept on going."
    
    scene ch12camp12
    with fasterfadein
    
    mira nudetalk "\"*Slurp* Mmmm, ahhh...\""
    mira nudetalk "\"Drained the last bit of regenerated semen out of you I see.\""
    mira nudetalk "\"You really bathed me in your cum.\""
    mira nudetalk "\"I see your dick is starting to go limp. The drug must've wore off.\""
    
    scene ch12camp13
    with dissolve
    "The girl stands and starts to leave."
    "You notice how wet she is... both from cum and sweat."
    mira nudetalk "\"You stay right there. I am going to call Ingrid now.\""
    
    scene black
    with dissolve
    pause 1
    
    scene ch12camp18
    with dissolve
    "You notice the sunrise and hope this is all over now..."
    "As much as you like sex, this was pure torture after the first 2 hours."
    "You satisfied half the camp most likely."
    
    scene black
    with dissolve
    pause 1
    
    scene ch12camp14
    with dissolve
    "After a few minutes you see the girl who is presumably in charge come in."
    ingrid talk "\"So you made it without saying a single word.\""
    ingrid talk "\"Not many people make it through the night without begging or spilling everything they have.\""
    
    scene ch12camp15
    with dissolve
    ingrid talk "\"I guess it's pointless to keep this up any longer.\""
    ingrid talk "\"At this point you are just wasting precious time in actually finding Luna.\""

    scene ch12camp19
    with dissolve
    "At this point you notice her angry expression and the large hunting knife she is holding."
    
    scene ch12camp20
    with dissolve
    mc nudethinking "Oh fuck! This is it... I am actually going to die here."
    scene ch12camp20
    with vpunch
    mc nudeshocked "\"Hey! Stop. Don't do this!\""
    mc nudeshocked "\"I don't know where your friend is! You have to believe me!\""
    scene ch12camp8
    with vpunch
    mc nudetalk3 "\"I can try and help you find her! Just let me live!\""
    
    scene ch12camp16
    with vpunch
    
    ingrid talk "\"Tell me where she is.\""
    ingrid talk "\"This is not a negotiation. You either speak or you die.\""
    mc nudeshocked "\"I told you everything I knew. YOU HAVE TO BELIEVE ME!\""
    
    "..."
    
    "Just as you were contemplating your imminent doom... something unexpected happened."
    
    scene ch12camp21
    with vpunch
    
    "The girl cut the binds instead."
    
    scene ch12camp22
    with dissolve
    
    "You finally get a good feel on your hands after being tied all night."
    
    scene ch12camp23
    with dissolve
    
    mc nudetalk2 "\"You're letting me go?\""
    ingrid talk "\"I am.\""
    ingrid talk "\"No matter how many times we've used this technique we always get the answers we seek by the end.\""
    ingrid talk "\"So I don't think you are lying.\""
    ingrid talk "\"Still, we need to talk.\""
    ingrid talk "\"I left some clothes for you to change into. Your older ones were far too damaged.\""
    mc nudetalk "\"Thank you.\""
    
    scene ch12camp17
    with fasterfadein
    
    ingrid talk "\"Meet me outside when you are ready. I am Ingrid by the way.\""
    mc nudetalk2 "\"[mc].\""
    
    scene ch12camp24
    with fasterfadein
    "You dress up with the clothes you were given."
    mc cthinking "These clothes are nice at least. I really thought they were going to kill me there."
    mc cthinking "I should go and meet with her and see what she has in mind."
    
    scene ch12camp25
    with dissolve
    
    "You get up and leave the tent."
    
    $ persistent.change = "New world 2" #mc in new clothes
    
    scene ch12camp26
    with dissolve
    "You approach Ingrid outside the tent."
    mc ctalk2 "\"Hey. Thanks for the clothes, again.\""
    ingrid talk "\"You're welcome.\""
    ingrid talk "\"Before we proceed with this I need to know...\""
    ingrid talk "\"Can I trust you?\""
    mc ctalk3 "\"Of course. I do want to help you guys.\""
    ingrid talk "\"Good, well, follow me then.\""
    
    scene ch12camp27
    with fasterfadein
    
    "You follow Ingrid to a house that looks like their war council one."
    "You meet a few of the girls which you slept with during the night and introduce yourself to them."
    ivy talk "\"You sure 'bout him? You trust him?\""
    ingrid talk "\"I do. And right now he is here to prove himself.\""
    ingrid talk "\"We don't kill people until we have proof of their guilt.\""
    ingrid talk "\"And I don't intend to hold hostages while Luna is not around.\""
    mira talk "\"About that... is the scout's information reliable?\""
    ivy talk "\"It seems to be. Apparently Luna was spotted being taken to a cave in the eastern mountains in Grëteland.\""
    ingrid talk "\"That will take a few days for us to reach...\""
    ingrid talk "\"It's better to take as few people as possible for this journey.\""
    
    scene ch12camp28
    with vpunch
    ivy talk "\"I want in!\""
    ivy talk "\"I need to do this.\""

    ingrid talk "\"No.\""
    
    scene ch12camp33
    with dissolve
    ivy talk "\"What do you mean no?!\""
    ivy talk "\"You know how much she means to me.\""
    
    scene ch12camp29
    with dissolve
    
    ingrid talk "\"I understand that you want her back. We all do.\""
    ingrid talk "\"But I am in charge right now and I want you to take my place until I come back.\""
    
    scene ch12camp33
    with dissolve
    
    ivy talk "\"You are going!? Alone?\""
    
    scene ch12camp29
    with dissolve
    
    ingrid talk "\"Not alone. I want [mc] to come with me.\""
    ingrid talk "\"Will that be fine with you [mc]?\""
    
    scene ch12camp30
    with dissolve
    
    mc ctalk "\"No problem.\""
    ingrid talk "\"Good.\""

    ivy talk "\"Wait.\""
    
    scene ch12camp34
    with vpunch
    
    ivy talk "\"You can't be serious.\""
    ivy talk "\"You want to take this guy with you instead one of your own?\""
    ivy talk "\"This is a mission to save our leader!\""
    scene ch12camp29
    with dissolve
    ingrid talk "\"I am well aware of that. I will bring her back to you, I promise.\""
    scene ch12camp33
    with dissolve
    ivy talk "\"If that is what you want, then fine.\""
    
    scene ch12camp31
    with dissolve
    
    ingrid talk "\"This is where we are on the map currently.\""
    scene ch12location1
    with Dissolve(1)
    $ quick_menu = False
    $ renpy.pause(3, hard=True)
    scene ch12camp31
    with dissolve
    $ quick_menu = True
    ingrid talk "\"On the way to Grëteland we will need to pass through a desert.\""
    ingrid talk "\"That will be the real challenge along the way there.\""
    
    scene ch12camp32
    with dissolve
    ingrid talk "\"And this is where she was spotted last.\""
    scene ch12location2
    with Dissolve(1)
    $ quick_menu = False
    $ renpy.pause(3, hard=True)
    scene ch12camp32
    with dissolve
    $ quick_menu = True
    ingrid talk "\"It will take a few days for us to reach there with horses.\""
    
    scene ch12camp36
    with dissolve
        
    ingrid talk "\"Let's go and prepare to leave.\""
    ingrid talk "\"Ivy, I am leaving you in charge.\""
    
    scene ch12camp33
    with dissolve
    
    ivy talk "\"Of course. I got this.\""
    mira talk "\"Have a safe journey and bring back Luna!\""
    ingrid talk "\"You got it.\""
    
    scene ch12camp35
    with vpunch
    
    ivy talk "\"Go and wash yourself. You stink.\""
    mira talk "\"I didn't have time for that!\""
    ivy talk "\"Whatever. Your body is oiled with cum. Go and wash now.\""
    
    scene ch12camp37
    with fasterfadein
    "You meet Ingrid outside after she gathered supplies for the trip."
    mc ctalk2 "\"Wait, what is this?\""
    ingrid talk "\"Ah. You've never seen one of those?\""
    ingrid talk "\"It's Luna's horse. They are a rare breed and hard to find and tame.\""
    mc ctalk3 "\"Hah. I can't believe this.\""
    mc ctalk2 "\"Can I pet him?\""
    ingrid talk "\"Sure, he doesn't bite.\""
    
    scene ch12camp38
    with dissolve
    
    mc ctalk "\"Hey there.\""
    mc ctalk2 "\"An actual unicorn.\""
    mc ctalk3 "\"This world is already amazing.\""
    mc ctalk2 "\"So you will be riding him?\""
    ingrid talk "\"Yeah. It's only appropriate for Luna to ride back on her own horse.\""
    
    scene ch12camp39
    with fasterfadein
    "Ingrid gives you a backpack full of supplies as you move towards the gate."
    "You exit and start your journey towards saving their leader."
    
    
    if ch11_saved_ruby:
        jump ch12desert1
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
        
        qm alienntalk "\"Ah, fuck!\""
        "..."
        qm alienntalk "\"I can't...\""
        scene ch12alien1
        with dissolve
        with vpunch
        qm alienntalk "\"Ahhhhhh~!!!\""
        with vpunch
        qm alienntalk "\"It's coming...\""
        with vpunch
        qm alienntalk "\"I can't hold it any longer!\""
        
        scene white
        with Dissolve(1)
        pause 1
        scene ch12alien2
        with Dissolve(1)
        with vpunch
        qm alienntalk "\"Ahhh!!\""
        qm alienntalk "\"Mmmmhhh...ahhh...\""
        scene ch12birth
        with dissolve
        "The female alien lie down on the floor and spreads her legs..."
        
        show screen ch12_alien_birth
        $ quick_menu = False
        $ renpy.show("ch12_alien_birth")
        $ renpy.transition(Dissolve(0.1))
        $ renpy.pause(12, hard=True)

    label ch12_alien_birth:
        hide screen ch12_alien_birth
        $ quick_menu = True
        qm alienntalk "\"Ah... I can feel it...\""
        qm alienntalk "\"My baby pushing against me...\""
        qm alienntalk "\"It's...coming...\""
        qm alienntalk "\"Ahhh~!\""
        
        scene white
        with Dissolve(1)
        pause 1
        
        scene ch12alien3
        with Dissolve(1)
        
        scene white
        with Dissolve(1)
        pause 1
        
        scene ch12alien3
        with Dissolve(1)
        
        qm alienntalk "\"Aghhhhhhh!!\""
        with vpunch
        
        scene white
        with Dissolve(1)
        pause 1
        
        scene ch12alien4
        with Dissolve(1)
        
        with vpunch
        
        qm alienntalk "\"Ah... hahh.... hah....\""
        qm alienntalk "\"My baby...\""
        
        scene ch12alien5
        with dissolve
        qm alienntalk "\"So cute...\""
        qm alienntalk "\"This is [mc]'s and my daughter.\""
        qm alienntalk "\"You have my genes so you will grow to an adult in a matter of days.\""
        qm alienntalk "\"My cute little baby.\""
        qm alienntalk "\"What should I name you?\""
        
        $ alien_daughter = renpy.input("Choose a first name for your 'daughter' \n(or just click enter for a default name)", length=10, with_none=None, pixel_width=None)

        if alien_daughter == "":
            $ alien_daughter="Elisanth"
            
        qm alienntalk "\"Your name is [ad]. My beautiful daughter.\""
        
        scene ch12alien6
        with dissolve
        ad babytalk "\"Ma...ma....\""
        qm alienntalk "\"That's right! I am your mommy.\""
        ad babytalk "\"Pa...pa?\""
        qm alienntalk "\"Daddy is not here right now, little angel. He is trying to find a new suitable home for us.\""
        qm alienntalk "\"Hopefully you will meet him once you get old enough.\""
        qm alienntalk "\"Now, be a good girl and keep sucking and slurping my milk to grow into a fine adult.\""
        scene black
        with fasterfadein
        "..."
        "Meanwhile back on the road with [mc] and Ingrid..."
        jump ch12desert1
        
label ch12desert1:
    $ quick_menu = False
    $ renpy.show("ch12_map_1")
    $ renpy.transition(Dissolve(1))
    $ renpy.pause(4.5, hard=True)

label ch12_map_1:
    
    stop music fadeout 5.0
    play music "music/Eastern Thought.mp3" fadein 10.0
    $ quick_menu = True
    "After traveling for two days straight you reach the desert area which left you more and more exhausted with every minute spent in there."
    
    scene ch12oasis1
    with Dissolve(1)
    
    mc ctalk2 "\"God damn... this is an absolute living hell.\""
    mc ctalk3 "\"I am absolutely melting here.\""
    
    scene ch12oasis2
    with dissolve
    
    ingrid talk "\"Yeah... this is the toughest part we have to get through.\""
    ingrid talk "\"Even though it's still super hot back home we should be happy...\""
    mc ctalk "\"What do you mean?\""
    
    ingrid talk "\"Winter is coming and it's not pretty.\""
    mc ctalk2 "\"There's still so much I don't know about this planet...\""
    ingrid talk "\"Yeah. Let's just say you will need to adapt to a lot of things.\""
    ingrid talk "\"We still have long way to go through the desert, but we should be getting closer to an oasis soon.\""
    ingrid talk "\"We can rest up there.\""
    
    with fasterfadein
    scene a few moments later
    $ quick_menu = False
    $ renpy.pause(2, hard=True)
    with fasterfadeout
    scene ch12oasis3
    with fadein
    $ quick_menu = True
    ingrid talk "\"Look! You see that?\""
    mc ctalk2 "\"Yeah. What is it?\""
    ingrid talk "\"That has to be the oasis. Let's go.\""
    
    scene ch12oasis4
    with fasterfadein
    "You move in closer and spot a paradise among the desert."
    ingrid talk "\"This is amazing.\""
    
    scene ch12oasis5
    with Dissolve(1)
    ingrid talk "\"I don't know about you, but I can't wait to get in the water.\""
    ingrid talk "\"It has a nice shade from the trees so it should be cold.\""
    
    scene ch12oasis6
    with Dissolve(1)
    
    "Without saying much more Ingrid removes all her clothes and drops them on the ground."
    ingrid ntalk "\"Ahh~ there's a nice breeze too.\""
    
    $ quick_menu = False
    scene ch12oasis7 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(3, hard=True)
    pause
    with dissolve
    $ quick_menu = True
    scene ch12oasis8
    with fasterfadein
    "\"*Splash*\""
    "Ingrid runs in and dives to the cool water."
    
    scene ch12oasis9
    with dissolve
    ingrid ntalk "\"Ahh~ the water is so nice.\""
    ingrid ntalk "\"Come on. Are you coming or not?\""
    
    $ quick_menu = False
    
    menu:
        "Get in the water":
            jump ch12desert3
        "Sit down and rest instead":
            $ch12_desert_sex = False
            jump ch12desert2
            

label ch12desert2:
    $ quick_menu = True
    scene ch12oasis11
    with fasterfadein
    mc ctalk2 "\"I will just rest a little bit first.\""
    ingrid ntalk "\"Sure, whatever. I will enjoy all this cold and refreshing water by myself!\""
    
    scene ch12oasis12
    with Dissolve(1)
    "You close your eyes for just a moment..."
    "But that's all it takes for you to drift off to sleep."
    jump ch12desert5
    
    
label ch12desert3:
    $ quick_menu = True
    scene ch12oasis10
    with vpunch
    "Without wasting anymore time you begin undressing."
    "You quickly remove your clothes and throw them next to Ingrid's."
    
    scene ch12oasis13
    with dissolve
    ingrid ntalk "\"Haha. Nice! Come here."
    "You run in and jump in the cold water."
    
    scene ch12oasis14
    with dissolve
    ingrid ntalk "\"Nice, isn't it?\""
    ingrid ntalk "\"Desert ain't so bad with little spots like this laying around.\""
    mc nudetalk "\"I can definitely agree with that.\""
    $ quick_menu = False
    menu:
        "Look down":
            jump ch12desert4
label ch12desert4:
    $ quick_menu = True
    scene ch12oasis15
    with dissolve
    "You look down and notice she is showing her perky tits right above the water."
    "Probably on purpose too."
    ingrid ntalk "\"Why are you so far away from me anyway? Come closer. I won't bite...\""
    ingrid ntalk "\"Too much...hehe.\""
    
    scene ch12oasis16
    with dissolve
    ingrid ntalk "\"You know, when we caught you I didn't get to have a turn with you.\""
    ingrid ntalk "\"Haven't had sex since we left camp.\""
    ingrid ntalk "\"A girl needs to have some stress released.\""
    ingrid ntalk "\"What do ya say? Wanna help each other out? I bet you want it too.\""
    $ quick_menu = False
    menu:
        "Have sex":
            $ch12_desert_sex = True
            jump ch12desertsex
        "Don't":
            $ch12_desert_sex = False
            jump ch12desertnosex

label ch12desertnosex:
    $ quick_menu = True
    mc nudetalk "\"Sorry. I am really not in the mood for that right now. I will go rest a bit since we have a long journey ahead of us.\""
    ingrid ntalk "\"Sure, your call.\""
    jump ch12desert5
    
    
label ch12desertsex:
    $ quick_menu = True
    mc nudetalk2 "\"Why not?\""
    mc nudetalk "\"We can have some fun.\""
    scene ch12oasis17
    with dissolve
    ingrid ntalk "\"That's what I like to hear.\""
    ingrid ntalk "\"This water will become pretty hot soon.\""
    ingrid ntalk "\"Mmm...\""
    scene ch12oasis18
    with dissolve
    ingrid ntalk "\"I am gonna enjoy this a lot.\""
    ingrid ntalk "\"Let's see what we have down there...\""
    
    scene ch12underwaterhj
    with dissolve
    ingrid ntalk "\"Mmm....\""
    
    show screen ch12_ingrid_hj
    $ quick_menu = False
    $ renpy.show("ch12_ingrid_hj")
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(12, hard=True)

label ch12_ingrid_hj:
    hide screen ch12_ingrid_hj
    $ quick_menu = True
    mc nudetalk "\"Ahh...\""
    ingrid ntalk "\"Are you about to...\""
    ingrid ntalk "\"Do it... ahh... cum!\""
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch12underwatercum
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch12underwatercum
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch12underwatercum
    with Dissolve(1)
    
    ingrid ntalk "\"Mmm. You released quite a bit.\""
    ingrid ntalk "\"Seems like you had to unload as well.\""
    
    scene ch12oasis18
    with dissolve
    
    ingrid ntalk "\"I am glad we did this, but you should go and rest a bit.\""
    ingrid ntalk "\"We will make camp here for the night.\""

    
label ch12desert5:
    with fasterfadein
    scene afewhourslater
    $ quick_menu = False
    $ renpy.pause(2, hard=True)
    with fasterfadeout
    scene ch12oasis19
    with fadein
    $ quick_menu = True
    
    "A few hours pass and you wake up."
    
    scene ch12oasis20
    with dissolve
    mc cthinking "It's already this late? Damn I slept a lot..."
    mc cthinking "I must be really tired."
    
    scene ch12oasis21
    with Dissolve(1)
    
    mc ctalk3 "\"Hey, Ingrid. Did I miss anything?\""
    ingrid talk "\"Nah. You are good.\""
    ingrid talk "\"You must've been really tired... I did make you come with me straight after that long night which you had to endure.\""
    mc ctalk2 "\"It wasn't all that bad, hehe.\""
    ingrid talk "\"Haha. I understand now why you didn't complain too much about it, you perv.\""
    ingrid talk "\"Anyway... I was wondering... what is your story?\""
    mc ctalk "\"Oh, man... where do I even start on that?\""
    mc ctalk3 "\"The night is not long enough for me to cover everything that has happened to me so far.\""
    ingrid talk "\"You seem like a pretty interesting individual, [mc].\""
    ingrid talk "\"I do want to hear your story.\""
    mc ctalk "\"Ok, well, you asked for it...\""
    
    scene black
    with Dissolve(1)
    pause 1
    
    scene ch12oasis21
    with Dissolve(1)
    ingrid talk "\"Geez. That is crazy.\""
    ingrid talk "\"You know... once we deal with our own problems and find Luna, I don't think my people would mind if your people joined us.\""
    ingrid talk "\"It's still not for me to say, but if you prove yourself I do believe they wouldn't mind.\""
    mc ctalk2 "\"That's all I want. But let's help find Luna first. That's the priority.\""
    ingrid talk "\"Yeah...\""
    ingrid talk "\"Let's get some rest... we have a long ride tomorrow.\""
    jump ch12forest1

label ch12forest1:
    $ quick_menu = False
    $ renpy.show("ch12_map_2")
    $ renpy.transition(Dissolve(1))
    $ renpy.pause(4.5, hard=True)

label ch12_map_2:
    $ quick_menu = True
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch12forest1
    with Dissolve(1)
    ingrid talk "\"I believe this is it?\""
    ingrid talk "\"It should be anyway... according to the source.\""
    
    scene ch12forest2
    with dissolve
    mc ctalk2 "\"Seems so.\""
    mc ctalk "\"We should leave the horses here.\""
    
    scene ch12forest4
    with dissolve
    mc ctalk3 "\"One of us should stay behind and keep watch and stay with the horses.\""
    mc ctalk2 "\"We will have no way to go back otherwise and it took us days with horses alone.\""
    scene ch12forest3
    with dissolve
    ingrid talk "\"Yeah. Good point.\""
    ingrid talk "\"I will --\""
    scene ch12forest5
    with vpunch
    mc cshocked2 "\"{size=+10}AGHHHHHHHHHHHH!!{/size}\""
    mc shocked2 "\"My head!!!\""
    
    scene black
    with Dissolve(1)
    pause 1
    
    scene ch12forest7
    with Dissolve(1)
    qm aavatalk "\"[mc]...\""
    qm aavatalk "\"Come...\""
    qm aavatalk "\"You are so close...\""
    qm aavatalk "\"I am waiting for you...\""
    qm aavatalk "\"Come to me...\""
    
    scene black
    with Dissolve(1)
    pause 1
    
    scene ch12forest8
    with Dissolve(1)
    with vpunch
    qm aavatalk "\"You will be mine...\""
    
    scene black
    with Dissolve(1)
    pause 1
    
    scene ch12forest6
    with Dissolve(1)
    ingrid talk "\"Hey, what's wrong??\""
    ingrid talk "\"Are you okay?\""
    ingrid talk "\"Talk to me.\""
    
    scene ch12forest9
    with dissolve
    "The vision of the alien disappears and your headache passes away."
    mc ctalk "\"I am sorry, I got a sharp pain in my head all of a sudden...\""
    mc ctalk2 "\"I am okay now though, no worries.\""
    ingrid talk "\"You scared me there.\""
    ingrid talk "\"You should stay here and I'll go --\""
    mc ctalk3 "\"No. I will go alone and you'll stay with the horses.\""
    ingrid talk "\"What? Why? What if the pain in your head returns?\""
    mc ctalk2 "\"I'll be fine. Let me do this for you. I will bring back Luna if she is in this cave.\""
    ingrid talk "\"...Fine.\""
    
    scene ch12forest10
    with dissolve
    ingrid talk "\"But take this at the very least.\""
    ingrid talk "\"Luna was kidnapped from what we know.\""
    ingrid talk "\"There might be enemies around so watch out.\""
    mc ctalk2 "\"Thanks. I'll be careful.\""
    
    scene ch12forest11
    with fasterfadein
    "You make a torch and start heading down the cave..."
    mc cthinking "Let's bring back that girl..."
    mc cthinking "I need to be useful so they let us in after."
    
    scene black
    with Dissolve(1)
    pause 1
    
    stop music fadeout 5.0
    "After a few minutes of walking down and down and down you finally reach something..."
    jump ch12tomb1

label ch12tomb1:
    scene ch12tomb1
    with Dissolve(1)
    
    
    play music "music/Modern Horror Film Music.mp3" fadein 3.0
    
    mc cthinking "What is this place?"
    mc cthinking "Looks like some kind of a tomb..."
    mc cthinking "This doesn't seem to be a regular cave at all."
    
    scene ch12tomb2
    with dissolve
    
    mc cshocked "What the fuck is this?!"
    
    $ quick_menu = False
    
    menu:
        "Look at Aurora":
            jump ch12auroralooked
            
        "Look at the girl in the center":
            jump ch12lookedatgirl
            
        "Look at the far back":
            jump ch12lookedatfarback

#Aurora looked-------------------------------------------------------------------------------------------------------------------
    
label ch12auroralooked:
    $ quick_menu = False
    scene ch12tomb5 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(3, hard=True)
    pause
    with dissolve
    $ quick_menu = True
    mc cthinking "Is that..."
    mc cthinking "Aurora?"
    mc cthinking "She and her commander boarder our ship at one point..."
    mc cthinking "She was looking for that alien which invaded us..."
    mc cthinking "What is she doing here?"
    mc cthinking "She seems to be pregnant...very late pregnancy from the looks of it."
    scene ch12tomb6
    with dissolve
    mc cthinking "And she looks to have a whole puddle of cum underneath her."
    mc cthinking "Jesus..."
    mc cthinking "They must've had their way with her so many times..."
    $ quick_menu = False
    menu:
        "Look at the girl in the center":
            jump ch12auroralooked2
        "Look at the far back":
            jump ch12auroralooked4
label ch12auroralooked2:
    scene ch12tomb4
    with fasterfadein
    $ quick_menu = True
    "You look over at the girl in the middle..."
    mc cthinking "This girl..."
    mc cthinking "Her hands are chained on that stone."
    mc cthinking "Is that Luna? I gotta ask her."
    $ quick_menu = False
    menu:
        "Look at the far back":
            jump ch12auroralooked3
            
label ch12auroralooked3:
    scene ch12tomb3
    with fasterfadein
    $ quick_menu = True
    "You take a look at the far back..."
    "Something seems to be pulling you that way..."
    "You notice something spreading through the wall...some kind of a blood hole."
    mc cthinking "What the fuck is this place?!"
    jump ch12tomb2
    
    
label ch12auroralooked4:
    scene ch12tomb3
    with fasterfadein
    $ quick_menu = True
    "You take a look at the far back..."
    "Something seems to be pulling you that way..."
    "You notice something spreading through the wall...some kind of a blood hole."
    mc cthinking "What the fuck is this place?!"
    $ quick_menu = False
    menu:
        "Look at the girl in the center":
            jump ch12auroralooked5
            
label ch12auroralooked5:
    scene ch12tomb4
    with fasterfadein
    $ quick_menu = True
    "You look over at the girl in the middle..."
    mc cthinking "This girl..."
    mc cthinking "Her hands are chained on that stone."
    mc cthinking "Is that Luna? I gotta ask her."
    jump ch12tomb2
    
#-------------------------------------------------------------------------------------------------------------------

#Girl looked-------------------------------------------------------------------------------------------------------------------
label ch12lookedatgirl:
    scene ch12tomb4
    with fasterfadein
    "You look over at the girl in the middle..."
    mc cthinking "This girl..."
    mc cthinking "Her hands are chained on that stone."
    mc cthinking "Is that Luna? I gotta ask her."
    $ quick_menu = False
    menu:
        "Look at Aurora":
            jump ch12lookedatgirl2
        "Look at the far back":
            jump ch12lookedatgirl4
    
label ch12lookedatgirl2:
    scene ch12tomb5 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(3, hard=True)
    pause
    with dissolve
    $ quick_menu = True
    mc cthinking "Is that..."
    mc cthinking "Aurora?"
    mc cthinking "She and her commander boarder our ship at one point..."
    mc cthinking "She was looking for that alien which invaded us..."
    mc cthinking "What is she doing here?"
    mc cthinking "She seems to be pregnant...very late pregnancy from the looks of it."
    scene ch12tomb6
    with dissolve
    mc cthinking "And she looks to have a whole puddle of cum underneath her."
    mc cthinking "Jesus..."
    mc cthinking "They must've had their way with her so many times..."
    $ quick_menu = False
    menu:
        "Look at the far back":
            jump ch12lookedatgirl3
            
label ch12lookedatgirl3:
    scene ch12tomb3
    with fasterfadein
    $ quick_menu = True
    "You take a look at the far back..."
    "Something seems to be pulling you that way..."
    "You notice something spreading through the wall...some kind of a blood hole."
    mc cthinking "What the fuck is this place?!"
    jump ch12tomb2
    
    
label ch12lookedatgirl4:
    scene ch12tomb3
    with fasterfadein
    $ quick_menu = True
    "You take a look at the far back..."
    "Something seems to be pulling you that way..."
    "You notice something spreading through the wall...some kind of a blood hole."
    mc cthinking "What the fuck is this place?!"
    $ quick_menu = False
    menu:
        "Look at Aurora":
            jump ch12lookedatgirl5

label ch12lookedatgirl5:
    scene ch12tomb5 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(3, hard=True)
    pause
    with dissolve
    $ quick_menu = True
    mc cthinking "Is that..."
    mc cthinking "Aurora?"
    mc cthinking "She and her commander boarder our ship at one point..."
    mc cthinking "She was looking for that alien which invaded us..."
    mc cthinking "What is she doing here?"
    mc cthinking "She seems to be pregnant...very late pregnancy from the looks of it."
    scene ch12tomb6
    with dissolve
    mc cthinking "And she looks to have a whole puddle of cum underneath her."
    mc cthinking "Jesus..."
    mc cthinking "They must've had their way with her so many times..."
    jump ch12tomb2
#-------------------------------------------------------------------------------------------------------------------

#Far back looked-------------------------------------------------------------------------------------------------------------------
label ch12lookedatfarback:
    scene ch12tomb3
    with fasterfadein
    "You take a look at the far back..."
    "Something seems to be pulling you that way..."
    "You notice something spreading through the wall...some kind of a blood hole."
    mc cthinking "What the fuck is this place?!"
    $ quick_menu = False
    menu:
        "Look at Aurora":
            jump ch12lookedatfarback2
        "Look at the girl in the center":
            jump ch12lookedatfarback4
    
    
label ch12lookedatfarback2:
    scene ch12tomb5 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(3, hard=True)
    pause
    with dissolve
    $ quick_menu = True
    mc cthinking "Is that..."
    mc cthinking "Aurora?"
    mc cthinking "She and her commander boarder our ship at one point..."
    mc cthinking "She was looking for that alien which invaded us..."
    mc cthinking "What is she doing here?"
    mc cthinking "She seems to be pregnant...very late pregnancy from the looks of it."
    scene ch12tomb6
    with dissolve
    mc cthinking "And she looks to have a whole puddle of cum underneath her."
    mc cthinking "Jesus..."
    mc cthinking "They must've had their way with her so many times..."
    $ quick_menu = False
    menu:
        "Look at the girl in the center":
            jump ch12lookedatfarback3
            
label ch12lookedatfarback3:
    scene ch12tomb4
    with fasterfadein
    $ quick_menu = True
    "You look over at the girl in the middle..."
    mc cthinking "This girl..."
    mc cthinking "Her hands are chained on that stone."
    mc cthinking "Is that Luna? I gotta ask her."
    jump ch12tomb2
    
label ch12lookedatfarback4:
    scene ch12tomb4
    with fasterfadein
    $ quick_menu = True
    "You look over at the girl in the middle..."
    mc cthinking "This girl..."
    mc cthinking "Her hands are chained on that stone."
    mc cthinking "Is that Luna? I gotta ask her."
    $ quick_menu = False
    menu:
        "Look at Aurora":
            jump ch12lookedatfarback5
            
label ch12lookedatfarback5:
    scene ch12tomb5 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(3, hard=True)
    pause
    with dissolve
    $ quick_menu = True
    mc cthinking "Is that..."
    mc cthinking "Aurora?"
    mc cthinking "She and her commander boarder our ship at one point..."
    mc cthinking "She was looking for that alien which invaded us..."
    mc cthinking "What is she doing here?"
    mc cthinking "She seems to be pregnant...very late pregnancy from the looks of it."
    scene ch12tomb6
    with dissolve
    mc cthinking "And she looks to have a whole puddle of cum underneath her."
    mc cthinking "Jesus..."
    mc cthinking "They must've had their way with her so many times..."
    jump ch12tomb2
#-------------------------------------------------------------------------------------------------------------------
label ch12tomb2:
    scene ch12tomb7
    with dissolve
    mc cshocked "What the freaking hell is going on down here?"
    mc cthinking "First thing's first. Let's check if this is actually Luna."
    
    scene ch12tomb8
    with fasterfadein
    
    mc ctalk2 "\"Hey, are you Luna?\""
    luna talk "\"Yes? Who are you? How did you get here?\""
    mc ctalk "\"I am [mc]. I am here to rescue you, Luna.\""
    luna talk "\"You should get out of here before they come back.\""
    
    scene ch12tomb9
    with Dissolve(1)
    mc ctalk2 "\"Hang on. I will free you really quick.\""
    luna talk "\"Uhh...\""
    
    scene ch12tomb10
    with vpunch
    "You swing the axe down on the chain."
    mc ctalk2 "\"One more time should do it.\""
    
    scene ch12tomb9
    with Dissolve(1)
    pause 1
    
    scene ch12tomb10
    with vpunch
    "You swing again and you hear the chain pop off."
    
    scene ch12tomb12
    with dissolve
    luna talk "\"Thanks...\""
    qm aavatalk "\"[mc]... come...\""
    luna talk "\"We should get out of here right now.\""
    luna talk "\"Hey! Where are you going?\""
    "You ignore her and keep going forward."
    
    scene ch12tomb13
    with dissolve
    qm aavatalk2 "\"That's it, [mc].\""
    qm aavatalk "\"You are finally here.\""
    
    scene ch12tomb14
    with Dissolve(1)
    "You watch as hands start pushing forward, through the bloody hole..."
    qm aavatalk "\"Mmhhh...\""
    
    scene ch12tomb15
    with Dissolve(1)
    "The rest of the body starts to emerge..."
    
    if breed_with_alien_queen:
        "You immediately recognize her as the Queen."
        "Now it all makes sense for Aurora to be here... They must've lost the battle against her."
    else:
        "You recognize her as the one who keeps appearing in your head and visions..."
        "She guided you here..."
        
    scene ch12tomb16
    with Dissolve(1)
    
    if breed_with_alien_queen:
        qm aavatalk2 "\"[mc]. I finally got to meet you again.\""
        qm aavatalk "\"I've waited for such a long time...\""
        qm aavatalk2 "\"Our child has grown and had children of their own.\""
        qm aavatalk "\"You have a whole branch of family members here, [mc].\""
        qm aavatalk2 "\"The seed you planted inside me has bloomed and flourished.\""
        qm aavatalk "\"Now that aside...\""
        qm aavatalk2 "\"I feel a bit offended by the fact you sent these sluts after me.\""
        qm aavatalk "\"At the same time though... I am glad you did. They were impregnated so many times I lost count.\""
        qm aavatalk2 "\"Lots of grandchildren. Hehe.\""
        qm aavatalk "\"Unfortunately your crew mates -- Edis and Amir are gone for a long time.\""
        qm aavatalk2 "\"But they were very kind in popping out as many kids as possible.\""
        qm aavatalk "\"Ahh... Amir... he had the most magnificent cock. His grandchildren are still around. Quan should be coming back soon. They are almost as gifted as he was.\""
        qm aavatalk2 "\"My other children I've spread around. They are lurking for preys. I will make this whole planet mine, [mc]. And I want you to be a part of it.\""
        mc ctalk3 "\"You were waiting for me... all this time. Setting this trap and knowing exactly the coordinates from Karin and Aurora who gave it to me in the first place.\""
        mc ctalk2 "\"You set this kidnapping up so that I come here and rescue Luna.\""
        qm aavatalk "\"Yes, [mc]. It was all for you. Now become a part of me...\""
    else:
        qm aavatalk "\"[mc]. I am glad to finally get to meet you in person.\""
        qm aavatalk2 "\"I've waited for you for such a long time...\""
        qm aavatalk "\"After getting Edis and Amir and their amazing contribution to my children... I had to meet the man in charge.\""
        qm aavatalk2 "\"The man who sent these sluts after me.\""
        qm aavatalk2 "\"I am a bit offended by that fact.\""
        qm aavatalk "\"At the same time though... I am glad you did. They were impregnated so many times I lost count.\""
        qm aavatalk2 "\"Lots of grandchildren. Hehe.\""
        qm aavatalk "\"Unfortunately your crew mates -- Edis and Amir are gone for a long time.\""
        qm aavatalk2 "\"But they were very kind in popping out as many kids as possible.\""
        qm aavatalk "\"Ahh... Amir... he had the most magnificent cock. His grandchildren are still around. Quan should be coming back soon. They are almost as gifted as he was.\""
        qm aavatalk2 "\"My other children I've spread around. They are lurking for preys. I will make this whole planet mine, [mc]. And I want you to be a part of it.\""
        mc ctalk3 "\"You were waiting for me... all this time. Setting this trap and knowing exactly the coordinates from Karin and Aurora who gave it to me in the first place.\""
        mc ctalk2 "\"You set this kidnapping up so that I come here and rescue Luna.\""
        qm aavatalk "\"Yes, [mc]. It was all for you. Now become a part of me...\""
    
    $ quick_menu = False
    menu:
        "Accept her and become a part of her":
            jump ch12tomb3
        "Chop her fucking head off":
            jump ch12tomb4
            
            
label ch12tomb3:
    $ quick_menu = True
    mc ctalk3 "\"I... accept your offer... I want this too.\""
    qm aavatalk2 "\"I am so happy to hear that, [mc].\""
    scene ch12tomb17
    with Dissolve(1)
    qm aavatalk "\"You can start whenever you are ready.\""
    qm aavatalk2 "\"Mate with me~\""
    
    $ quick_menu = False
    
    menu:
        "Lick her ass first":
            jump ch12tomblick
        "Start fucking her":
            jump ch12tombfuck
            
label ch12tomblick:
    scene ch12tomblick
    with Dissolve(1)
    $ quick_menu = True
    "You kneel down in front of her magnificent ass and bury your face right into her ass."
    
    show screen ch12_aava_lick
    $ quick_menu = False
    $ renpy.show("ch12_aava_lick")
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(12, hard=True)

label ch12_aava_lick:
    hide screen ch12_aava_lick
    $ quick_menu = True
    mc cpleasure "\"*Slurp*, *Lick*, *Slurp*\""
    qm aavapleasure "\"Aaah~ keep going just like that.\""
    "You keep slurping and eating her ass out."
    "All her juices flow directly in your mouth as you devour her ass and lick her deep inside her anus."
    
    "You decide that's enough and move on to fucking her."
    
    jump ch12tombfuck
    
label ch12tombfuck:
    scene ch12tombsex
    with Dissolve(1)
    $ quick_menu = True
    "You position your cock outside her vagina and rub it at the entrance."
    qm aavapleasure "\"Mmm. Don't tease me like that. Fuck me already.\""
    
    show screen ch12_aava_sex
    $ quick_menu = False
    $ renpy.show("ch12_aava_sex")
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(12, hard=True)

label ch12_aava_sex:
    hide screen ch12_aava_sex
    $ quick_menu = True
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch12tombsexcum
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch12tombsexcum
    with Dissolve(1)
    mc cpleasure "\"Fuck... I am cumming~!\""
    qm aavapleasure "\"Do it! Fill me up.\""
    qm aavapleasure "\"Ahhh~ It's time for you to join me.\""
    
    scene ch12tomb19
    with vpunch
    "Before you can even pull your cock out of her vagina something comes out and traps your body in."
    "Unable to move an inch it keeps sucking you in."
    "The blood on the wall gets soft enough for your body to move in slowly eating you alive."
    
    scene ch12tomb20
    with Dissolve(1)
    "Your body becoming a fodder..."
    "At this point you stop caring."
    "Everything you want is to feel more pleasure and become part of something greater."
    
    scene ch12tomb21
    with Dissolve(1)
    pause 3
    
    scene gameover4
    $ quick_menu = False
    with Dissolve(1)
    $ renpy.pause(2, hard=True)
    jump thanks
    
label ch12tomb4:
    scene ch12tomb23
    with vpunch
    $ quick_menu = True
    mc ctalk3 "\"Nah. I don't think so.\""
    qm aavatalk2 "\"Wait... think about this before you do anything!\""
    qm aavatalk "\"Think about the possibilities!\""
    qm aavatalk2 "\"The infinite pleasure I can bring you!\""
    mc ctalk2 "\"I've heard enough.\""
    
    scene ch12tomb24
    with vpunch
    "You swing the axe right in her neck... as blood starts spraying everywhere."
    qm aavatalk "\"Aaaaaaaaghhhhh---\""
    
    scene ch12tomb25
    with Dissolve(1)
    "You pull the axe back from her neck."
    qm aavatalk "\"*Cough*... *Cough*...\""
    qm aavatalk "\"All... I wanted...\""
    qm aavatalk "\"was...\""
    qm aavatalk "\"a family...\""
    qm aavatalk "\"*Cough*...\""
    $ quick_menu = False
    menu:
        "Finish her":
            jump ch12tomb5
            
label ch12tomb5:
    scene ch12tomb26
    with vpunch
    $ quick_menu = True
    "You swing again, with all your might, and you finally chop her head off."
    "You move back not to get covered from all the blood pouring out."
    
    with vpunch
    qm quan "\"{size=+10}MOTHER!!!!!!{/size}\""
    
    "You hear a loud yell behind you."
    
    scene ch12tomb27
    with Dissolve(1)
    
    "You turn around and spot some sort of a grotesque beast."
    mc cthinking "Is this who she was talking about earlier?"
    mc cthinking "Is this Quan? Amir's grandson? Jesus Christ."
    
    scene ch12tomb28
    with Dissolve(1)
    "The beast starts charging towards you."
    with vpunch
    "Before you have time to react accordingly and defend yourself he headbutts you straight to the ground."
    mc cshocked2 "\"Aghhhhhhhhhh!\""
    
    scene ch12tomb29
    with dissolve
    "You lie on the blood skinned ground trying to catch your breath."
    
    qm quan "\"{size=+10}YOU DIE!{/size}\""
    
    scene ch12tomb30
    with dissolve
    
    "You hear the beast yell and you turn around to see him getting ready to smash your face in with his huge fists."
    
    with vpunch
    qm quan "\"{size=+10}DIEEEEEEEE!!!!!!!!!!{/size}\""
    
    scene ch12tomb31
    with vpunch
    qm quan "\"{size=+10}ARGHHHHH!{/size}\""
    "Just as you were about to lose all hope you see someone stopping him."
    
    scene ch12tomb32
    with vpunch
    qm quan "\"{size=+10}AGHH!{/size}\""
    qm quan "\"{size=+10}UGHHHH{/size}\""
    
    scene ch12tomb33
    with Dissolve(1)
    "You catch your breath again and stand up and see Luna holding him in."
    luna talk "\"Hurry.\""
    luna talk "\"Finish him off. I can't hold him for much longer!"
    $ quick_menu = False
    menu:
        "Kill him":
            jump ch12tomb6
            
label ch12tomb6:
    scene bloodsplatter
    with fasterfadein
    $ quick_menu = True
    "You swing your axe straight to his head and finish him off."
    
    scene ch12tomb34
    with Dissolve(1)
    "You can't help but feel guilt over all of this..."
    "You just killed his mother, so of course he would try to attack you."
    
    luna talk "\"Come on. We need to move.\""
    luna talk "\"More of these creatures will be coming if we don't get out of here soon.\""
    
    mc ctalk3 "\"I have to free Aurora too.\""
    
    scene ch12tomb35
    with vpunch
    "You move over and free her."
    mc ctalk2 "\"Hey, Aurora. I don't know if you remember me. It's [mc] from Paradise.\""
    mc ctalk "\"We met... long time ago.\""
    
    scene ch12tomb36
    with Dissolve(1)
    aur nudetalk "\"[mc]...\""
    aur nudetalk "\"I... remember.\""
    
    scene ch12tomb37
    with dissolve
    aur nudetalk "\"You came...\""
    aur nudetalk "\"I was losing hope. The only thing I cling to is that you'd eventually make it here...\""
    mc ctalk "\"I am guessing it's just you? Karin...\""
    aur nudetalk "\"Yes. It's just me now.\""
    mc ctalk2 "\"I am really sorry.\""
    
    scene ch12tomb38
    with Dissolve(1)
    luna talk "\"Sorry to interrupt your chat, guys. But we need to get out of here.\""
    luna talk "\"Right now!\""
    stop music fadeout 5.0
    mc ctalk2 "\"You're right. Let's move.\""
    
    jump ch12ambush
    
label ch12ambush:
    with fasterfadein
    scene meanwhile
    $ quick_menu = False
    $ renpy.pause(2, hard=True)
    with fasterfadeout
    scene ch12ambush1
    with fadein
    $ quick_menu = True
    

    play music "music/Eastern Thought.mp3" fadein 10.0
    
    ingrid talk "\"Ugh.\""
    ingrid talk "\"I should've went with him\""
    ingrid talk "\"If this goes south it will be my fault now.\""
    
    "*Horse footsteps*"
    
    scene ch12ambush2
    with vpunch
    ingrid talk "\"Huh??\""
    ingrid talk "\"Who is there?\""
    
    scene ch12ambush3
    with dissolve
    
    qm guard "\"Ohohoh.\""
    qm guard "\"Lookie, lookie. What do we have here?\""
    
    scene ch12ambush4
    with vpunch
    
    ingrid talk "\"I want no trouble. Just leave me be.\""
    qm guard "\"I think you are looking for trouble waving that knife around.\""
    qm guard "\"How about you drop it and we'll talk?\""
    ingrid talk "\"How about you fuck yourself?\""
    
    scene ch12ambush5
    
    qm ramsay "\"How about now, sweet-cheeks?\""
    qm ramsay "\"Drop your knife.\""
    
    scene ch12ambush6
    with dissolve
    qm ramsay "\"I won't ask again.\""
    scene ch12ambush7
    qm ramsay "\"Attagirl.\""
    qm ramsay "\"Stay still now.\""
    
    scene ch12ambush8
    with fasterfadein
    qm ramsay "\"You're Ingrid, right?\""
    ingrid talk "\"You know my name?\""
    qm ramsay "\"Of course.\""
    qm ramsay "\"We are the part of the Queen's army.\""
    qm ramsay "\"Your leader's disobeyance and refusal to kneel and swear allegiance is the reason why this is happening now.\""
    qm ramsay "\"A little birdie told us you would be here.\""
    qm ramsay "\"We really only wanted Luna, but having her second one in command as well is perfect.\""
    ingrid talk "\"Fuck you.\""
    qm ramsay "\"You have a very dirty mouth.\""
    qm ramsay "\"I wonder if it became like that from sucking too many cocks? Hahaha\""
    qm guard "\"Hahahaha!\""
    qm ramsay "\"Nice knife you have here. And I see you brought Luna's horse. We'll be taking that one.\""
    scene ch12ambush9
    with Dissolve(1)
    qm ramsay "\"Here, take the knife.\""
    qm ramsay "\"Since we're waiting for your friends to come out of that cave I can kill a little time with the little miss here.\""
    qm guard "\"Where you going, Ramsay?\""
    scene ch12ambush10
    with vpunch
    ramsay talk "\"I am just gonna see how dirty her mouth really is, hahahaha.\""
    ingrid talk "\"{size=+10}Let me go, you bastard!{/size}\""
    qm guard "\"Don't be too long.\""
    ingrid talk "\"{size=+10}You fucker!!{/size}\""
    scene ch12ambush11
    with vpunch
    ingrid talk "\"Ahhhhh~!\""
    ramsay talk "\"You talk too much.\""
    ramsay talk "\"I am sure you are enjoying this, you little slut.\""
    ingrid talk "\"Fuck you!\""
    ramsay talk "\"Hehehe.\""
    
    scene ch12ambush12
    with fasterfadein
    luna talk "\"I see light!\""
    luna talk "\"We are almost there.\""
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch12ambush13
    with Dissolve(1)
    
    qm guard "\"Oh. Look who finally made it out!\""
    qm guard "\"We see some extras, but that's just fine.\""
    luna talk "\"You guys?\""
    luna talk "\"You don't take no for an answer.\""
    qm guard "\"No, we don't.\""
    luna talk "\"Where is Ingrid? What did you do to her?\""
    qm guard "\"She is having fun behind the trees, don't worry about her.\""
    luna talk "\"...\""
    with vpunch
    mc ctalk2 "\"{size=+10}You piece of shit!{/size}\""
    scene ch12ambush14
    with dissolve
    qm guard "\"Whoa. You better tell your boyfriend there to shut his mouth and to drop his weapon before I order my men to split his skull wide open.\""
    luna talk "\"[mc]. Stop.\""
    luna talk "\"Drop the axe. We can't win this.\""
    luna talk "\"You might take one out, if you are lucky, but the next one will kill you.\""
    luna talk "\"It's not worth it. Just drop the axe.\""
    
    scene ch12ambush15
    with vpunch
    "You throw the axe on the ground."
    qm guard "\"What a good puppy. It's nice that you know your place.\""
    
    scene ch12ambush16
    with vpunch
    "The guard comes next to you and punches you hard."
    qm guard "\"And your place right now is the ground.\""
    "You fall down."
    
    scene ch12ambush17
    with dissolve
    qm guard "\"Next time you better watch your mouth before you speak.\""

    
    scene ch12ambush18
    with vpunch
    
    scene black
    with fadein
    
    scene ch12ambush18
    with vpunch

    scene black
    with fadein
    qm guard "\"Hey, can we have some fun with these 2? Ramsay is having fun with that bitch behind the trees somewhere. We should too.\""
    qm guard "\"The blue skinned one is for me. I like pregnant girls.\""
    qm guard "\"We can take turns,who cares. Let's be quick before we have to leave.\""
    
    
    if ch11_saved_ruby:
        jump ch12throne
    else:
        jump ch12training

label ch12training:
    with fadein
    pause 3
    stop music fadeout 5.0
    play music "music/Ambient Thriller Motif.mp3" fadein 10.0
    l angry "\"{size=+10}Do you hear me?!{/size}\""
    
    scene ch12training1
    with Dissolve(1)
    
    l angry "\"Let me out right now!\""
    with vpunch
    l angry "\"Hey!! Answer me!\""
    
    scene ch12training2
    with dissolve
    qm alienntalk "\"Stop banging on the glass. You are wasting your energy, which you will need plenty of.\""
    qm alienntalk "\"Your purpose is only one --\""
    qm alienntalk "\"To help with my daughter's combat skills.\""
    qm alienntalk "\"{size=+10}[ad]? You ready?{/size}\""
    
    scene ch12training3
    with fasterfadein
    ad nudetalk "\"{size=+10}I am coming in a minute, mother!{/size}\""
    ad nudethinking "Ah...this body of mine..."
    $ quick_menu = False
    scene ch12training4 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(3, hard=True)
    pause
    with dissolve
    $ quick_menu = True
    ad nudethinking "So lewd... So sensitive...So...different."
    scene ch12training5
    with fasterfadein
    ad nudethinking "I feel pain... yet pleasure at the same time."
    ad nudethinking "Why was I born this way?"
    
    scene ch12training6
    with Dissolve(1)
    ad nudethinking "I have to find my purpose."
    ad nudethinking "Mother is hiding things from me."
    ad nudethinking "I don't know why, but I feel connection to the humans."
    
    scene ch12training7
    with Dissolve(1)
    ad thinking "My costume hides this grotesque body of mine..."
    ad thinking "Imperfect... unlike those human girls here."
    ad thinking "I should go. Mother is waiting."
    
    scene ch12training8
    with fasterfadein
    
    ad talk "\"I am here, mother. Open the door.\""
    
    scene ch12training9
    with hpunch
    
    qm alienntalk "\"Do your best, dear.\""
    qm alienntalk "\"I will be watching carefully.\""
    ad talk "\"Of course.\""
    
    $ quick_menu = False
    scene ch12training10 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(3, hard=True)
    pause
    with dissolve
    $ quick_menu = True
    scene ch12training11
    with dissolve
    l talk "\"You...\""
    l talk "\"Tell that thing to open the door.\""
    
    scene ch12training12
    with dissolve
    
    ad talk "\"That 'thing' is my mother.\""
    ad talk "\"I will make you show some respect towards her.\""
    ad talk "\"Tell you what though. If you manage to win against me, she will open the door for you.\""
    ad talk "\"So you better show me everything you got.\""
    with vpunch
    ad talk "\"Let's go!\""
    stop music fadeout 5.0
    play music "music/Eastern Thought.mp3" fadein 10.0
    jump ch12throne
    
label ch12throne:
    with fasterfadein
    scene onedaylater
    $ quick_menu = False
    $ renpy.pause(2, hard=True)
    with fasterfadeout
    scene black
    with fadein
    $ quick_menu = True
    
    scene ch12throne1
    with Dissolve(1)
    ramsay talk "\"You stand before the rightful Queen of all the Kingdoms.\""
    ramsay talk "\"Danylynn Dragonborn, The Destroyer of Chains, the Lightbringer, The Mother of Dragons, The Protector of the Realms.\""
    
    $ quick_menu = False
    scene ch12throne2 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(3, hard=True)
    pause
    with dissolve
    $ quick_menu = True
    scene ch12throne3
    with dissolve
    
    dany talk "\"Who are you bringing me, Ramsay?\""
    ramsay talk "\"My Queen... We captured Luna from Ghendralin.\""
    ramsay talk "\"She was where we expected her to be. But she had other people with her. He was one of them.\""
    ramsay talk "\"Apparently he saved her from her captivity.\""
    
    dany talk "\"I see. Bring him closer.\""
    
    scene ch12throne4
    with fasterfadein
    dany talk "\"What is your name?\""
    mc ctalk "\"[mc].\""
    
    scene ch12throne5
    with vpunch
    ramsay talk "\"You will kneel and address her as 'your grace'.\""
    mc ctalk "\"...\""
    ramsay talk "\"{size=+10}Do you understand me?!{/size}\""
    mc ctalk2 "\"Yes...\""
    
    scene ch12throne6
    with dissolve
    dany talk "\"So, [mc]...\""
    dany talk "\"I want to make it clear that I am no tyrant.\""
    dany talk "\"But I do want people to show their respect for me.\""
    dany talk "\"If people cooperate with me it's way easier and we don't have to go to any extremes which, unfortunately, this situation seems to be.\""
    
    scene ch12throne7
    with dissolve
    
    dany talk "\"Now show your respect towards me.\""
    "Dany shoves her feet in your face."
    $ quick_menu = False
    menu:
        "Kiss her foot":
            $ quick_menu = True
            $ch12_throne_footkiss = True
            $ch12_throne_footrefuse = False
            $ch12_throne_footlick = False
            scene ch12throne8
            with dissolve
            mc ctalk "\"*Chu*, *Kiss*\""
            "You kiss her toes gently."
            scene ch12throne10
            with dissolve
            dany talk "\"I am glad you understand your place.\""
            dany talk "\"It will make things much easier.\""
            scene ch12throne13
            with dissolve
            dany talk "\"Ramsay, take him to his cell. I need to see the next prisoner. I'll visit him later.\""
            ramsay talk "\"At once, your grace.\""
            jump startch13
        "Lick her foot":
            $ quick_menu = True
            $ch12_throne_footlick = True
            $ch12_throne_footrefuse = False
            $ch12_throne_footkiss = False
            scene ch12throne8
            with dissolve
            mc ctalk "\"*Chu*, *Kiss*\""
            "You start by kissing her toes gently."
            scene ch12throne9
            with hpunch
            "Then you start licking her toes."
            "Your tongue goes through all her toes before she pulls back."
            scene ch12throne11
            with dissolve
            dany talk "\"Oh my!\""
            dany talk "\"Are you showing affection to me or you are just a pervert who loves female feet?\""
            dany talk "\"Maybe both? Hehe.\""
            scene ch12throne13
            with dissolve
            dany talk "\"Ramsay, take him to his cell. I need to see the next prisoner. I'll visit him later.\""
            ramsay talk "\"At once, your grace.\""
            jump startch13
        "Refuse to do anything":
            $ quick_menu = True
            $ch12_throne_footrefuse = True
            $ch12_throne_footkiss = False
            $ch12_throne_footlick = False
            mc ctalk "\"I will not do that... your grace.\""
            scene ch12throne12
            with dissolve
            dany talk"\"That's a shame. I guess you are the kind who doesn't want to cooperate after all.\""
            dany talk "\"Ramsay, take him to his cell. I need to see the next prisoner. I'll deal with him later.\""
            ramsay talk "\"At once, your grace.\""
            jump startch13