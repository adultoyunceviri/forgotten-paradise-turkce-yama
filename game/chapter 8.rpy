label decontamination:
scene decontamination1
with dissolve

"You bring Jane back to the ship safely..."

"..."

"Decontamination complete!"

scene decontamination3
with dissolve

j sslayer2 "\"I... I can't believe you came for me.\""
j sslayer2 "\"...I owe you my life, [mc].\""

"Jane points out she needs a moment to rest."

scene decontaminationjanetalkingtomc
with dissolve

j sslayer5 "\"I didn't know you had military experience. Lucky me I guess, haha...\"" 

mc sslayer2 "\"Even if I didn't I still would've tried to help instead of hoping for the best... although that monster was something else...\""

j sslayer3 "\"I never thought such things existed... it must've been drawn from what happened to the Earth..... which I still can't believe is real.\""

mc sslayer2 "\"I know what you mean... I think it got struck by something on the other side and our sensors couldn't detect anything. Was it an attack? And if so I don't think we are safe here either... as some of the last survivors.\""

j sslayer4 "\"You're right... I don't think we are safe here... and after that monster it pretty much confirms that. But where can we go? We will have to set route to somewhere...\""

mc sslayerthinking "She seems to be really grateful to me, so I might be able to get her card with her permission...I should ask her."

$ quick_menu = False

menu:
    "Ask for her security keycard":
        $ quick_menu = True
        scene decontaminationmctalkingtojane
        with dissolve
        mc sslayer2 "\"Listen...Jane, uhm... You remember that person that infiltrated the ship a few weeks ago?\""
        j sslayer5 "\"Yeah? What about her?\""
        mc sslayer2 "\"Well, I believe she is innocent and the crew members of the ship were doing some kind of experiment on all the passengers that were picked or at the very least my whole family.\""
        j sslayer4 "\"Wait... what?!?\""
        j sslayer3 "\"I am a crew member as well and I don't know anything about this.\""
        mc sslayer2 "\"I believe you weren't involved, but other people like Jack, Amir and Melisa are.\""
        j sslayer5 "\"What kind of experiment are we talking about?\""
        mc sslayer2 "\"Memory loss. The only reason I know about all of this is because I was warned before hand and I had the chance to reverse the effect of what they tried to give me before I arrived.\""
        mc sslayer2 "\"But nevermind all of that. I need to ask you a big favor here and your trust.\""
        j sslayer5 "\"I believe you. You also saved me... and I am not surprised that the fat bastard Amir is involved in all of this.\""
        j sslayer5 "\"What do you need from me?\'"
        mc sslayer2 "\"Just your security keycard and... some clothes.\""
        scene decontaminationjanesc1
        j sslayer5 "\"Only that? Here, take it. It will grant you access to my room as well in the engineering part of the ship down below.\""
        j sslayer5 "\"I just need a bit more to rest here... I will join up with you later and don't worry, I am on your side.\""
        scene decontaminationmctalkingtojane
        with dissolve
        mc sslayer2 "\"Thank you, Jane! It means a lot to know you trust me.\""
        j sslayer5 "\"Go and save her too, hero.\""
        scene black
        "You nod in agreement and rush towards Jane's room."
        jump janesroompt2

label janesroompt2:
"On the way you pick up your clothes as well."
"You make your way down and feel relief you find it rather quickly."
scene janeroommcenters
with fadein
if jane_dinner:
    mc sslayerthinking "I expected a mess and I wasn't disappointed... might take me a moment to find some matching clothes in this mess though..."
else:
    mc sslayerthinking "Wow... what a mess. It might take me a moment to find the proper clothes."

scene janeroommcsearchbed
with dissolve
mc sslayer2 "..."
mc sslayer2 "This should do. I got a few clothes. Have to go to her cell now!"
             
scene black
with dissolve
"You leave and make your way where you last saw Jack go."
scene cellmcunlocksdoor
with fadein
mc sslayerthinking "Come on... work! I hope her card has clearance to open this too..."
"You hear a scanning sound and afterwards the door start to open..."
scene cellmcunlocksdoor2
with dissolve
mc sslayerthinking "Easy peasy. Let's go."
scene cellmcenters
with fadein
"You enter the room and look for a moment around the room..."
scene celllexalaying
with fadein
"You spot her on the ground laying with chains on... completely naked."

$ quick_menu = False

menu:
    "Approach her":
        $ quick_menu = True
        "You approach her and try not to scare her as you do."
        jump lexacellapproach
        
label lexacellapproach:
mc sslayer2 "\"Hey... I am friendly. I won't hurt you. What's your name?"
"You see her opening her eyes slowly."
scene celllexanoticesyou
with dissolve
l talk "\"You...came for me... My name is Lexa...\""
mc sslayer2 "\"Lexa, I am [mc], I will get you out of here.\""
l talk "\"H...How? The key is on him.\""
scene cellmcunshackleslexa
with dissolve
"You crouch down and check the chains up close."
mc sslayerthinking "She is right... the key might be with Jack, but I can more than likely melt this down with my laser pistol."
scene cellmcshootschainscam
with dissolve
mc sslayer2 "\"Listen... this might sound dirty and wrong, but I need you to spread your legs for me.\""
l talk "\"It does sound dirty, but I wouldn't say wrong, mmm.\""
scene celllexaspreadsherlegs
with dissolve
"She looks up at you and does what you said without any hesitation..."
"You can see her whole body including her pussy. Just looking at her erotic body full of tatooes makes you hard, but you easily hide that with your body armor on."
scene cellmcshootschains
with dissolve
"You aim at the chains that bind her feet and arms."
mc sslayer2 "\"Just stay like that and don't move an inch. I am a good shot and I won't miss as long as you don't move.\""
"She nods."
$ quick_menu = False
menu:
    "Shoot":
        $ quick_menu = True
        jump aftershootingchains
        
label aftershootingchains:
scene cellmcshootschains2
with flash

"You shoot and the laser melts down the chains completely and setting her free."
$ quick_menu = False
scene celllexaunshackledportrait with fade:
    subpixel True
    yalign 1.0
    pause 2.0
    linear 7.0 yalign 0.0
pause
$ quick_menu = True
"Lexa feels her wrists for the first time in weeks being completely freed from her bonds."
l talk "\"Ah... it feels so good to be free again."
mc sslayer2 "\"You're welcome. I brought you some clothes for you to wear."
"You point at the table and watch as Lexa moves closer, but to your surprise instead of getting dressed she sits in a provocative pose."
$ quick_menu = False
scene celllexaonchairportrait with fade:
    subpixel True
    yalign 1.0
    pause 2.0
    linear 7.0 yalign 0.2
pause
$ quick_menu = True
l talk "\"I need to take a shower before I dress because I stink. And before that... I have a favor to ask of you...\""
"You can only imagine what she has in mind."
mc sslayer2 "\"W-What is it?\""
l talk "\"I was injected with quite a few different strong drugs which made me insanely horny and frustrated. I need you to fuck me. Right now! Please.\""
scene cellmcshockedatlexa
with dissolve
mc sslayer2 "\"A-Are you serious? Can't you withstand it?\""
l talk "\"I wouldn't ask you if I could.\""
mc sslayerthinking "\"What do I do? Do I actually fuck her when it's clearly the drugs speaking?\""

$ quick_menu = False

menu:
    "Fuck her":
        $ quick_menu = True
        $ fuck_lexa_cell = True
        scene cellmcremovesarmor1
        with fadein
        "You say fuck it and start to remove your suit."
        mc sslayer2 "\"I will help you out in that case.\""
        scene cellmcremovesarmor2
        with dissolve
        l talk "\"My hero {image=gui/heartdialogue.png}\""
        scene cellmcremovesarmor3
        with dissolve
        l talk "\"Choose whatever hole you want and fuck me as hard as you want and don't forget to cum inside me.\""
        mc nudetalk "\"Rough and inside, huh? Got it.\""
        scene cellmcabouttofucklexa
        with dissolve
        "You move closer and now you need to make another choice..."
        mc nudethinking "Fuck her ass or her pussy?"
        jump fuckinglexacell
    "Refuse":
        $ quick_menu = True
        $ fuck_lexa_cell = False
        scene celllexasexrefuse
        with fadein
        mc sslayer2 "\"I'm sorry, but I can't do that. You will get over it, you probably just need a shower and the feeling will fade away\""
        l angry "\"It's fine... I don't expect you to fuck a defiled slut like myself anyway.\""
        jump jackenterscellrefusedsex
label jackenterscellrefusedsex:
scene celllexasurprised
with dissolve
"You hear the door behind Lexa unlock."
l doubt "\"Quick, you must hide! He is coming in!\""
scene celllexasurprised2
with dissolve
"Unfortunately you didn't have enough time to even react to what you were being told as you see Jack march in."
scene celljackentering
with dissolve
jack angry "\"What the hell do you think you're doing, [mc]?! Freeing my prisoner?!\""
mc sslayer2 "\"Listen, Jac--\""
jack angry "\"You think I wouldn't find out? How did you even get access to her cell?!\""
mc sslayer2 "\"I know what you and your team are doing here and even though it's too late to expose you to anyone down on Earth everyone else here should be aware.\""
scene celljackchargingclothedmc
with dissolve
jack angry "\"You don't know anything!\""
"You get charged and unable to dodge you take on the hit."
scene celljackchargingclothedmc2
with dissolve
mc sslayershocked "\"Ahhh!!\""
scene celljackchargingclothedmc3
with dissolve
"Jack slams you against the wall and takes away your breath immediately."
mc sslayershocked "\"Aghhh *Cough*\""
scene celllexapickingupgun0
with dissolve
jack angry "\"Even if you're a passenger you are not allowed to do whatever you want. Since you're so eager you can join her as her cellmate.\""
scene celllexapickingupgun1
mc sslayer2 "\"*Cough*\""
mc sslayer2 "\"Y-You won't get away with this!\""
scene celllexapickingupgun2
with dissolve
l angry "\"Hey, meat head!\""
l angry "\"Let him go right now and put on the handcuffs you brought with you or I will blow your head off.\""
scene celljackhandcuffedclothed
with dissolve
"Jack releases his grip on your neck."
mc sslayershocked "\"*Cough* *Cough*\""
l angry "\"Now you will have a taste of your own medicine and rot in this cell.\""
jack angry2 "\"You... don't understand.\""
l angry "\"Oh we understand perfectly. You better not speak again and make me change my mind about not blowing your brain right now.\""
l angry "\"Let's go, [mc].\""
scene black
with dissolve
jump lexashowers
        
label fuckinglexacell:
$ quick_menu = False
menu:
    "Fuck her pussy":
        $ quick_menu = True
        $ fuck_lexa_ass_cell = False
        $ fuck_lexa_pussy_cell = True
        mc nudetalk "Her dripping pussy is too inviting to pass."
        scene cellmcfuckslexapussy
        with dissolve
        "You placed your cock on her inviting cunt and start pounding away."
        "She wanted a rough fuck and that's exactly what you plan to give her."
        $ quick_menu = False
        show screen mc_fucks_lexa_ass_cell
        $ renpy.show("mc_fucks_lexa_ass_cell")
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(12, hard=True)

        label mc_fucks_lexa_ass_cell:
        hide screen mc_fucks_lexa_ass_cell
        $ quick_menu = True
        l pleasure "\"Yes, yesss, fuck my pussy harder!\""
        mc nudepleasure "I need to decide where to cum... she did say inside, but should I?"
        
        $ quick_menu = False
        
        menu:
            "Cum inside her":
                $ quick_menu = True
                mc nudepleasure "Inside feels way too good to pass on."
                mc nudepleasure "\"Cumming~!\""
                scene cellmcfuckslexacuminside
                with flash
                scene cellmcfuckslexacuminside
                with flash
                scene cellmcfuckslexacuminside
                with flash
                l pleasure "\"Yess, cum inside me as much as you can!!\""
                "You unleash your build up sperm inside her and take out your cock out."
                scene cellmccumsinsidepussy2
                "You watch her pussy drip with your cum."
                l pleasure "\"Mmm... it feels so god damn good.\""
                "You hear a faint sound of your cum gashing out of her pussy as it starts dripping down her leg."
                l talk "\"So hot.\""
                l talk "\"I really needed that fuck. But now I really need that shower as well.\""
                jump aftercellsexlexa
                
            "Cum on her back":
                $ quick_menu = True
                mc nudetalk3 "She said I can cum inside, but outside is just as good and less risky... for obvious reasons."
                mc nudepleasure "Getting close..."
                mc nudepleasure "\"Cumming~!\""
                scene cellmcfuckslexacumsonass1
                with flash
                scene cellmcfuckslexacumsonass1
                with flash
                scene cellmcfuckslexacumsonass1
                with flash
                mc nudepleasure2 "\"Hahh...\""
                scene cellmcfuckslexacumonassoutside2
                with dissolve
                l pleasure "\"You should've cum inside me, but this still feels nice. Made my dirty body even more dirty~\""
                jump aftercellsexlexa
    "Fuck her ass":
        $ quick_menu = True
        $ fuck_lexa_ass_cell = True
        $ fuck_lexa_pussy_cell = False
        mc nudetalk "Her ass is too tempting to pass on."
        scene cellmcabouttofucklexaass
        with dissolve
        "You press your cock on the entrance of her ass which already seems lubed up for some reason."
        "She was horny or was that just some sweat coming from her? Doesn't matter, you pressed on."
        
        $ quick_menu = False
        show screen mc_fucks_lexa_pussy_cell
        $ renpy.show("mc_fucks_lexa_pussy_cell")
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(12, hard=True)

        label mc_fucks_lexa_pussy_cell:
        hide screen mc_fucks_lexa_pussy_cell
        
        $ quick_menu = True
        mc nudepleasure "Fuck... I am getting close... Should I really cum inside her?"
        $ quick_menu = False
        menu:
            "Cum inside her ass":
                $ quick_menu = True
                $ lexa_cum_inside_ass_cell = True
                $ lexa_cum_inside_pussy_cell = False
                $ lexa_cum_outside_cell = False
                mc nudepleasure "She did say I should cum inside her..."
                mc nudepleasure "\"I am getting close...\""
                scene cellmcfuckslexacuminside
                l pleasure "\"Yesss~ splatter my insides with your white stuff.\""
                l pleasure "\"Aaahh mmm~\""
                mc nudepleasure2 "\"Cumming~~\""
                scene cellmccumsinsideass1
                with flash
                scene cellmccumsinsideass1
                with flash
                scene cellmccumsinsideass1
                with flash
                l pleasure "\"Mmmmmm. I feel your hot spunk inside me.\""
                scene cellmccumsinsideass2
                with dissolve
                "You hear a faint sound of your cum gashing out of her anus and starts dripping down her."
                l talk "\"So hot.\""
                l talk "\"I really needed that ass fucking. But now I really need that shower as well.\""
                jump aftercellsexlexa
                
            "Cum outside":
                $ quick_menu = True
                $ lexa_cum_inside_ass_cell = False
                $ lexa_cum_inside_pussy_cell = False
                $ lexa_cum_outside_cell = True
                mc nudepleasure "I am getting close... and even though she said it was okay to do it inside, I am the one in control."
                "You take out your cock from her ass and unleash your cum on her back."
                scene cellmcfuckslexacumsonass1
                with flash
                scene cellmcfuckslexacumsonass1
                with flash
                scene cellmcfuckslexacumsonass1
                with flash
                mc nudepleasure2 "\"Hahh...\""
                scene cellmcfuckslexacumonassoutside2
                with dissolve
                l pleasure "\"You should've cum inside me, but this still feels nice. Made my dirty body even more dirty~\""
                jump aftercellsexlexa

label aftercellsexlexa:
scene celllexaaftersex
with fadein
"Lexa sits back down on the chair."
l talk "\"The drug's effect will go away soon... but you have no idea how badly I needed this.\""
l talk "\"That meat head kept defiling me and injecting me with all kinds of drugs just to get me to talk.\""
mc nudetalk "\"He will get what is coming to him.\""
scene celllexasurprised
with dissolve
"As you say that you hear the door unlock."
l doubt "\"Quick, you must hide! He is coming in!\""
scene celllexasurprised2
with dissolve
"Unfortunately you didn't have enough time to even react to what you were being told as you see Jack march in."
scene celljackentering
with dissolve
jack angry "\"What the hell do you think you're doing, [mc]?! Fucking and freeing my prisoner?!\""
mc nudetalk2 "\"Listen, Jac--\""
jack angry "\"You think I wouldn't find out? How did you even get access to her cell?!\""
mc nudetalk3 "\"I know what you and your team are doing here and even though it's too late to expose you to anyone down on Earth everyone else here should be aware.\""
scene celljackchargingnudemc
with dissolve
jack angry "\"You don't know anything!\""
"You get charged and unable to dodge you take on the hit."
scene celljackchargingnudemc2
with dissolve
mc nudeshocked "\"Ahhh!!\""
scene celljackchargingnudemc3
with dissolve
"Jack slams you against the wall and takes away your breath immediately."
mc nudeshocked "\"Aghhh *Cough*\""
scene celllexapickingupgun0nude
with dissolve
jack angry "\"Even if you're a passenger you are not allowed to do whatever you want. Since you're so eager to be with her you can join her as her cellmate.\""
scene celllexapickingupgun1
mc nudetalk "\"*Cough*\""
mc nudetalk3 "\"Y-You won't get away with this!\""
scene celllexapickingupgun2nude
with dissolve
l angry "\"Hey, meat head!\""
l angry "\"Let him go right now and put on the handcuffs you brought with you or I will blow your head off.\""
scene celljackhandcuffednude
with dissolve
"Jack releases his grip on your neck."
mc nudeshocked "\"*Cough* *Cough*\""
l angry "\"Now you will have a taste of your own medicine and rot in this cell.\""
jack angry2 "\"You... don't understand.\""
l angry "\"Oh we understand perfectly. You better not speak again and make me change my mind about not blowing your brain right now.\""
l angry "\"Let's go, [mc].\""
jump lexashowers

label lexashowers:
scene black
with dissolve
"You both leave Jack in the cell and lock him inside as you make your way to the showers."

scene showersmclexaenter
with fadein
l talk "\"So... you risked your life to save me. I will not forget that.\""
l talk "\"Are you sure you don't want a shower yourself?\""
scene showersmclexaenter2
with dissolve
mc sslayer2 "\"I think I am okay.\""
scene showerslexainvitingmc
with dissolve
if fuck_lexa_cell:
    l talk "\"That fight that went back in the cell made me really horny again. Do you think you can get your friend down there up again for me?\""
    l talk "\"What do you say? He can't interrupt us again.\""
    jump sexinglexashower
else:
    l talk "\"I am still really frustrated and even though you refused earlier I am hoping you can reconsider since that fight made me even more wet.\""
    l talk "\"What do you say? He can't interrupt us now.\""
    jump sexinglexashower

label sexinglexashower:
scene showerslexainvitingmc
with dissolve
mc sslayer2 "What should I do?"

$ quick_menu = False

menu:
    "Fuck her":
        $ quick_menu = True
        $ showers_lexa_sex = True
        if fuck_lexa_cell:
            mc sslayer2 "\"Round 2? I might be able to do it and seeing you nude is helping a lot.\""
            jump showerssexlexa
        else:
            mc sslayer2 "\"You know what? I will do it. I don't have to worry about Jack interrupting us anymore, so we can enjoy ourselves now.\""
            jump showerssexlexa
        
    "Decline":
        $ quick_menu = True
        $ showers_lexa_sex = False
        if fuck_lexa_cell:
            mc sslayer2 "\"Sorry, Lexa, but I have to pass this time.\""
            l talk "\"It's okay... don't worry about it. I will find a way to relief myself inside the shower.\""
            mc sslayer2 "\"I will be outside if you need me.\""
            l talk "\"Alright, thanks.\""
            jump declinedshowersexlexa
        else:
            mc sslayer2 "\"Sorry, Lexa, but I have to decline again.\""
            l talk "\"It's okay... don't worry about it. I will find a way to relief myself inside the shower. I shouldn't have asked you again.\""
            mc sslayer2 "\"I will be outside if you need me.\""
            l talk "\"Alright, thanks.\""
            jump declinedshowersexlexa
            
label declinedshowersexlexa:
scene black
with dissolve
"You take the time to remove your armor and dress back normally as you don't think you will need the armor again after dealing with Jack and locking him in."
scene showersmcwaiting
with fadein
"You stand outside as you wait for her..."
"You hear soft moans coming from her shower cabin."
"After a few minutes they become more intense and you guess she just came."
"After some minutes you hear the water stop and you pass her the clothes."
l talk "\"Ah, these are a little bit tight, but they fit at least.\""
"She opens the curtains and reveals her outfit."
l atalk "\"Ta-daa~\""
$ quick_menu = False
scene showerslexaclothedportrait with fade:
    subpixel True
    yalign 1.0
    pause 2.0
    linear 7.0 yalign 0.0
pause
$ quick_menu = True
l atalk "\"Well, what do you think?\""
mc talk2 "\"Wow, gorgeous.\""
l atalk "\"Haha. Flatterer.\""
l atalk "\"It's really tight though... especially on my butt.\""
scene showerslexashowingass
with dissolve
"Lexa turns around and shows her gorgeous ass."
mc talk3 "\"I think it looks great on you."
l atalk "\"Of course you do. Because you like my ass.\""
"At this moment you hear the communication device given to you by Ruby turn on as she tells you to meet with her."
scene showerslexaclothedtalks
with dissolve
l atalk "\"So... what now?\""
mc talk2 "\"I was called in to a meeting. We should go there.\""
l atalk "\"I doubt your people will be very fond of me...\""
mc talk3 "\"We have bigger issues right now... the Earth is absolutely destroyed... and having an innocent prisoner freed is the least of their trouble.\""
l adoubt "\"Earth destroyed?? What do you mean?\""
mc talk2 "\"Come on, I will fill you in on the way...\""
scene black
with dissolve
"You both leave the showers and you explain everything that has happened so far to Lexa."
"You eventually arrive at the room Ruby called you to come in."
jump meetingforedis

label showerssexlexa:
l talk "\"Come over here then...\""
"You remove your armor and move in closer."
scene showersmcabouttofucklexa1
with dissolve
l talk "\"You like me, don't you?\""
l talk "\"Talk dirty to me, degrade me. Talk how much you like to fuck me.\""
scene showersmcabouttofucklexa2
with dissolve
"She guides my hand towards her pussy."
mc nudetalk "\"You're so wet, you slut.\""
l pleasure "\"Yess... finger my cunt.\""
mc nudetalk2 "\"You dirty slut, this is what you wanted since we've walked in here didn't you?\""
l pleasure "\"Mmm, yesss~\""
mc nudetalk2 "\"So much juice coming from your dripping pussy...\""
scene showerslexasuckonfinger
with dissolve
mc nudetalk "\"Here, taste your own slutty juice.\""
l pleasure "\"Mmmmmm...\""
mc nudetalk2 "\"Do you like it, slut?\""
scene showerslexasuckonfinger2
with dissolve
l pleasure "\"Yes. I love the taste of it.\""
l pleasure "\"Kiss me. Let me show you how it tastes~\""
scene showerslexakissmc2
with dissolve
"You both share a long and sloppy kiss exchanging saliva and more."
"The kiss seem to continue forever until you break free."
scene showerslexakissmc
with dissolve
mc nudethinking "She tastes salty and... strange... I guess she really needs to freshen up... who knows how that bastard used her."
l pleasure "\"I hope you liked this exchange. Now it's time for you to fuck me hard.\""
"She didn't waste any time and opened herself for you to fuck her pussy and you happily obliged."

scene showersmcfuckslexa
with dissolve
"You place your cock on her wet pussy and start thrusting."

$ quick_menu = False
show screen showers_mc_fucks_lexa
$ renpy.show("showers_mc_fucks_lexa")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label showers_mc_fucks_lexa:
hide screen showers_mc_fucks_lexa
$ quick_menu = True

l pleasure "\"Yeeeeessss~~ fucking fuck me!\""
mc nudepleasure2 "\"I am getting close...\""
l pleasure "\"Ahh, you can cum inside or I can drink your cum like the dirty little slut I am~\""
mc nudepleasure "What should I do?"

$ quick_menu = False

menu:
    "Cum inside her pussy":
        $ quick_menu = True
        $ lexa_showers_cum_inside_pussy = True
        $ lexa_showers_cum_on_face = False
        mc nudepleasure "\"I'm cumming~~\""
        l pleasure "\"Yess~ fill my slutty pussy with your cum.\""
        scene showersmccuminsidelexa
        with flash
        scene showersmccuminsidelexa
        with flash
        scene showersmccuminsidelexa
        with flash
        l pleasure "\"Ahh so much fresh cum inside my pussy. It's overflowing.\""
        scene showersmccuminsidelexa2
        with flash
        "You pop your cock out of her pussy and a stream of cum escaping her pussy follows."
        l pleasure "\"I can feel your semen inside me...\""
        l pleasure "\"It feels... so hot......\""
        l talk "\"I should really get in the shower now before I mess up the floor with cum everywhere.\""
        jump aftersexshowerslexa
    "Cum in her mouth":
        $ quick_menu = True
        $ lexa_showers_cum_inside_pussy = False
        $ lexa_showers_cum_on_face = True
        mc nudetalk "\"Your mouth, please.\""
        scene showersfacial1
        with dissolve
        "Lexa kneels down and starts stroking your cock."
        mc nudepleasure "\"Ahh, just like that...\""
        l pleasure "\"Cum for me, baby, splatter my mouth with your cum~\""
        mc nudepleasure2 "\"Cumming~~\""
        scene showersfacial2
        with flash
        scene showersfacial2
        with flash
        scene showersfacial2
        with flash
        "You gush out your cum right to her waiting mouth."
        scene showersfacial3
        with flash
        l pleasure "\"Tht--asty~~\""
        "Lexa tries to speak but her words are barely understandable with all of the cum inside her mouth."
        mc nudetalk2 "\"Swallow it, my little slut.\""
        scene showersfacial4
        with dissolve
        l pleasure "\"*Gulp* *Gulp* *Gulp*\""
        "You watch her gulp down all your semen with ease."
        scene showersfacial5
        with dissolve
        mc nudetalk3 "\"Show me.\""
        mc nudetalk2 "\"Open your mouth. Say aaah.\""
        scene showersfacial6
        with dissolve
        l pleasure "\"Aaaaaaah~~\""
        "Lexa opens her mouth and you see she swallowed your whole load.\""
        mc nudetalk "\"Good. Now you can go and take the shower.\""
        jump aftersexshowerslexa

label aftersexshowerslexa:
scene black
with dissolve
"You take the time to ditch the armor and dress up normally."
"Knowing that Jack is locked up gives you enough reason to do that."
scene showersmcwaiting
with fadein
"After some minutes you hear the water stop and you pass her the clothes."
l talk "\"Ah, these are a little bit tight, but they fit at least.\""
"She opens the curtains and reveals her outfit."
$ quick_menu = False
scene showerslexaclothedportrait with fade:
    subpixel True
    yalign 1.0
    pause 2.0
    linear 7.0 yalign 0.0
pause

$ quick_menu = True

l atalk "\"Well, what do you think?\""
mc talk2 "\"Wow, gorgeous.\""
l atalk "\"Haha. Flatterer.\""
l atalk "\"It's really tight though... especially on my butt.\""
scene showerslexashowingass
with dissolve
"Lexa turns around and shows her gorgeous ass."
mc talk3 "\"I think it looks great on you."
l atalk "\"Of course you do. Because you like my ass.\""
"At this moment you hear the communication device given to you by Ruby turn on as she tells you to meet with her."
scene showerslexaclothedtalks
with dissolve
l atalk "\"So... what now?\""
mc talk2 "\"I was called in to a meeting. We should go there.\""
l atalk "\"I doubt your people will be very fond of me...\""
mc talk3 "\"We have bigger issues right now... the Earth is absolutely destroyed... and having an innocent prisoner freed is the least of their trouble.\""
l adoubt "\"Earth destroyed?? What do you mean?\""
mc talk2 "\"Come on, I will fill you in on the way...\""
scene black
with dissolve
"You both leave the showers and you explain everything that has happened so far to Lexa."
"You eventually arrive at the room Ruby called you to come in."
jump meetingforedis

label meetingforedis:
scene meetingmcandlexaenter
with fadein
if saved_dahlia_from_edis:
    "You both enter and you see everyone arguing.\""
    scene meetingentering1
    with dissolve
    d talk "\"Oh here is [mc]. He was the one who saved me so he can confirm what this bastard was doing to me.\""
    m talk "\"[mc]? Is that true and why is SHE with you??\""
    scene meetingmclexatalk
    with dissolve
    mc talk2 "\"That's true. Edis was raping her and I stopped him.\""
    mc talk "\"And this is Lexa. She was locked in and tortured by the crew of this very ship who made experiments on the passengers.\""
    m talk2 "\"Listen, [mc]... there is an explanation for all of that.\""
    mc talk "\"I will be really glad to hear it. But now with our planet gone you people won't get the justice for what you've done here. Although I doubt you would've anyway.\""
    scene meetingdahliarubylookatyou
    with dissolve
    d talk2 "\"I don't know what you guys are talking about, but we need to decide what to do with this scumshit over here. I should just off him so we can focus on the bigger problems we have.\""
    m talk "\"Let's wait for Jack to come and we will all decide together.\""
    scene meetingmclexatalk
    with dissolve
    mc talk2 "\"Jack isn't coming. He is serving his sentence in the cell where Lexa was locked and tortured.\""
    m angry "\"Well.... that explains why he is not here yet.\""
    scene meetingamirtalking
    with dissolve
    amir talk "\"I say we just off this poor bastard. The last we need is a rapist on our ship for however long it takes us to land on some new place.\""
    if jane_dinner:
        mc talk2 "Sure, but you are no different you fat fuck. Treating Jane like a fuck toy and using her against her will is no different than what Edis has done."
        jump meetingforedisamir
    else:
        jump meetingforedisamir
else:
    "You both enter and you see everyone arguing.\""
    scene meetingentering1
    with dissolve
    d talk "\"Why should I let this bastard live?! He is lucky I didn't have my sword with me when I finally struggled free from the rope he tied me with.\""
    m talk "\"We will wait for everyone to come here and then we will decide, Dahlia.\""
    m talk2 "\"[mc]? Why is SHE with you??\""
    scene meetingmclexatalk
    with dissolve
    mc talk "\"This is Lexa. She was locked in and tortured by the crew of this very ship who made experiments on the passengers.\""
    m talk2 "\"Listen, [mc]... there is an explanation for all of that.\""
    mc talk "\"I will be really glad to hear it. But now with our planet gone you people won't get the justice for what you've done here. Although I doubt you would've anyway.\""
    scene meetingdahliarubylookatyou
    with dissolve
    d talk2 "\"I don't know what you guys are talking about, but we need to decide what to do with this scumshit over here. I should just off him so we can focus on the bigger problems we have.\""
    m talk "\"Let's wait for Jack to come and we will all decide together.\""
    scene meetingmclexatalk
    with dissolve
    mc talk2 "\"Jack isn't coming. He is serving his sentence in the cell where Lexa was locked and tortured.\""
    m angry "\"Well.... that explains why he is not here yet.\""
    scene meetingamirtalking
    with dissolve
    amir talk "\"I say we just off this poor bastard. The last we need is a rapist on our ship for however long it takes us to land on some new place.\""
    if jane_dinner:
        mc talk2 "Sure, but you are no different you fat fuck. Treating Jane like a fuck toy and using her against her will is no different than what Edis has done."
        jump meetingforedisamir
    else:
        jump meetingforedisamir

label meetingforedisamir:
scene meetingalarmgoingoff
with fadein
"As everyone was arguing for various of things an alarm started beeping right above everyone."
amir angry "\"What the fuck is this now?! Are we hit???\""
m angry "\"Ruby?\""
r ttalk2 "\"Give me a moment.\""
scene meetingrubyconnecting2
with dissolve
"Ruby closes her eyes and seem to connect to the ship and the alarm stops."
"..."
scene meetingrubyconnecting
with dissolve
r ttalk "\"We are being boarded.\""
d angry2 "\"What?!\""
amir angry "\"Fucking great.\""
m angry "\"This is the last thing we needed.\""
mc talk2 "\"Can't we defend somehow?\""
scene meetingrubyconnecting3
with dissolve
r ttalk2 "\"The ship is still in no condition to repell invaders. I advise you not to provoke or attack the aliens when they arrive.\""
l atalk "\"What do they want?\""
r ttalk "\"They said they have a few conditions we must uphold and they will leave without harming anyone.\""
amir angry "\"This is crazy. We should hide.\""
r ttalk "\"There is nowhere to hide. They are already boarding.\""
l atalk "\"You can understand their language?\""
r ttalk "\"Yes. I have a build in decryptor for languages. There is a device that is a work in progress for humans as well, but right now I will be the bridge for the communication between them.\""

with fasterfadein
scene meanwhile
$ quick_menu = False
pause 2.5
with fasterfadeout
$ quick_menu = True

scene airlockalienshipdock
with fadein
"..."
scene airlockaliensentering
with fadein
"..."

scene black
with dissolve
"Back at [mc] and company..."

scene meetingbigalienstopdoorfromclosing
with fadein
"The door opens and the first alien comes in. About the average human size, but doesn't look anything alike..."
"Then you notice an arm holding the door and just by the size of it you can imagine the monster that will enter next."
scene meetingbigaliencomesin
with dissolve
"An absolute hulk sized monster enters the room. Having a rough time fitting through the door itself."
scene meetingalienstalk
with dissolve

qm creature1talk "\"Opanieliocovfgo opajhaopanielio. Nielio gioog lox jha fiuog gioog fiuog lox jha nielio nielio fiuog.\""
qm creature1talk2 "\"Nielio gioog opalox gioonielio gotcovfgo nieliolox fiuog. Gioogcovfgo jha loxopanieliogot jhanielio lox jhanielio giooggot fiuog Fiuognielioso.\""
qm creature1talk "\"Gioog jha nieliojha lox fiuog fiuograycovfgo lox loxla fiuog miuogioog.\""

scene meetingalientoucheslexa
with dissolve
"The alien moves in closer to Lexa."

qm creature1talk2 "\"Jha gioog gioog goonielio opa mee gioog gioogmee gioog gioog gioognielio giooggot lox gioog fiuoggioogmiuoso.\""
qm creature1talk2 "\"Nielio gioog gioogopajhanielio got loxgot gioog loxgot opagioog jha gioog' jhanielio gioog gioogloxopa.\""

m talk "\"What is he saying, Ruby?\""
r ttalk2 "\"He said they first want a volunteer male to mate with their Queen.\""
r ttalk2 "\"And a female of our choosing to join their ship forever and lastly a male of their choosing will join them as well.\""
r ttalk "\"They said no one will be harmed if we do as they say.\""
d talk2 "\"This is ridiculous! They want 2 people to join them forever? Who would volunteer to do that from the females in the first place?\""
m talk "\"Actually... I have an idea about the female we could give them.\""

scene meetingalientongueonlexa
with dissolve
"All of a sudden the alien extended his tongue out of his mouth right into Lexa's cleavage."
"You stand in shock and owe at what you are witnessing. Although Ruby said we shouldn't provoke them is this really something we can allow?"

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

$ quick_menu = False

menu:
    "Don't provoke them":
        $ quick_menu = True
        $ provoked_aliens = False
        "Sometimes the best thing to do is... nothing... it could make things only more dangerous for everyone if they get provoked."
        mc shocked2 "Just...endure it, Lex..."
        jump noprovocationaliens
    "Push him away":
        $ quick_menu = True
        $ breed_with_alien_queen = False
        $ persistent.change = "Edis female"
        $ provoked_aliens = True
        "Your anger boils as you watch what this alien does to Lexa right in front of your eyes and you decide to act."
        scene meetingmcpushesalien
        with dissolve
        "Without hesitation, you gather all your strength and push the alien that is harassing Lexa to the ground."
        qm creature1talk "\"loxgot gioog loxgot!!\""
        qm creature3talk "\"Opaloxgotgot!!!\""
        scene meetingbigalienscreams
        with dissolve
        "The big alien at the back violently screams at what you just did."
        "He charges towards you."
        scene meetingbigalienpunchmc
        with dissolve
        "Unable to block his huge fist he strikes your face."
        "You fly through the room and fall flat on the floor from the punch you just received."
        scene meetingmcknockedout
        with dissolve
        "You watch as Lexa stands right above you and watch you slowly lose consciousness..."
        scene meetingmcknockedout2
        with dissolve
        "You try and keep your eyes open, but it gets harder and harder."
        scene meetingmcknockedout3
        with dissolve
        "Your vision gets blurry and you completely lose consiousness."
        scene black
        with fadein
        "..."
        "You hear a faint voice speaking next to you..."
        qm randomz "\"... he'll be okay.\""
        "..."
        scene meetingmcwakesup
        with fadein
        "You wake up and the first thing you see is Lexa standing next to you..."
        "Holding your hand tightly."
        l atalk "\"Hey there. How are you feeling?\""
        mc talk2 "\"Hey yourself... like I just got punched by a 9 foot alien, but otherwise not that bad.\""
        scene meetingmcwakesup2
        with dissolve
        l atalk "\"You stood up for me... I really appreciate that.\""
        l atalk "\"A lot happened while you were unconscious...\""
        scene meetingjackpunchalienbnw2
        with fadein
        "Lexa explains how Jack somehow broke free from the cell and came in to stop the aliens as they were trying to take their prey away."
        scene meetingjackarmbnw00
        with dissolve
        "Sadly he got overwhelmed and ended up with a broken hand."
        scene meetingamirpickedbnw2
        with fadein
        "Then they decided to pick Amir to mate with their Queen and ultimately they kept him as their choice..."
        "Probably for his large cock he acquired not that long ago."
        scene eassimmelisagivesedisbottlebnw
        with fadein
        "For the female counterpart pick, Melisa gave the great idea to transform Edis with the prototype elixir drug she was testing into a female."
        scene eassimedisbecomesfemalebnw2
        with dissolve
        "And it worked!"
        scene eassimedisbecomesfemalebnw4
        with dissolve
        "They sent him as the female volunteer that would join their ship."
        scene meetingmcwakesup2
        with dissolve
        l atalk "\"And after that they left like they promised.\""
        mc talk3 "\"Wow... how long was I knocked out?\""
        m talk "\"A few hours.\""
        "You hear Melisa reply back instead and you turn to face her."
        scene meetingmelisatalktomc
        with dissolve
        m talk2 "\"Listen, [mc]. I need you to come with me.\""
        m talk "\"We have some important things to discuss.\""
        m talk2 "\"Please, follow me.\""
        jump startch9
        
        
#---------------------------------------------------------------------------------------------------------------------------------


label noprovocationaliens:
scene meetingalienstalk
with dissolve
"The alien eventually moves back to the door."
qm creature1talk2 "\"Lox? Fiuoglox gioog jhanielio giooggot fiuog Fiuognielioso?\""
r ttalk "\"They are waiting for us to pick the male to volunteer.\""
d talk2 "\'There is no way anyone would be willing to go with these creatures.\""
r ttalk2 "\"I am afraid we don't have much choice.\""
scene meetingmelisatalkstoyou
with dissolve
m talk "\"Actually... I have an idea how to save the female we have to send.\""
d talk "\"What is your plan?\""
m talk2 "\"I have an experimental prototype drug that can transform a person's gender. It's not a hundred percent tested to work yet, but we can try and use it on Edis and send him instead.\""
m talk "\"We don't lose anything in the process even if it ends up not working.\""
scene meetingdahliagrabsedis2
with dissolve
d talk2 "\"That sounds really good to me.\""
d talk "\"Hear that, cupcake? You will hopefully grow tits soon.\""
scene meetingdahliagrabsedis
with dissolve
r talk "\"What about the male volunteer?\""
scene meetingamirtalking
with dissolve
amir talk "\"There is no way I am going to volunteer for this shit.\""
m talk "\"Seeing as we don't have much of a choice right now it's between you and [mc] here.\""

$ quick_menu = False

menu:
    "Step up and volunteer":
        $ quick_menu = True
        $ breed_with_alien_queen = True
        mc talk3 "\"I will do it.\""
        l adoubt "\"What?!\""
        mc talk2 "\"I volunteer to go with them.\""
        scene meetingdahliarubylookatyou
        with dissolve
        d talk2 "\"That's really brave of you [mc].\""
        l atalk "\"Why though? You don't know what they will do to you there.\""
        mc talk3 "\"Someone has to go. I will be fine, don't worry about me. Remember that I'll come back, they will choose who to join them afterwards...\""
        "At that moment you hear the door open again..."
        scene meetingjackpunchalien1
        with dissolve
        "You can't believe your eyes..."
        "You see Jack entering and he attacks the aliens straight ahead."
        scene meetingjackpunchalien2
        with dissolve
        jack angry "\"You better get the fuck out of here right now!\""
        qm creature3talk "\"Uopohhh\""
        scene meetingjackarm01
        with dissolve
        "Jack goes for another swing, but gets stopped in his tracks..."
        qm creature3talk "\"Ray jhala!\""
        scene meetingjackarm00
        with dissolve
        "All you could hear is the bones crack and echo through the whole room."
        jack angry "\"Aaaaaaaaaaahhhhh!!\""
        scene meetingjackarm3
        "Jack collapses down on the floor..."
        "Holding his wrist in agony."
        scene meetingjackarm5
        with dissolve
        qm creature1talk2 "\"Fiuog! Fiuog jhaopa loxcfg opa lox jhanieo gioee got.\""
        d angry "\"What is he saying?\""
        r ttalk "\"He says they want [mc] to come with them right now.\""
        "You decide it's best not to piss them off more than this and you walk towards them."
        scene meetingmctaken
        with dissolve
        "As you leave with both aliens you watch Jack on the floor with completely broken wrist."
        "Although you hate him, you can't deny that he earned some respect for doing what he did today."
        jump mcmatingwithalienqueen
        
    "Keep quiet and see what happens":
        $ quick_menu = True
        $ breed_with_alien_queen = False
        mc thinking "There is no way I will volunteer to go with them..."
        "At that point you hear the door open again..."
        scene meetingjackpunchalien1
        with dissolve
        "You can't believe your eyes..."
        "You see Jack entering and he attacks the aliens straight ahead."
        scene meetingjackpunchalien2
        with dissolve
        jack angry "\"You better get the fuck out of here right now!\""
        qm creature3talk "\"Uopohhh\""
        scene meetingjackarm01
        with dissolve
        "Jack goes for another swing, but gets stopped in his tracks..."
        qm creature3talk "\"Ray jhala!\""
        scene meetingjackarm00
        with dissolve
        "All you could hear is the bones crack and echo through the whole room."
        jack angry "\"Aaaaaaaaaaahhhhh!!\""
        scene meetingjackarm3
        "Jack collapses down on the floor..."
        "Holding his wrist in agony."
        scene meetingjackarm4
        with dissolve
        "The smaller alien points at Amir."
        qm creature1talk2 "\"Fiuog! Fiuog jhaopa loxcovfgo giooggot opa lox jhanielio gioogmee got.\""
        d angry "\"What is he saying?\""
        r ttalk "\"We took too long to pick a male to mate with their Queen, so they are picking instead. They picked Amir to go with them.\""
        scene meetingamirpicked
        with dissolve
        amir angry "\"Are you kidding me?! ME?! The one who funded this trip and kept you all alive right now instead of burning down on Earth!?\""
        d angry "\"Do you see us in much of a position to do anything about it right now after witnessing what happened to Jack?!\""
        scene meetingamirpicked2
        with dissolve
        "Amir might have a huge ego, but he is still a coward and he doesn't want anything like that to happen to him, so he accepts his fate."
        m talk "\"Dahlia... can you help me carry Edis and prepare him?\""
        d talk "\"Of course, let's go.\""
        jump afteramirpickedbyaliens

label mcmatingwithalienqueen:

$ quick_menu = False

menu:
    "Watch Edis transformation and genderbend sex scene":
        $ quick_menu = True
        scene a few minutes later
        $ quick_menu = False
        with fasterfadein
        pause 2.0
        with fasterfadeout                                                                
                                                
        scene eassimtrioenters
        $ quick_menu = True
        with fasterfadein   
        d talk "\"This bastard is heavy.\""
        m talk2 "\"He will lose weight soon.\""
        d talk2 "\"Hey... do you think you can do a partial effect?\""
        m talk2 "\"What do you have in mind?\""
        d talk "\"I want to grow a penis and have a little bit of fun with him before we give him to those creatures.\""
        m talk "\"Hmm...\""
        m talk2 "\"I might have something in mind. I will give you something to drink right now and the effect should go away. Finding a permanent solution like the one for our friend here is harder than a temporary one.\""
        d talk2 "\"Good. Give it to me.\""
        m talk "\"Help me strap him on the chair first.\""
        scene eassimedisboundonchair
        with dissolve
        d talk2 "\"I am so glad this bastard will get what is coming to him.\""
        m talk "\"I am hoping this drug will work as not many tests were performed so far, but let's see...you drink this and for him...\""
        scene eassimmelisagivesedisbottle2
        with dissolve
        m talk "\"I just need him to swallow a few drops of this...\""
        scene eassimmelisagivesedisbottle
        with dissolve
        m talk2 "\"And voala.\""
        m talk "\"That should do it.\""
        scene eassimedisboundonchair
        with dissolve
        d talk "\"How long until it takes effect?\""
        m talk "\"A couple of minutes should be enough.\""
        scene a few minutes later
        $ quick_menu = False
        with fasterfadein
        pause 2.0
        with fasterfadeout        

        scene eassimedisboundonchair
        with fasterfadein
        $ quick_menu = True
        d talk "\"Look he started to change!\""
        scene eassimedisbecomesfemale1
        with dissolve
        d talk "\"His dick started to retract!\""
        d talk2 "\"This was all worth it just for this moment alone!\""
        scene black
        with dissolve
        "A couple more minutes later..."
        scene eassimedisbecomesfemale2
        with fadein
        d talk "\"Look. He is transforming again!\""
        m talk "\"Incredible. It's working.\""
        scene eassimedisbecomesfemale3
        with dissolve
        d talk2 "\"His dick is gone, he grew tits, his hair got longer, he lost weight.\""
        m talk "\"It seems his breasts are not done growing, look!\""
        scene eassimedisbecomesfemale4
        with dissolve
        d talk "\"Wow. I am kind of jealous. He grew such huge melons in no time.\""
        scene eassimdahliagrowingdick1
        with dissolve
        d talk2 "\"Ah... I feel it starting to grow for me too.\""
        scene eassimdahliagrowingdick2
        with dissolve
        d talk "\"This feels incredible... so this is how it feels to have a dick.\""
        d talk2 "\"Oh my...\""
        scene eassimdahliagrowingdick3
        with dissolve
        d talk "\"It's rock hard. I can feel it pulsing.\""
        d talk2 "\"You bitch will feel how I felt.\""
        scene eassimdahliaabouttofuckedis
        with dissolve
        "Dahlia slaps Edis across the face."
        d talk "\"Wake up bitch. Your dinner has arrived.\""
        edis aangry "\"Wha--...\""
        edis aangry2 "\"WHAT THE FUCK IS THIS?! What have you done to me!?\""
        scene eassimdahliaabouttofuckedis2
        with dissolve
        d talk2 "\"Karma, bitch.\""
        d talk "\"Make sure you enjoy it as this will be the first of many dicks you will receive in the near future.\""
        edis aangry "\"G-Get the fuck off.\""
        d talk2 "\"Sure, right after I impregnate your cunt.\""
        
        $ quick_menu = False
        show screen dahlia_fucks_edis
        $ renpy.show("dahlia_fucks_edis")
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(12, hard=True)

        label dahlia_fucks_edis:
        hide screen dahlia_fucks_edis
        
        $ quick_menu = True
        d talk "\"I am about to explode inside your virgin cunt, bitch.\""
        d pleasure "\"Accept all my semen inside you and get pregnant!\""
    
        scene eassimdahliacumming
        with flash
        scene eassimdahliacumming
        with flash
        scene eassimdahliacumming
        with flash
        edis aangry "\"Aaaah!!\""
        d talk2 "\"I can feel your cunt filled up with my semen.\""
        d talk2 "\"I stretched your slutty pussy so much! You should thank me. It will help you out a lot for your new life.\""
        scene eassimdahliacumming2
        with dissolve
        edis insane "\"Aiiiiiiiiii!!\""
        d talk "\"When you give birth to a red skinned baby, remember who it's from and what led you to this outcome.\""
        scene black
        with dissolve
        d talk2 "\"I am done with him. We can escort him to their ship now.\""
        jump mcpickedskipedistransformation
        
    "Skip":
        $ quick_menu = True
        jump mcpickedskipedistransformation


label mcpickedskipedistransformation:         #mc mating with queen
$ persistent.change = "Edis female"
with fasterfadein
scene meanwhile
$ quick_menu = False
pause 2.5
with fasterfadeout
$ quick_menu = True

scene airlockalienshipdock
with fadein
"You are escorted to the dock where the alien vessel entrance was located..."
scene alienshiphallway
with dissolve
"You walk through dark and long hallways that feel like you are walking inside a creature's insides."
scene alienshiphallway2
with fadein
"You eventually reach your destination destination..."
"You can see some form sitting in the distant hallway waiting for you."
qm aavatalk2 "\"Loxnielio. Opacovfgo gioog lox nielio...\""
qm aavatalk "\"Gioog nielionielio lox lox pax. Gioog ray gioog fiuoggioogmiuoso lagioognielio nielio.\""
"You hear the Queen speak as you get closer to her.\""
scene aavatalkstomc
with dissolve
qm aavatalk "\"Loxnieliofiuog opagioog. Gioog gioog soso nieliofiuogcovfgo fiuog.\""
"You expected to see a monster, but instead get pleasantly surprised."
mc shocked2 "Wow... she is actually not even remotely close to being as ugly as these creatures are."
mc talk3 "She has smooth skin, but she is covered in something... like a parasite that covers her entire body."
scene aavabodychange1
with dissolve
"She sits in a provocative pose and spreads her legs."
qm aavatalk2 "\"Ogmiuoso lagioognieli.\""
scene aavabodychange2
with dissolve
"You see as this thing leaves her body and reveals a very humanoid body."
scene aavabodychange3
with dissolve
"Eventually revealing her full body."
"You take the moment to look closer."
scene aavabodyupclose
with dissolve
"She didn't just look like a Queen, but more like a Goddess."
"You admired the perfect symmetry of her body."
"Feeling mesmerised you keep looking her seductive body until your thoughts get interrupted."

qm aavatalk2 "\"Loxnielio pax, opala nielio jhaopa.\""

mc talk3 "I don't need to know what she is saying to know what I need to do..."
mc talk3 "They were very specific as to what they wanted me to do."
"You take off your clothes and position yourself on top of her and don't waste any time as you penetrate her alien cunt and start pounding her hard."

$ quick_menu = False
show screen mc_fucks_alien_queen
$ renpy.show("mc_fucks_alien_queen")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label mc_fucks_alien_queen:
hide screen mc_fucks_alien_queen

$ quick_menu = True
qm aavapleasure "\"Opala nielio jha! Opala Nielio Jha. Opacovfgo.\""
"The creature looked like it just came and you were about to as well..."

$ quick_menu = False

menu:
    "Cum inside":
        $ quick_menu = True
        mc nudepleasure2 "\"I am cumming~\""
        scene mccumsinsideaava
        with flash
        scene mccumsinsideaava
        with flash
        scene mccumsinsideaava
        with flash
        "You send a torrents of cum inside her. Filling her up so much that semen gush out of her."
        qm aavatalk2 "\"Gotgioog fiuog opajhaopanielio. Gioog gioog jha fiuog jha got.\""
        "You get up and dress as the creature that brought you here starts escorting you back to Paradise."
        "You look back one last time before leaving seeing the Queen standing proud... with semen still dripping from her genitals."
        $ quick_menu = False
        scene aavaaftersexportrait with fade:
            subpixel True
            yalign 1.0
            pause 2.0
            linear 7.0 yalign 0.0
        pause
        jump mcmatingwithqueenend

label mcmatingwithqueenend:
scene meetingamirpicked3
with dissolve
$ quick_menu = True
"As you return the creatures make their pick for permanent male to join their spaceship..."
"They picked Amir... probably for the huge dick he recently enlarged to inhuman size. The Queen will probably love it."
"He didn't struggle much as he was afraid of getting the treatment Jack got..."
scene black
with fadein
"You can't even believe what transpired in the last few hours."
"Wrapping your head around it is too much."
scene meetingmelisatalktomc
with fadein
m talk2 "\"Listen, [mc]. I am glad you are back. I need you to come with me.\""
m talk "\"We have some important things to discuss.\""
m talk2 "\"Please, follow me.\""
jump startch9
        
label afteramirpickedbyaliens:
$ quick_menu = False
menu:
    "Watch Edis transformation and genderbend sex scene":
        $ quick_menu = True
        scene a few minutes later
        $ quick_menu = False
        with fasterfadein
        pause 2.0
        with fasterfadeout                                                                
                                                
        scene eassimtrioenters
        $ quick_menu = True
        d talk "\"This bastard is heavy.\""
        m talk2 "\"He will lose weight soon.\""
        d talk2 "\"Hey... do you think you can do a partial effect?\""
        m talk2 "\"What do you have in mind?\""
        d talk "\"I want to grow a penis and have a little bit of fun with him before we give him to those creatures.\""
        m talk "\"Hmm...\""
        m talk2 "\"I might have something in mind. I will give you something to drink right now and the effect should go away. Finding a permanent solution like the one for our friend here is harder than a temporary one.\""
        d talk2 "\"Good. Give it to me.\""
        m talk "\"Help me strap him on the chair first.\""
        scene eassimedisboundonchair
        with dissolve
        d talk2 "\"I am so glad this bastard will get what is coming to him.\""
        m talk "\"I am hoping this drug will work as not many tests were performed so far, but let's see...you drink this and for him...\""
        scene eassimmelisagivesedisbottle2
        with dissolve
        m talk "\"I just need him to swallow a few drops of this...\""
        scene eassimmelisagivesedisbottle
        with dissolve
        m talk2 "\"And voala.\""
        m talk "\"That should do it.\""
        scene eassimedisboundonchair
        with dissolve
        d talk "\"How long until it takes effect?\""
        m talk "\"A couple of minutes should be enough.\""
        scene a few minutes later
        $ quick_menu = False
        with fasterfadein
        pause 2.0
        with fasterfadeout        

        scene eassimedisboundonchair
        with fasterfadein
        $ quick_menu = True
        d talk "\"Look he started to change!\""
        scene eassimedisbecomesfemale1
        with dissolve
        d talk "\"His dick started to retract!\""
        d talk2 "\"This was all worth it just for this moment alone!\""
        scene black
        with dissolve
        "A couple more minutes later..."
        scene eassimedisbecomesfemale2
        with fadein
        d talk "\"Look. He is transforming again!\""
        m talk "\"Incredible. It's working.\""
        scene eassimedisbecomesfemale3
        with dissolve
        d talk2 "\"His dick is gone, he grew tits, his hair got longer, he lost weight.\""
        m talk "\"It seems his breasts are not done growing, look!\""
        scene eassimedisbecomesfemale4
        with dissolve
        d talk "\"Wow. I am kind of jealous. He grew such huge melons in no time.\""
        scene eassimdahliagrowingdick1
        with dissolve
        d talk2 "\"Ah... I feel it starting to grow for me too.\""
        scene eassimdahliagrowingdick2
        with dissolve
        d talk "\"This feels incredible... so this is how it feels to have a dick.\""
        d talk2 "\"Oh my...\""
        scene eassimdahliagrowingdick3
        with dissolve
        d talk "\"It's rock hard. I can feel it pulsing.\""
        d talk2 "\"You bitch will feel how I felt.\""
        scene eassimdahliaabouttofuckedis
        with dissolve
        "Dahlia slaps Edis across the face."
        d talk "\"Wake up bitch. Your dinner has arrived.\""
        edis aangry "\"Wha--...\""
        edis aangry2 "\"WHAT THE FUCK IS THIS?! What have you done to me!?\""
        scene eassimdahliaabouttofuckedis2
        with dissolve
        d talk2 "\"Karma, bitch.\""
        d talk "\"Make sure you enjoy it as this will be the first of many dicks you will receive in the near future.\""
        edis aangry "\"G-Get the fuck off.\""
        d talk2 "\"Sure, right after I impregnate your cunt.\""
        
        $ quick_menu = False
        show screen dahlia_fucks_edis3
        $ renpy.show("dahlia_fucks_edis3")
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(12, hard=True)

        label dahlia_fucks_edis3:
        hide screen dahlia_fucks_edis3
        $ quick_menu = True
        
        d talk "\"I am about to explode inside your virgin cunt, bitch.\""
        d pleasure "\"Accept all my semen inside you and get pregnant!\""
    
        scene eassimdahliacumming
        with flash
        scene eassimdahliacumming
        with flash
        scene eassimdahliacumming
        with flash
        edis aangry "\"Aaaah!!\""
        d talk2 "\"I can feel your cunt filled up with my semen.\""
        d talk2 "\"I stretched your slutty pussy so much! You should thank me. It will help you out a lot for your new life.\""
        scene eassimdahliacumming2
        with dissolve
        edis insane "\"Aiiiiiiiiii!!\""
        d talk "\"When you give birth to a red skinned baby, remember who it's from and what led you to this outcome.\""
        scene black
        with dissolve
        d talk2 "\"I am done with him. We can escort him to their ship now.\""
        jump afteredistransformationandamirpicked
        
    "Skip":
        jump afteredistransformationandamirpicked

label afteredistransformationandamirpicked:
$ persistent.change = "Edis female"
scene black
with dissolve
$ quick_menu = True
"You can't even believe what transpired in the last few hours."
"Wrapping your head around it is too much. The aliens ultimately kept Amir as their choice... probably for his huge inhuman dick."
"You eventually see Melisa returning to the room after they successfuly transformed Edis into a female and transported him to the alien ship after which they left like they promised."
scene meetingmelisatalktomc
with fadein
m talk2 "\"Listen, [mc]. I need you to come with me.\""
m talk "\"We have some important things discuss.\""
m talk2 "\"Please, follow me.\""
jump startch9

