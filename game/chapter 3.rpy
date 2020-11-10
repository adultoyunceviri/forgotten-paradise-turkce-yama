label startof03:

with fasterfadein
scene thenextday
$ quick_menu = False
pause 2.5
with fasterfadeout

scene goingtolunch
with fasterfadein
$ quick_menu = True
mc thinking "I should look out for Jack and follow him to find out where he keeps that girl locked."
mc thinking "His usual routine is in a bit from now, so I have time to get some lunch."

scene elysebreakfasteating
with fadein
mc thinking "Elyse! I should see how she is doing."

scene elysebreakfast0x
with dissolve
mc talk "\"Hey, Elyse. Good afternoon.\""
e nudetalk "\"Hi. Going to eat as well?\""
mc talk2 "\"Yeah. Do you mind if I join you?\""
e nudetalk "\"Feel free.\""

show elysebreakfast1
with dissolve
mc talk2 "\"So, you like it up here so far?\""

scene elysebreakfast2
with dissolve
e nudetalk "\"It's alright. But I feel like I am missing something, but I can't really tell what...\""
mc talk "\"Perhaps home?\""
e nudetalk2 "\"I don't know....\""
mc thinking "She should eventually recover her memories... right?... That's what that old man said anyway..."
e nudetalk "\"What about you?\""
mc talk "\"Me?\""
mc thinking "\"Hm...\""
mc talk "\"Not sure honestly\""
e nudetalk "\"Oh, come on!\""
e nudetalk2 "\"Ok then, what is something you wish you had, but don't?\""
mc talk "\"What kind of question is that, haha.\""
e nudetalk "\"Come on, you asked me and it's only fair you answer my question now.\""
mc talk3 "\"Sigh, I don't know...Probably daughters...\""
mc shocked "Shit. I shouldn't have said that."
mc shocked "What if she gets her memories back and remembers this conversation?..."
mc shocked "Her memories from before still know me as her father even though I am not..."
e nudetalk2 "\"Daughters, hmm?\""
e nudetalk "\"What would you name them?\""
mc shocked "Fuck."
mc thinking "I have to lie."
mc talk "\"Ana and Tania.\""
e nudetalk "\"Oh, nice names.\""
mc thinking "These are the names I would've given them if my wife didn't insist on picking both..."
scene black
with dissolve
"You decide it's best to change the subject and talk about different stuff..."
scene elysebreakfast4
with dissolve
mc talk "\"So, what are your plans today?\""
e nudetalk "\"There isn't much to do here, but I always enjoy using the jacuzzi. So I will probably be doing that.\""
mc talk2 "\"Oh that sounds like fun. I haven't actually tried it out yet.\""
e nudetalk2 "\"Whaaat? You haven't? You should totally join me then.\""
mc talk "\"Haha. I might just accept your invitation.\""

scene elysebreakfast3
with dissolve
"Out of the corner of your eye, you spot him -- Jack!"

scene elysebreakfast5
with fadein
e nudetalk "\"Great! I will wait for you in about an hour from now, not that time actually matters anymore, but that's around the time I usually go.\""
mc talk2 "\"Sounds good, Elyse.\""

mc talk2 "\"Nice talking with you Elyse, but I have something to do real quick. I hope to catch up with you later.\""
e nudetalk2 "\"Oh, sure. See you.\""
scene black
with dissolve
"You quickly get up so you don't miss him."
scene jackcell1
with dissolve
"You follow him deep down through the ship in a secluded area you didn't even know existed."
scene jackbeforecell1
with dissolve
"He eventually stops at a door to enter a code and you know the door will automatically close behind him..."
#menu to use invis pill here if you have it

if invisibility_pill:
    $ quick_menu = False
    menu:
        "Take invisibility pill":
            $ quick_menu = True
            $ watched_lexa = True
            scene eating invis pill 1
            with dissolve
            mc thinking "No better chance to take this than now I guess."
            scene eating invis pill 2
            $ renpy.pause(1.5, hard=True)
            $ renpy.transition(Dissolve(0.1800))
            scene cell invis 3
            $ renpy.pause(1.5, hard=True)
            $ renpy.transition(Dissolve(0.1800))
            scene cell invis 4
            $ renpy.pause(1.1, hard=True)
            $ renpy.transition(Dissolve(0.1800))
            scene cell invis 2
            with dissolve
            mc "This actually worked... !!"
            mc "I have to remove my clothes and follow him quick before the door closes behind him."
            scene jackbeforecell5
            $ renpy.pause(1.1, hard=True)
            $ renpy.transition(Dissolve(0.1800))
            scene jackbeforecell6
            $ renpy.pause(1.1, hard=True)
            $ renpy.transition(Dissolve(0.1800))
            jump lexacell1
        "Don't (skip voyeur)":
            $ quick_menu = True
            $ watched_lexa = False
            scene eating invis pill 3
            with dissolve
            mc thinking "I don't want to bet my luck on this and get caught... I will find another way."
            jump didntfollowjack
        
else:
    $ watched_lexa = False
    "If I took that invisiblity pill yesterday I would've been fine to go in, but now I can't and have to find another way... I can't let him spot me."
    jump didntfollowjack
    
    
    
    
    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Jack interrogation part----------------------------------------------------------------------------------------------------------------------------------------------


label lexacell1:
"You follow him in and as you enter the room you spot the girl..."
$ quick_menu = False
scene lexa portrait with fade:
    subpixel True
    yalign 1.0
    pause 2.0
    linear 7.0 yalign 0.0
pause

$ quick_menu = True

mc "So this is where he keeps her..."
scene jackenterslexacell00
with dissolve
"You walk in the corner of the room to observe."
jack talk "\"Did you sleep well, Lexa?\""
l closedeyes "\"...\""
jack laugh "\"Hahaha. Still refusing to communicate, are we?\""
jack angry "\"All I got was your name, so if you are unwilling to say anything for weeks, then you are little to no use to me.\""
scene jackenterslexacell01
with dissolve
jack talk "\"Wakey, wakey!\""
jack stare "\"Maybe I can at least have some fun with you...\""
l pain "\"Hahh..\""
jack talk "\"Already wet?\""
jack talk2 "\"You sure are a bitch in heat aren't you?\""
mc "Fuck..... I have to find a way to set her free..."
jack angry "\"Remember how rude you were to me in the meeting?\""
jack laugh "\"Not so rude now, are we?\""

$ quick_menu = False
show screen jack_fucks_lexa_0
$ renpy.show("jack_fucks_lexa_0")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label jackfuckslexa0:
hide screen jack_fucks_lexa_0
scene jacklickslexa1
with dissolve

$ quick_menu = True
jack stare "\"You have a very nice taste.\""
jack talk "\"It's making me horny just thinking about it.\""
"Jack removes his pants and starts pounding her front..."

$ quick_menu = False
show screen jack_fucks_lexa_1
$ renpy.show("jack_fucks_lexa_1")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label jackfuckslexa1:
hide screen jack_fucks_lexa_1
$ quick_menu = True
jack talk2 "\"You are a real good and tight fuck, but I am not done yet.\""

scene jackunhookslexa
with dissolve
"Jack reaches for the top to unhook her."

"And bends her over on the table..."
scene lexa portrait 2 with fade:
    subpixel True
    yalign 1.0
    pause 2.0
    linear 7.0 yalign 0.0
pause

jack talk "\"Now I am going to fuck your brains out.\""


$ quick_menu = False
show screen jack_fucks_lexa_2
$ renpy.show("jack_fucks_lexa_2")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label jackfuckslexa2:
hide screen jack_fucks_lexa_2
$ quick_menu = True
jack angry2 "\"I am getting close, bitch...\""
jack angry2 "\"Take it deep in you!!!\""
scene 02 jack fucks lexa11
with flash
scene 02 jack fucks lexa11
with flash
scene 02 jack fucks lexa11
with flash


"Jack splatters her insides with gallons of his cum..."

jack angry2 "\"Ah, that was nice.\""
jack angry2 "\"You are a good fuck toy.\""
jack angry "\"I will continue to enjoy myself with you until you start talking.\""
$ quick_menu = False
scene lexa portrait 3 with fade:
    subpixel True
    yalign 1.0
    pause 2.0
    linear 7.0 yalign 0.0
pause
$ quick_menu = True
mc "I think I've seen enough... I have to leave before this pill loses it's effect and I end up in a room with a person who is 3 times my size."
mc "I have to be smart and find a way to unlock this door..."
jump followedjack

scene black
with dissolve
"You make your escape and dress back up on the way out..."

jump chloec1
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Chloe part-----------------------------------------------------------------------------------------------------------------------------------------------------------------
label didntfollowjack:
scene black
with dissolve
"You walk back thinking what Jack is doing with her and how the hell you will get in..."

mc unhappy "These people can't get away with this. They ruined my life and I am stuck here pretending to be a clueless lab rat."

mc thinking "Perhaps I should pay a visit to Melisa soon and see if I can make her cooperate somehow."

jump chloec1

label followedjack:
scene black
with dissolve
mc thinking "It seems the effect of the pill ended just in time..."

mc shocked "I can't believe what I witnessed... I have to find a way to get in there again and release her."

mc unhappy "These people can't get away with this. They ruined my life and I am stuck here pretending to be a clueless lab rat."

mc thinking "Perhaps I should pay a visit to Melisa soon and see if I can make her cooperate somehow."

jump chloec1

label chloec1:
scene chloecitadel2
with dissolve
"As you walk back you see Chloe looking at Earth in deep thoughts..."

scene chloecitadel1
$ renpy.pause(1.5, hard=True)
$ renpy.transition(Dissolve(0.2300))
mc thinking "I should probably say hello."

scene chloecitadel3
with dissolve

mc talk "\"Hey, can I join you?\""
chloe talk2 "\"Sure, I don't mind.\""
scene chloecitadel4
with dissolve
mc talk3 "\"Beautiful view.\""
chloe talk "\"It would've been hella beautiful if I had something left for me there.\""
mc talk3 "\"Oh?\""
mc talk2 "\"I remember during the meeting that Jack mentioned you survived a devastating storm of some sort?\""
chloe talk "\"Yeah, that place took everyone I loved away from me anyway... Even before the storm.\""
chloe talk2 "\"So fuck it. I am starting fresh and with the money this trip provides I will be able to move on.\""
mc talk3 "\"That's good at least.\""
chloe talk "\"I just have to survive this place as well.\""
mc talk "\"What do you mean?\""
chloe talk2x "\"Everyone is super stuck-up and I can't find a good pal to release some tension either.\""
mc talk2 "\"You mean...\""
chloe talk2 "\"Fucking.\""
mc talk3 "\"Ohhhhh.\""
mc talk2 "\"Haha-ha... I see.\""
mc thinking "The conversation turned super awkward in no time."
$ quick_menu = False
menu:
    "Offer to help":
        $ quick_menu = True
        $ declined_chloe_sex = False
        mc thinking "Elyse will have to wait for me a little bit longer."
        mc talk3 "\"You know... I could help out with that.\""
        chloe talk "\"Well, fuck me... figuratively ... and literally. You actually have the balls.\""
        chloe talk2 "\"Why not? Follow me. I managed to get access to a room with a good view and a double bed.\""
        jump fuckchloe1
    
    "Don't":
        $ quick_menu = True
        $ chloe_spectate_talk = True
        $ declined_chloe_sex = True
        mc talk2 "\"I hope someone turns up eventually.\""
        chloe sigh "\"With those beta males on the ship I doubt it. No offense.\""
        chloe yummy2 "\"I might go for a girl though.\""
        mc talk "\"A girl, huh?\""
        chloe talk "\"I actually found a nice girl that I clicked with during the meeting when we first arrived.\""
        chloe talk2x "\"She is hella cute and I'd love to eat her out.\""
        mc talk "\"Uh-oh, sounds nice. Good luck.\""
        chloe yummy2 "\"No need for luck. No one can resist my charms.\""
        mc talk3 "\"Is that so?\""
        mc talk "\"How will I know if you really did it though?\""
        chloe talk2x "\"You can watch if you want, I don't care. I will let you know when I get on with her.\""
        mc talk3 "\"I will be expecting it!\""
        mc thinking "I don't want to be late for my meeting with Elyse... I should leave now."
        mc talk2 "\"Sorry, but I have to go now. See you later.\""
        chloe talk "\"Sure. Bye.\""
        jump elyseontime

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
#Chloe fuck part-----------------------------------------------------------------------------------------------------------------------------------------------------------------
label fuckchloe1:

scene chloeroom
with dissolve
"She grabbed your hand and led you to the room she was talking about."
chloe talk "\"So what do you think?\""
chloe talk2 "\"It's nothing big, but it will do the job pretty nicely.\""
mc talk3 "\"Wow. Wait...\""
mc talk2 "\"How did you get access to this room in the first place?\""
chloe talk "\"A good ninja never reveals their secret.\""
scene chloekiss1
with dissolve
mc talk "\"You are a ninja, huh?\""
chloe talk "\"Yes I am~\""
"Chloe leans in closer to kiss you."
scene chloekiss2
with dissolve
chloe kiss "\"Mmmmgh..\""
chloe yummy2 "\"Mmh.\""
chloe talk2x "\"You taste nice. Now fuck me.\""
chloe talk2x "\"I need this badly so let's get to it already.\""
mc talk3 "\"It will be my pleasure.\""
scene black
with dissolve
"You both quickly remove your clothes and she spreads her legs on the bed."
mc nudetalk "\"You ready?\""
chloe snyummy2 "\"Yes. Enough talk. Fuck me, now.\""

$ quick_menu = False
show screen mc_fucks_chloe
$ renpy.show("mc_fucks_chloe")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label mcfuckschloe:
hide screen mc_fucks_chloe
$ quick_menu = True
mc nudepleasure "\"Hahh..\""
mc nudepleasure "\"I am about to cum...\""
chloe snpleasure "\"Do it!\""

$ quick_menu = False
menu:
    "Cum inside":
        $ quick_menu = True
        $ chloe_spectate_talk = False
        mc nudepleasure "\"Ahhh!!\""
        $ cum_inside_chloe = True
        $ cum_outside_chloe = False
        jump chloecuminside

    "Cum outside":
        $ quick_menu = True
        $ chloe_spectate_talk = True
        $ cum_outside_chloe = True
        $ cum_inside_chloe = False
        jump chloecumoutside


label chloecuminside:
scene chloefuckcuminside1
with flash
scene chloefuckcuminside1
with flash
scene chloefuckcuminside1
with flash
mc nudepleasure "\"Fuck~!\""

scene chloefuckcuminside2
with dissolve
chloe snsigh "\"Are you serious!?\""
chloe snangry "\"Did you just cum inside me!?\""
mc nudetalk "\"Sorry...\""
chloe snangry "\"Fucking hell. What if I get pregnant, asshole? You are also old enough to be my dad.\""
chloe snangry "\"Fuck. Get out.\""
scene black
with dissolve
"You take your clothes and leave quickly before waiting for the situation to get even worse."
jump elyselate

    

label chloecumoutside:
scene chloefuckcumonbelly
with flash
scene chloefuckcumonbelly
with flash
scene chloefuckcumonbelly
with flash
mc nudepleasure "\"Fuck~!\""

scene chloefuckcumonbelly2
with dissolve

chloe snpleasure "\"MmMmMm...\""
chloe sntalk2 "\"Hot.\""
chloe sntalk2x "\"Needed a good fuck for a while.\""
mc nudetalk2 "\"Glad I was able to provide.\""
mc nudetalk "\"Let me know if you end up needing another one.\""
chloe sntalk "\"I will let you know, but I want to try and roll in some pussy juice too. There's some fine choices on the ship.\""
mc nudetalk2 "\"I wholeheartedly agree with you on that.\""
chloe sntalk "\"I actually found a nice girl that I clicked with during the meeting when we first arrived.\""
chloe sntalk2 "\"She is hella cute and I'd love to eat her out.\""
mc nudetalk "\"Uh-oh, sounds nice.\""
mc nudetalk "\"Any spectators allowed?\""
chloe sntalk2x "\"What? You wanna watch?\""
chloe snsigh "\"Old pervert.\""
chloe snyummy2 "\"I will let you know if I get it on with her.\""

mc nudetalk2 "\"Thanks, I gotta run now though.\""
chloe sntalk "\"Running to fuck another girl, are we?\""
mc nudetalk "\"Not really.\""
chloe sntalk2 "\"You're a bad liar. Go.\""
scene black
with dissolve
"You dress and leave for the jacuzzi."
jump elyselate


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#Elyse part-----------------------------------------------------------------------------------------------------------------------------------------------------------------
label elyseontime:
scene black
with dissolve
"You walk to the room where the jacuzzi is located, change your clothes and enter."

scene elysejacuzzi1
with fadein
"The first thing you see shocks you."
"You watch Elyse drinking heavily and bottles laying all around her."

scene elysejacuzzi2
with dissolve
mc nudeshocked "What are you doing Elyse?? God..."
mc nudethinking "I should go and try to salvage what I can..."

"You say hello and enter the jacuzzi."
scene elysejacuzzi3
with dissolve
mc nudetalk2 "\"Celebrating something?\""
e nudedrunktalk2 "\"Just relaxing a bit. Alcohol helps with that.\""
mc nudetalk3 "\"I didn't know you drink.\""
e nudeskeptical "\"How do you know what I do and don't do??\""
mc nudethinking "Ooops..."
mc nudetalk3 "\"I just don't see you as the type, that's all.\""
e nudejealous "\"Hmph. Well, I am the type. I do whatever I want.\""
e nudejealous "\"I don't need anyone to babysit me.\""
mc nudetalk2 "\"That's fine. I didn't mean it like that anyway.\""

scene black
with dissolve
"You talk for a bit to get the conversation back on track and try and get on her good side."
"And then the conversation takes an unexpected turn..."

scene elysejacuzzi3
with dissolve
e nudedrunktalk2 "\"So if you had your daughters selected for this trip would you let them go?\""
mc nudetalk "\"I mean... if they are 18 and over, sure. They are adults and I believe they can take care of themselves.\""
e nudedrunktalk3 "\"Even if it means they might get fucked or worse?\""
mc nudeshocked "\"What the...\""
mc nudeshocked "\"Of course not, if I know that beforehand...\""

scene elysejacuzzi4
with dissolve
"Elyse moves in closer."
e nudedrunktalk2 "\"You know [mc]... *hic* ... I feel like you understand me.\""
e nudedrunktalk3 "\"I feel like I can get closer to you...\""
mc nudethinking "Uhh.. I don't like where this is going..."
e nudedrunktalk2 "\"This god damn top is killing me...\""
e nudedrunktalk3 "\"I am taking it off...\""

scene elysejacuzzi5
with dissolve
e nudehappy "\"Much better.\""
mc nudeshocked "Oh...my...god..."
e nudekiss "\"I... need... to...\""
e nudekiss "\"kiss you...\""

"Elyse leans in closer for a kiss."
mc nudeshocked "What do I do? Oh god!"
mc nudeshocked "Do I let this happen? There is no turning back..."

$ quick_menu = False
menu:
    "Let it happen":
        $ quick_menu = True
        $ sex_with_elyse = True
        jump jacuzzi7
    "Stop her":
        $ quick_menu = True
        $ sex_with_elyse = False
        jump jacuzziend

label jacuzzi7:
scene elysejacuzzi6
with dissolve
"You don't fight and wait for whatever she is about to do..."
"She kisses you and shares her saliva with you."
"She keeps kissing you for what seems to be an eternity."

scene elysekiss3
with dissolve
"Until she finally breaks the kiss with a mouthful of saliva."
e nudekiss "\"Hahh...\""
e nudedrunktalk3 "\"Mhh..ahhh.\""
mc nudetalk "\"That was... wow...\""
e nudehappy "\"Yes, it was...\""

scene elysejacuzzi6x
with dissolve
"Elyse stands up and removes her bikini and spreads her legs..."
e nudedrunktalk2 "\"Now take me!\""
"You lost all rational thinking as blood rushes down to your lower body as you penetrate her."

$ quick_menu = False
show screen mc_fucks_elyse
$ renpy.show("mc_fucks_elyse")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label mcfuckselyse:
hide screen mc_fucks_elyse
scene jacuzzicum1
$ quick_menu = True
"You feel you are about to burst..."
mc nudepleasure "\"I am gonna cum...\""

scene jacuzzicum3
with dissolve
e nudepleasure "\"Ah..Hahh..Ah... Cum inside me! *Hic*\""
"Elyse crosses her legs around your waist making it harder to make a choice..."
mc nudepleasure "\"She is obviously drunk... Where should I do it?\""
$ quick_menu = False
menu:
    "Inside her":
        $ quick_menu = True
        $ cum_inside_elyse = True
        $ cum_outside_elyse = False
        scene elysecloseuppussy
        with dissolve
        mc nudepleasure "\"Ahh~\""
        mc nudepleasure "\"Cumming!!\""
        $ came_inside_elyse = True
        $ came_outside_elyse = False
        scene jacuzzicum2
        with flash
        scene jacuzzicum2
        with flash
        scene jacuzzicum2
        with flash
        "Her legs were holding your waist and making the choice even harder than it needs to be..."
        scene jacuzzicuminside2
        with dissolve
        e nudedrunktalk3 "\"This was *hic* the best sex I've ever had *hic*\""
        mc nudethinking "I am scared to even ask the number..."
        e nudehappy "\"I win, ha-ha-ha....ha...\""
        scene jacuzzicuminside3
        with dissolve
        "Elyse passes out with cum still flowing out of her..."
        mc nudeshocked "She passed out? Great..."
        mc nudethinking "I have to clean her up and get her back to her room..."
        scene black
        with dissolve
        "You clean her, dress her back and pick her up."
        scene elysejacuzzi8
        with dissolve
        mc nudetalk "\"El, can you tell me where your room is located?\""
        mc nudetalk2 "\"El?\'"
        e nudedrunktalk3 "\"Uhh...\""
        e nudedrunktalk2 "\"AA106\""
        mc nudetalk2 "\"What Wing is that in?\""
        "You ask, but she passed out again."
        mc nudetalk "\"God damn it.\""
        
        scene black
        with dissolve
        "You carry her around until you eventually find the mentioned room..."
        jump enterelyseroom
    
    "Outside":
        $ quick_menu = True
        $ cum_inside_elyse = False
        $ cum_outside_elyse = True
        scene jacuzzicum1
        "You manage to pull her legs apart with a lot of will power..."
        mc nudepleasure "\"I am cumming~!\""
        e nudepleasure "\"Yesssssss~~\""
        scene jacuzzicumoutside1
        with flash
        scene jacuzzicumoutside1
        with flash
        scene jacuzzicumoutside1
        with flash
        $ renpy.pause(2.0, hard=True)
        $ renpy.transition(Dissolve(0.1800))
        scene jacuzzicumoutside2
        with dissolve
        e nudedrunktalk3 "\"You made a ... *hic* mess *hic*... out of me *hic* ...\""
        "Elyse says as she passes out."
        mc nudetalk "\"El? Elyse??\""
        mc nudethinking "\"Oh, man... I have to clean her up and get her back to her room...\""
        scene black
        with dissolve
        "You clean her, dress her back and pick her up."
        scene elysejacuzzi8
        with dissolve
        mc nudetalk "\"El, can you tell me where your room is located?\""
        mc nudetalk3 "\"El?\""
        e nudedrunktalk2 "\"Uhh...\""
        e nudedrunktalk3 "\"AA106\""
        mc nudetalk2 "\"What Wing is that in?\""
        "You ask, but she passed out again."
        mc nudetalk "\"God damn it.\""
        
        scene black
        with dissolve
        "You carry her around until you eventually find the mentioned room..."
        jump enterelyseroom
        
label jacuzziend:
scene elysejacuzziangry
with dissolve
mc nudetalk2 "\"We can't do this, Elyse.\""
e nudesad "\"Why the *hic* hell not???\""
mc nudetalk "\"You're obviously drunk and this is not a rational choice. Let me take you back to your room.\""
e nudejealous "\"No. Go away. I can find my own way back *hic*.\""
"You feel like you shouldn't stir the fire more and decide to go back to your room."

scene black
with dissolve
jump nosexend
#--------------------------------------------------------------------------------------------------------------------------------



#Jacuzzi Late--------------------------------------------------------------------------------------------------------------------

label elyselate:
$ sex_with_elyse = False
"You walk to the room where the jacuzzi is located, change your clothes and enter."

scene elysejacuzzi7
with dissolve
"You are shocked the moment you enter..."
"Finding Elyse with head down and beer bottle in hand..."
mc nudeshocked "What the..."
mc nudeshocked "How much did you drink Elyse??"
mc nudeshocked "Perhaps if I didn't fool around with Chloe I would've made it in time before she got this much wasted..."
mc nudethinking "I should pick her up and carry her to her room."

scene elysejacuzzi8
with dissolve
$ renpy.pause(1, hard=True)
$ renpy.transition(Dissolve(0.1800))
e nudedrunktalk3 "\"*Hic*\""
e nudedrunktalk2 "\"You cam--e... *hic*\""
mc nudetalk3 "\"Yes... a little bit late.\""
e nudedrunktalk3 "\"It's okaaaaaaay~\""
e nudehappy "\"Let's partyyyyyy!\""
e nudedrunktalk2 "\"*Hic*\""
scene black
with dissolve
mc nudetalk3 "\"Some other time, let's get you to bed first...\""
mc nudetalk2 "\"Where is your room located?\""
e nudedrunktalk3 "\"Mhhh... Wing C, *hic* room number AA106\""
jump enterelyseroom










#-----------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------------

label elyselate2:
"You walk to the room where the jacuzzi is located, change your clothes and enter."

scene elysejacuzzi7
with dissolve
"You are shocked the moment you enter..."
"Finding Elyse with head down and beer bottle in hand..."
mc nudeshocked "What the..."
mc nudeshocked "How much did you drink Elyse??"
mc nudeshocked "Perhaps if I didn't fool around with Chloe I would've made it in time before she got this much wasted..."
mc nudethinking "I should pick her up and carry her to her room."

scene elysejacuzzi8
with dissolve
$ renpy.pause(1, hard=True)
$ renpy.transition(Dissolve(0.1800))
e nudedrunktalk3 "\"*Hic*\""
e nudedrunktalk2 "\"You cam--e... *hic*\""
mc nudetalk3 "\"Yes... a little bit late.\""
e nudedrunktalk3 "\"It's okaaaaaaay~\""
e nudehappy "\"Let's partyyyyyy!\""
e nudedrunktalk2 "\"*Hic*\""
scene black
with dissolve
mc nudetalk3 "\"Some other time, let's get you to bed first...\""
mc nudetalk2 "\"Where is your room located?\""
e nudedrunktalk3 "\"Mhhh... Wing C, *hic* room number AA106\""
jump enterelyseroom

#-----------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------------






#Elyse room-------------------------------------------------------------------------------------------------------------------------------

label enterelyseroom:
    
scene black
with dissolve

"As you enter her room you get shocked yet again..."

scene elyseroom0x
with fadein
z pleasedbb "\"Hmm, is that so?\""
scene elyseroom0xx
with dissolve
"beep-boop-beep"
z talk2bb "\"What is it?\""
z talkbb "\"Oh my god!\""
scene elyseroom1
with dissolve
z talk2bb "\"What happened?\""
mc nudethinking "Zoey and Elyse are placed in the same room... really?!"
scene elyseroom2
with dissolve
mc nudetalk3 "\"She drank a little bit too much. She is okay though.\""
mc nudetalk2 "\"Just need to sleep it off.\""
mc nudetalk "\"Which bed is hers?\""
z talkbb "\"The top one.\""

scene elyseroom3
with dissolve
"You place her gently on the top bed."
mc nudetalk "\"Rest well, El.\""
scene elyseroom4
with dissolve
z desirebb "\"Where did you find her?\""

if sex_with_elyse:
    
    mc nudetalk2 "\"We had a meeting at the jacuzzi, but when I got there she was already pretty drunk.\""
    z flirtingbb  "\"So did you fuck her?\""
    mc nudeshocked "\"What??\""
    z desirebb "\"It's a pretty simple question. Did you fuck her?\""
    
    $ quick_menu = False
    
    menu:
        "Yes":
            $ quick_menu = True
            mc nudethinking "I can't believe I am going to share this with her..."
            mc nudetalk3 "\"Yes, I did.\""
            jump nozoeysex
        "No (lie)":
            $ quick_menu = True
            mc nudetalk2 "\"Um, no. She tried to do something, but I refused.\""
            jump zoeysexlied


else:
    mc nudetalk2 "\"We had a meeting at the jacuzzi, but I was a bit late and when I got there she was already passed out.\""
    z talkbb "\"So you didn't get to fuck her?\""
    mc nudeshocked "\"What? No!\""
    z talk2bb "\"Hmm. I see.\""
    z flirtingbb "\"I am asking because we had a little friendly bet as to who will be able to sleep with someone else before the other one does.\""
    z happybb "\"So I'd figured you'd take an advantage from that siutation.\""
    mc nudeshocked "\"What kind of bet is that??\""
    z talk2bb "\"Eh, it's really not that big of a deal.\""
    z winkbb "\"So you wanna help me win that bet?\""
    mc nudeshocked "\"What!?\""
    z flirtingbb "\"You didn't hear me? Do.You.Want.To.Fuck.Me?\""
    jump zoeysex



#-----------------------------------------------------------------------------------------------------------------

label nozoeysex:
z talk2bb "\"I see. So she won our little bet then. Damn.\""
mc nudetalk "\"What bet?\""
z winkbb "\"Oh we just had a bet as to who will get to fuck someone else faster. I was positive she wouldn't pull it off being reserved and all, but I guess alcohol helps with that.\""
mc nudetalk2 "\"Hmm, well she didn't give me much choice and jumped straight on me.\""
z happybb "\"Yeah, I'd bet.\""
z talk2bb "\"Anyways, thank you for bringing her.\""
mc nudetalk "\"Of course. Anytime.\""
scene black
with dissolve
"You leave with all kind of questions in your mind..."
jump onlyelyseend

#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------

label zoeysex:
$ quick_menu = False
menu:
    "Unable to respond":
        $ quick_menu = True
        $ mc_zoey_sex = True
        "You freeze straight up without being able to respond as to what you just heard."
        z talkbb "\"I will take your silence as a yes.\""
        jump zoeychloesex2
    

    "No":
        $ quick_menu = True
        $ mc_zoey_sex = False
        mc nudetalk3 "\"I am sorry Zoey, but I can't do that. You deserve someone special and that is not me.\""
        z talk2bb "\"How do you know what I deserve and what I don't?!\""
        z talkbb "\"I guess there are more gays on the ship than I thought. Shame.\""
        z talk2bb "\"Thanks for bringing her back, but I need to be alone now. Please leave.\""
        scene black
        with dissolve
        "You leave with all kind of questions in your mind..."
        "Does Zoey hate you now?"
        jump onlychloeend

#-----------------------------------------------------------------------------------------------------------------

label zoeysexlied:
z talk2bb "\"Hmm. I see.\""
z talkbb "\"I guess she gambled too much on that alcohol to help her win the bet.\""
mc nudetalk3 "\"What bet??\""
z flirtingbb "\"Oh, we just had a friendly bet as to who will get to fuck someone else first.\""
mc nudeshocked "\"What kind of bet is that!?\""
z talk2bb "\"Eh, it's not that big of a deal.\""
z winkbb "\"So you wanna help me win that bet?\""
mc nudeshocked "\"What!?\""
z flirtingbb "\"You didn't hear me? Do.You.Want.To.Fuck.Me?\""
$ quick_menu = False
menu:
    "Unable to respond":
        $ quick_menu = True
        $ mc_zoey_sex = True
        "You freeze straight up without being able to respond as to what you just heard."
        z nudetalk "\"I will take your silence as a yes.\""
        jump zoeysexlied2
    

    "No":
        $ quick_menu = True
        $ mc_zoey_sex = False
        mc nudetalk3 "\"I am sorry Zoey, but I can't do that. You deserve someone special and that is not me.\""
        z nudetalk2 "\"How do you know what I deserve and what I don't?!\""
        z nudetalk "\"I guess there are more gays on the ship than I thought. Shame.\""
        z nudetalk2 "\"Thanks for bringing her back, but I need to be alone now. Please leave.\""
        scene black
        with dissolve
        "You leave with all kind of questions in your mind..."
        "Does Zoey hate you now?"
        jump onlyelyseend


#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------

label zoeychloesex2:

scene elyseroom4x
with dissolve
"Before you even realize she started taking her clothes off and quickly pulled down your shorts too."
"One thing led to another and you were both on the bed and you just let it happen..."

scene elyseroomfuckingzoey1
with dissolve
"You were both were feeling great pleasure."
"You couldn't believe just how tight she was."

$ quick_menu = False
show screen mc_fucks_zoey
$ renpy.show("mc_fucks_zoey")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label mcfuckszoey:
hide screen mc_fucks_zoey

$ quick_menu = True
"You just stared at her perky tities and big blue eyes as she bounced up and down on your cock."
scene zoeycumming1
with dissolve

"You pushed her down and continued to pound her pussy for a couple more minutes until you started to feel yourself getting close..."
mc nudetalk "\"Ahh... I am getting close.\""
z nudepleasure "\"Cum wherever you want~~\""
mc nudepleasure "\"Hnng....\""
$ quick_menu = False
menu:
    "Cum inside":
        $ quick_menu = True
        $ zoey_cum_inside = True
        $ zoey_cum_outside = False
        scene zoeycuminside1
        with dissolve
        mc nudepleasure "\"Hahh...Hnn..Ahh..\""
        mc nudepleasure "\"Cumming!\""
        "You let yourself go as you let jet of cum flow deep inside of her..."
        scene zoeycuminside2
        with flash
        scene zoeycuminside2
        with flash
        scene zoeycuminside2
        with flash
        scene zoeycuminside2
        $ renpy.pause(2.8, hard=True)
        $ renpy.transition(Dissolve(0.1800))
        scene zoeycuminside3
        with dissolve
        "As you take out your member, your cum starts leaking from her pussy..."
        "You notice a mixture of blood and cum and realize she was a virgin until now..."
        "You decide to keep quiet about it as if you haven't noticed it..."
        scene zoeycuminside4
        with dissolve
        z nudepleasure "\"Mhhh~\""
        z nudehappy "\"I guess that means I win the bet~!\""
        mc nudetalk "\"Ah-ha. Congratulations I guess.\""
        z nudeflirting "\"Thanks for doing this with me.\""
        mc nudetalk2 "\"You're welcome... I guess...\""
        scene black
        with dissolve
        "You say goodbye to her as you get up and leave when guilt hits you hard."
        mc nudethinking "What is wrong with me? Did I really just do that... I must be losing my mind..."
        jump zoeychloeend
        
    "Cum outside":
        $ quick_menu = True
        $ zoey_cum_inside = False
        $ zoey_cum_outside = True
        scene zoeycumoutside1
        with dissolve
        mc nudepleasure "\"Hahh...Hnn..Ahh..\""
        mc nudepleasure "\"Cumming!\""
        "You quickly take out your member from her vagina and let a stream of cum out..."
        scene zoeycumoutside2
        with flash
        scene zoeycumoutside2
        with flash
        scene zoeycumoutside2
        with flash
        $ renpy.pause(2.0, hard=True)
        $ renpy.transition(Dissolve(0.1800))
        scene zoeycumoutside3
        with dissolve
        "Your cum covers her belly and all the way to the top of her breasts."
        z nudepleasure "\"Mhhh~\""
        z nudehappy "\"I guess this is proof that I win the bet~!\""
        mc nudetalk "\"Ah-ha. Congratulations I guess.\""
        z nudeflirting "\"Thanks for doing this with me.\""
        mc nudetalk2 "\"You're welcome... I guess...\""
        scene black
        with dissolve
        "You say goodbye to her as you get up and leave when guilt hits you hard."
        mc nudethinking "What is wrong with me? Did I really just do that... I must be losing my mind..."
        jump zoeychloeend
#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------

label zoeysexlied2:

scene elyseroom4x
with dissolve
"Before you even realize she started taking her clothes off and quickly pulled down your shorts too."
"One thing led to another and you were both on the bed and you just let it happen..."
"You couldn't help yourself for some reason... it was as if you were possessed."

scene elyseroomfuckingzoey1
with dissolve
"You were both were feeling great pleasure."
"You couldn't believe just how tight she was."

$ quick_menu = False
show screen mc_fucks_zoeylie
$ renpy.show("mc_fucks_zoeylie")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label mcfuckszoeylie:
hide screen mc_fucks_zoeylie

$ quick_menu = True
"You just stared at her perky tities and big blue eyes as she bounced up and down on your cock."
scene zoeycumming1
with dissolve

"You pushed her down and continued to pound her pussy for a couple more minutes until you started to feel yourself getting close..."
mc nudetalk "\"Ahh... I am getting close.\""
z nudeflirting "\"Cum wherever you want~~\""
mc nudepleasure "\"Hnng....\""
$ quick_menu = False
menu:
    "Cum inside":
        $ quick_menu = True
        $ zoey_cum_inside = True
        $ zoey_cum_outside = False
        scene zoeycuminside1
        with dissolve
        mc nudepleasure "\"Hahh...Hnn..Ahh..\""
        mc nudepleasure "\"Cumming!\""
        scene zoeycuminside2
        with flash
        scene zoeycuminside2
        with flash
        scene zoeycuminside2
        with flash
        $ renpy.pause(2.8, hard=True)
        $ renpy.transition(Dissolve(0.1800))
        scene zoeycuminside3
        with dissolve
        "As you take out your member, your cum starts leaking from her pussy..."
        "You notice a mixture of blood and cum and realize she was a virgin until now..."
        "You decide to keep quiet about it as if you haven't noticed it..."
        scene zoeycuminside4
        with dissolve
        z nudetalk2 "\"Mhhh~\""
        z nudetalk "\"I guess that means I win the bet~!\""
        mc nudetalk "\"Ah-ha. Congratulations I guess.\""
        z nudetalk2 "\"Thanks for doing this with me.\""
        mc nudetalk2 "\"You're welcome... I guess...\""
        scene black
        with dissolve
        "You say goodbye to her as you get up and leave when guilt hits you hard."
        mc nudethinking "What is wrong with me? Did I really just do that...I must be losing my mind..."
        jump elysezoeyend
        
    "Cum outside":
        $ quick_menu = True
        $ zoey_cum_inside = False
        $ zoey_cum_outside = True
        scene zoeycumoutside1
        with dissolve
        mc nudepleasure "\"Hahh...Hnn..Ahh..\""
        mc nudepleasure "\"Cumming!\""
        "You quickly take out your member from her vagina and let a stream of cum out..."
        scene zoeycumoutside2
        with flash
        scene zoeycumoutside2
        with flash
        scene zoeycumoutside2
        with flash
        $ renpy.pause(2.0, hard=True)
        $ renpy.transition(Dissolve(0.1800))
        scene zoeycumoutside3
        with dissolve
        "Your cum covers her belly and all the way to the top of her breasts."
        z nudetalk2 "\"Mhhh~\""
        z nudetalk "\"I guess this is proof that I win the bet~!\""
        mc nudetalk "\"Ah-ha. Congratulations I guess.\""
        z nudetalk2 "\"Thanks for doing this with me.\""
        mc nudetalk2 "\"You're welcome... I guess...\""
        scene black
        with dissolve
        "You say goodbye to her as you get up and leave when guilt hits you hard."
        mc nudethinking "What is wrong with me? I must be losing my mind..."
        jump elysezoeyend
#-----------------------------------------------------------------------------------------------------------------




#-----------------------------------------------------------------------------------------------------------------

label onlyelyseend:
#$ watched_lexa = True or False
$ sex_with_elyse = True
$ mc_zoey_sex = False
$ declined_chloe_sex = True

scene roomch3
with dissolve

"I need to relax and just forget that today happened..."

"but flashbacks keep coming in your mind from earlier today..."

mc nudethinking "What I did with Elyse..."

if cum_inside_elyse:
    scene bnwjacuzzicuminside2
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "Unable to resist after she held me tight with both legs, I ended up cumming inside her..."

else:
    scene bnwjacuzzicumoutside2
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "I came all over her body..."

scene roomch3
with dissolve
mc nudethinking "At least I didn't do anything stupid like this with Zoey..."
mc nudethinking "I don't know what came over me back in the jacuzzi... I have to free my mind from such thoughts and try and focus on the real issue that started all of this in the first place..."
mc nudethinking "I have to find a way to free the captured girl."
"You keep thinking things through until you finally drift off to sleep."
jump ch4start


#-----------------------------------------------------------------------------------------------------------------







#-----------------------------------------------------------------------------------------------------------------

label elysezoeyend:
#$ watched_lexa = True or False
$ sex_with_elyse = True    
$ mc_zoey_sex = True
$ declined_chloe_sex = True

scene roomch3
with dissolve

mc nudethinking "I need to relax and just forget that today happened..."

"but flashbacks keep coming in your mind from earlier today..."

mc nudethinking "What I did with Elyse..."

if cum_inside_elyse:
    scene bnwjacuzzicuminside2
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "Unable to resist after she held me tight with both legs, I ended up cumming inside her..."

else:
    scene bnwjacuzzicumoutside2
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "I came all over her body..."

scene black
with dissolve
mc nudethinking "And then with Zoey..."

if zoey_cum_inside:
    scene bnwzoeycuminside3
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "Even went as far as cumming inside her..."

else:
    scene bnwzoeycumoutside3
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "Cumming all over her small body..."

scene roomch3
with dissolve
mc nudethinking "I don't know what came over me... I have to free my mind from such thoughts and try and focus on the real issue that started all of this in the first place..."
mc nudethinking "I have to find a way to free the captured girl."

"You keep thinking things through until you finally drift off to sleep."

jump ch4start

#-----------------------------------------------------------------------------------------------------------------







#-----------------------------------------------------------------------------------------------------------------

label onlychloeend:
#$ watched_lexa = True or False
$ sex_with_elyse = False   
$ mc_zoey_sex = False
$ declined_chloe_sex = False

scene roomch3
with dissolve

mc nudethinking "What happened today..."

mc nudethinking "I ended hooking up with Chloe..."

if cum_inside_chloe:
    scene bnwchloefuckcuminside1
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "She was pissed at me for cumming inside her..."

else:
    scene bnwchloefuckcumonbelly2
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "Splattering her belly with my cum~!"

scene roomch3
with dissolve
mc nudethinking "And then Zoey asking me to help her win that ridiculous bet... to fuck someone..."
mc nudethinking "They are changing in something I never knew..."
mc nudethinking "Either way... I have to focus on the matter at hand..."
mc nudethinking "I have to find a way to free the captured girl."

"You keep thinking things through until you finally drift off to sleep."

jump ch4start


#-----------------------------------------------------------------------------------------------------------------






#-----------------------------------------------------------------------------------------------------------------

label elysechloeend:
#$ watched_lexa = True or False
$ sex_with_elyse = True    
$ mc_zoey_sex = False
$ declined_chloe_sex = False

scene roomch3
with dissolve


mc nudethinking "What happened today..."

mc nudethinking "I ended hooking up with Chloe..."

if cum_inside_chloe:
    scene bnwchloefuckcuminside1
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "She was pissed at me for cumming inside her..."
else:
    scene bnwchloefuckcumonbelly2
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "Splattering her belly with my cum~!"

scene black
with dissolve
mc nudethinking "And then in the jacuzzi with Elyse..."

if cum_inside_elyse:
    scene bnwjacuzzicuminside2
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "Unable to resist after she held me tight with both legs, I ended up cumming inside her..."
else:
    scene bnwjacuzzicumoutside2
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "I came all over her body..."
scene roomch3
with dissolve
mc nudethinking "I don't know what came over me... I have to free my mind from such thoughts and try and focus on the real issue that started all of this in the first place..."
mc nudethinking "I have to find a way to free the captured girl."

"You keep thinking things through until you finally drift off to sleep."
jump ch4start

#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------

label zoeychloeend:
#$ watched_lexa = True or False    
$ mc_zoey_sex = True
$ sex_with_elyse = False
$ declined_chloe_sex = False

scene roomch3
with dissolve


mc nudethinking "What happened today..."

mc nudethinking "I ended hooking up with Chloe..."

if cum_inside_chloe:
    scene bnwchloefuckcuminside1
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "She was pissed at me for cumming inside her..."
else:
    scene bnwchloefuckcumonbelly2
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "Splattering her belly with my cum~!"
scene black
with dissolve
mc nudethinking "And then as if I was possesed I ended up fucking Zoey..."

if zoey_cum_inside:
    scene bnwzoeycuminside3
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "Even went as far as cumming inside her..."
else:
    scene bnwzoeycumoutside3
    with dissolve
    $ renpy.pause(1.4, hard=True)
    $ renpy.transition(Dissolve(0.1800))
    mc nudethinking "Cumming all over her small body..."
scene roomch3
with dissolve
mc nudethinking "I don't know what came over me... I have to free my mind from such thoughts and try and focus on the real issue that started all of this in the first place..."
mc nudethinking "I have to find a way to free the captured girl."

"You keep thinking things through until you finally drift off to sleep."
jump ch4start

#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------

label nosexend:
#$ watched_lexa = True or False
#$ chloe_spectate_talk = True or False
$ sex_with_elyse = False    
$ mc_zoey_sex = False
$ declined_chloe_sex = True

scene roomch3

with dissolve
mc nudethinking "\"I managed to keep my composure from all the lust surrounding me today even if it was tempting...\""
mc nudethinking "\"I have to focus on the real issue at hand that started all of this in the first place..."
mc nudethinking "I have to find a way to free the captured girl."

"You keep thinking things through until you finally drift off to sleep."
jump ch4start
#-----------------------------------------------------------------------------------------------------------------




#-----------------------------------------------------------------------------------------------------------------

#label endpop:
#scene black
#with fadein
#voidstar talk "\"Thank you so much for playing the current version (0.3) of Forgotten Paradise!\""
#voidstar talk "\"This is all the time I had to develop the game, but make sure to check all the routes possible as there are a few different ones in this version.\""
#voidstar talk "\"If you'd like to support the game and follow the development, then please do that at my Patreon: https://www.patreon.com/Vo1dStar\""
#voidstar talk "\"Even a single dollar helps. Thank you for believing in me and see you in the next version~!\""
#jump thanks

#-----------------------------------------------------------------------------------------------------------------



