label yourroomafterparty:
    
scene black
with dissolve

"You make your way back to your room..."

scene mcafterpartysleep0
with fadein

mc talk3 "Fuck... need to get..."
mc talk3 "to... bed..."

scene mcsleepingafterparty
with fadein

"You barely manage to remove your clothes before you collapse on top of the bed..."

"...drifting off to sleep."

with fadein
scene asteroidonly
$ renpy.pause(4, hard=True)

with fasterfadein
scene sometimelater
$ quick_menu = False
pause 2.5
with fasterfadeout

scene dahliaafterparty
with fasterfadein
$ quick_menu = True

d talk "\"Fuck that party really wrecked me. My head is spinning so much...\""
d talk "\"That drink wasn't a joke.\""

scene dahliaafterparty
with vpunch

d surprised "\"What th--\""

scene dahliaafterparty
with vpunch

d surprised "\"W...\""

scene dahliafallingdown
with vpunch

d surprised "\"Aaah--\""

scene dahliafallingdown
with vpunch

d surprised "\"AHH~!\""

scene dahliafallingdown2
with vpunch

d surprised "\"Ug---\""

scene dahliapassedouthallway
with fadein

"..."

"......"

with fasterfadein
scene meanwhile
$ quick_menu = False
pause 2.5
with fasterfadeout

scene black
with fasterfadein
$ quick_menu = True

"You are awoken in shock after a huge quake shakes the ship and the books above you fall on top of your head."

scene mcawokenshocked
with fadein

mc nudeshocked2 "What the hell is going on!? What was that?!"
mc nudeshocked2 "It sounded like we were hit..."
mc nudeshocked2 "I should dress up quickly and go check out what happened!"

scene black
with fadein

"You dress up quickly and run to the direction of the huge sound earlier."
"You move through the starboard side of the ship and as you enter you question if you are really awake..."

scene mcbastionrunning
with fadein

mc shocked "What the hell!?"
mc shocked "This can't be right..."
mc shocked "This is not... Earth... right?!"
mc shocked "This has to be a dream... it has to be!"

"As you keep running you see someone in front of you..."

scene bastionjanerunning2
with dissolve

mc shocked "Jane? Is that Jane?"
mc shocked2 "\"Jane!\""

scene bastionjanerunning
with dissolve

j sslayer3 "\"[mc]?!\""
j sslayer3 "\"C'mon, keep up!\""

"She motions you as she continues to sprint forward."

scene bastionmcjanerunning
with fasterfadein

mc shocked2 "\"Jane, what the hell is going on?\""
j sslayer4 "\"There is no time to explain the details, but just know that we were hit by something...and...\""
mc shocked2 "\"And?!\""
j sslayer3 "\"And as you can see for yourself the Earth might be gone too.\""
mc shocked "\"How does that even happen?! Don't we have defense systems, didn't we get a warning?!\""
j sslayer4 "\"I can't go in details, but it seems we lost power to all defenses when this happened.\""
j sslayer3 "\"Our weapons are currently offline due the damage our ship received.\""
mc shocked2 "\"So if we are getting attacked...\""
j sslayer4 "\"That's right... we can't fight back.\""
j sslayer3 "\"That is what I am trying to undo right now. I am going to see the damage and see how to begin repairs.\""

scene mcjanebastionexit
with fadein

mc talk3 "\"Let me help somehow.\""
j sslayer4 "\"You can't help with that. It will be faster and safer if I go alone.\""
mc talk3 "\"What can I do then?\""
j sslayer3 "\"Go to the command center and see if anybody else needs help.\""
mc talk3 "\"Okay. I will do that. Stay safe.\""
j sslayer3 "\"You too.\""

with fasterfadein
scene meanwhile
$ quick_menu = False
pause 2.5
with fasterfadeout

scene ediscomingupstairs
with fasterfadein
$ quick_menu = True

edis talk "\"Everything went to hell, huh?\""
edis talk "\"The Mayans were only 68 years off.\""

scene edisfindingdahlia
with fadein

edis laugh "\"What do we have here?\""
edis talk "\"I found myself a knocked out bitch.\""
edis talk "\"Everything is you and your people's fault.\""
edis talk "\"You cursed our home planet and destroyed it just like you did yours...\""
edis talk "\"You will do as fine entartainment for the world's end.\""

scene edisdraggingdahlia1
with fadein
$ renpy.pause(2, hard=True)

scene dahliadragged
with fadein

edis talk "\"You are already half naked, you stupid whore.\""
edis laugh "\"Look at your tit coming out of that slutty bra.\""

scene dahliaontable
with dissolve

edis talk "\"Look at you. You have no shame.\""
edis talk "\"I bet you already slept with half the ship...men or women alike.\""

scene dahliaontable2
with fadein

edis talk "\"Before we begin a small precaution...\""
edis talk "\"Just in case... even though I am sure you will be happy your cunt to be stuffed with anything.\""

"Edis unbuckles his belt and climbs on top of Dahlia."

scene dahliawakingup
with fadein

edis talk "\"I changed my mind. I want you to be awake. It will make this much better.\""
edis talk "\"Wake up, whore.\""

d surprised "\"Wh... What the fuck?\""
d angry "\"Did you tie me up, you assface?\""

edis laugh "\"Still insults even in a situation like this.\""
edis laugh "\"I knew this would be fun.\""
edis smirk "\"I will enjoy breaking you.\""

d angry2 "\"You better untie me right the fuck now!\""

edis laugh "\"Slut, you better know your place!\""
edis smirk "\"You will learn how to talk to me.\""

d angry3 "\"When I get free I will fucking kill you.\""
d angry2 "\"You won't get away with this!\""

edis laugh "\"I have nothing to lose!\""
edis laugh "\"Earth's gone and we are on our way too. Nobody will care what happens to you now.\""

d angry "\"What the fuck?!\""
d surprised "\"HELP!\""

edis laugh "\"Scream all you want, nobody will come for you.\""
edis laugh "\"You better save your energy though, as we have a long session in front of us.\""

scene edisfuckingdahliax
with dissolve

edis smirk "\"I waited a long fucking time for this.\""
edis laugh "\"I will enjoy breaking you.\""

$ quick_menu = False
show screen edisfuckingdahlia
$ renpy.show("edisfuckingdahlia")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label edisfuckingdahlia:
hide screen edisfuckingdahlia

scene black
with fadein
$ renpy.pause(2, hard=True)

scene mcrushingtocc
with dissolve

$ quick_menu = True
"You enter the command center and spot Ruby inside..."

"...standing in a very provocative pose."

$ quick_menu = False

menu:
    "Check her out":
        $ quick_menu = True
        scene dahliacloseupcc
        with dissolve
        mc thinking "Even as an android she is sexy as fuck."
        mc thinking "Why am I thinking of this right now? Our lives might be over and this is what I am doing..."
        jump arrivingatcc
    "Focus":
        $ quick_menu = True
        mc thinking "Focus, [mc]. No time for this right now."
        jump arrivingatcc
        
label arrivingatcc:
scene cctalkingtoruby
with fasterfadein

mc talk3 "\"Ruby! Are you okay?\""
r ttalk "\"I am fine, [mc]. Thank you for asking. From what I can see you are unharmed.\""
mc talk2 "\"Yes... I am fine, but what about the others?\""
r ttalk2 "\"I am unsure about everyone else. Right now I can only establish connection with Jane as she has the device I gave her earlier for communication.\""
r ttalk "\"I have to send her the location of the breach.\""

scene ccmctalkingtojane
with dissolve

r ttalk2 "\"Jane? Do you copy? Over.\""

"..."

scene airlockjane1
with fadein
j sslayer "\"Copy. I am about to exit. Over.\""
"..."
scene airlockjane2
with dissolve
j sslayer "\"And done!\""

scene airlockjane3
with dissolve
r ttalk "\"I am sending you the coordinates. Over.\""
j sslayer "\"Copy that. Over.\""

scene breachjaneabouttogoin
with fadein
$ renpy.pause(2, hard=True)

scene janecheckingoutbreach
with fadein

j sslayer "\"I am at the breach.\""
j sslayer "\"Going in. Over\""

scene breachjanegoesin
with dissolve

mc talk3 "\"How bad is it, Jane? Over.\""

j sslayer "\"It looks pretty bad, but it can be repaired. Good news is that it was sealed from the rest of the ship otherwise we would be in a very nasty situation right now.\""
j sslayer "\"This is definitely one of our lesser problems right n--\""

with vpunch
qm empty "\"REEARRGHLLLHRRRRRRRRR!!\""

mc shocked "\"J-Jane?! What was that!?\""

"Jane turns to her left where the scary loud noise came from..."

scene breachjanespottingalien
with vpunch

"Only to find a huge monster lurking in the shadows..."

"..."

mc shocked "\"Jane? Do you copy?\""

qm tentacle "\"RRAAAAUUUGGHH!\""

j sslayer2 "\"OH GOD!\""

scene breachjanestartstorun
with fadein

"Jane begins to run away as fast as she possibly could in low gravity."

"But the monster has other plans..."

j sslayer2 "\"Aaahh!!\""

mc shocked "\"Jane? Jane! What is happening!?\""

scene breachjanestartstorun2
with dissolve

j sslayer2 "\"There is something on the breach! A monster of some kind. It grabbed my leg!\""
r ttalk "\"Jane whatever happens you can't go back inside with that thing on you.\""
         
mc shocked2 "\"What?!\""

scene ccmctalkingtojane
with fadein

mc shocked2 "\"Jane talk to us.\""

r ttalk "\"We lost connection.\""

mc talk3 "\"We need to help her!\""

r ttalk2 "\"There is nothing we can do, she is a well trained expert and she will know how to handle this.\""

mc shocked "\"She is fighting against a damn alien unharmed! Tell me where she's most likely to be?\""

scene cctalkingtoruby
with dissolve

r ttalk "\"Here. I will upload you the coordinates. Also take this piece of electronic on you so we can keep constant communication.\""

scene ccmcleaving
with dissolve

mc talk3 "\"Thanks. I will let you know when I am there.\""

scene black
with fasterfadein
"You make your way as fast as you can through the hallways to get to Jane's possible location."
"But as you move through the hallways you hear a faint noise coming from one of the rooms down the hallway..."

scene mcbeforemeetingedis
with dissolve

mc thinking "Huh, did I hear something or am I imagining things?"
mc thinking "Do I even have the time to check right now?"
$ quick_menu = False
menu:
    "Investigate":
        $ quick_menu = True
        mc thinking "Maybe someone is hurt... I should check just in case."
        $ saved_dahlia_from_edis = True
        scene mcrunningintolab
        with dissolve
        mc thinking "Another laboratory? This is like the third one..."
        "As you approach the door you hear the noise better."
        qm empty "\"--ELP!\""
        mc shocked "Someone is calling for help!!"
        scene edistakesdahliafrombehind
        with fasterfadein
        edis smirk "\"Your ass is too good for a slut like you.\""
        edis laugh "\"Hahah---\""
        scene edisfuckingdahliabehindmccomingin
        with vpunch
        edis talk "\"Huh?\""
        edis talk "\"Who the fuck?\""
        scene mcpunchingedis
        with vpunch
        "You don't even hesitate, you go straight for the knock out and punch the living shit out of Edis."
        edis talk "\"Ugggh--\""
        
        scene mcknocksedisout
        with dissolve
        
        mc talk2 "\"Are you hurt?\""
        d surprised "\"... Thank god...\""
        "You untie her."
        
        scene dahliahuggingmc
        with vpunch
        "As you untie her she jumps to hug you."
        
        d talk "\"Thank you... I thought nobody would come...\""
        mc talk3 "\"You're safe now...\""
        d talk "\"Thanks to you...\""
        
        scene dahliaafterrapeangry
        with dissolve
        d angry "\"Wait here while I go and get my sword to finish this bastard once and for all!\""
        mc shocked2 "\"Wait, Dahlia! Don't. He is knocked out.\""
        d angry2 "\"So what?! He deserves it.\""
        mc talk3 "\"I promise you, he will get what he deserves.\""
        d angry "\"And what if he doesn't?!\""
        mc talk3 "\"I will make sure he does.\""
        
        scene mckneelingoveredis
        with dissolve
        
        d talk "\"You saved me... I trust your judgement.\""
        mc talk3 "\"Thank you for that.\""
        mc talk3 "\"Now help me tie this bastard up.\""
        
        scene edistiedup
        with dissolve
        
        mc talk3 "\"This will do.\""
        mc shocked "\"Oh fuck... I totally forgot about Jane!\""
        d surprised "\"What about Jane?\""
        mc talk3 "\"Long story... listen, I have to go, but please don't do anything stupid. Gather the others if you can.\""
        scene black
        with fasterfadein
        d talk "\"Will do. Be safe.\""
        mc talk3 "\"Thanks! You too.\""
        
        jump aftercchallway
        
    "No time":
        $ quick_menu = True
        mc thinking "I don't have time for this... Jane is in grave danger!"
        $ saved_dahlia_from_edis = False
        jump aftercchallway

label aftercchallway:
scene black
with fasterfadein
if saved_dahlia_from_edis:
    mc thinking "I hope I am not too late..."
else:
    mc thinking "This must be it..."
    
scene mcrunninginobservation
with fadein

"You enter the wing in which Ruby gave you coordinates to."
"You sprint through and go to the room with the outside view."

scene mcentersobserationroom
with dissolve

mc thinking "Is this it?"
mc thinking "Oh my god... this really isn't a dream is it? What a fucked up day."

"You look around to see if you can spot Jane, but you don't see her anywhere."

scene mcentersobserationroom2
with dissolve

mc talk3 "\"Jane do you copy?"
"..."
j sslayer "\"On your left\""

scene mcentersobserationroom3
with dissolve

mc talk3 "\"Left?\""
mc talk3 "\"Oh!!\""

"You spot Jane on your left and move closer to the window."

scene observationjanelookingatyou
with dissolve

j sslayer "\"Hey there, champ.\""

mc talk3 "\"Hey yourself!\""

j sslayer "\"Did I worry you guys for a second?\""

mc talk3 "\"You did... a lot.\""

j sslayer "\"Sorry for cutting communnication like that, but the monster detected sound waves and I couldn't really escape otherwise.\""

mc talk3 "\"It's fine! I am just glad you are safe.\""

j sslayer "\"Haha, yeah me too.\""

scene observationjanelookingatyou2
with dissolve

j sslayer "\"Next time I should be bringing weapons on repairs I supp--\""

mc talk3 "\"JANE!! ABOVE YOU!\""

j sslayer2 "\"W-What!?\""

scene observationjanecaughtupintentacles
with vpunch

j sslayer2 "\"AAHHH--\""

mc shocked2 "\"YOU BASTARD! LET HER GO!\""

j sslayer2 "\"[mc]...\""

mc shocked "Oh no... what can I do in this situation....."

$ quick_menu = False

menu:
    "Contact Ruby for help":
        $ quick_menu = True
        $ game_over_1 = False
        jump aftertentacleattacks
    
    "Watch in despair":
        $ quick_menu = True
        $ game_over_1 = True
        jump gameover1
        
label gameover1:
    
scene janetentacles
with fasterfadein

"You give up all hope and just watch in full despair at what is unfolding before your eyes..."

"The creature has locked Jane in such a way that she can't break free..."

"But what is more, the creature is playing with her body it seems..."

"Rubbing it's tentacles around her breasts and crotch."

$ quick_menu = False
show screen tentaclegropesjane
$ renpy.show("tentaclegropesjane")
$ renpy.transition(Dissolve(1))
$ renpy.pause(12, hard=True)

label tentaclegropesjane:
hide screen tentaclegropesjane

scene tentaclepenetration1
with fadein

$ quick_menu = True
"It seems as if the monster is done playing with her and starts trying to penetrate her suit through her crotch..."

"It violently pushes more and more..."

scene tentaclepenetration2
with dissolve

"Until it pushes through the fabric enough to enter her vagina."

j sslayer2 "\"AAAAH!\""

scene tentaclepenetration4
with dissolve

"Jane screams in pain and continues to struggle all in vain..."
"The monster's grip becomes tighter and tighter."

scene tentaclepenetration3
with vpunch

"It finally manages to rip part of her suit and start penetrating her..."

scene tentaclepenetration5
with vpunch

j sslayer2 "\"AHHHH!!!\""
j sslayer2 "\"OH MY GOD...\""

scene tentaclepenetration5
with dissolve

j sslayer2 "\"I.... I can.....\""
j sslayer2 "\"I can feel it...\""
j sslayer2 "\"It's going up my stomach...\""

scene tentaclepenetration6
with dissolve

j sslayer2 "\"AARGHHHH--\""

"The monster continues to penetrate her all the way up..."

scene tentaclepenetration7
with fadein

"Eventually reaching the exit of her mouth... Jane already dead at that point..."

scene mcaftermath1badending1
with fadein

mc shocked2 "\"I failed her... I failed everybody...\""

mc shocked2 "\"...I ...\""

mc shocked2 "\"I couldn't do anything...\""

with fasterfadein
scene afewmonthslater
$ quick_menu = False
pause 2.5
with fasterfadeout

scene mcaftermath2badending1
$ quick_menu = True
with fasterfadein

"A few months after the disaster of the doomsday, the end of Paradise's crew arrived."

"Without an enginner and with more and more problems escalating and with [mc]'s faith lost it didn't take too long for most of the crew to start fighting among each other..."

"Not focused on survival, but on ending what little had survived after the apocalypse."

"After being on route to another potential planet the ship got hit by a meteorite shower and with no expert on fixing the damage it only spelled doom for everyone."

scene gameover1aftermath
with fadein

"To make the process more painless the ship was charged head-on to a nearby planet core..."

"I guess it made sense to end it the same way everyone on Earth did."

"Nothing and no one left to tell the tale... Paradise was gone in a blink... and everyone else on board the Forgotten Paradise..."

with fadein
scene gameover1
$ quick_menu = False
$ renpy.pause(5, hard=True)
jump thanks

label aftertentacleattacks:
mc thinking "I have to do something right now!"
scene mcrunningforsuit
with dissolve
mc talk3 "\"Ruby! Ruby do you copy!?\""
r ttalk "\"Yes, [mc].\""
mc talk3 "\"Listen, give me the authorization to get a suit and a weapon asap.\""
r ttalk2 "\"Hey, I can't do that. Your safet--\""
mc shocked "\"Fuck my safety! I will be fine! Jane won't be!\""
mc shocked "\"I am also the only one with outer space training and military training. I can take on this thing.\""
mc shocked2 "\"Give me the authorization now and guide me to the location of the suit...\""

scene black
with fadein
"You were able to convince Ruby and she allowed you to try and help Jane."
"She guided you to where the emergency fighter suit is kept..."

scene labsuitonly
with fadein

mc shocked2 "Holy...shit... this is it? Never seen one of these before."
mc talk3 "Nevermind that... I will admire it later... let's activate it first..."

scene mcactivvatingsuit
with dissolve

mc talk3 "\"Ruby, help me out here?\""
r ttalk "\"Leave it to me, [mc].\""

"..."

"......"

"........."



r ttalk2 "\"It should be online and powered up. You can equip it.\""

scene mclookingatsuitupclose
with dissolve

mc talk3 "\"Let's see what this bad boy feels like...\""

scene black
with fadein

"You equip the suit and try to get a good feel of it..."

scene mclookingathandsinsuit
with fadein

mc sslayer "\"Holy...\""
mc sslayer "\"Shit...\""

scene mclookingathandsinsuit2
with dissolve

mc sslayer "\"This feels incredible.\""
mc sslayer "\"It feels light as hell, but powerful at the same time.\""
r ttalk "\"This suit is meant for crew emergencies for when we are under attack.\""
mc sslayer "\"I will do it justice. Now show me where the weapons are.\""
r ttalk2 "\"On your right.\""

scene mclookingatweaponraft
with dissolve

r ttalk "\"I have already unlocked them, so you can pick one up.\""
mc sslayer "\"Good job. Let's check them out.\""

scene mcholdingweaponinlab
with dissolve

mc sslayer "\"Very nice grip on it and seems light as well.\""
r ttalk2 "\"It's a laser gun, so be careful not to shoot the wrong thing. There is no undoing it.\""
r ttalk "\"[mc], A temporary small gravity field towards the ship was activated when Jane went outside, so you will be safe without a rope.\""
mc sslayer "\"Gotcha.\""

scene mcleavinglab
with fadein

mc sslayer "\"It's time to kick ass and chew bubble gum...\""
r ttalk2 "\"Huh?\""
mc sslayer "\"Sorry, I felt like a badass so I wanted to say something cool.\""
r ttalk "\"Just don't get too ahead of yourself. Jane is a well trained expert and she got caught by that thing.\""
mc sslayer "\"Of course, I'll be careful. Send me the coordinates...\""

scene mcleavingairlock
with fadein

mc sslayer "\"Let's end this son of a bitch!\""
"You leave and make your way towards Jane and the monster."

scene mclookingattentacle
with fadein

mc sslayer "\"I see it, there it is.\""
mc sslayer "\"I am not too late. Let's fuck him up.\""

scene janetentacles
with dissolve

j sslayer "\"Ughhh...\""

scene tentaclemonstermouth
with dissolve

qm tentacle "\"RRRRGGHHEEEE\""

$ quick_menu = False

menu:
    "Aim":
        $ quick_menu = True
        scene mcshootingtentacle1
        mc sslayer "Let's do this!"
        "You bounce forward and aim precisely at the monster's upper body."
        mc sslayer "\"Hey! Shit brain!\""
        scene janelookingyourwayoutside
        with dissolve
        qm tentacle "\"RRRRRRAAAGGH\""
        j sslayer2 "\"Huh? [mc]!?\""
        $ quick_menu = False
        menu:
            "Shoot":
                $ quick_menu = True
                scene mcshootingtentacle2
                with vpunch
                mc sslayer "\"Eat this!\""
                scene mcshootingtentacle3
                with vpunch
                qm tentacle "\"RGHEEEEEEEAAARGH\""
                qm tentacle "\"GHAAAAARRH\""
                "The tentacle monster loosens it's grip on Jane allowing her to break free."
                scene janebreakingfreefrommonster
                with dissolve
                "Jane propel herself from the monster."
                "*Swoosh*"
                jump catchingjaneaftermonster

label catchingjaneaftermonster:
scene mccarryingjanetosafety
with vpunch
"You catch her as she pushed herself forward."
mc sslayer "\"You're safe now.\""
mc sslayer "\"Let's get you home.\""

scene black
with fadein

"Meanwhile on another spaceship not that far away..."

qm empty "\"Vui...pax toimee vui so dohh?\"\n(Yess...you bring me good newss?)"

scene aavagivingorders2
with fadein

qm creature2talk "\"Vui, sodoh! Vui rayvui paxlox ray socovfgtoiray sovuimee meevuiray!\"\n(Yes, mother! We have found a potential breeding species!)"
qm creature1talk "\"La ray' la so rayvui vui vuicovfg ray toi sopax jhadoh.\"\n(They don't seem to have any defenses at this point either.)"

scene aavagivingorders
with dissolve

qm aavatalk2 "\"Lox la meecovfgo loxdohopa opadoh?\"\n(And they have different genders?)"
qm aavatalk "\"Toi tee meetoi pax toimee.\"\n(We need male and female.)"
qm creature2talk "\"Vui, sodoh.\"\n(Yes, mother.)"

scene aavainlust1
with dissolve

qm aavatalk "\"Mee... rayso meetoi toi jha toiso...\"\n(Ah... this makes me so excited...)"
qm aavatalk2 "\"So pax' opa jha teetoi...\"\n(I can't wait to breed...)"

scene aavainlust2
qm aavatalk "\"Miuo'toi toigot vuijha jha lox... jhatoi la sodoh teeopatoi jhatoi dohtee...\"\n(You've been such good boys... come help mother release some stress...)"
qm creature1talk "\"Vui, sodoh.\"\n(Yes, mother.)"
qm creature2talk "\"So so toi miuo paxopavuitee.\"\n(It will be our pleasure.)"
scene black
with dissolve
jump decontamination