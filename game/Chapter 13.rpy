label startch13:
    scene black
    with fadein
    "You are being dragged through the underground of the castle..."
    "Deep underground levels until you reach the cells."
    scene ch13dungeon0
    with Dissolve(1)
    
    "Ramsay kicks you."
    ramsay talk "\"Move it. The cell on your left.\""

    scene ch13dungeon1
    with dissolve
    
    ramsay talk "\"You will be sharing a cell with her.\""
    mc ctalk "\"Luna?\""
    scene ch13dungeon3
    with dissolve
    pause
    
    scene ch13dungeon4
    with dissolve
    luna talk "\"[mc]?\""
    
    scene ch13dungeon2
    with vpunch
    ramsay talk "\"Now get your ass in there!\""
    with vpunch
    
    scene ch13dungeon5
    with dissolve
    ramsay talk "\"You two should get comfortable with each other.\""
    ramsay talk "\"You will be spending the rest of your days down here.\""
    
    scene ch13dungeon6
    with dissolve
    luna talk "\"That's how your 'Queen' does things, huh?\""
    luna talk "\"Whoever she can't subdue under her thumb she imprison or executes.\""
    
    scene ch13dungeon5
    with dissolve
    ramsay talk "\"She is your Queen too and you better start referring to her that way to make your stay here more pleasant.\""
    scene ch13dungeon7
    with dissolve
    luna talk "\"Fuck your Queen! Where is Ingrid?!\""
    scene ch13dungeon5
    with dissolve
    ramsay talk "\"Ingrid? That slut is dead. You won't see her again.\""
    ramsay talk "\"Had a good time before that with her though, haha!\""
    scene ch13dungeon7
    with dissolve
    luna talk "\"Y-You killed her?! You bastard!\""
    luna talk "\"You will fucking die for what you've done!\""
    ramsay talk "\"I will give you some time to work on your manners. We have all the time in the world now, hehehe.\""
    
    scene ch13dungeon12
    with fasterfadein
    luna talk "\"How are you doing? Did they hurt you?\""
    mc ctalk2 "\"Me? I am fine. What about you??\""
    luna talk "\"I am fine as well...\""
    luna talk "\"I can't believe Ingrid is dead...\""
    mc ctalk3 "\"This bastard will pay, you have my word.\""
    luna talk "\"... Thank you, [mc].\""
    mc ctalk2 "\"What about Aurora?\""
    luna talk "\"The blue skinned girl?\""
    mc ctalk "\"Yeah.\""
    
    scene ch13dungeon8
    with fasterfadein
    luna talk "\"She is here. Right on the opposite side of our cell.\""
    luna talk "\"Look!\""
    $ quick_menu = False
    menu:
        "Look at the direction she is pointing at":
            jump ch13dungeon1
        "Look at her ass instead":
            jump ch13dungeon2
    
label ch13dungeon2:
    scene ch13dungeon9
    with dissolve
    $ quick_menu = True
    "You completely disregard the direction Luna is pointing at and stare at her ass instead."
    luna talk "\"They separated us from the start.\""
    luna talk "\"I hope they treated her fine...\""
    luna talk "\"Her pregnancy looks very far along too...\""
    "..."
    "... ..."
    "... ... ..."
    scene ch13dungeon10
    with dissolve
    luna talk "\"Naughty boy.\""
    luna talk "\"Where are you looking?\""
    luna talk "\"We will have plenty of time to do that later.\""
    scene ch13dungeon11
    with dissolve
    luna talk "\"As I was saying... I hope they were treating her right.\""
    luna talk "\"She is not even with our clan... they have no reason to hold her hostage.\""
    jump ch13dungeon3
label ch13dungeon1:
    scene ch13dungeon11
    with dissolve
    $ quick_menu = True
    "You look at the direction Luna is pointing and notice Aurora sitting in a small cell."
    luna talk "\"They separated us from the start.\""
    luna talk "\"I hope they treated her fine...\""
    luna talk "\"Her pregnancy looks very far along too...\""
    luna talk "\"She is not even with our clan... they have no reason to hold her hostage.\""
    jump ch13dungeon3

label ch13dungeon3:
    scene ch13dungeon12
    with fasterfadein
    luna talk "\"So here we are...in the biggest shitthole on the planet.\""
    mc ctalk "\"Could be worse. You could still be chained underground.\""
    luna talk "\"It's the same thing, no? Except I have some breathing room here and not being completely chained to a wall.\""
    mc ctalk2 "\"Yeah. And you have me for company!\""
    luna talk "\"Yes, indeed.\""
    scene ch13dungeon13
    with dissolve
    "Luna moves her finger across your arm."
    luna talk "\"Speaking of which... it will get boring here fast.\""
    luna talk "\"Do you want to 'fill' the time with me?\""
    $ quick_menu = False
    menu:
        "Have fun with her":
            $ch13_dungeon_luna_sex = True
            jump ch13dungeon5
        "Save your strength":
            $ch13_dungeon_luna_sex = False
            jump ch13dungeon4
            
label ch13dungeon4:
    scene ch13dungeon12
    with dissolve
    $ quick_menu = True
    mc ctalk2 "\"I think we should save our strength.\""
    mc ctalk3 "\"Who knows when a moment might arise for us to escape.\""
    mc ctalk "\"We should be on full focus.\""
    luna talk "\"Ah... of course, you're right...I should've been more considerate.\""
    mc ctalk2 "\"No, no. It's fine, really.\""
    mc ctalk "\"If the circumstances were different I would've taken you up on that offer any day.\""
    luna talk "\"That's nice to hear.\""
    scene black
    with Dissolve(1)
    "The next two days pass without any interaction outside of your own cell."
    jump ch13dungeon7

label ch13dungeon5:
    scene ch13dungeon14
    with dissolve
    $ quick_menu = True
    mc ctalk "\"Sure, why the heck not.\""
    mc ctalk2 "\"I guess we should make the best of our time in this cell.\""
    scene ch13dungeon15
    with dissolve
    luna talk "\"I am glad we think alike.\""
    scene ch13dungeon16
    with dissolve
    "Luna removes her breast plate."
    luna talk "\"So? What do you think?\""
    $ quick_menu = False
    menu:
        "Take a closer look at her tits":
            jump ch13dungeon6

label ch13dungeon6:
    scene ch13dungeon17
    with dissolve
    $ quick_menu = True
    mc ctalk3 "\"You have some of the most amazing breasts I've seen, Luna.\""
    luna talk "\"Come on. Don't be shy. Touch them, caress them, worship them.\""
    scene white
    with dissolve
    pause 1
    
    scene ch13dungeon18
    with Dissolve(1)
    "You grab her left breast and squeeze it gently."
    luna talk "\"Ahhhnnn~\""
    luna talk "\"Come here you!\""
    
    scene ch13motorboating
    with vpunch
    
    "Luna grabs your head and you begin to motorboat her huge melons."
    
    $ quick_menu = False
    show screen ch13_luna_motorboat
    $ renpy.show("ch13_luna_motorboat")
    $ renpy.pause(12, hard=True)

    label ch13_luna_motorboat:
    hide screen ch13_luna_motorboat
    $ quick_menu = True
    
    mc ctalk "\"Mmmhmmmmm...\""
    luna talk "\"I am sure you want your cock inbetween my tits by now.\""

    scene ch13titsfuck
    with dissolve
    luna talk "\"Let me show you what heaven feels like.\""
    
    $ quick_menu = False
    show screen ch13_luna_tittyfuck
    $ renpy.show("ch13_luna_tittyfuck")
    $ renpy.pause(12, hard=True)

    label ch13_luna_tittyfuck:
    hide screen ch13_luna_tittyfuck
    
    scene ch13dungeon19
    with dissolve
    $ quick_menu = True
    luna talk "\"Are you ready for the main dish?\""
    luna talk "\"My pussy is soaked and ready to devour your cock.\""
    mc ctalk2 "\"Fuck yes I am.\""
    
    scene white
    with dissolve
    pause 1
    
    scene ch13wallfuck
    with Dissolve(1)
    "You pin her on the wall and insert your penis in her and begin thrusting."
    
    $ quick_menu = False
    show screen ch13_luna_sex
    $ renpy.show("ch13_luna_sex")
    $ renpy.pause(12, hard=True)

    label ch13_luna_sex:
    hide screen ch13_luna_sex
    $ quick_menu = True
    luna talk "\"Ahh~Hnnnnh~Mmmmm...\""
    luna talk "\"Your cock feels so good around my cunt!\""
    luna talk "\"Don't stop... mmmm... never stop... hahh...\""
    
    luna talk "\"Hahh...Hnnn...Mmmmhh...\""
    
    luna talk "\"Fuck me faster!!\""
    
    "You increase your momentum."
    
    $ quick_menu = False
    show screen ch13_luna_sex2
    $ renpy.show("ch13_luna_sex2")
    $ renpy.pause(12, hard=True)

    label ch13_luna_sex2:
    hide screen ch13_luna_sex2
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch13wallfuck2
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch13wallfuck2
    with Dissolve(1)
    
    scene ch13dungeon27
    with fadein
    $ quick_menu = True
    "You both continue fucking like wild animals for the next two days..."
    "You only stop when you hear foosteps appraoching."
    
    jump ch13dungeon7
    

label ch13dungeon7:
    scene ch13dungeon20
    with fasterfadein
    luna talk "\"Do you hear that?\""
    luna talk "\"Someone is coming this way.\""
    scene ch13dungeon28
    with vpunch
    "You both watch as Ramsay approach Aurora's cell."
    ramsay talk "\"Wakey, wakey.\""
    ramsay talk "\"Come on. You are coming with me.\""
    scene ch13dungeon29
    with dissolve
    "Without putting any fight, Aurora willingly goes with Ramsay."
    mc cunhappy "\"Hey, asshole! Where are you taking her!?\""
    scene ch13dungeon30
    with dissolve
    ramsay talk "\"None of your business, cockroach.\""
    luna talk "\"When are we going to get some food? You are going to starve us to death?!\""
    ramsay talk "\"Did you learn some manners?\""
    luna talk "\"...\""
    ramsay talk "\"Heh.\""
    scene black
    with Dissolve(1)
    "A few hours later Aurora returns to her cell."
    scene ch13dungeon31
    with Dissolve(1)
    luna talk "\"Aurora! Are you all right?!\""
    "..."
    scene ch13dungeon21
    with vpunch
    ramsay talk "\"Do not respond to them, unless you want to have an unpleasant time, blueberry.\""
    ramsay talk "\"Now here's your food.\""
    ramsay talk "\"You will get the bear minimum until you submit.\""
    luna talk "\"That is not enough food for both of us! You haven't fed us in days!\""
    
    scene ch13dungeon23
    with dissolve
    ramsay talk "\"Yeah? You guys are hungry?\""
    ramsay talk "\"I'll tell you what...\""
    
    scene ch13dungeon22
    with dissolve
    ramsay talk "\"You suck my dick right now and I will consider a second plate.\""
    ramsay talk "\"What do you say?\""
    
    if persistent.show_ntr:
        scene ch13dungeon24
        with dissolve
        "Luna looks at your direction for approval."
        "You both haven't eaten in days and this one plate will hardly satisfy even a single hungry person."
        $ quick_menu = False
        menu:
            "Just nod your head and let her do it":
                jump ch13dungeon9
            "Get angry and refuse Ramsay's offer":
                jump ch13dungeon8
                
    else:
        jump ch13dungeon8
        
label ch13dungeon8:
    $ch13_ramsay_blowjob = False
    scene ch13dungeon26
    with vpunch
    $ quick_menu = True
    mc cshocked "\"Don't do anything, Luna! This guy can go suck his own cock, but I doubt he can even see it, let alone suck it.\""
    scene ch13dungeon23
    with dissolve
    ramsay talk "\"Oh, yeah? You have a pretty fucking big mouth. At least I will eat dinner tonight while you can fight for whatever is left on this plate. You better get used to it.\""
    
    scene ch13dungeon41
    with fasterfadein
    "Ramsay leaves and you sit around the plate and share whatever is on it."
    "It might not be enough, but at least you didn't let Luna defile herself for more."
    
    jump ch13dungeon10
    

label ch13dungeon9:
    scene ch13dungeon25
    with dissolve
    $ quick_menu = True
    $ch13_ramsay_blowjob = True
    "You just nod your head to the side in approval."
    "Your desire to survive kicks in and you just accept what she has to do and she does too."
    
    scene ch13dungeon25x1
    with fasterfadein
    "It doesn't take long until you start hearing slurping and gagging sounds."
    "You don't want to watch, but you are unable to unhear the dirty sounds coming from Luna's mouth as she sucks the cock through the bars."
    $ quick_menu = False
    menu:
        "Take a peek":
            jump ch13dungeon9x
            
label ch13dungeon9x:
    scene ch13dungeon25x2
    with dissolve
    $ quick_menu = True
    "The curiousity took the best of you, so you peeked at what was happening."
    
    $ quick_menu = False
    show screen ch13_luna_ntr_bj
    $ renpy.show("ch13_luna_ntr_bj")
    $ renpy.pause(12, hard=True)

    label ch13_luna_ntr_bj:
    hide screen ch13_luna_ntr_bj
    
    scene ch13dungeon33
    with vpunch
    $ quick_menu = True
    ramsay talk "\"Ah!... Shit...\""
    ramsay talk "\"Do it faster, slut.\""
    

    $ renpy.show("ch13_luna_ntr_bj2")

    label ch13_luna_ntr_bj2:
    
    luna talk "\"Mmm... *Chuupa* *Slurp*\""
    luna talk "\"*Gag*, *Kuuh* Mmmnnn...\""
    ramsay talk "\"You really know how to suck a cock, don't you?\""
    ramsay talk "\"You were made for this.\""
    ramsay talk "\"That's enough.\""
    
    scene ch13dungeon33
    with vpunch
    
    ramsay talk "\"I am a man who keeps his word, so you will get your second plate...\""
    ramsay talk "\"with extra sauce even.\""
    
    
    $ renpy.show("ch13_ramsay_masturbation")

    label ch13_ramsay_masturbation:
    
    "Ramsay takes his cock and puts it above one of the plates and begins masturbating."
    mc ctalk2 "\"What the fuck are you doing!!\""
    ramsay talk "\"Hahh... I am doing you a favor.\""
    ramsay talk "\"Don't worry... Heh... I will give my extra sauce only to one of the plate's. Luna would be thankful for the extra 'food' I am providing.\""
    mc ctalk "\"Fucking bastard.\""
    ramsay talk "\"Ahh...shit. I am about to...\""
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch13dungeon34
    with Dissolve(1)

    scene white
    with Dissolve(1)
    pause 1
    
    scene ch13dungeon34
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch13dungeon35
    with Dissolve(1)
    
    ramsay talk "\"There we go.\""
    ramsay talk "\"Enjoy your meal!\""
    
    scene ch13dungeon36
    with fadein
    "Ramsay leaves and Luna gives you the clean plate."
    "Unable to even think anymore you begin eating."
    
    scene ch13dungeon37
    with dissolve
    "You then remember what happened with Luna's plate."
    scene ch13dungeon38
    with dissolve
    mc cthinking "Disgusting..."
    mc thinking "It's full of cum... absolutely soaked with that bastard's cum."
    
    scene ch13dungeon37
    with dissolve
    mc ctalk2 "\"Hey... are you sure about this?\""
    mc ctalk3 "\"We can just share my plate...\""
    
    scene ch13dungeon39
    with dissolve
    "You look at Luna as she is chewing with a moutful of cum."
    luna talk "\"*Gulp*\""
    scene ch13dungeon40
    with dissolve
    "She licks her lips for anything remaining."
    luna talk "\"Don't worry about me. I am not disgusted by this.\""
    luna talk "\"We need to survive by any means, right?\""
    luna talk "\"This is protein and we need every bit of food to survive. They intend to break our spirits and keep us starved.\""
    "She was right, but you couldn't help but get hard after seeing her swallow so much cum from her plate..."
    
    jump ch13dungeon10
    
    
    
    
label ch13dungeon10:

    with fasterfadein
    scene twoweekslater
    $ quick_menu = False
    $ renpy.pause(2, hard=True)
    with fasterfadeout
    scene black
    with fadein
    $ quick_menu = True
    "Two weeks pass since then..."
    "Time seem to have stopped... seconds turned into minutes, minutes into hours, hours into days..."
    "Getting fed was a rare occurrence and although their goal was to break your spirit, it hasn't happened yet."
    scene ch13dungeon29
    with Dissolve(1)
    
    "You saw them take Aurora almost every day until they took her one day and she didn't return back to her cell for days."
    "You expected the worst... until she came back one day."
    
    scene ch13dungeon32
    with fasterfadein
    "Her belly was flat as she seems to have given birth."
    "You were just happy she was alive and well."
    
    scene ch13dungeon42
    mc cbthinking "This is crazy..."
    mc cbthinking "We will never get out of this hell hole..."
    mc cbthinking "There is no one that can help us..."
    
    "Just as you were in deep thoughts and despair you hear loud noise coming from the hallway..."
    
    scene ch13dungeon43
    with vpunch
    mc cbtalk "\"Huh?!\""
    mc cbtalk2 "\"Hey, Luna. Do you hear that?\""
    
    scene ch13dungeon44
    with dissolve
    luna talk "\"It's probably nothing, [mc]... Save your strength.\""
    mc cbtalk3 "\"No. Something is going on in the hallway!\""
    
    scene ch13dungeon45
    with dissolve
    luna talk "\"What are you talking ab--\""
    mc cbtalk "\"Shh. Listen.\""
    with vpunch
    
    scene ch13dungeon46
    with fasterfadein
    qm guard "\"Hey, how did you get down here?\""
    qm guard "\"Stop right there!\""
    qm guard "\"I am warning y--\""
    
    scene ch13dungeon47
    with vpunch
    qm guard "\"Aghhhh!!\""
    
    scene ch13dungeon48
    with dissolve
    ingrid talk "\"This one had the keys... good.\""
    
    scene ch13dungeon49
    with fasterfadein
    luna talk "\"{size=+13}Ingrid?!{/size}\""
    with vpunch
    mc cbtalk2 "\"Oh my god. You are alive!\""
    ingrid talk "\"Of course I am. Why did you think I was dead?\""
    luna talk "\"That bastard Ramsay told us you were...\""
    ingrid talk "\"Ugh. Of course he did.\""
    
    scene ch13dungeon50
    with dissolve
    "You noticed the blood dripping from her knife."
    mc cbtalk3 "\"I see you've slaughtered your way in.\""
    ingrid talk "\"Yeah. So we gotta move, fast.\""
    ingrid talk "\"Let me get you out of here.\""
    
    scene black
    with Dissolve(1)
    "Ingrid unlocks your cell door."
    
    scene ch13dungeon51
    with Dissolve(1)
    luna talk "\"I am... I am...\""
    luna talk "\"I am so happy to see you...\""
    
    scene ch13dungeon52
    with dissolve
    ingrid talk "\"Me too... I am sorry I took so long...\""
    luna talk "\"It doesn't matter... what matters is that you are here now.\""
    
    scene ch13dungeon53
    with dissolve
    ingrid talk "\"Good to see you, [mc]. I am glad you are okay.\""
    mc cbtalk "\"Yeah, glad you are okay too, Ingrid.\""
    "As you were catching up with Ingrid you almost forgot one thing..."
    "You looked across and saw Aurora..."
    
    scene ch13dungeon54
    with dissolve
    "She stayed silent and just watched."
    "Her sad expression broke your heart."
    mc cbtalk2 "\"Guys. We can't forget Aurora.\""
    
    scene ch13dungeon55
    with dissolve
    "You move closer to her cell."
    mc cbtalk3 "\"Hey, Aurora. How are you doing? Are you okay?\""
    aur nudetalk "\"I am okay, [mc]...\""
    mc cbtalk2 "\"We will get you out of here! Ingrid open the cell!\""
    
    scene ch13dungeon56
    with dissolve
    ingrid talk "\"I...I am sorry... I didn't find the key to her cell.\""
    mc cbtalk "\"We must find the keys and set her free!\""
    aur nudetalk "\"[mc]...\""
    mc cbtalk2 "\"We can't let her stay here... who knows what they will do to her.\""
    aur nudetalk "\"[mc]!\""
    
    scene ch13dungeon58
    with dissolve
    aur nudetalk "\"It's fine. You need to leave without me.\""
    mc cbtalk "\"What? No...\""
    mc cbtalk3 "\"We will get you out... we just have to...\""
    aur nudetalk "\"There is no time. They will be alerted at any moment and after seeing dead bodies of guards you will not go back to a cell...\""
    aur nudetalk "\"Thank you... for everything.\""
    aur nudetalk "\"I have only one request from you...\""
    mc cbtalk2 "\"What is it...?\""
    aur nudetalk "\"Kiss me.\""
    $ quick_menu = False
    menu:
        "Kiss her":
            jump ch13dungeon11
            
label ch13dungeon11:
    scene ch13dungeon57
    with dissolve
    $ quick_menu = True
    "You lock lips together in a passionate kiss."
    "Aurora moves her tongue around yours and eventually breaks up the kiss and moves away from the cell."
    
    scene ch13dungeon59
    with dissolve
    mc cbtalk "\"I will find a way to get you out of here, Aurora!\""
    mc cbtalk "\"I will come back for you!\""
    luna talk "\"[mc]... we have to go.\""
    
    scene ch13dungeon60
    with fasterfadein
    "On the way out you see the guard that was asigned to guard your cell."
    ingrid talk "\"Take his sword, [mc].\""
    ingrid talk "\"We might need it later.\""
    ingrid talk "\"I've found a way out through an underground passage that leads to outside.\""
    ingrid talk "\"It's our only option right now. We need to be quick.\""
    jump ch13tunnel1
    

label ch13tunnel1:
    scene black
    with Dissolve(1)
    "You grab the sword and you follow Ingrid down through the underground passage."
    
    scene ch13tunnel1
    with Dissolve(1)
    luna talk "\"What happened these past 2 weeks with you Ingrid?\""
    ingrid talk "\"Ugh... where do I even begin?\""
    jump ch13flashback
    
label ch13flashback:
    scene ch13flashback1
    with fadein
    ingrid talk "\"That bastard took me to a secluded area in the forest.\""
    ramsay talk "\"Heh. You don't look so tough now, bitch.\""
    
    scene ch13flashback2
    with dissolve
    ingrid talk "\"He didn't waste any time and began undressing.\""
    ramsay talk "\"You're such a slut. I bet you whore yourself to your whole camp.\""
    scene ch13flashback3
    with dissolve
    ramsay talk "\"Sluts like you are only good for one thing.\""
    scene ch13flashback4
    with vpunch
    ramsay talk "\"To satisfy my cock!\""
    scene ch13flashback5
    with fasterfadein
    ramsay talk "\"Look at your feet though.\""
    ramsay talk "\"I'd say you are perfectly created for your purpose!\""
    ramsay talk "\"Let me smell and lick your feet a little bit will ya?\""
    
    scene ch13flashback6
    with vpunch
    ingrid talk "\"Smell this, you asshole!\""
    
    scene ch13flashback7
    ramsay talk "\"Woah. *Cough* That wasn't very nice.\""
    ramsay talk "\"You almost broke my nose there.\""
    
    scene ch13flashback8
    with dissolve
    ramsay talk "\"But I like a fighter. It makes it that much better.\""
    ramsay talk "\"Now, come here.\""
    
    scene ch13flashback9
    with vpunch
    ramsay talk "\"You can kick all you want now.\""
    ramsay talk "\"You will only hurt your beautiful feet in the process though.\""
    ingrid talk "\"You...bastard...\""
    "..."
    ramsay talk "\"Mmmmmmmm...\""
    
    scene ch13flashback10
    with dissolve
    ramsay talk "\"You are definitely a keeper.\""
    ramsay talk "\"Now, let's see what we have down here...\""
    ramsay talk "\"My, my. You seem wet already.\""
    ramsay talk "\"Or is that just sweat? Either way... I am digging in.\""
    
    $ quick_menu = False
    show screen ch13_ingrid_cunnilingus
    $ renpy.show("ch13_ingrid_cunnilingus")
    $ renpy.pause(12, hard=True)

    label ch13_ingrid_cunnilingus:
    hide screen ch13_ingrid_cunnilingus
    $ quick_menu = True
    ingrid talk "\"Ahh!!\""
    
    scene white
    with Dissolve(1)
    pause 1

    scene ch13flashback11
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1

    scene ch13flashback12
    with Dissolve(1)
    
    ramsay talk "\"Ahh, you're quite the squirter. Are you trying to drown me here?\""
    
    scene ch13flashback13
    with fasterfadein
    
    ramsay talk "\"Now that I satisfied you, it's only fair that you satisfy me, don't you agree?\""
    ramsay talk "\"Now come here...\""
    
    scene ch13flashback14
    with dissolve
    ramsay talk "\"Spread those slutty legs for me... yes...\""
    ramsay talk "\"I am going to cum so deep in your cunt, that you will get pregnant with triplets.\""
    
    scene ch13flashback15
    with vpunch
    ingrid talk "\"Fuck you, asshole!\""
    ramsay talk "\"Ughh, aghhh!!!\""
    
    scene ch13flashback16
    with dissolve
    ramsay talk "\"You...fucking.......bitch!!\""
    ingrid talk "\"After that I ran as far away as possible and managed to lose him eventually.\""
    jump ch13tunnel2
    
label ch13tunnel2:
    scene ch13tunnel2
    with fasterfadein
    luna talk "\"Oh, dear...\""
    luna talk "\"I am glad you escaped that pig!\""
    
    if ch13_ramsay_blowjob:
        luna talk "\"Too bad you didn't damage his balls permanently.\""
        ingrid talk "\"What do you mean?\""
        luna talk "\"Err... nevermind...\""
        
    else:
        luna talk "\"Hopefully his reproduction system is damaged permanently.\""
        
    scene black
    with Dissolve(1)
    "A few minutes later you reach the end of the pathway and see daylight coming from the horizon...\""
    
    scene ch13tunnel3
    with Dissolve(1)
    "Unfortunately you also see a familiar figure standing between you and the exit."
    ingrid talk "\"Shit.\""
    ramsay talk "\"Welcome back, dear. I knew you'd run back to me eventually.\""
    
    scene ch13tunnel4
    with dissolve
    mc cbtalk2 "\"You two go on ahead. I will deal with him.\""
    ingrid talk "\"What?!\""
    luna talk "\"What are you talking about, [mc]! He is a trained knight and in full body armor!\""
    luna talk "\"You have just one sword... let us help you.\""
    
    scene ch13tunnel5
    with dissolve
    mc cbtalk3 "\"I will deal with him alone. You need to scout ahead. There might be an ambush waiting for us.\""
    mc cbtalk "\"Okay? I will meet you outside!\""
    luna talk "\"Okay... if this is what you really want.\""
    ingrid talk "\"You better meet us outside!\""
    mc cbtalk2 "\"You got it.\""
    
    scene ch13tunnel6
    with fasterfadein
    "The girls start running towards the exit like you told them to...\""
    
    with vpunch
    ramsay talk "\"You think I will let the sluts get away? Ha!\""
    
    scene ch13tunnel7
    with vpunch
    "You jump high in the air with an attack to get his attention."
    mc cbtalk3 "\"Worry about yourself!\""
    
    scene ch13tunnel8
    with vpunch
    ramsay talk "\"You bastard! You won't buy them any time!\""
    ramsay talk "\"I will cut you down like butter and then I will catch up to them!\""
    mc cbtalk "\"We will see about that.\""
    
    with fasterfadein
    "You continue to fight for a few minutes and manage to deflect and dodge his attacks so far..."
    
    scene ch13tunnel9
    with dissolve
    ramsay talk "\"You're not bad for a rookie, but it's time for you to die!\""
    "Ramsay swings his sword from his right side."
    $ quick_menu = False
    menu:
        "Dodge to the right":
            jump ch13tunnel3
        "Counter attack him":
            jump ch13tunnel4
        "Dodge backwards":
            jump ch13tunnel5
            
label ch13tunnel3:
    scene ch13tunnel11
    with vpunch
    $ quick_menu = True
    "You try and dodge to the right, but you end up in the range of his attack instead."
    ramsay talk "\"{size=+13}HA! I got you, you bastard!{/size}\""
    scene bloodsplatter
    with Dissolve(1)
    "Ramsay cuts through your upper body..."
    
    scene ch13tunnel12
    with Dissolve(1)
    ramsay talk "\"You lie down there and die thinking how you failed those whores.\""
    "The last thing you hear is his evil laugh and loud footsteps as he moves in the direction of Luna and Ingrid."
    
    scene gameover5
    $ quick_menu = False
    with Dissolve(1)
    $ renpy.pause(2, hard=True)
    jump thanks
    
label ch13tunnel4:
    scene ch13tunnel10
    with vpunch
    $ quick_menu = True
    "You try and counter attack him, but he is fast enough to block with his shield."
    
    scene ch13tunnel11
    with vpunch
    "After which he pushes your sword to the side using his shield and leaves you open for an attack."
    ramsay talk "\"{size=+13}HA! I got you, you bastard!{/size}\""
    scene bloodsplatter
    with Dissolve(1)
    "Ramsay cuts through your upper body..."
    
    scene ch13tunnel12
    with Dissolve(1)
    ramsay talk "\"You lie down there and die thinking how you failed those whores.\""
    "The last thing you hear is his evil laugh and loud footsteps as he moves in the direction of Luna and Ingrid."
    
    scene gameover6
    $ quick_menu = False
    with Dissolve(1)
    $ renpy.pause(2, hard=True)
    jump thanks
    
label ch13tunnel5:
    scene ch13tunnel13
    with hpunch
    $ quick_menu = True
    "Not having armor has it's benefits as it allows you to move quickly and dodge his swing."
    "As you moved backwards for a moment it seemed as time stopped and you were able to analyze your opponent and his weaknesses."
    "You notice his attack left him open for you to strike."
    $ quick_menu = False
    menu:
        "Target his neck":
            jump ch13tunnel6
            
label ch13tunnel6:
    scene ch13tunnel14
    with vpunch
    $ quick_menu = True
    "Without much hesitation you dash forward and slice right through Ramsay's neck."
    "Blood starts gushing out of his neck."
    
    scene ch13tunnel15
    with dissolve
    "Ramsay drops on his knees and releases his weapon and shield."
    ramsay talk "\"*Cough*, *Cough*...\""
    ramsay talk "\"I yield, I yield!\""
    
    scene ch13tunnel16
    with dissolve
    ramsay talk "\"*Cough*... You wouldn't kill a man that surrendered and is defenseless, right?\""
    "You think for a moment how much you'd love to splatter his brains through the wall, but you see that the fatal wound you gave him will probably do the job."
    ramsay talk "\"That's right... you're a hero and heroes don't murder defenseless people.\""
    
    scene ch13tunnel17
    with Dissolve(1)
    "You decide to not even respond and continue walking forward, showing him mercy."
    ramsay talk "\"*Cough*...\""
    
    scene ch13tunnel18
    with dissolve
    ramsay talk "\"That's right...you're a hero.\""
    ramsay talk "\"But heroes like you don't get to live that long!\""
    
    scene ch13tunnel19
    with dissolve
    "You hear him get up and turn around, but before you have the chance to stop him he stabs you directly."
    scene ch13tunnel20
    with Dissolve(1)
    mc cbtalk2 "\"Arghhh!\""
    
    scene ch13tunnel21
    with hpunch
    "Ramsay manages to stab you in the intestines."
    ramsay talk "\"I will... see you in hell.\""
    
    scene ch13tunnel22
    with dissolve
    "Ramsay collapses to the ground."
    $ quick_menu = False
    menu:
        "Leave him to bleed to death":
            jump ch13tunnel7
        "Cut off his head":
            jump ch13tunnel8
            
label ch13tunnel7:
    $ quick_menu = True
    $ch13_chopped_ramsay_head = False
    "You decide to let him suffer and leave him to die a slow painful death."
    scene ch13tunnel25
    with dissolve
    "You make your way towards the exit, but you slowly feel your body get weaker and weaker."
    "As you approach, the exit you hear thunder and rain coming from outside."
    stop music fadeout 6.0
    play ambient "sfx/Thunder.mp3"
    play music "music/Rain.mp3" fadein 10.0
    jump ch13forest1
    
    
    
    
label ch13tunnel8:
    $ch13_chopped_ramsay_head = True
    scene ch13tunnel23
    with dissolve
    $ quick_menu = True
    "Not a word was said, as both men understood what was going to happen."
    "You position yourself and raise your sword with both hands."

    scene ch13tunnel24
    with vpunch
    "With one fell swoop, you cut through Ramsay's head... blood gushing through his severed head."
    "You catch your breath and continue towards the exit..."
    
    scene ch13tunnel25
    with dissolve
    "You feel your body get weaker and weaker..."
    "As you approach the exit, you hear thunder and rain coming from outside."
    stop music fadeout 6.0
    play ambient "sfx/Thunder.mp3"
    play music "music/Rain.mp3" fadein 10.0
    jump ch13forest1
    
    
label ch13forest1:
    scene black
    with Dissolve(1)
    stop ambient fadeout 5.0
    "You continue to walk through the forest until you hear nearby scream."
    
    scene ch13forest1
    with Dissolve(1)
    "As you approach the sounds, you notice Luna and Ingrid taking out another guard."
    
    scene ch13forest2
    #thunder sound here
    with vpunch
    ingrid talk "\"Aghh!\""
    
    scene ch13forest3
    with dissolve
    "You try and talk, but due to the heavy rain and thunder they are unable to hear you."
    luna talk "\"I think that's the last one.\""
    
    scene ch13forest4
    with dissolve
    ingrid talk "\"Huh? No.\""
    ingrid talk "\"Look! Another one is coming this way!\""
    
    scene ch13forest5
    with dissolve
    ingrid talk "\"Wait... is that...\""
    
    scene ch13forest7
    with vpunch
    play ambient "sfx/Thunder.mp3"
    ingrid talk "\"{size=+13}[mc]?!{/size}\""
    
    scene ch13forest6
    with dissolve
    stop ambient fadeout 5.0
    ingrid talk "\"He is hurt! Quickly!\""
    
    scene ch13forest8
    with dissolve
    "With the last bit of strength you fall on your knees."
    
    scene black
    with Dissolve(1)
    ingrid talk "\"[mc]! Stay with me.\""
    "..."
    
    scene ch13forest9
    with Dissolve(1)
    ingrid talk "\"[mc]!\""
    ingrid talk "\"You will be okay...\""
    ingrid talk "\"*Sob* You will make it.\""
    
    scene ch13forest10
    with dissolve
    play ambient "sfx/Thunder.mp3"
    "You look up at the sky as everything starts to become less noisy and more clear and vivid."
    scene ch13forest11
    stop ambient fadeout 5.0
    with vpunch
    pause 1
    
    scene ch13forest10
    with Dissolve(1)
    
    jump ch13forest2
    
label ch13forest2:
    stop music fadeout 5.0
    
    $ quick_menu = False
    $ renpy.show("ch13_flashback_mc")
    $ renpy.pause(5, hard=True)

    label ch13_flashback_mc:
    $ quick_menu = True
    "Your life flashes through your eyes until one exact moment in time sticks out..."
    
    scene ch13mcflashback24
    with Dissolve(1)
    
    qm strangertalk2 "\"Oh, another word of advice...\""
    qm strangertalk "\"When you are in dire need, and believe me you will know when that is, search for the witch Elisande. She will help you out.\""
    mc miltalk "\"... I will keep that in mind.\""
    
    scene ch13forest9
    with fasterfadein
    play ambient "sfx/Thunder.mp3"
    play music "music/Rain.mp3" fadein 10.0
    
    ingrid talk "\"Where can we take him, Luna?!\""
    
    stop ambient fadeout 5.0
    ingrid talk "\"It will take days to get back to our camp... he won't make the trip!\""
    luna talk "\"We are in enemy territory, we can't stay here...\""
    ingrid talk "\"Perhaps we should go ba--\""
    luna talk "\"{size=+13}No! Don't you dare suggest that!{/size}\""
    scene ch13forest12
    with dissolve
    
    mc cbtalk "\"Eli--sande...\""
    ingrid talk "\"What? [mc]? What did you say?\""
    mc cbtalk "\"Take me to Elisande...\""
    ingrid talk "\"Who is that? I don't know who she is...\""
    
    scene ch13forest13
    with dissolve
    luna talk "\"Eli...sande...\""
    luna talk "\"He can't mean THAT Elisande.\""
    
    ingrid talk "\"You know her?\""
    luna talk "\"Yeah. She is a witch and I don't know if it's a good idea to approach her.\""
    ingrid talk "\"We are out of options here, Luna! We have to do this.\""

    scene ch13forest14
    with dissolve
    luna talk "\"Okay, I guess you have a point. Let's go, I will lead the way... She is usually spotted camping towards the beach side.\""
    
    jump ch13tent1

label ch13tent1:
    
#    with fasterfadein
#    scene afewhourslater
#    $ quick_menu = False
#    $ renpy.pause(2, hard=True)
#    with fasterfadeout
    scene black
    with fadein
#    $ quick_menu = True
    stop music fadeout 3.0
    "After a few hours of walking through the forest you finally reach the beach..."
    
    scene ch13tent1
    with Dissolve(1)
    play music "music/Eastern Thought.mp3" fadein 19.0
    luna talk "\"Do you see the light coming from that tent?\""
    luna talk "\"That has to be her.\""
    ingrid talk "\"Be careful. We are still in enemy territory.\""
    
    scene ch13tent2
    with fasterfadein
    "You all approach the tent and get dizzy just from breathing in the air there."
    
    $ quick_menu = False
    scene ch13tent3 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(5, hard=True)
    $ quick_menu = True
    "You are presented with a sight of a woman sitting on a divan, smoking through some sort of hookah."
    with dissolve
    scene ch13tent4
    with fasterfadein
    pause
    
    scene ch13tent5
    with Dissolve(1)
    "The woman finally pays enough attention to you."
    qm elihtalk "\"I tink ya came to da wron' tent.\""
    
    scene ch13tent2
    ingrid talk "\"Are you Elisande?!\""
    
    scene ch13tent5
    eli htalk "\"I am.\""
    eli htalk "\"Who be askin'?\""
               
    scene ch13tent6
    ingrid talk "\"You've got to help us! [mc] is gravely injured and we need your help...\""
    ingrid talk "\"We've got nowhere else to go... you're our only hope.\""
    
    scene ch13tent5
    eli htalk "\"'Tis too bad. I don't be helpin' strangers like that.\""
    eli htalk "\"Who is he and where he be comin' from?\""
    
    scene ch13tent6
    ingrid talk "\"He is not from around here, okay?! He came from another planet! YOU HAVE TO SAVE HIS LIFE!\""
    with vpunch
    luna talk "\"Ingrid!\""
    
    eli htalk "\"Wait... Anotha' planet you say?\""
    ingrid talk "\"That's right.\""
    
    
    scene ch13tent7
    with dissolve
    eli htalk "\"Let 'im lie down hea', quickly.\""
    
    scene ch13tent8
    with dissolve
    eli htalk "\"Could 'e be...\""
    ingrid talk "\"Please... save his life.\""
    eli htalk "\"Hmm...\""
    
    scene ch13tent9
    with dissolve
    eli htalk "\"You'a lucky.\""
    eli htalk "\"Da stab didn' penetrate any vital organs and he didn' lose too much blood.\""
    eli htalk "\"You did good not removing the blade. He be dead by now otherwise.\""
    eli htalk "\"Give me som' space and time. I be fixing 'im up.\""
    
    
    with fasterfadein
    scene sometimelater
    $ quick_menu = False
    $ renpy.pause(2, hard=True)
    with fasterfadeout
    scene ch13tent10
    with fadein
    $ quick_menu = True
    
    "Sunlight shines through the tent as the morning comes."
    
    scene ch13tent11
    ingrid talk "\"Wh-What happened?\""
    luna talk "\"Is he all right?\""
    
    scene ch13tent12
    eli htalk "\"Wound was no danger. But blade be full of royal poison on it.\""
    eli htalk "\"Strong enough poison to paralyze you in matta of minutes and kill you in a few hours.\""
    
    $ quick_menu = False
    scene ch13tent13 with fade:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0000001
    $ renpy.pause(5, hard=True)
    $ quick_menu = True
    eli nudetalk "\"'Tis the only way to slow this down before it kills him.\""
    with dissolve
    scene ch13tent14
    with vpunch
    ingrid talk "\"{size=+13}What the hell are you doing?!{/size}\""
    eli nudetalk "\"Savin' his life.\""
    luna talk "\"Stop, Ingrid. Let her do it.\""
    
    scene ch13tent15
    "Elisande climbs on top of you."
    eli nudetalk "\"Let us begin.\""
    
    $ quick_menu = False
    show screen ch13_elisande_sex
    $ renpy.show("ch13_elisande_sex")
    $ renpy.pause(12, hard=True)

    label ch13_elisande_sex:
    hide screen ch13_elisande_sex
    
    scene ch13tent16
    with vpunch
    $ quick_menu = True
    eli nudetalk "\"DOH-nahss-doh-gah-MAH-tahss-tohss\""
    eli nudetalk "\"OH • oh-hoh-RAY-lah • TAH-bah • OHL\""
    scene ch13tent17
    with vpunch
    eli nudetalk "\"NOH-ray • OHD • PAH-suh-buhs • OHL\""
    eli nudetalk "\"zoh-nuh-RAY-nuh-suhjzh vah-OH-ahn • OHD\""
    scene ch13tent18
    with vpunch
    eli nudetalk "\"toh-OH-aht • NOH-noo-KAH-fay\""
    eli nudetalk "\"guh-MEE-kah-luh-ZOH-mah • PEE-lah\""
    scene ch13tent19
    with vpunch
    eli nudetalk "\"KEE-kuh-lay • KAH-ah! • ZOH-ruh-jzhay!\""
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch13tent20
    with Dissolve(1)

    scene white
    with Dissolve(1)
    pause 1
    
    scene ch13tent20
    with Dissolve(1)
    
    scene white
    with Dissolve(1)
    pause 1
    
    scene ch13tent21
    with Dissolve(1)
    
    eli nudetalk "\"Hahh...Mmhhahh..Hahh...\""
    
    $ persistent.change = "New world 3"
    
    scene black
    with Dissolve(1)
    "A few moments later..."
    
    scene ch13tent24
    with Dissolve(1)
    ingrid talk "\"What happened?\""
    ingrid talk "\"Is he okay?\""
    ingrid talk "\"What did you do to him?!\""
    
    scene ch13tent22
    with dissolve
    eli nudetalk "\"He be fine fo' now.\""
    eli nudetalk "\"There be only one way to revert this poison. Unfortunately I do not possess the ingridient needed fo' the antidote.\""
    scene ch13tent23
    with dissolve
    eli nudetalk "\"The only alternative was... to do a soul binding ritual...\""
    ingrid talk "\"Soul binding ritual?! What are you talking about??\""
    eli nudetalk "\"'Tis a double-edged sword.\""
    eli nudetalk "\"I stop da sprea' of poison in his body, but fo' a cost.\""
    scene ch13tent24
    ingrid talk "\"I don't get what you're talking about!\""
    ingrid talk "\"Is he going to be okay or not?\""
    eli nudetalk "\"You can as' him yo'self.\""
    with vpunch
    ingrid talk "\"What?\""
    scene ch13tent25
    "..."
    "... ..."
    "... ... ..."
    eli nudethinking "Come on, don't be shy."
    mc elinudetalk "\"Ughh...\""
    mc elinudetalk "\"... Hello, girls.\""
    with vpunch
    ingrid talk "\"{size=+13}WHAT?!{/size}\""
    luna talk "\"Huh?!\""
    mc elinudetalk "\"Let us dress and we will explain everything.\""
    
    jump startch14