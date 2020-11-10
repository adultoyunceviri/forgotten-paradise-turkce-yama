label startch9:
scene black
with fasterfadein
"While you were making your way to talk privately with Melisa, you heard Ruby's voice over the intercom saying that another ship is headed our way."
"Hearing that put you on edge, but she continued saying that they mean no harm and just want some sort of information."
"A few minutes later you arrive in one of the medical rooms with Melisa."

scene ch9medbay1
with fadein

mc talk2 "\"So...?\""

m talk "\"Please, [mc]. Hear me out.\""
m talk2 "\"I know how all of this must look and honestly I would've done the same thing in your position.\""

mc talk "\"And what's that? Overthrow the evil organization which experiment on innocent people?\""

m talk "\"Let me finish.\""
m talk2 "\"You're right, it is an experiment.\""
m talk "\"It was a serum which would've made a lot of things a lot easier.\""
m talk2 "\"It was meant to get information out of spies.\""
m talk "\"But in order to do that we had to make sure it was actually working properly.\""
m talk2 "\"And testing it on people who are aware of what they are being tested with just doesn't validate it's use.\""
m talk "\"So, yes, we had to test this on unexpected civilians for the best possible results.\""
m talk2 "\"And sadly you and the others were the 'lucky' ones...\""
m talk "\"I don't expect you to forgive me or something like that I just need you to understand that it was nothing personal.\""

mc shocked "\"Yeah, sure. Tell that to my wife.\""

m talk "\"You know... it's not permanent thing. But would you be okay for your wife to recover her memories faster to begin with?\""

$ quick_menu = False

menu:
    "Yes, I want her to recover as fast as possible.":
        $ quick_menu = True
        mc talk2 "\"Of course I want her to get her memories back as soon as possible...\""
        mc talk3 "\"There is no question about it.\""
        m talk "\"I see...\""
    "Maybe not...":
        $ quick_menu = True
        mc thinking "She does making a fair point... knowing what my wife has done and is doing at the moment..."
        mc talk "\"Maybe you're right. It doesn't excuse you for what you've done however.\""
        mc talk2 "\"Things wouldn't be the way they are if it wasn't for you people.\""
        m talk "\"Maybe... or maybe it just speeded up the process? Perhaps she just showed her true colors.\""
        mc shocked "\"*Tsk*\""
        "You can't help, but feel disgusted just thinking about it."

scene ch9medbay2
with dissolve
m talk2 "\"Anyway, that's not the only reason I asked you to come here.\""
m talk "\"Please, have a sit.\""

"You walk over and sit on the medical bed."

scene ch9medbay3
with dissolve
m talk "\"Ruby mentioned earlier that there was a device which can help translate any language. It's still not finished, but it's far along that I can implement it.\""
m talk2 "\"Do you trust me to do that for you?\""
mc thinking "Ruby did mention that and I doubt the android is part of their little group."
mc talk2 "\"I guess.\""
m talk "\"Good. We need to rebuild our trust.\""
m talk2 "\"Another step towards that is making you take the lead of Paradise for the time being.\""
mc talk "\"What do you mean?\""

scene ch9medbay4
with dissolve
"She proceeds to implant the device in your neck."
m talk "\"What I mean is trust is a two way street.\""
m talk2 "\"With Jack being out of commission for the time being and with Amir not being present as a board member... And you proven yourself numerous times...\""
m talk "\"I believe you can be in charge. With what you've done so far to help here and with your millitary service you are best suited. Whatever decision you make we will support it.\""
mc talk3 "\"Really? Well, I guess I could do it.\""
m talk2 "\"Of course you can. I already let everyone know that you will be in charge.\""
mc thinking "That's a ballsy move to make, but I will gladly take the reins from these people."
". . ."

scene ch9medbay3
with fasterfadein
m talk "\"And you are done!\""
m talk2 "\"How do you feel? Do you understand what I am saying?\""
mc talk3 "\"Of course I do. Why wouldn't I?\""
m talk "\"Because I just spoke Japanese and you replied back in Japanese. So the device does work properly.\""
mc talk2 "\"Wow. Indeed. So I reply back in the language that I was last spoken to?\""
m talk2 "\"Correct.\""

scene ch9medbay5
with dissolve
m talk2 "\"You know how grateful I am that you are willing to make this work...\""
"She begins rubbing your thigh towards your crotch."

$ quick_menu = False

menu:
    "Let her continue":
        $ quick_menu = True
        $ ch9_melisa_sex = True
        mc talk2 "\"Oh yeah? Show me.\""
        scene ch9medbay6
        with dissolve
        "She gets down and removes her already unbuttoned blouse."
        "She then proceeds to unbutton your jeans and slide them down with your underwear..."
        scene ch9medbay7
        with dissolve
        m nudetalk "\"Mmmm. Here he is.\""
        m nudetalk2 "\"Let me stroke you a little.\""
        
        $ quick_menu = False
        show screen ch9_med_hj
        $ renpy.show("ch9_med_hj")
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(12, hard=True)

        label ch9_med_hj:
        hide screen ch9_med_hj
        $ quick_menu = True
        
        mc pleasure "\"Mmm~ hahh~~\""
        
        "You feel yourself getting closer and closer."
        $ quick_menu = False
        menu:
            "Cum":
                $ quick_menu = True
                mc pleasure2 "\"Fuck! I am coming!\""
                m nudepleasure "\"Yess~ spray me~~\""
                m nudepleasure "\"Spray my whore face with your juice!!!\""
                "Her dirty words push you over the edge--"
                scene ch9medbaycumoutside
                with flash
                scene ch9medbaycumoutside
                with flash
                scene ch9medbaycumoutside
                with flash
                scene ch9medbaycumoutside2
                with flash
                "You spray her whole face with your cum, even hitting her right eye."
                mc talk2 "\"Oops, sorry about that.\""
                m nudetalk "\"It's fine, don't worry about it, [mc].\""
                jump ch9aftermelsex
            "Tell her to blow you":
                $ quick_menu = True
                mc pleasure "\"Blow me.\""
                m nudepleasure "\"Mmm~ it will be my pleasure.\""
                
                $ quick_menu = False
                show screen ch9_med_bj
                $ renpy.show("ch9_med_bj")
                $ renpy.transition(Dissolve(1))
                $ renpy.pause(12, hard=True)

                label ch9_med_bj:
                hide screen ch9_med_bj
                $ quick_menu = True
                
                "You feel yourself getting close again."
                $ quick_menu = False
                menu:
                    "Cum inside her mouth":
                        $ quick_menu = True
                        mc pleasure2 "\"Cumming~\""
                        scene ch9medbaycuminside
                        with flash
                        scene ch9medbaycuminside
                        with flash
                        scene ch9medbaycuminside
                        with flash
                        "You fill her mouth full of your cum as it starts to spill out."
                        m nudepleasure "\"*Gulp*, *Gulp*, *Gulp*\""
                        m nudepleasure "\"*Slurp*,*Gulp*, *Slurp*\""
                        "She cleans your dick after swallowing all she could."
                        jump ch9aftermelsex
                    "Cum on her face":
                        $ quick_menu = True
                        mc pleasure2 "\"Quick, let me cum on your face.\""
                        scene ch9melhandjob
                        "She pops your dick out of her mouth and a few quick strokes is all it takes for you to finish."
                        scene ch9melhandjob
                        with flash
                        scene ch9medbaycumoutside
                        with flash
                        scene ch9medbaycumoutside
                        with flash
                        scene ch9medbaycumoutside2
                        with flash
                        scene ch9medbaycumoutside2
                        with flash
                        "You splash her face with hot jizz and even cover her right eye."
                        mc talk2 "\"Oops, sorry about that.\""
                        m nudetalk "\"It's fine, don't worry about it, [mc].\""
                        jump ch9aftermelsex
    "Push her away":
        $ quick_menu = True
        $ ch9_melisa_sex = False
        scene ch9medbay5reject
        with vpunch
        mc shocked "\"No!\""
        mc shocked "\"We might be at peace right now, but this doesn't mean anything more.\""
        m talk "\"Sure... Of course, I understand completely.\""

        jump ch9rubyintercom

label ch9aftermelsex:
scene ch9medbay8
with fadein
"After a few minutes Melisa cleans herself and comes back."
m talk "\"I hope we can begin to trust each other again. A chance is all I ask.\""
mc talk "\"We will see where this goes, but I am willing to give it a chance at least.\""
"You can't help, but notice the immediate smile on her face after she hears your words."
"She must sincerely want this."
jump ch9rubyintercom

label ch9rubyintercom:
with fasterfadein
scene meanwhile
$ quick_menu = False
pause 2.5
with fasterfadeout

scene ch9arrivalportrait with fade:
    subpixel True
    yalign 1.0
    pause 2.0
    linear 8.0 yalign 0.1
pause
with fasterfadein

scene ch9medbay9
with fasterfadein

$ quick_menu = True

"At this moment you hear Ruby's voice on the intercom..."
r ttalk "\"[mc], our guests have arrived. Please make your way to the meeting room.\""

scene ch9medbay8
with dissolve

mc talk "\"Well, I guess duty calls.\""
m talk "\"Yeah.\""

scene ch9medbay10
with dissolve

m talk2 "\"Hey... thanks again for giving me and the crew a chance.. Commander.\""
mc talk "\"There's not much else I can do. We are stuck together now.\""
"You say as you leave into the hallway."

if saved_dahlia_from_edis:
    scene ch9medbay11
    with vpunch
    d talk "\"Hey, 'commander'.\""
    "Dahlia says giggling."
    mc talk "\"Haha, hey yourself Dahlia.\""
    scene ch9medbay13
    with dissolve
    d talk2 "\"I think that title is well suited for my savior.\""
    d talk "\"And I think my savior needs to be rewarded.\""
    scene ch9medbay12
    with vpunch
    "She says as she grabs your crotch."
    d talk "\"Would you like me to come by later to show you how grateful I am?\""
    $ quick_menu = False
    menu:
        "Ask her to visit your room":
            $ quick_menu = True
            $ accept_dahlia_visit = True
            scene ch9medbay13
            with dissolve
            mc talk3 "\"Sure, you're welcome to come by and show me your 'gratitude', hehe.\""
            d talk "\"Great~ I will swing by your room a bit later.\""
            jump ch9meeting
            
        "Decline":
            $ quick_menu = True
            $ accept_dahlia_visit = False
            scene ch9medbay13
            with dissolve
            mc talk "\"It's okay, Dahlia. I appreciate your offer, but I will pass. I am just glad you are okay.\""
            d talk2 "\"What? Are you sure? I don't offer myself to just anyone.\""
            mc talk2 "\"Yeah, I am sure. Thanks though!\""
            d talk "\"Well, okay. Thank you again for saving my life though...\""
            mc talk3 "\"Don't mention it. Anyone would've done the same.\""
            jump ch9meeting
else:
    scene black
    $ accept_dahlia_visit = False
    jump ch9meeting

label ch9meeting:
scene black
with fadein
"You walk to the specified room to meet the crew of the ship that boarded you now..."

scene ch9meeting1
with fasterfadein
"You meet Ruby outside the room."
r ttalk2 "\"So. [mc]. I understand you are in charge now. If there's anything you need from me you can let me know, okay?\""
mc talk2 "\"Of course. I will let you know.\""
r ttalk "\"Great.\""
mc talk "\"What are we dealing with here now? Who are they?\""
r ttalk "\"They appear to be on a hunt for some criminal.\""
r ttalk2 "\"They don't mean any harm to us, they just want information.\""
r ttalk "\"And if we cooperate they said they'd reward us with food and other necessities for our travels.\""
mc talk2 "\"Well, that sounds reasonable. I will see them now.\""
r ttalk2 "\"Of course. They are waiting for you inside on my left.\""

scene ch9meeting2
with fadein
"You enter through the door."
"You weren't sure what to expect, you were expecting something big, muscular and ugly based on your previous encounter."
"But you were really surprised how wrong you were."

scene ch9meeting4
with dissolve
"You see an alien with a blue skin and weird tentacles coming from the head sitting in a meditative pose."
"The other one resembling human next to her, seem really arrogant as she has placed her feet on the table almost as if proclaiming the ship for herself already."
qm karintalk "\"The Commander, I presume?\""
"You hear the humanoid begin to speak."
"You are stunned for a moment as you understand her perfectly, but then remembered the device Melisa just placed in your neck."
"Seems to be doing a great job so far."
scene ch9meeting3
with dissolve
mc talk "\"That's right. I am [mc]. And you are?\""
"You make your way to a chair and sit down."

scene ch9meeting5
with dissolve
shp talk "\"I am Karin and this here is my companion -- Aurora.\""
mc talk "\"What can we do for you?\""
shp talk "\"Before we begin, I gotta ask... is the planet you're orbiting around... your home world?\""
mc talk2 "\"Indeed it is...\""
shp talk "\"How misfortunate....\""
shp talk "\"Okay, well, let me wake up my companion here and get straight to the point.\""
scene ch9meeting6
with vpunch
shp talk "\"Psst. Hey.\""
shp talk "\"Wake up, Aury.\""
"She snaps her fingers a few more times."

scene ch9meeting7
with vpunch
aur talk "\"I am awake!!\""
"You hear the blue alien speak in an angry, but cute voice."
shp talk "\"Sorry about that, darling. You know I'd let you meditate all day long if we weren't in a hurry.\""
shp talk "\"The Commander is here and we need to get the information for our hunt.\""
scene ch9meeting8
with dissolve
aur talk "\"Ah, of course! Where are my manners? I am Aurora.\""
scene ch9meeting9
with dissolve
aur talk "\"I hope you don't mind my meditation here... I had to remove my boots.\""
aur talk "\"It's hard for me to meditate otherwise and it's uncomfortable doing that on a chair too.\""
scene ch9meeting10
with vpunch
aur talk "\"B-But don't worry! My feet are perfectly clean!!\""
aur talk "\"See?\""
shp talk "\"Mmm... sparkling clean even.\""
mc talk "\"You're good. Don't worry about it.\""

scene ch9meeting13
with dissolve
"She takes out some sort of device out."
aur talk "\"First I'd like to say you will be rewarded for your cooperation, we will give you important resources for your time and cooperation also a destination for a habitable world... And something extra...\""
mc thinking "Resources are something we need badly at this point and we can't pass this oportunity... I wonder what they mean by 'something extra'?"
aur talk "\"Well, we are here because we've been chasing a particular ship and it's captain for a long time now.\""
aur talk "\"And our trail suggests they stayed at this proximity for a bit which is unusual for them to do, unless...\""
aur talk "\"Unless they have selected a new prey to dominate over which we believe was your crew.\""

scene ch9meeting12
with dissolve
aur talk "\"The target we are looking for is a pale female alien that is also referred to as 'Queen'.\""
aur talk "\"She sends her minions or most commonly known as her children, to do get her new male and female counterpart from different species to mate with.\""
aur talk "\"Producing many abominations and not taking no for an answer.\""
aur talk "\"Anyway, she was put for intergalactic search after attacking a colony of ours.\""

scene ch9meeting14
with dissolve
shp talk "\"She and her children must be captured at all costs.\""
shp talk "\"They wreck havoc across the galaxy and if you can give us accurate information if they visited you it will help a lot.\""
mc talk "\"Well... I know who you are talking about.\""
mc talk2 "\"They did come and go not that long ago.\""
mc talk3 "\"Probably an hour or two before your arrival.\""
mc talk "\"They did take a female and male from our crew.\""
mc talk2 "\"With our planet in flames we were in no position to oppose them even though some of us tried...\""

scene ch9meeting11
with dissolve
shp talk "\"I understand completely. They are not an easy foe even if you were prepared to face them.\""
shp talk "\"Can you upload the possible route of their arrival and leave? As in which way they went after they visited you?\""
scene ch9meeting14
with dissolve
mc talk2 "\"I believe we can do that. Ruby, our android, can assist you with uploading the data over to you.\""
shp talk "\"Great!\""
shp talk "\"That's one sexy android if you don't mind me saying.\""
shp talk "\"If we had one of those on our ship I'd be motorboating her titties all day whenever I can.\""
aur talk "\"*Ahem*\""
"You hear the blue alien get slightly annoyed or jealous."
shp talk "\"Anyway, Aury, how about we give him the extra reward for his cooperation?\""

scene ch9meeting15
with dissolve
mc talk "\"And what reward would that be?\""
aur talk "\"The greatest reward of all -- pleasure.\""

scene ch9meeting17
with vpunch
"She places her foor right on your crotch and strokes it gently."
shp talk "\"Believe me, her foot is a gift which should be experienced.\""
shp talk "\"Her 900 years have given her enough experience to make her an absolute expert at everything possible.\""
mc talk "\"Ah... damn.\""

$ quick_menu = False

menu:
    "Ask to fuck Karin instead":
        $ quick_menu = True
        scene ch9meeting19
        with dissolve
        mc talk2 "\"Why don't you join in? I'd love to have the full package for my amazing cooperation.\""
        shp talk "\"Hahahaha. I love cocky males. It makes me even hornier.\""
        scene ch9meeting20
        with dissolve
        shp talk "\"It's your lucky day, boy. I will grant your wish.\""
        shp talk "\"But once you cum, that's it.\""
        shp talk "\"We have a criminal to catch.\""
        scene ch9meeting22
        with dissolve
        "You unbutton your jeans and remove your pants."
        shp nudetalk "\"Mmm, like what you see?\""
        shp nudetalk "\"Do you like my cunt?\""
        mc talk "\"It looks amazing, yes.\""
        shp nudetalk "\"C'mon, Aury. Why haven't you removed your robe already?\""
        scene ch9meeting23
        with dissolve
        "And so she did without any hesitation."
        shp nudetalk "\"Now climb on top of me and let me eat that mouthwatering blue cunt of yours while I get my pussy stuffed by a hard cock.\""
        "You hold your cock that is already hard as a rock and straight as an arrow and move in closer."
        $ quick_menu = False
        scene ch9meetingportrait with fade:
            subpixel True
            yalign 1.0
            pause 2.0
            linear 7.0 yalign 0.1
        pause
        with fasterfadein
        $ quick_menu = True
        "Aurora climbs on top of Karin and puts her pussy lips right on top of her mouth."
        scene ch9meeting24
        with fasterfadein
        "In return you take your cock in your right hand and place it on the entrance of her pussy."
        "Feeling her wetness as you push forward."
        scene ch9meeting25
        with flash
        shp nudetalk "\"Mmmmm~~~\""
        "You hear her soft moans as you push forward."
        
        $ quick_menu = False
        show screen ch9_meeting_vag
        $ renpy.show("ch9_meeting_vag")
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(12, hard=True)

        label ch9_meeting_vag:
        hide screen ch9_meeting_vag
        
        $ quick_menu = True
        mc nudepleasure "\"Hnngg, haaahh, hahh--\""
        "You feel yourself getting closer and closer."
        "You pick up the pace."
        $ quick_menu = False
        show screen ch9_meeting_vag2
        $ renpy.show("ch9_meeting_vag2")
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(12, hard=True)

        label ch9_meeting_vag2:
        hide screen ch9_meeting_vag2
        $ quick_menu = True
        "Watching Aurora's ass right in front of you makes you go over the edge even faster--"
        
        jump ch9meetingjanecum
        
        

    "Tell Aurora to proceed with her feet":
        $ quick_menu = True
        scene ch9meeting21
        with dissolve
        mc talk "\"Please, continue.\""
        shp talk "\"Haha. I told you. Her feet are out of this world.\""
        scene ch9footjob
        with dissolve
        "You remove your pants as she places her foot on top of your dick."
        
        $ quick_menu = False
        show screen ch9_meeting_footjob
        $ renpy.show("ch9_meeting_footjob")
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(12, hard=True)

        label ch9_meeting_footjob:
        hide screen ch9_meeting_footjob
        $ quick_menu = True
        
        mc talk "\"Ahh..Hnnn...Hahhh...\""
        mc talk2 "\"I am getting close....\""
        "Aurora begins to move faster."
        $ quick_menu = False
        show screen ch9_meeting_footjob2
        $ renpy.show("ch9_meeting_footjob2")
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(12, hard=True)

        label ch9_meeting_footjob2:
        hide screen ch9_meeting_footjob2
        menu:
            "Cum":
                $ quick_menu = True
                scene ch9cumonfoot0
                with dissolve
                mc pleasure "\"Cumming!!~\""
                scene ch9cumonfoot0
                with flash
                scene ch9cumonfoot0
                with flash
                scene ch9cumonfoot
                with flash
                scene ch9cumonfoot
                with flash
                mc pleasure "\"Ahhhh...\""
                aur talk "\"Mmm.\""
                scene ch9cumonfoot2
                with vpunch
                "You see her lifting her foot and starting to lick the cum from it."
                "She slurps everything up."
                scene ch9meeting18
                with dissolve
                aur talk "\"That was delicious. I will save a sample for later.\""
                scene black
                with fadein
                "..."
                jump aftersexmeeting
    "Stop her":
        $ quick_menu = True
        scene ch9meeting21
        with dissolve
        mc talk2 "\"Thanks for this, but it's really not necessary.\""
        mc talk "\"We will take the extra resources that you can spare however.\""
        shp talk "\"Aww, disappointing. But it saves us time at least.\""
        shp talk "\"C'mon, put your boots back on, Aury. We are leaving.\""
        scene ch9meetingleavenosex
        with dissolve
        shp talk "\"We will leave the cargo with your android. Best of luck to you.\""
        mc talk "\"You too.\""
        scene ch9meetingleaveaftersex2
        with dissolve
        "And just like that they left."
        "..."
        scene black
        with fadein
        "After a few minutes you go back to your cabin along with Ruby..."
        jump ch9cabin


label ch9meetingjanecum:
mc nudepleasure2 "Ahh, almost there... what should I do?"
$ quick_menu = False
menu:
    "Cum inside":
        $ quick_menu = True
        mc nudepleasure "\"Ahhh~~ fuuck---\""
        scene ch9meetingvaginal
        with flash
        scene ch9meetingvaginal
        with flash
        scene ch9cumred
        with flash
        scene ch9cumred
        with flash
        mc nudepleasure "\"Ahhh~ MMm fuuck~~~\""
        scene ch9cumred2
        with flash
        "You pop your cock out of her cunt and a spray of cum follows out."
        shp nudetalk "\"I can feel your hot spunk in me.\""
        shp nudetalk "\"It will be nice to perform test on this. Aurora, save a sample.\""
        scene ch9cumblue
        with dissolve
        aur nudetalk "\"Ahhh~~ o-of course~\""
        scene black
        with fadein
        "They continue licking each other for a little while longer until they both cum and get up."
        "..."
        jump aftersexmeeting
        
    "Pull out":
        $ quick_menu = True
        mc nudepleasure "Maybe use Aurora's pretty holes?"
        mc nudepleasure "\"Aurora, let me cum inside you!\""
        scene ch9cumblue2
        with flash
        "She moves her butt your way and exposes it with one hand."
        mc nudepleasure "\"Ahhh.\""
        $ quick_menu = False
        menu:
            "Cum inside her ass":
                $ quick_menu = True
                scene ch9cumblue2
                with flash
                mc nudepleasure2 "\"Cumming~!\""
                scene ch9cumblue2
                with flash
                scene ch9meetingcuminblueass
                with flash
                scene ch9meetingcuminblueass
                with flash
                aur nudetalk "\"Ahhhh~~\""
                scene ch9meetingcuminblueass2
                with dissolve
                shp nudetalk "\"Mmhhh~ *Slurp* *Gulp* Hahh~\""
                shp nudetalk "\"*Slurp* Ahhh *Slurp*\""
                "You can see Karin eating Aurora's ass with all the cum you just sprayed inside her."
                "She eats her ass thoroughly and doesn't let a single drop slip her tongue."
                scene black
                with fadein
                "..."
                jump aftersexmeeting
            "Cum inside her pussy":
                $ quick_menu = True
                scene ch9cumblue2
                with flash
                mc nudepleasure2 "\"Cumming~!\""
                scene ch9cumblue2
                with flash
                scene ch9meetingcuminbluepussy
                with flash
                scene ch9meetingcuminbluepussy
                with flash
                aur nudetalk "\"Mmmm..\""
                scene ch9cumblue
                with vpunch
                aur nudetalk "\"Ahh,haah,,,mmhhh.\""
                aur nudetalk "\"Eat it all~\""
                shp nudetalk "\"Mmhhh~ *Slurp* *Gulp* Hahh~\""
                scene ch9meetingcuminbluepussy2
                with dissolve
                "You hear the slurping sounds coming from Karin..."
                "You can only imagine she is eating the cum you just sprayed inside Aurora."
                scene black
                with fadein
                "..."
                jump aftersexmeeting


label aftersexmeeting:
scene black
with fadein
"After cleaning up they move to the exit."
scene ch9meetingleaveaftersex
with fasterfadein
aur talk "\"Bye, bye! It was fun!\""
mc talk "\"It sure was. Thank you too.\""
scene ch9meetingleaveaftersex2
with dissolve
"And just like that they were gone..."
"You had a pretty good time at the very least."
scene black
with fadein
"After a few minutes you go back to your cabin along with Ruby..."
jump ch9cabin

label ch9cabin:
scene ch9roomrubytalk
with fasterfadein
r ttalk "\"They did leave the resources just as they had promised and the coordinates to a habitable world.\""
mc talk "\"That's really good news. Finally something turns right and we get something our way.\""
r ttalk2 "\"But...\""
mc talk2 "\"But?\""
r ttalk "\"To reach that planet it will take approximately 200 years.\""
mc talk "\"Oh...\""
r ttalk2 "\"But we could use the cryo chambers.\""
mc talk2 "\"We have those here? Enough for everyone?\""
r ttalk "\"Yes.\""
mc talk3 "\"Then that's what we are going to do.\""
r ttalk2 "\"Understood. I will make preparations and let you know once I check them for any defects.\""
mc talk2 "\"Got it. I will be taking a quick rest.\""

scene ch9roomwalking
with dissolve
"Ruby leaves and you head inside your cabin."

scene ch9roomlaying
with fasterfadein
"You undress and sit down to rest for a bit."
"You stare at your destroyed home planet and can't help but feel depression, but at the same time hope."
"After given such a position. You are glad your family is here with you, so it doesn't hurt as much, but it's still as shitty as it gets."
scene ch9roomsleep
with fasterfadein
"After some more thoughts you slowly drift off to sleep..."
scene black
with fadein

if accept_dahlia_visit:
    $ quick_menu = False
    menu:
        "Wake up":
            $ quick_menu = True
            "You slowly wake up as you feel shifting around your bed happen."
            jump ch9wakeup
        
else:
    jump endofch9


label ch9wakeup:
$ quick_menu = False
menu:
    "Open eyes":
        $ quick_menu = True
        scene ch9roomwakingup2
        with fasterfadein
        "You slowly open your eyes."
        jump ch9wakeup2

label ch9wakeup2:
scene ch9roomwakingup
with fasterfadein
"After you open your eyes you just stare and enjoy the view presented in front of you."
mc nudethinking "One of the best things to see after waking up for sure."
mc nudetalk "\"Hey, Dahlia.\""
scene ch9roomdahliatalks
with dissolve
d surprised "\"Oh... hey, [mc]\""
d talk "\"I am sorry... did I wake you up?\""
mc nudetalk2 "\"No,no,no. Don't worry about it.\""
"You can almost see tears in her eyes. I guess she got emotional looking at the Earth... or what's left of it."
mc nudetalk2 "\"You okay?\""
scene ch9roomdahliatalks2
with dissolve
d talk "\"It's just crazy... you know? The thing you've always known has always been there and then one day *puff* -- it's gone.\""
d talk "\"Just like that...\""
scene ch9roomdahliatalks3
with dissolve
mc nudetalk3 "\"I know... it's crazy.\""
d talk2 "\"After my home world's destruction and coming to Earth and being able to somewhat fit in just to have it destroyed... it's not fair.\""
mc nudetalk2 "\"The good news is that we managed to find a possible habitable world that we will make our way to... in 200 years or so with the cryo chambers...\""
d talk "\"I heard from Ruby. I doubt it can ever replace the hole Earth left in our hearts, but we need to survive somehow.\""
mc nudetalk "\"Indeed.\""
scene ch9roomremovetrunks
with vpunch
"She turns around and starts removing your underwear."
d talk "\"Anyway, I came for a different reason, not just to feel sad about it.\""
d talk2 "\"Hopefully you can help with that.\""
mc nudetalk "\"I think I am up for the task.\""
scene ch9roomremovetrunks2
with vpunch
"She removes the underwear in one fell swoop."
d talk "\"Good. Because I really want to please you.\""
scene ch9roomhandjob
with dissolve
"She grabs your cock with her gentle, but firm hands."

$ quick_menu = False
show screen ch9_room_hj
$ renpy.show("ch9_room_hj")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label ch9_room_hj:
hide screen ch9_room_hj

$ quick_menu = True
mc nudepleasure "\"Mmmmm...\""
mc nudepleasure "\"That's it...\""
$ quick_menu = False
show screen ch9_room_hj2
$ renpy.show("ch9_room_hj2")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label ch9_room_hj2:
hide screen ch9_room_hj2

$ quick_menu = True
mc nudepleasure "Her hands are like heaven..."
$ quick_menu = False
menu:
    "Cum":
        $ quick_menu = True
        mc nudepleasure "\"Ahhhh---\""
        scene ch9roomhandjobcum1
        with flash
        scene ch9roomhandjobcum1
        with flash
        scene ch9roomhandjobcum1
        with flash
        scene ch9roomhandjobcum2
        with flash
        "You cum and make a mess on yourself."
        mc nudetalk "\"Shit, sorry.\""
        d talk "\"Hey, it's fine. Would've loved for you to have lasted longer, but as long as you felt good that is enough for me.\""
        scene ch9roomboots
        with fasterfadein
        "After cleaning up and talking a bit more, Dahlia puts her boots back on and leaves the room."
        scene ch9roomsleep
        with dissolve
        "A few minutes later you fall asleep again..."
        scene black
        with fasterfadein
        jump endofch9
    "Hold it":
        $ quick_menu = True
        mc nudepleasure "Ah... I should try and hold it..."
        jump ch9roomrub

label ch9roomrub:
scene ch9roomrubpussy
with vpunch
"After a few more moments she shifts gears and gets on top of you..."
"Rubbing your dick, but this time with her clit."

$ quick_menu = False
show screen ch9_room_rub
$ renpy.show("ch9_room_rub")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label ch9_room_rub:
hide screen ch9_room_rub
$ quick_menu = True

mc nudepleasure "\"Ah fuck... this is too good...\""

$ quick_menu = False

menu:
    "Cum":
        $ quick_menu = True
        mc nudepleasure "\"Shiiii---\""
        scene ch9rubcum
        with flash
        scene ch9rubcum
        with flash
        scene ch9rubcum
        with flash
        scene ch9rubcum2
        with flash
        "You cum and splash yourself with your own semen."
        mc nudetalk "\"Crap... sorry.\""
        d talk "\"Hey, it's fine. Would've loved for you to have lasted longer, but as long as you felt good that is enough for me.\""
        scene ch9roomboots
        with fasterfadein
        "After cleaning up and talking a bit more, Dahlia puts her boots back on and leaves the room."
        scene ch9roomsleep
        with dissolve
        "A few minutes later you fall asleep again..."
        scene black
        with fasterfadein
        jump endofch9
        
    "Hold it":
        $ quick_menu = True
        mc nudepleasure "Need to hold it ..."
        jump ch9roomvag

label ch9roomvag:
$ch9_cum_inside_dahlia = True
scene ch9roomplacingdick
with vpunch
"After a few more moments Dahlia gets up and moves her panties a little to the side and she places your cock on top of her cunt."
"You can instantly feel her wetness..."
scene ch9roomvag
with flash
"You enter her and feel a bliss of pleasure flow through you."

$ quick_menu = False
show screen ch9_room_vag2
$ renpy.show("ch9_room_vag2")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label ch9_room_vag2:
hide screen ch9_room_vag2
$ quick_menu = True
"She then speeds up her movements..."

$ quick_menu = False
show screen ch9_room_vag
$ renpy.show("ch9_room_vag")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label ch9_room_vag:
hide screen ch9_room_vag
$ quick_menu = True
mc nudepleasure "\"Ahh... getting close...\""

d pleasure "\"Cum~!\""
d pleasure "\"Hahh.. Cum inside me!\""
$ quick_menu = False

menu:
    "Cum inside her":
        $ quick_menu = True
        $ ch9_dahlia_cum_inside = True
        scene ch9vagcum
        with dissolve
        "Unable to think straight anymore you pour her cunt full of semen."
        scene ch9vagcum2
        with flash
        scene ch9vagcum2
        with flash
        scene ch9vagcum2
        with flash
        mc nudetalk "\"Oh man... this was amazing.\""
        d talk "\"I concur. It feels so hot inside me right now.\""
        mc nudetalk2 "\"Was it okay to do it inside you like that?\""
        d talk2 "\"I mean... yeah. It's not a safe day, but don't worry. If I get pregnant I will take care of the child.\""
        "Her words shock you. Becoming a father might be the last thing you want right now given the circumstances, but then again..."
        "The species must continue somehow so reproducing is important."
        scene ch9roomboots
        with fasterfadein
        "After cleaning up and talking a bit more, Dahlia puts her boots back on and leaves the room."
        scene ch9roomsleep
        with dissolve
        "A few minutes later you fall asleep again..."
        scene black
        with fasterfadein
        jump endofch9

label endofch9:
with fadein

jump startch10
