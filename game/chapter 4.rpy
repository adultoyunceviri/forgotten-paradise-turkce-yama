label ch4start:
#scene the next day

with fasterfadein
scene thenextday
$ quick_menu = False
pause 2.5
with fasterfadeout

show mcstretching
with fasterfadein
$ quick_menu = True


mc thinking "Today I am going to try and get to convince Melisa to help me out somehow. She seems the only reliable crew member that can help me."
mc thinking "But I will have to find her first."
mc thinking "Starting from the Command Center is my best bet to find an actual crew member."

scene a few moments later
$ quick_menu = False
with fasterfadein
pause 2.0
with fasterfadeout


scene comingincommandcenter
$ quick_menu = True
with fasterfadein

hide mcstretching

mc thinking "This is the Command Center and I see someone over there. I can't quite see who it is from here though..."

"You move in a bit closer..."

scene closeupcommandcenter
with dissolve

#persistent change on the main menu
$ persistent.change = "Ruby 1"

mc thinking "\"Oh.. it's Ruby?"

mc talk "\"Hi Ruby!\""

scene closeupcommandcenter2
with dissolve

r ttalk "\"Hello, [mc]. What brings you here?\""

mc talk "\"I couldn't recognize you there for a second.\""
mc talk3 "\"New hairstyle?\""

r ttalk "\"Yes. One of the benefits of being an android is having little to no problems changing your physical appearance. Hair being the most easy part.\""

mc talk "\"That is pretty neat advantage to have indeed!\""
mc talk2 "\"I also love your new hair. It suits you.\""

r ttalk "\"Ha-ha. Thank you.\""
r ttalk2 "\"Did you need any help with something?\""

mc talk2 "\"Oh, right. I was actually looking for someone and was hoping to find some direction to their whearabouts from here if at all possible.\""

r ttalk "\"Who do you need to find?\""

mc talk3 "\"Melisa.\""
mc talk2 "\"Any idea where she might be?\""

r ttalk2 "\"Melisa, hmm? I think she should be at wing D in one of her labs there.\""
r ttalk "\"I think she has an appointment with Amir.\""

mc talk "\"Thanks... that's really helpful.\""

r ttalk "\"It's my pleasure, [mc].\""
r ttalk2 "\"Hmm... my signals seem to detect a large amount of stress coming from you, [mc].\""
r ttalk "\"Is there anything I can help you with to relieve that stress?\""

mc talk "\"Um...\""
mc talk2 "\"I think I am okay, really.\""

r ttalk2 "\"You sure? Perhaps you need help with some sexual relieve?\""
r ttalk "\"You know I am trained to provide that service too if necessary. Don't be shy.\""

mc talk "\"Well... since she offered... should I accept?\""

$ quick_menu = False

menu:
    "Accept her offer":
        $ quick_menu = True
        $ accepted_sex_ruby = True
        mc talk2 "\"Why the heck not. Show me what you got.\""
        
        r ttalk2 "\"It will be my pleasure, [mc].\""
        r ttalk "\"Please get comfortable and let me do all the work.\""
        jump sex_ruby
    "Decline":
        $ quick_menu = True
        $ accepted_sex_ruby = False
        mc talk "\"Thanks, but no thanks. I am in a bit of a hurry as well.\""
        
        r ttalk "\"Okay then. If you ever need to release tension and have nobody to help you, I can be of service.\""
        
        mc talk2 "\"Thank you, Ruby. I will keep that in mind for the future.\""
        jump after_ruby_cc

label sex_ruby:

scene rubyblowjob00
with dissolve

"Ruby kneels down and takes out your member..."

#animation here

$ quick_menu = False
show screen ruby_bj_1
$ renpy.show("ruby_bj_1")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label ruby_bj_1:
hide screen ruby_bj_1

scene rubyblowjob00
with dissolve

$ quick_menu = True
mc pleasure "Ahh... I can feel myself getting close... should I finish on her now or try and hold on to get a feel for her 'properties' down there too?"
$ quick_menu = False
menu:
    "Cum on her breasts":
        $ quick_menu = True
        $ ruby_came_on_breasts = True
        $ ruby_came_inside = False
        mc pleasure "\"Hahh... I am getting close, Ruby.\""
        mc pleasure2 "\"Can I finish on your breasts?\""
        
        r ttalk2 "\"Of course.\""
        scene cummingonbreasts 1
        with dissolve
        
        mc pleasure "\"Hahh...\""
        mc pleasure2 "\"Cumming!\""
        
        scene cummingonbreasts 2
        with flash
        scene cummingonbreasts 2
        with flash
        scene cummingonbreasts 2
        with flash
        
        $ renpy.pause(1.1, hard=True)
        
        scene cummingonbreasts 3
        with dissolve
        r ttalk "\"I hope this was all of your stress out since it was quite a lot.\""
        mc talk "\"I sure feel less... stressful.\""
        scene cummingonbreasts 4
        with dissolve
        r ttalk2 "\"That is good. If you ever need help again let me know. We can't have people stressed and unhappy here.\""
        mc thinking "Yeah... 'unhappy' and 'stressed'... I wonder why."
        mc talk2 "\"Definitely.\""
        
        scene rubyaftersex2
        with dissolve
        
        r ttalk "\"Well, I hope you can find your way to Wing D on your own since I still have some work left to do here...\""
        r ttalk2 "\"...And some cleaning up.\""
        mc talk "\"Of course. I think I will be fine. Thanks and see you for now.\""
        r ttalk2 "\"Good bye for now and keep your stress levels in check.\""
        jump after_ruby_cc
        
    "Hold it":
        $ quick_menu = True
        $ ruby_came_on_breasts = False
        $ ruby_came_inside = True
        mc talk "\"You are really good at this, but you think we can go to phase 2 now?\""
        
        r ttalk "\"Phase 2?\""
        
        mc talk2 "\"You know... actual fucking? If you're able to provide that kind of service too.\""
        
        r ttalk2 "\"Of course we may.\""
        
        r ttalk "\"Use my artifical pussy to your delight.\""
        
        "Ruby climbs on top of the control panel and reveals her body to you."
        
        scene rubysittingportrait with fade:
            subpixel True
            yalign 1.0
            pause 2.0
            linear 7.0 yalign 0.0
        pause

        "You climb on top of her and start pounding her pussy."
        
        #animation here
        
        $ quick_menu = False
        show screen mc_fuck_ruby
        $ renpy.show("mc_fuck_ruby")
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(12, hard=True)

        label mc_fuck_ruby:
        hide screen mc_fuck_ruby
        
        $ quick_menu = True
        mc pleasure "She really knows how to tighten her pussy just the right way... she is making me cum already..."
        mc pleasure2 "I guess cumming inside her won't be an issue, so I will let myself go with the flow..."
        mc pleasure "\"I am cumming!!~\""
        
        scene cumminginsideruby1
        with flash
        scene cumminginsideruby1
        with flash
        scene cumminginsideruby1
        with flash
        
        $ renpy.pause(1.1, hard=True)
        
        scene fuckingrubyscene
        with dissolve
        
        mc talk "\"This is not a problem, right?\""
        
        r ttalk "\"Not at all. It won't hurt my inside system at all and obviously we can't conceive a baby, but that wouldn't been an issue either, even if we could.\""
        
        mc thinking "Somehow she makes it sound hot."
        mc talk "\"Well, thanks for this Ruby. It's much appreciated.\""
        
        r ttalk2 "\"My pleasure, [mc]. Anytime you have the need you can let me know if you cannot find a partner.\""
        
        mc talk2 "\"Thank you, Ruby. I will keep it in mind. See you for now!\""
        jump after_ruby_cc
        
jump after_ruby_cc

label after_ruby_cc:
if accepted_sex_ruby:
    
    with fadein
    scene hallwaychloezoey00

    mc thinking "Well that was nice and unexpected. She provides these kind of services too? She comes with the whole package."
    mc thinking "I wonder if she provides these... services... to everybody on the ship?"
    mc thinking "Now to get back on track and get to Wing D..."
    "\"FUCK~~ Mmmmm.\""
    mc thinking "What the?"
    show hallwaylistening
    with dissolve
    "\"You tasty so good you little cutie~\""
    mc thinking "Someone is having a good time. Isn't this Zoey's room? I can't tell who's voice this is though..."
    "\"I am dripping wet~\""
    mc thinking "It sounds really hot in there."
    mc thinking "Anyway, she has roommates so it could be someone else."
    mc thinking "Now to get back on track and find Melisa's lab..."
    jump aftermeetingchloehallway

else:
    scene hallwaychloezoey0
    with dissolve
    mc thinking "I don't have the time to fool around right now."
    mc thinking "Although it's nice to know she is programmed to do these sort of things."
    jump chloe_in_hallway

label chloe_in_hallway:

scene hallwaychloezoey0
with dissolve

"As you were having thoughts, you suddenly see Chloe and she seems to be with Zoey next to her!"


scene hallwaychloezoey1
with dissolve

chloe talk "\"So you are sharing your room with other people, huh?\""

z talk "\"Yes, but I am okay with it. It's not that big of a deal.\""

chloe talk2 "\"Are they here now?\""

z talk2 "\"They shouldn't be.\""

chloe talk "\"I hope so. Would suck to be interrupted.\""

scene hallwaychloezoey2
with dissolve

mc shocked "What are they going to do?"

"Chloe seem to have noticed you"    

if chloe_spectate_talk:

    scene hallwaychloezoey
    with dissolve

    mc thinking "Is she gesturing me to follow her?"
    mc shocked "Is Zoey the girl she was talking about?"
    mc thinking "Zoey is also leading her to her room..."

    scene chloekeepquiet
    with dissolve

    mc thinking "She is telling me to be quiet now..."
    mc thinking "I guess Zoey didn't notice me..."
    mc thinking "Should I watch what they are going to do?"
    mc thinking "I can only imagine what Chloe has in mind..."
    $ quick_menu = False
    menu:
        "Watch":
            $ quick_menu = True
            $ watched_chloe_fuck_zoey = True
            mc thinking "Might as well watch. I want to make sure Zoey is okay with this if anything."
            scene hallwaychloezoey4
            with dissolve
            mc thinking "With Zoey having no memories of me I really can't tell her what to do..."
            mc thinking "Be responsible..."
            scene lookinginsidezoeyroom
            with dissolve
            mc shocked "Woah... she doesn't waste any time does she?"
            mc thinking "She is stripping her clothes off..."
            mc thinking "I will go in a little bit closer to get a better angle."
            scene closeupchloeass
            with dissolve
            mc thinking "She really knows how to show off."

            chloe nudetalk "\"Come on, you knew what we were going to do. Strip off!\""
            chloe nudeyummy "\"I want to see this cute little body of yours.\""
            z pleased "\"Are you sure though? I don't know if this is the best place... did you lock the door?\""
            chloe nudeyummy2 "\"Of course, sweety. You don't have to worry about that, now get comfortable on that bed.\""
            scene closeupchloeass2
            with dissolve
            z nudedesire "\"I... I've never been with a girl before...\""
            chloe nudetalk "\"You have nothing to be scared of. I will make you feel really good.\""
            chloe nudeyummy "\"Now, spread your legs for me.\""
            scene chloeeatingzoey0
            with dissolve
            z nudetalk "\"Like this?\""
            chloe nudeyummy2 "\"Just like that. Mmmmm. Let me taste your cute little pussy.\""
            
            #animation here
            
            $ quick_menu = False
            show screen chloe_eats_zoey
            $ renpy.show("chloe_eats_zoey")
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(12, hard=True)

            label chloe_eats_zoey:
            hide screen chloe_eats_zoey
            
            scene chloeeatingzoey
            with flash
            scene chloeeatingzoey
            with flash
            scene chloeeatingzoey
            with flash
            $ quick_menu = True
            z nudepleasure "\"Oh GOD!!\""
            z nudepleasure "\"I am cumming!\""
            chloe nudeyummy "\"Yess~ squirt it all in my mouth..\""
            chloe nudeyummy2 "\"Let me drink your juices.\""
            z nudeflirting "\"Hahh..Hahh...\""
            
            scene chloeremovespanties
            with dissolve
            
            chloe nudetalk "\"You are fucking delicious, Zoey. But I am really horny now and I need you to return the favor, okay?\""
            z nudeflirting "\"Okay.\""
            chloe nudetalk2 "\"Let me get these panties off... They are already dripping wet from the anticipation.\""
            
            scene chloeonzoey
            with dissolve
            
            chloe nudeyummy "\"Are you ready, sweety?\""
            chloe nudeyummy2 "\"Are you ready to eat my cunt?\""
            z nudetalk "\"Yes...\""
            chloe nudetalk2 "\"I can't wait for you to slurp up all of my juices...\""
            chloe nudetalk "\"It's making me feel so hot...\""
            chloe nudetalk2 "\"I haven't been this horny since I fucked with Rachel...\""
            z nudetalk2 "\"Who?\""
            chloe nudetalk "\"Nevermind, just start eating me!\""
            
            #animation 2 here
            
            $ quick_menu = False
            show screen Chloe_Sits_On_Zoey
            $ renpy.show("Chloe_Sits_On_Zoey")
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(12, hard=True)

            label Chloe_Sits_On_Zoey:
            hide screen Chloe_Sits_On_Zoey
            
            show chloecumming
            with flash
            show chloecumming
            with flash
            show chloecumming
            with flash
            $ quick_menu = True
            chloe nudepleasure "\"Oh FUUUUU--CK~!\""
            chloe nudepleasure "\"I am cumming~!\""
            chloe nudepleasure "\"EAT MY JUICES YOU LITTLE SLUT!\""
            chloe nudepleasure "\"Ahh...Hah...Hahh...\""
            chloe nudetalk "\"Holy... fuck...\""
            chloe nudetalk2 "\"I need a cigaratte...\""
            
            scene zoeyaftersex
            with dissolve
            
            hide chloecumming
            
            chloe nudetalk "\"I really messed you up there, huh?\""
            chloe nudetalk2 "\"Sorry for calling you a slut. I got carried away...\""
            z nudetalk "\"It's fine! I liked it. It suits you being the dominating kind.\""
            chloe nudetalk "\"Oh yeah? Well if we ever fuck again I will be sure to remember that.\""
            z nudetalk2 "\"Who is Rachel anyway?\""
            
            scene chloesmokingaftersex
            with dissolve
            
            chloe nudetalk2 "\"Oh, it's my girl back on Earth. It's kind of... complicated.\""
            z nudetalk "\"Oh, okay... I just hope she is okay with you doing this?\""
            
            chloe nudetalk "\"You don't have to worry your pretty little head about it. You and me are together now and that's what matters.\""
            
            mc thinking "Welp... I saw everything I needed to see... time to make my leave."
            jump aftermeetingchloehallway
        "Don't":
            $ quick_menu = True
            $ watched_chloe_fuck_zoey = False
            mc thinking "I probably shouldn't be watching on Zoey like this... I just have to trust that she'd be responsible."
            mc thinking "Now I need to get to Wing D..."
            jump aftermeetingchloehallway
        
else:
    
    scene hallwaychloezoey3
    with dissolve

    $ watched_chloe_fuck_zoey = False
    "She looks at your direction and flips you right off."
    mc shocked "What the...!?"
    mc thinking "I guess she is still mad I came inside of her..."
    mc thinking "But she and Zoey? What are they going to do? They are going to Zoey's room it seems..."

    scene hallwaydoorclosed
    with dissolve

    mc thinking "God damn she even locked the door behind her..."
    mc thinking "She must be really mad."
    mc thinking "I hope she can let go of what happened..."
    mc thinking "Nevermind that... I still have to get to Wing D..."
    jump aftermeetingchloehallway



#---------------------------------------------------------------------------------------------------------------------------------------------------

        
label aftermeetingchloehallway:
scene hallwaymc1
with dissolve
mc thinking "It should be this way... I think. I am still unfamiliar with the whole layout of the ship."

hide hallwaylistening

with fasterfadein
scene meanwhile
$ quick_menu = False
pause 2.5
with fasterfadeout

scene beforeassimroom1
with fasterfadein
$ quick_menu = True



d talk "\"So what exactly are we doing here?\""
d talk2 "\"You said you had some proposition to help me and my people?\""

amir talk "\"Of course, of course. I am not a liar.\""
amir talk "\"I know your people are going through hard time back on Earth and they could use all the financial support they can get.\""
amir smile "\"But how far are you willing to go to help your people?\""
amir talk "\"You are the minority and not everybody is okay with having you there.\""
amir smile "\"I personally don't care and welcome you, but I am sure you could use the help.\""

d talk "\"I can only imagine you will want something in return.\""

amir smile "\"Well, I do want to help you and in return all I ask is for you to help me.\""

d talk "\"With what?\""

amir talk "\"It's quite simple, really.\""

scene beforeassimroom2
with dissolve

amir smile "\"Unless you are opposed to doing that kind of stuff in order to help your people?\""
amir talk "\"We are all free folk here and it is your decision.\""

d talk "\"So you want me to help you get off? We didn't need to come here for you to tell me that.\""

amir talk "\"We do, actually. I wouldn't make you do something against your will.\""
amir smile "\"The reason we are here is for you to see what you will be dealing with.\""

d talk2 "\"What do you mean?\""

amir talk "\"You will see in a second. Let's go in and greet Melisa.\""

scene melisacloseup
with dissolve
amir talk "\"Hello there, Melisa. I hope I am not too early.\""

m smile "\"You came just in time, Amir.\""
m talk "\"The serum is tested and complete. We can proceed if you are ready to go.\""

scene dahliaamirreanimm2
with dissolve

amir smile "\"Of course. Let's get right to business.\""

scene dahliaamirreanimm
with dissolve

d talk "\"Serum...?\""

scene dahliaamirreanimm2
with dissolve

amir talk "\"You will see in a sec, sweet cheeks.\""
amir smile "\"Just tell me what I have to do.\""

m talk "\"Start by removing your clothes.\""

scene amirnudereanimm
with fadein

amir nudetalk "\"Simple enough.\""

m smile "\"Mm, yes, quite.\""
m talk "\"But to proceed we are going to need you to get hard... down there.\""
m smile "\"I am guessing Dahlia is here to provide these services? Or if not I can help with that.\""

scene amirthinking
with dissolve

amir nudetalk "\"Hmm, who should it be?\""
$ quick_menu = False
menu:
    "Dahlia":
        $ quick_menu = True
        amir nudetalk "\"Dahlia can you start your service to me with this simple task?\""
        amir nudesmile "\"Removing your clothes would be appreciated as it will speed up the process.\""
        
        d talk "\"I suppose I can use my hand.\""
        d talk2 "\"We need to discuss the details about your end of the deal though.\""
        
        amir nudetalk "\"Later. First we do this.\""
        
        scene melisapointingtochair
        with dissolve
        
        m talk "\"Great. Now please, get comfortable on the chair over there.\""
        
        scene amirsittingdown
        with dissolve
        
        m talk "\"Note that you can't actually cum. I just need you to get hard. It's important.\""
        
        amir nudesmile "\"It will be hard with such a devilishly sexy looking girl stroking me, but I will do my best.\""
        
        m smile "\"Whenever you are ready Dahlia.\""
        
        scene dahliahjamir 00
        with dissolve
        
        "Dahlia strips her top off and kneels down."
        
        #animation here
        
        $ quick_menu = False
        show screen dahlia_hj_amir
        $ renpy.show("dahlia_hj_amir")
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(12, hard=True)

        label dahlia_hj_amir:
        hide screen dahlia_hj_amir

        scene dahliahjamir 05
        with dissolve
        
        $ quick_menu = True
        m talk "\"Now that you are hard we can continue to step 2 and apply the serum on top of your erect penis.\""
        m talk "\"Be aware that you might experience a little bit of a pain, but it will pass in a matter of seconds.\""
        amir nudetalk "\"I can take it. Go on.\""
        
        scene amirdroplet
        with dissolve
        
        m smile "\"Just a few drops will suffice.\""
        amir nudetalk "\"What the... shit??\""
        
        scene amirpainassim
        with dissolve
        
        amir nudeangry "\"WOAH... FUCK.\""
        amir nudeangry "\"You weren't kidding about the pain this causes.\""
        m talk "\"Minor inconvinience really. In the grand scheme of things the pain will be well worth it.\""
        amir nudeangry "\"SHIIIIIIIT. IT BURNS. I CAN FEEL IT GROWING.\""
        m smile "\"My,my... and it continues to grow.\""
        
        scene amirdickgrow0
        $ renpy.pause(1.5, hard=True)
        $ renpy.transition(Dissolve(0.1800))
        scene amirdickgrow
        $ renpy.pause(1.5, hard=True)
        $ renpy.transition(Dissolve(0.1800))
        
        d surprised "\"What the fuck!?\""
        
        
        jump afterdahliahjamir
        
        
        
        
    "Melisa":
        $ quick_menu = True
        amir nudetalk "\"Since you offered, Melisa. I'd love to use your services.\""
        
        m smile "\"Of course. It will be my pleasure to help out.\""
        
        scene melisapointingtochair
        with dissolve

        m talk "\"Please, sit down on the chair and get comfortable.\""
        
        scene amirsittingdown
        with dissolve

        m nudetalk "\"Note that you can't actually cum. I just need you to get hard. It's important.\""
        
        amir nudetalk "\"It will be kind of hard with such a sexy girl stroking me, but I will try my best.\""
        
        m nudesmile "\"Why, thank you.\""

        scene melisahjamir 00
        with dissolve

        m nudetalk "\"Alright then. Let me begin.\""
        
        #animation here
        
        $ quick_menu = False
        show screen melisa_hj_amir
        $ renpy.show("melisa_hj_amir")
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(12, hard=True)

        label melisa_hj_amir:
        hide screen melisa_hj_amir
        
        scene melisahjamir 05
        with dissolve
        
        $ quick_menu = True
        m nudetalk "\"Mm you are nice and hard. Now we can continue to step 2 and apply the serum on top of your erect penis.\""
        m nudetalk "\"Be aware that you might experience a little bit of a pain, but it will pass in a matter of seconds.\""
        amir nudetalk "\"I can take it. Go on.\""
        
        scene amirdropletnude
        with dissolve
        
        m nudesmile "\"Just a few drops will suffice.\""
        amir nudetalk "\"What the... shit??\""
        
        scene amirpainassim
        with dissolve

        amir nudeangry "\"WOAH... FUCK.\""
        amir nudeangry "\"You weren't kidding about the pain this causes.\""
        m nudetalk "\"Minor inconvinience really. In the grand scheme of things the pain will be well worth it.\""
        amir nudeangry "\"SHIIIIIIIT. IT BURNS. I CAN FEEL IT GROWING.\""
        m nudesmile "\"My,my... and it continues to grow.\""
        
        scene amirdickgrow0
        $ renpy.pause(1.5, hard=True)
        $ renpy.transition(Dissolve(0.1800))
        scene amirdickgrow
        $ renpy.pause(1.5, hard=True)
        $ renpy.transition(Dissolve(0.1800))
    
        d surprised "\"What the fuck!?\""
        
        jump aftermelisahjamir
