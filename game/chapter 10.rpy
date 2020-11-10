label startch10:
scene black
with fasterfadein
"After a few hours..."
scene ch10room1
with fasterfadein
mc nudethinking "Ah, all rested up."
"You dress up..."
scene ch10room2
mc thinking "Let's see what Ruby found out about the cryo chamber."

scene ch10cc1
with fadein
"You enter the Command Center and see Ruby already there."
mc talk3 "\"Hey, Ruby.\""


r ttalk "\"Hi, [mc].\""
r ttalk2 "\"I have some bad news...\""
mc talk "\"What is it?\""
r ttalk "\"It seems there is a slight problem with the cryo chambers...\""
mc talk "\"How 'slight' in terms of time to fix are we talking about here?\""
r ttalk2 "\"Approximately 10 months.\""
mc shocked "\"{size=+10}10 months?!{/size}\""
mc talk3 "\"That's way too long...\""
r ttalk "\"It's nothing when you will be sleeping for the next 200 years.\""
mc talk2 "\"That's a good point I guess...\""
mc talk "\"Let Jane know and get to work on fixing it then. We can't waste anymore time.\""
r ttalk2 "\"Roger that. In the mean time, let me show you something.\""

scene ch10cc2
with fasterfadein
"You move in closer."

mc talk2 "\"What am I looking at here, Ruby?\""
r ttalk "\"You can use this screen to check on each camera on Paradise, [mc].\""
r ttalk2 "\"If you're looking for someone this is the best way to find them.\""
r ttalk "\"Do you want to look someone up right now for demonstration?\""

if persistent.show_ntr:
    $ quick_menu = False
    menu:
        "Look up what Cassandra is doing":
            $ quick_menu = True
            $ch10cass_ntr = True
            mc talk "\"Let me see what Cassandra is up to.\""
            scene black
            with dissolve
            r ttalk "\"Of course.\""
            scene ch10andrecass1
            with fadein
            cass nudetalk "\"Mm, baby~\""
            a shirttalk2 "\"*Chu* *Slurp*\""
            scene ch10andrecass2
            with dissolve
            a shirttalk "\"You like that?\""
            cass nudetalk2 "\"I love it~\""
            cass nudetalk "*Slurp*"
            cass nudetalk2 "\"Lie down.\""
            scene ch10andrecasshj
            with fasterfadein
            cass nudetalk "\"So hard already. I love it.\""
            
            $ quick_menu = False
            show screen ch10_cass_hj
            $ renpy.show("ch10_cass_hj")
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(12, hard=True)

            label ch10_cass_hj:
            hide screen ch10_cass_hj
            
            $ quick_menu = True
            a shirttalk2 "\"Ah, I love it, babe.\""
            cass nudetalk "\"Mmm~ I can see that.\""

            
            
            scene ch10andrecass4
            with dissolve
            
            a shirttalk2 "\"I can already feel you dripping wet down there.\""
            
            a shirttalk2 "\"Let's move on to the main event.\""
            
            cass nudetalk2 "\"Yes~!\""
            
            scene ch10andrecass2vag
            with fasterfadein
            
            a shirttalk2 "\"You ready?\""
            
            cass nudetalk "\"Yesss. Fuck me already.\""
            
            scene ch10andrecass2vag
            with flash
            
            $ quick_menu = False
            show screen ch10_cass_vag
            $ renpy.show("ch10_cass_vag")
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(12, hard=True)

            label ch10_cass_vag:
            hide screen ch10_cass_vag
            $ quick_menu = True
            cass nudepleasure "\"{size=+10}GO FASTER!!!{/size}\""
            
            $ quick_menu = False
            show screen ch10_cass_vag2
            $ renpy.show("ch10_cass_vag2")
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(12, hard=True)

            label ch10_cass_vag2:
            hide screen ch10_cass_vag2
            
            $ quick_menu = True
            a shirttalk2 "\"Ah... I am about to...\""
            
            cass nudepleasure "\"Do it. Fill me inside.\""
            
            a shirttalk2 "\"You sure?\'"
            
            cass nudepleasure "\"Yes. I want your baby. Do it! {size=+7}Impregnate me!!!{/size}\""
            
            
            scene ch10andrecum1
            with vpunch
            a shirttalk2 "\"I am cumming!!\""
            scene ch10andrecum1
            with flash
            scene ch10andrecum1
            with flash
            scene ch10andrecum1
            with flash
            scene ch10andrecum1
            with flash
            cass nudepleasure "\"Mmmmm, yesss~\""
            cass nudepleasure "\"I can feel your semen filling me up.\""

            scene ch10andrecum2
            with vpunch
            cass nudepleasure "\"Ahhhh... I can't keep it all inside me...\""
            scene ch10cc2
            with fasterfadein
            r ttalk "\"You got how this works?\""
            mc talk "\"...\""
            r ttalk2 "\"Are you okay, [mc]?\""
            mc talk2 "\"I am fine...\""
            "Witnessing your wife getting impregnated is not fine at all, but you can't express your feelings to a machine."
            jump ch10afterntr
else:
    $ch10cass_ntr = False
    scene black
    with fasterfadein
    r ttalk "\"And just like that...\""
    "..."
    scene ch10cc2
    with fasterfadein
    r ttalk2 "\"You understood how to use it?\""
    mc talk "\"Yeah, I got it.\""
    jump ch10afternontr
    with fasterfadein


label ch10afternontr:
scene ch10ccruby1
with dissolve

r ttalk "\"Is there anything else I can do for you right now, Commander?\""
$ quick_menu = False
menu:
    "Undress":
        $ quick_menu = True
        mc talk2 "\"Yes, actually. I'd like for you to undress right now.\""
        jump ch10rubysexx2
    "No, that's all for now":
        $ quick_menu = True
        mc talk "\"No. That would be all.\""
        jump aftertimeskip3

label ch10rubysexx2:
scene ch10ccruby2
with dissolve
r nudettalk "\"Of course, [mc].\""
r nudettalk2 "\"Anything I can do to be of service.\""

scene ch10cc4
with fasterfadein
"Ruby undresses and sits in a provocative pose on the chair next to you."
$ quick_menu = False
menu:
    "Fuck her":
        jump ch10rubysexx3

label ch10rubysexx3:
$ch10ruby = True
scene ccanim
with dissolve
$ quick_menu = True
mc talk2 "\"Ready?\""
r nudettalk "\"I am ready for you, Commander.\""
scene ccanim
with flash
"You insert your penis in her and start fucking her."

with flash

$ quick_menu = False
show screen ch10_ruby2
$ renpy.show("ch10_ruby2")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label ch10_ruby2:
hide screen ch10_ruby2
$ quick_menu = True
mc pleasure "\"I am getting close...\""

r nudettalk2 "\"Cum wherever you want, [mc].\""
$ quick_menu = False
menu:
    "Cum on her stomach":
        $ quick_menu = True
        
        scene ch10cccum1
        with flash
        mc pleasure2 "\"I am cumming~\""
        scene ch10cccum1
        with flash
        scene ch10cccum1
        with flash
        scene ch10cccum2
        with flash
        scene ch10cccum2
        with flash
        scene ch10cccum3
        with flash
        mc pleasure "\"Ah...\""
        mc pleasure "\"Hahh... feeling a little bit better...\""
        mc talk "\"That was nice. Thank you, Ruby.\""
        r nudettalk "\"My pleasure, Commander.\""
        scene black
        with fadein
        jump aftertimeskip3

    "Cum inside her":
        $ quick_menu = True
        scene ch10cccum4
        with flash
        mc pleasure2 "\"I am cumming~\""
        scene ch10cccum4
        with flash
        scene ch10cccum4
        with flash
        scene ch10cccum4
        with flash
        mc pleasure "\"Ah...\""
        mc pleasure "\"Hahh... feeling a little bit better...\""
        mc talk "\"That was nice. Thank you, Ruby.\""
        r nudettalk "\"My pleasure, Commander.\""
        scene black
        with fadein
        jump aftertimeskip3


label ch10afterntr:
scene ch10ccruby1
with dissolve

r ttalk "\"Is there anything else I can do for you right now, Commander?\""
$ quick_menu = False
menu:
    "Undress":
        $ quick_menu = True
        mc talk2 "\"Yes, actually. I'd like for you to undress right now.\""
        jump ch10rubysex
    "No, that's all for now":
        $ quick_menu = True
        mc talk "\"No. That would be all.\""
        jump aftertimeskip1

label ch10rubysex:
scene ch10ccruby2
with dissolve
r nudettalk "\"Of course, [mc].\""
r nudettalk2 "\"Anything I can do to be of service.\""

scene ch10cc4
with fasterfadein
"Ruby undresses and sits in a provocative pose on the chair next to you."
$ quick_menu = False
menu:
    "Fuck her":
        jump ch10rubysex2

label ch10rubysex2:
$ch10ruby = True
scene ccanim
with dissolve
$ quick_menu = True
mc talk2 "\"Ready?\""
r nudettalk "\"I am ready for you, Commander.\""
scene ccanim
with flash
"You insert your penis in her and start fucking her."

with flash

$ quick_menu = False
show screen ch10_ruby
$ renpy.show("ch10_ruby")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label ch10_ruby:
hide screen ch10_ruby
$ quick_menu = True
mc pleasure "\"I am getting close...\""

r nudettalk2 "\"Cum wherever you want, [mc].\""
$ quick_menu = False
menu:
    "Cum on her stomach":
        $ quick_menu = True
        
        scene ch10cccum1
        with flash
        mc pleasure2 "\"I am cumming~\""
        scene ch10cccum1
        with flash
        scene ch10cccum1
        with flash
        scene ch10cccum2
        with flash
        scene ch10cccum2
        with flash
        scene ch10cccum3
        with flash
        mc pleasure "\"Ah...\""
        mc pleasure "\"Hahh... feeling a little bit better...\""
        mc talk "\"That was nice. Thank you, Ruby.\""
        r nudettalk "\"My pleasure, Commander.\""
        scene black
        with fadein
        jump aftertimeskip1

    "Cum inside her":
        $ quick_menu = True
        scene ch10cccum4
        with flash
        mc pleasure2 "\"I am cumming~\""
        scene ch10cccum4
        with flash
        scene ch10cccum4
        with flash
        scene ch10cccum4
        with flash
        mc pleasure "\"Ah...\""
        mc pleasure "\"Hahh... feeling a little bit better...\""
        mc talk "\"That was nice. Thank you, Ruby.\""
        r nudettalk "\"My pleasure, Commander.\""
        scene black
        with fadein
        jump aftertimeskip1

label aftertimeskip1:
$ quick_menu = False
scene sixmonthslater
with fadein
$ renpy.pause(2, hard=True)

scene black
with fadein

$ quick_menu = True
mc thinking "6 months have passed..."

scene ch10sixmonths1
with fadein

mc thinking "Time seem to have stopped... everything is the same and everyone is on edge."
mc thinking "It doesn't help that my family still doesn't remember me and probably won't remember me in the remaining 4 months that we need to fix the cryogenic pods."
mc thinking "Not to mention my wife..."
scene ch10sixmonths2
with fasterfadein
"As you move closer you hear footsteps coming from the stairs leading to the upper level."

$ quick_menu = False
scene ch10sixmonths4 with fade:
    subpixel True
    yalign 1.0
    pause 2.0
    linear 7.0 yalign 0.01
pause

scene ch10sixmonths3
with dissolve
$ quick_menu = True
"You check on your right and spot Cassandra and Andre coming down the stairs."
mc thinking "Talk about the devil..."

scene ch10sixmonths5
with dissolve

a njtalk "\"Oh, hey [mc].\""
mc talk2 "\"Hey there. How are you guys doing?\""
a njtalk2 "\"Good. Good.\""
a njtalk "\"We were just heading to Melisa for our checkup.\""
scene ch10sixmonths6
with dissolve
cass ptalk "\"He is kicking quite strong in there.\""
a njtalk2 "\"Hahaha. So it's a he is that so?\""
cass ptalk "\"Yep. It's a he. And I already have a name for him, but you will have to wait to find out!\""
scene ch10sixmonths5
with dissolve
mc talk "\"Well, I won't waste your time then. Melisa must be waiting for you. Take care for now.\""
a njtalk "\"Thank you, [mc]. And thank you for everything you've been doing lately.\""
mc talk2 "\"Don't mention it...\""
"You say with obvious grimace to the man who fucked and impregnated your wife."
label aftertimeskip2:
$ quick_menu = False
scene fourmonthslater
with fadein
$ renpy.pause(2, hard=True)

scene ch10cc6
with fadein

$ quick_menu = True
"Months have passed and today was the day for the long sleep ahead."
"Jane fixed the issue and everything seems to be in working condition with the cryo chambers."
scene ch10cc7
with fasterfadein
"You go in and check if there is anything interesting on the cameras..."
$ quick_menu = False
menu:
    "Check on Melisa's lab":
        $ quick_menu = True
        scene ch10medbay1
        with fadein
        m talk "\"So, how are we feeling today, Cassandra?\""
        cass ptalk "\"We are pretty good. His cold seems to have gone away.\""
        "You hear a faint baby scream in the room."
        cass ptalk "\"There, there. I will feed you now, don't cry.\""
        m talk2 "\"That's good to hear. Remember to take those vitamins I gave you today as well. One after each meal.\""
        scene ch10medbay2
        with dissolve
        cass ptalk "\"Of course. He doesn't seem to refuse to eat them either which is good.\""
        "You hear sucking noises from the room."
        cass pthinking "\"There, there A.J. All better now.\""
        m talk "\"I am really glad to witness, hopefully, the first of many babies as we repopulate.\""
        cass ptalk "\"I am honored to be the first one, haha.\""
        cass ptalk "\"I was actually curious if this cryo sleep will be dangerous for him? Since he is so young still.\""
        m talk2 "\"It shouldn't be any issue.\""
        cass ptalk "\"Even development wise?\""
        scene ch10medbay1
        with dissolve
        m talk "\"It should be fine, don't worry.\""
        m talk2 "\"Speaking of which you should both prepare for that.\""
        cass ptalk "\"Yeah. We are going to do that right now.\""
        scene ch10cc7
        with fadein
        mc thinking "Cassandra gave birth a few weeks ago to a healthy boy... everyone was extremely happy that the human race is repopulating, except maybe for me."
        mc thinking "I got over it eventually... after endless nights watching her with a different man. It's something you have to get over or let it slowly kill you."
        mc thinking "Anyway... Today is the big day. We will finally go in cryo sleep and wake up in about 200 years from now and hopefully in our new home."
        mc thinking "Is there anyone I should visit before that?"
        jump ch10ccvisit

label aftertimeskip3:
scene tenmonthslater
with fadein
$ renpy.pause(2, hard=True)

scene ch10cc6
with fadein
mc thinking "10 months have passed since then. Not much has changed except everyone eagerly waiting for the day we fix the cryogenic pods and hopefully wake up next to our new home."
mc thinking "Today is that day."
scene ch10cc7
with fadein
mc thinking "Is there anyone I should visit before that?"
jump ch10ccvisit

label ch10ccvisit:
scene ch10cc7
with fasterfadein
$ quick_menu = False
menu:
    "Visit Elyse & Zoey":
        $ quick_menu = True
        jump ch10elysezoey1
    "Visit Chloe":
        $ quick_menu = True
        jump ch10chloe1

#------------------------------------------------------------------------------------------------------------------------------------------------
label ch10elysezoey1:
    if mc_zoey_sex:
        jump ch10elysezoey2
    elif sex_with_elyse:
        jump ch10elysezoey2
    else:
        scene black
        with fadein
        "You visit Zoey and Elyse in their room..."
        "You talk with them a bit and see how they are doing."
        "After seeing them prepared you go back to the Command Center..."
        jump ch10elysezoey3

label ch10elysezoey2:
$ch10_elysezoey_sex = True
scene ch10elysezoey1
with fasterfadein
"You enter their room and see them sitting on Zoey's bed."
mc talk "\"Hi, girls.\""
z pleasedbb "\"Oh, hi [mc]!\""
e nudetalk "\"[mc]? Something wrong?\""
mc talk2 "\"Nah. I just came to check on my 2 favorite girls.\""
e nudehappy "\"Favorite girls, huh?\""
e nudehappy "\"But who is the favorite in the room? Me or her?\""
mc thinking "Oh no..."
scene ch10elysezoey2
with dissolve
z talkbb "\"Haha. We were actually arguing who's boobs were better.\""
z flirtingbb "\"It's obviously mine, but we need a third person to decide, so good timing!\""
scene ch10elysezoey3
with fasterfadein
"Before you can even say anything they remove their tops and reveal their breasts to you."
z nudetalk2 "\"It's obviously mine, right? Bigger and more firm.\""
e nudeskeptical "\"Bigger doesn't necessarily mean better.\""
z nudeflirting "\"Suuuure. That's what someone with small breasts would say.\""
e nudesad "\"*Grrr*\""
mc thinking "*Sigh* I need to do something before they start pulling each other's hair."
scene ch10elysezoey4
with dissolve
mc talk3 "\"Both are great, okay?\""
mc talk2 "\"There is no need for competition when both of you are winners.\""
mc talk "\"Small breasts are cute and Zoey's breasts are nice and firm. There is nothing wrong with either of them.\""
scene ch10elysezoey3
with dissolve
z nudetalk "\"Come on. That's no answer. Give them a feel at least before you decide.\""
z nudepleased "\"Give Elyse's tits a squeeze. Come on.\""
"You feel trapped and do as you're being told..."
scene ch10elysezoey5
with fasterfadein
"*Squeeze*"
mc thinking "Even though they are small... they are quite nice. I love her tits."
mc talk2 "\"Okay. They are perfect.\""
z nudeflirting "\"Mine next!\""
scene ch10elysezoey6
with vpunch
"Zoey pushes Elyse out of the way and moves right into your palms."
"*Squeeze* *Squeeze*"
"..."
z nudeflirting "\"They are so good you can't stop squeezing them, right?\""
mc talk3 "\"Ahah... both are great...I don't know what else to say.\""
z nudepleased "\"Forget the competition... All of this touching probably made you horny. Let's take care of the problem.\""
scene ch10elysezoey
with fasterfadein
"She unbuckles your pants and reveals your cock."
"Elyse joins in and they both start licking you without even asking for permission."
$ quick_menu = False
show screen ch10_elysezoey2
$ renpy.show("ch10_elysezoey2")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label ch10_elysezoey2:
hide screen ch10_elysezoey2
$ quick_menu = True
mc pleasure "\"Crap...\""
mc pleasure2 "\"I am about to...\""
$ quick_menu = False
menu:
    "Cum":
        $ quick_menu = True
        scene ch10elysezoey7
        with flash
        scene ch10elysezoey7
        with flash
        scene ch10elysezoey7
        with flash
        "You cum and splatter both their faces with semen."
        mc pleasure "\"Ahh....\""
        e nudepleasure "\"Mmmhh *Slurp*, *Suck*, *Lick*...\""
        z nudepleasure "\"That was really nice, [mc]. But you should leave now and let us clean up and prepare.\""
        mc talk3 "\"Of course.\""
        scene black
        with fadein
        mc thinking "*Sigh*... these girls..."
        "You move back to the Command Center."
        jump ch10elysezoey3

label ch10elysezoey3:
scene ch10cc7
with fasterfadein
"Who else should I visit?"
$ quick_menu = False
menu:
    "Chloe":
        jump ch10elysezoey4

label ch10elysezoey4:
if declined_chloe_sex:
    scene black
    with fadein
    $ quick_menu = True
    "You check up with Chloe and see if she is all prepared."
    "You spend some time with her and move back to the Command Center."
    jump ch10aftervisits
else:
    scene ch10chloe1
    with fasterfadein
    "You check the cameras and see Chloe sitting and watching the stars."
    "You get up and move to her location."
    scene ch10chloe2
    with fasterfadein
    "After a few minutes you arrive."
    scene ch10chloe3
    with dissolve
    mc talk2 "\"Hey Chloe. How are you doing?"
    chloe nudetalk2 "\"Oh, yo [mc].\""
    mc talk "\"What are you doing here all alone?\""
    chloe nudetalk "\"Just looking at the stars.\""
    chloe nudetalk2 "\"They are quite beautiful, don't you think?\""
    mc talk3 "\"Yeah. They are.\""
    chloe nudetalk "\"Would you like to join me?\""
    mc talk "\"Sure.\""
    scene ch10chloe4
    with fasterfadein
    "You sit down next to her."
    chloe nudetalk2 "\"Beautiful, yet so distant. I can't really see the Sun anymore either.\""
    chloe nudetalk "\"*Sigh*\""
    scene stars
    with dissolve
    mc talk2 "\"Yeah... I know what you mean.\""
    mc talk "\"But soon we will have a new Sun and a new Earth to call home.\""
    chloe nudetalk "\"Soon, huh?\""
    chloe nudetalk2 "\"If you mean 200 years then sure, that's like nothing.\""
    scene ch10chloe4
    with fasterfadein
    mc talk3 "\"200 in cryo sleep will be like a blink of an eye.\""
    mc talk "\"You won't even feel it.\""
    chloe nudetalk "\"I hope so.\""
    scene ch10chloe5
    with fasterfadein
    with vpunch
    "Chloe jumps in your arms."
    mc talk2 "\"Wow.\""
    chloe nudetalk2 "\"It will be pretty lonely 200 years you know...\""
    scene ch10chloe6
    with dissolve
    mc talk "\"Yeah?\""
    chloe nudetalk "\"Yep. So do you want to do something fun right now before that?\""
    $ quick_menu = False
    menu:
        "Have sex":
            $ quick_menu = True
            $ch10_chloe_sex = True
            mc talk2 "\"All right. Let's do this, Chloe.\""
            scene ch10chloe9
            with fasterfadein
            "Chloe lays down on the bench and removes her panties."
            chloe nudetalk "\"Ready?\""
            mc talk "\"Yeah.\""
            chloe nudetalk2 "\"Then what are you waiting for? Start fucking me.\""
            
            scene ch10chloeanim
            with dissolve
            "You do as your being told and start fucking her."
            $ quick_menu = False
            show screen ch10_chloe2
            $ renpy.show("ch10_chloe2")
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(12, hard=True)

            label ch10_chloe2:
            hide screen ch10_chloe2
            $ quick_menu = True
            chloe nudepleasure "\"Ahh...ahhh....mmmh...\""
            chloe nudepleasure "\"Go faster...\""
            $ quick_menu = False
            show screen ch10_chloe2x
            $ renpy.show("ch10_chloe2x")
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(12, hard=True)

            label ch10_chloe2x:
            hide screen ch10_chloe2x
            $ quick_menu = True
            mc pleasure2 "\"Ah... I am getting close...\""
            chloe nudepleasure "\"Mmm... yesss... Finish on my bellyyyy~\""
            
            scene ch10chloe7
            with flash
            mc pleasure "\"Ahhh---\""
            scene ch10chloe7
            with flash
            scene ch10chloe8
            with flash
            scene ch10chloe8
            with flash
            mc talk2 "\"That was great, Chloe.\""
            chloe nudetalk2 "\"I liked that too.\""
            chloe nudetalk "\"I have to go clean now.\""
            mc talk "\"Sure, I have to go now anyway.\""
            scene black
            with fadein
            "You leave and head back to the Command Center."
            jump ch10aftervisits
        "Say you gotta go":
            $ quick_menu = True
            $ch10_chloe_sex = False
            mc talk "\"Sorry, Chloe. I have to go and prepare myself and you should too.\""
            scene black
            with fadein
            chloe nudetalk2 "\"Yeah, sure, whatever. Just go.\""
            "You leave and head back to the Command Center."
            jump ch10aftervisits


#------------------------------------------------------------------------------------------------------------------------------------------------
label ch10chloe1:
if declined_chloe_sex:
    scene black
    with fadein
    "You check up with Chloe and see if she is all prepared."
    "You spend some time with her and move back to the Command Center."
    jump ch10chloe2
else:
    scene ch10chloe1
    with fasterfadein
    "You check the cameras and see Chloe sitting and watching the stars."
    "You get up and move to her location."
    scene ch10chloe2
    with fasterfadein
    "After a few minutes you arrive."
    scene ch10chloe3
    with dissolve
    mc talk2 "\"Hey Chloe. How are you doing?"
    chloe nudetalk2 "\"Oh, yo [mc].\""
    mc talk "\"What are you doing here all alone?\""
    chloe nudetalk "\"Just looking at the stars.\""
    chloe nudetalk2 "\"They are quite beautiful, don't you think?\""
    mc talk3 "\"Yeah. They are.\""
    chloe nudetalk "\"Would you like to join me?\""
    mc talk "\"Sure.\""
    scene ch10chloe4
    with fasterfadein
    "You sit down next to her."
    chloe nudetalk2 "\"Beautiful, yet so distant. I can't really see the Sun anymore either.\""
    chloe nudetalk "\"*Sigh*\""
    scene stars
    with dissolve
    mc talk2 "\"Yeah... I know what you mean.\""
    mc talk "\"But soon we will have a new Sun and a new Earth to call home.\""
    chloe nudetalk "\"Soon, huh?\""
    chloe nudetalk2 "\"If you mean 200 years then sure, that's like nothing.\""
    scene ch10chloe4
    with fasterfadein
    mc talk3 "\"200 in cryo sleep will be like a blink of an eye.\""
    mc talk "\"You won't even feel it.\""
    chloe nudetalk "\"I hope so.\""
    scene ch10chloe5
    with fasterfadein
    with vpunch
    "Chloe jumps in your arms."
    mc talk2 "\"Wow.\""
    chloe nudetalk2 "\"It will be pretty lonely 200 years you know...\""
    scene ch10chloe6
    with dissolve
    mc talk "\"Yeah?\""
    chloe nudetalk "\"Yep. So do you want to do something fun right now before that?\""
    $ quick_menu = False
    menu:
        "Have sex":
            $ quick_menu = True
            $ch10_chloe_sex = True
            mc talk2 "\"All right. Let's do this, Chloe.\""
            scene ch10chloe9
            with fasterfadein
            "Chloe lays down on the bench and removes her panties."
            chloe nudetalk "\"Ready?\""
            mc talk "\"Yeah.\""
            chloe nudetalk2 "\"Then what are you waiting for? Start fucking me.\""
            
            scene ch10chloeanim
            with dissolve
            "You do as your being told and start fucking her."
            $ quick_menu = False
            show screen ch10_chloe
            $ renpy.show("ch10_chloe")
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(12, hard=True)

            label ch10_chloe:
            hide screen ch10_chloe
            $ quick_menu = True
            chloe nudepleasure "\"Ahh...ahhh....mmmh...\""
            chloe nudepleasure "\"Go faster...\""
            $ quick_menu = False
            show screen ch10_chloex
            $ renpy.show("ch10_chloex")
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(12, hard=True)

            label ch10_chloex:
            hide screen ch10_chloex
            $ quick_menu = True
            mc pleasure2 "\"Ah... I am getting close...\""
            chloe nudepleasure "\"Mmm... yesss... Finish on my bellyyyy~\""
            
            scene ch10chloe7
            with flash
            mc pleasure "\"Ahhh---\""
            scene ch10chloe7
            with flash
            scene ch10chloe8
            with flash
            scene ch10chloe8
            with flash
            mc talk2 "\"That was great, Chloe.\""
            chloe nudetalk2 "\"I liked that too.\""
            chloe nudetalk "\"I have to go clean now.\""
            mc talk "\"Sure, I have to go now anyway.\""
            scene black
            with fadein
            "You leave and head back to the Command Center."
            jump ch10chloe2
        "Say you gotta go":
            $ quick_menu = True
            $ch10_chloe_sex = False
            mc talk "\"Sorry, Chloe. I have to go and prepare myself and you should too.\""
            scene black
            with fadein
            chloe nudetalk2 "\"Yeah, sure, whatever. Just go.\""
            "You leave and head back to the Command Center."
            jump ch10chloe2

jump ch10chloe2

label ch10chloe2:
scene ch10cc7
with fasterfadein
"Who else should I visit?"
$ quick_menu = False
menu:
    "Elyse & Zoey":
        jump ch10chloe3

label ch10chloe3:
    if mc_zoey_sex:
        jump ch10chloe4
    elif sex_with_elyse:
        jump ch10chloe4
    else:
        scene black
        with fadein
        $ quick_menu = True
        "You visit Zoey and Elyse in their room..."
        "You talk with them a bit and see how they are doing."
        "After seeing them prepared you go back to the Command Center..."
        jump ch10aftervisits

label ch10chloe4:
$ch10_elysezoey_sex = True
scene ch10elysezoey1
with fasterfadein
$ quick_menu = True
"You enter their room and see them sitting on Zoey's bed."
mc talk "\"Hi, girls.\""
z pleasedbb "\"Oh, hi [mc]!\""
e nudetalk "\"[mc]? Something wrong?\""
mc talk2 "\"Nah. I just came to check on my 2 favorite girls.\""
e nudehappy "\"Favorite girls, huh?\""
e nudehappy "\"But who is the favorite in the room? Me or her?\""
mc thinking "Oh no..."
scene ch10elysezoey2
with dissolve
z talkbb "\"Haha. We were actually arguing who's boobs were better.\""
z flirtingbb "\"It's obviously mine, but we need a third person to decide, so good timing!\""
scene ch10elysezoey3
with fasterfadein
"Before you can even say anything they remove their tops and reveal their breasts to you."
z nudetalk2 "\"It's obviously mine, right? Bigger and more firm.\""
e nudeskeptical "\"Bigger doesn't necessarily mean better.\""
z nudeflirting "\"Suuuure. That's what someone with small breasts would say.\""
e nudesad "\"*Grrr*\""
mc thinking "*Sigh* I need to do something before they start pulling each other's hair."
scene ch10elysezoey4
with dissolve
mc talk3 "\"Both are great, okay?\""
mc talk2 "\"There is no need for competition when both of you are winners.\""
mc talk "\"Small breasts are cute and Zoey's breasts are nice and firm. There is nothing wrong with either of them.\""
scene ch10elysezoey3
with dissolve
z nudetalk "\"Come on. That's no answer. Give them a feel at least before you decide.\""
z nudepleased "\"Give Elyse's tits a squeeze. Come on.\""
"You feel trapped and do as you're being told..."
scene ch10elysezoey5
with fasterfadein
"*Squeeze*"
mc thinking "Even though they are small... they are quite nice. I love her tits."
mc talk2 "\"Okay. They are perfect.\""
z nudeflirting "\"Mine next!\""
scene ch10elysezoey6
with vpunch
"Zoey pushes Elyse out of the way and moves right into your palms."
"*Squeeze* *Squeeze*"
"..."
z nudeflirting "\"They are so good you can't stop squeezing them, right?\""
mc talk3 "\"Ahah... both are great...I don't know what else to say.\""
z nudepleased "\"Forget the competition... All of this touching probably made you horny. Let's take care of the problem.\""
scene ch10elysezoey
with fasterfadein
"She unbuckles your pants and reveals your cock."
"Elyse joins in and they both start licking you without even asking for permission."
$ quick_menu = False
show screen ch10_elysezoey
$ renpy.show("ch10_elysezoey")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label ch10_elysezoey:
hide screen ch10_elysezoey
$ quick_menu = True
mc pleasure "\"Crap...\""
mc pleasure2 "\"I am about to...\""
$ quick_menu = False
menu:
    "Cum":
        $ quick_menu = True
        scene ch10elysezoey7
        with flash
        scene ch10elysezoey7
        with flash
        scene ch10elysezoey7
        with flash
        "You cum and splatter both their faces with semen."
        mc pleasure "\"Ahh....\""
        e nudepleasure "\"Mmmhh *Slurp*, *Suck*, *Lick*...\""
        z nudepleasure "\"That was really nice, [mc]. But you should leave now and let us clean up and prepare.\""
        mc talk3 "\"Of course.\""
        scene black
        with fadein
        mc thinking "*Sigh*... these girls..."
        "You move back to the Command Center."
        jump ch10aftervisits








label ch10aftervisits:
scene black
with dissolve
"A little bit later..."
scene ch10cc7
with fasterfadein
mc thinking "Is there anyone else I want to visit? I guess I should check on Jane too and make sure everything is in order before going."
mc thinking "I wonder wha---"
scene ch10cc8
with vpunch
l atalk "\"Guess who!!\""
mc thinking "\"Hmm...\""
mc thinking "\"Santa?\""
scene ch10cc9
with vpunch
l atalk "\"Haha. Close enough.\""
mc talk3 "\"So, did you bring any gifts?\""
l atalk "\"Hmm... no, but I see  you have a gift rising up there for me instead.\""
scene ch10cc10
with dissolve
l atalk "\"Do you want me to unwrap it with my foot?\""
$ quick_menu = False
menu:
    "Accept":
        $ quick_menu = True
        $ch10_lexa_fj = True
        mc talk2 "\"You know I do.\""
        scene ch10lexaanim
        with dissolve
        l atalk "\"Hehehe.\""
        l atalk "\"Already hard. This won't take long.\""
        $ quick_menu = False
        show screen ch10_lexa
        $ renpy.show("ch10_lexa")
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(12, hard=True)

        label ch10_lexa:
        hide screen ch10_lexa
        $ quick_menu = True
        mc pleasure "\"Uh...\""
        l atalk "\"About to cum?\""
        
        scene ch10footjobcum1
        with flash
        l atalk "\"Do it. Splatter my feet with your hot jizz.\""
        mc pleasure2 "\"Ahhh...\""
        $ quick_menu = False
        menu:
            "Cum":
                $ quick_menu = True
                scene ch10footjobcum2
                with flash
                scene ch10footjobcum2
                with flash
                scene ch10footjobcum2
                with flash
                scene ch10footjobcum3
                with flash
                scene ch10footjobcum3
                with flash
                mc pleasure2 "\"Ahhh......\""
                l apleasure "\"Look at that. Made my feet all slimy with your cum.\""
                scene ch10cc11
                with fasterfadein
                l atalk "\"Hope you liked your Christams present, hehe.\""
                l atalk "\"It is that time of the year anyway, right? Or at least it was...\""
                mc talk2 "\"Yeah... Thanks, Lexa. Couldn't have asked for a better present.\""
                l atalk "\"Anything for my favorite Commander.\""
                mc talk3 "\"Tough competition.\""
                l atalk "\"I know, right? Anyway I will go and prepare now. See you for now."
                mc talk2 "\"Yeah, see you for now Lexa.\""
                scene ch10cc7
                with fasterfadein
                "Lexa leaves and you decide to make your way to Jane."
                jump ch10jane
    "Decline":
        $ quick_menu = True
        $ch10_lexa_fj = False
        scene ch10cc9
        with dissolve
        mc talk2 "\"I will pass on that, Lexa. Thanks for the offer though.\""
        l adoubt "\"Eh, your loss. I guess I will let you 'work' and go.\""
        scene ch10cc7
        with fasterfadein
        "Lexa leaves and you decide to make your way to Jane."
        jump ch10jane


label ch10jane:
scene ch10jane1
with fasterfadein
"You make your way to the Engineering Bay."
"You spot Jane reading a book on her bed."
$ quick_menu = False
menu:
    "Move closer":
        jump ch10jane2

label ch10jane2:
scene ch10jane2
with fasterfadein
$ quick_menu = True
mc talk2 "\"Hello there, miss. What book are you reading?\""
j dtalk2 "\"Haha, hey [mc]. It's not really a book. More like a manual.\""
j dtalk "\"I am just checking again to make sure everything is correct.\""
mc talk3 "\"That's very thoughtful of you, Jane. Thank you for all the hard work these past months.\""
j dtalk2 "\"Don't mention it. It actually helped me cope with everything that happened.\""
j dtalk "\"Keeping my mind busy and all.\""
mc talk2 "\"Yeah... I know what you mean.\""
scene ch10jane3
with dissolve
j dtalk "\"Anyway... want to do something together since we are about to go?\""
j dtalk2 "\"You know I can really give you good pleasure. You deserve it for keeping everything together like you did.\""
mc talk "\"Um...\""
scene ch10jane4
with dissolve
j dtalk "\"I am sure my tits will convince you.\""
j dtalk2 "\"What do you say?\""
$ quick_menu = False
menu:
    "Take her up on the offer":
        $ quick_menu = True
        $ch10_jane_bj = True
        mc talk3 "\"Already convinced.\""
        scene ch10jane5
        with dissolve
        j nudeyummy "\"Hehehehe. I know what I am talking about.\""
        j nudeyummy "\"Now sit back...\""
        j nudeyummy "\"Relax...\""
        j nudeyummy "\"And put your cock inbetween my tits.\""
        scene ch10janecum1
        with fasterfadein
        "You do as she says and place your cocks inbetween the heaven's gates."
        j nudetalk2 "\"Now just enjoy the ride!\""
        $ quick_menu = False
        show screen ch10_jane
        $ renpy.show("ch10_jane")
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(12, hard=True)

        label ch10_jane:
        hide screen ch10_jane
        $ quick_menu = True
        mc pleasure "\"Mmhhh...\""
        mc pleasure2 "\"Ahh...\""
        j nudeyummy "\"Getting close? You can finish whenever you feel like it.\""
        mc pleasure "\"Uhh.......\""
        $ quick_menu = False
        menu:
            "Cum":
                $ quick_menu = True
                scene ch10janecum1
                with flash
                mc pleasure2 "\"Ahhh!\""
                scene ch10janecum2
                with flash
                scene ch10janecum2
                with flash
                scene ch10janecum2
                with flash
                scene ch10janecum2
                with flash
                scene ch10janecum3
                with flash
                "You cum splattering her whole chest with semen."
                j nudeyummy "\"Look at the mess you made...\""
                scene ch10jane7
                with fasterfadein
                mc talk3 "\"Hahh...\""
                mc talk2 "\"That was great, Jane.\""
                scene ch10jane6
                with dissolve
                j nudetalk2 "\"I am glad you enjoyed it.\""
                j nudetalk "\"You should go now and let me finish up here and clean up before joining everyone else.\""
                scene ch10jane7
                with dissolve
                mc talk "\"Yeah. Of course.\""
                jump ch10cryo
                
                
    "Refuse":
        $ quick_menu = True
        $ch10_jane_bj = False
        scene ch10jane9
        with fasterfadein
        mc talk "\"Thanks for the offer, Jane, but I will have to refuse.\""
        mc talk2 "\"You should finish up here and go since we are gathering soon.\""
        scene ch10jane8
        with dissolve
        j dpouty "\"Yeah... I will join everyone else in a bit.\""
        jump ch10cryo


label ch10cryo:
scene black
with fadein
"A couple of hours later..."
"Everyone seem to have already entered their cryo pod as you arrive there yourself..."
scene ch10cryo3
with fasterfadein
mc thinking "Okay... this is it."
mc thinking "It seems everyone is already in."
$ quick_menu = False
menu:
    "Check up close":
        jump ch10cryo2

label ch10cryo2:
$ quick_menu = True
"You move and check through the pods until you stop at Zoey's."
scene ch10cryo4
with fasterfadein
mc thinking "Sleeping like a peaceful angel."
mc thinking "She is a big reason why we even have this as an option right now."
mc thinking "Quite a few important years of her childhood went to this experiment..."
scene ch10cryo0
with flash
$ renpy.pause(2, hard=True)
scene ch10cryo4
with flash
mc shocked "Uhhhh.... Déjà vu..."
mc thinking "This all seems so familiar... as if I've done all of this before and going to do it again and again."
mc thinking "Weird... I shouldn't think more about it."
scene ch10cryo1
with dissolve
"You see Ruby standing by the door."
$ quick_menu = False
menu:
    "Go talk with her":
        jump ch10cryo3
label ch10cryo3:
$ quick_menu = True
"You move closer."
scene ch10cryo2
with fasterfadein

r ttalk "\"Commander.\""
mc talk3 "\"I see everyone is already asleep.\""
r ttalk2 "\"That's correct. You are the only one left.\""
mc talk2 "\"Before that... when we do get to this new planet...\""
mc talk3 "\"Don't wake anyone up except for me. We are not sure if this is our salvation or not.\""
mc talk "\"And if there is any issue during the 200 year trip you wake me up again.\""
r ttalk "\"I understand, Commander.\""
mc talk2 "\"I hope you're not too lonely...\""
r ttalk2 "\"I am an android, [mc]. I don't really have feelings like loneliness.\""
mc talk "\"Right... well godspeed to us all and may we wake up to a better world. I am going now.\""
r ttalk "\"Have a pleasant dream, [mc].\""
scene ch10cryo3
with dissolve
mc thinking "Even though she is not really human you can't help but feel really bad for her..."
mc thinking "200 years. And that's if we are lucky not to get boarded or God knows what else..."

$ quick_menu = False

menu:
    "Go to your pod":
        jump ch10cryo5
        
label ch10cryo5:
scene ch10cryo5
with fasterfadein
$ quick_menu = True
mc thinking "So this is my 'bed' I suppose."
mc thinking "I guess I should start undressing."
$ quick_menu = False
menu:
    "Undress":
        jump ch10cryo6
label ch10cryo6:
scene ch10cryo6
with fasterfadein
$ quick_menu = True
mc nudethinking "Okay... this is it."
$ quick_menu = False
menu:
    "Enter the cryogenic pod":
        jump ch10cryo7
label ch10cryo7:
scene ch10cryo7
with fasterfadein
$ quick_menu = True
mc nudetalk "\"Activate pod #1337\""
"..."
"\"Activation successful!\""
scene ch10cryo8
with dissolve
"You put the cover over yourself."
"..."
scene ch10cryo9
with vpunch
"The pod closes down in an instant."
mc nudetalk "This is it...."
mc nudetalk "Uh..."
mc nudetalk "Already..."
scene ch10cryo10
with dissolve
mc nudesleep "Feeling..."
scene ch10cryo11
with dissolve
mc nudesleep "\"Sleepy...\""
scene ch10cryo12
with dissolve
mc nudesleep "\"Good...\""
mc nudesleep "\"Night...\""
scene black
with fadein
#"..."
jump startch11