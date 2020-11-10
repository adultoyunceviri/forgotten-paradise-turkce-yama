# The script of the game goes in this file.

#r=ruby,z=zoey,jack=jack,e=elyse,a=andre,chloe=chloe,cass=cassandra,aur=aurora,shp=karin,m=melisa,l=lexa,d=dahlia

default persistent.show_ntr = True

init python:
    ### start a melody on the channel
    def mplay(fn, chan = "music", fin = 1.0, fout = 1.0):
        renpy.play(fn + ".mp3", channel = chan, loop = True, fadein = fin, fadeout = fout)
    ### pause channel
    def mpause(channel = "music"):
        c = renpy.audio.audio.get_channel(channel)
        c.pause()
    ### remove from pause
    def munpause(channel = "music"):
        c = renpy.audio.audio.get_channel(channel)
        c.unpause()
    ###  ### stop the melody
    def mstop(chan = "music", fout=1.0):
        renpy.music.stop(channel = chan, fadeout = fout)


# Declare characters used by this game. The color argument colorizes the
# name of the character.

#scene white
#with dissolve
#pause 1
#...
#scene ...
#with dissolve

define mc = Character("[player_name]", 
        color = "#85B200", 
        what_color="#85B200", 
        image = "mc")

image side mc elithinking = "side_image/side_mc_elithinking.png"
image side mc elitalk = "side_image/side_mc_elitalk.png"
image side mc elinudetalk = "side_image/side_mc_elinudetalk.png"
image side mc elinudethinking = "side_image/side_mc_elinudethinking.png"
image side mc elidressthinking = "side_image/side_mc_elidressthinking.png"
image side mc elidresstalk = "side_image/side_mc_elidresstalk.png"

image side mc thought = "side_image/side_mc_thought.png"

image side mc sslayer = "side_image/side_mc_sslayer.png"
image side mc sslayer2 = "side_image/side_mc_sslayer2.png"
image side mc sslayershocked = "side_image/side_mc_sslayershocked.png"
image side mc sslayerthinking = "side_image/side_mc_sslayerthinking.png"

image side mc millaugh = "side_image/side_mc_millaugh.png"
image side mc milunhappy = "side_image/side_mc_milunhappy.png"
image side mc milthinking = "side_image/side_mc_milthinking.png"
image side mc milpleasure = "side_image/side_mc_milpleasure.png"
image side mc miltalk = "side_image/side_mc_miltalk.png"
image side mc miltalk2 = "side_image/side_mc_miltalk2.png"
image side mc miltalk3 = "side_image/side_mc_miltalk3.png"
image side mc milshocked2 = "side_image/side_mc_milshocked2.png"
image side mc milshocked = "side_image/side_mc_milshocked.png"
image side mc milsmileshocked = "side_image/side_mc_milsmileshocked.png"

image side mc laugh = "side_image/side_mc_laugh.png"
image side mc sleep = "side_image/side_mc_sleep.png"
image side mc unhappy = "side_image/side_mc_unhappy.png"
image side mc thinking = "side_image/side_mc_thinking.png"
image side mc talk = "side_image/side_mc_talk.png"
image side mc talk2 = "side_image/side_mc_talk2.png"
image side mc talk3 = "side_image/side_mc_talk3.png"
image side mc shocked = "side_image/side_mc_shocked.png"
image side mc shocked2 = "side_image/side_mc_shocked2.png"
image side mc smileshocked = "side_image/side_mc_smileshocked.png"
image side mc pleasure2 = "side_image/side_mc_pleasure2.png"
image side mc pleasure = "side_image/side_mc_pleasure.png"

image side mc gymthinking = "side_image/side_mc_gymthinking.png"
image side mc gymtalk = "side_image/side_mc_gymtalk.png"
image side mc gymtalk2 = "side_image/side_mc_gymtalk2.png"
image side mc gymtalk3 = "side_image/side_mc_gymtalk3.png"
image side mc gymunhappy = "side_image/side_mc_gymunhappy.png"
image side mc gymshocked = "side_image/side_mc_gymshocked.png"
image side mc gymshocked2 = "side_image/side_mc_gymshocked2.png"
image side mc gympleasure = "side_image/side_mc_pleasure.png"

image side mc nudelaugh = "side_image/side_mc_nudelaugh.png"
image side mc nudeunhappy = "side_image/side_mc_nudeunhappy.png"
image side mc nudethinking = "side_image/side_mc_nudethinking.png"
image side mc nudesleep = "side_image/side_mc_nudesleep.png"
image side mc nudetalk = "side_image/side_mc_nudetalk.png"
image side mc nudetalk2 = "side_image/side_mc_nudetalk2.png"
image side mc nudetalk3 = "side_image/side_mc_nudetalk3.png"
image side mc nudeshocked = "side_image/side_mc_nudeshocked.png"
image side mc nudeshocked2 = "side_image/side_mc_nudeshocked2.png"
image side mc nudesmileshocked = "side_image/side_mc_nudesmileshocked.png"
image side mc nudepleasure2 = "side_image/side_mc_nudepleasure2.png"
image side mc nudepleasure = "side_image/side_mc_nudepleasure.png"

image side mc claugh = "side_image/side_mc_claugh.png"
image side mc csleep = "side_image/side_mc_csleep.png"
image side mc cunhappy = "side_image/side_mc_cunhappy.png"
image side mc cthinking = "side_image/side_mc_cthinking.png"
image side mc ctalk = "side_image/side_mc_ctalk.png"
image side mc ctalk2 = "side_image/side_mc_ctalk2.png"
image side mc ctalk3 = "side_image/side_mc_ctalk3.png"
image side mc cshocked = "side_image/side_mc_cshocked.png"
image side mc cshocked2 = "side_image/side_mc_cshocked2.png"
image side mc cpleasure2 = "side_image/side_mc_cpleasure2.png"
image side mc cpleasure = "side_image/side_mc_cpleasure.png"

image side mc cbtalk = "side_image/side_mc_cbtalk.png"
image side mc cbtalk2 = "side_image/side_mc_cbtalk2.png"
image side mc cbtalk3 = "side_image/side_mc_cbtalk3.png"
image side mc cbthinking = "side_image/side_mc_cbthinking.png"

image side mc wtalk1 = "side_image/side_mc_wtalk1.png"
image side mc wtalk2 = "side_image/side_mc_wtalk2.png"
image side mc wtalk3 = "side_image/side_mc_wtalk3.png"
image side mc wtalk4 = "side_image/side_mc_wtalk4.png"


define ad = Character("[alien_daughter]", 
        color = "#F1DDF7", 
        what_color="#F1DDF7", 
        image = "ad")
image side ad babytalk = "side_image/side_ad_babytalk.png"

image side ad nudethinking = "side_image/side_ad_nudethinking.png"
image side ad thinking = "side_image/side_ad_thinking.png"
image side ad talk = "side_image/side_ad_talk.png"
image side ad thinking2 = "side_image/side_ad_thinking2.png"
image side ad thinking3 = "side_image/side_ad_thinking3.png"
image side ad talk2 = "side_image/side_ad_talk2.png"
image side ad talk3 = "side_image/side_ad_talk3.png"
image side ad nudetalk = "side_image/side_ad_nudetalk.png"

image side ad pyjtalk = "side_image/side_ad_pyjtalk.png"

define eli = Character("Elisande",
        color = "#B78E7B", 
        image = "eli",
        what_color= "#B78E7B")
image side eli talk = "side_image/side_eli_talk.png"
image side eli htalk = "side_image/side_eli_htalk.png"
image side eli nudetalk = "side_image/side_eli_nudetalk.png"
image side eli thinking = "side_image/side_eli_thinking.png"
image side eli nudethinking = "side_image/side_eli_nudethinking.png"
image side eli dresstalk = "side_image/side_eli_dresstalk.png"
image side eli dressthinking = "side_image/side_eli_dressthinking.png"

define voidstar = Character("Void Star",
    color = "#FFFFFF",
    image = "voidstar")
image side voidstar talk = "side_image/side_voidstar_talk.png"

define alex = Character("Alex",
        color = "#FFFFFF",
        image = "alex")
image side alex talk = "side_image/side_alex_talk.png"
image side alex talk2 = "side_image/side_alex_talk2.png"
image side alex talk3 = "side_image/side_alex_talk3.png"


define qm = Character("???",
        color = "#FFFFFF",
        image = "qm")
image side qm reddragon = "side_image/side_qm_reddragon.png"

image side qm elihtalk = "side_image/side_qm_elihtalk.png"

image side qm alientalk = "side_image/side_qm_alientalk.png"
image side qm alienntalk = "side_image/side_qm_alienntalk.png"

image side qm guard = "side_image/side_qm_guard.png"
image side qm ramsay = "side_image/side_qm_ramsay.png"
image side qm quan = "side_image/side_qm_quan.png"

image side qm empty = "side_image/side_qm_empty.png"

image side qm strangertalk = "side_image/side_qm_strangertalk.png"
image side qm strangertalk2 = "side_image/side_qm_strangertalk2.png"
image side qm strangerlaugh = "side_image/side_qm_strangerlaugh.png"

image side qm aavatalk = "side_image/side_qm_aavatalk.png"
image side qm aavapleasure = "side_image/side_qm_aavapleasure.png"
image side qm aavatalk2 = "side_image/side_qm_aavatalk2.png"
image side qm creature1talk = "side_image/side_qm_creature1talk.png"
image side qm creature2talk = "side_image/side_qm_creature2talk.png"
image side qm creature1talk2 = "side_image/side_qm_creature1talk2.png"
image side qm creature3talk = "side_image/side_qm_creature3talk.png"

image side qm karintalk = "side_image/side_qm_karintalk.png"

image side qm tentacle = "side_image/side_qm_tentacle.png"

image side qm drivertalk2 = "side_image/side_qm_drivertalk2.png"

image side qm amirpleasure = "side_image/side_qm_amirpleasure.png"
image side qm amirangry = "side_image/side_qm_amirangry.png"
image side qm amirtalk = "side_image/side_qm_amirtalk.png"
image side qm amirsmile = "side_image/side_qm_amirsmile.png"

image side qm janepouty = "side_image/side_qm_janepouty.png"
image side qm janeblow = "side_image/side_qm_janeblow.png"

image side qm rubytalk = "side_image/side_qm_rubytalk.png"

image side qm melisatalk = "side_image/side_qm_melisatalk.png"

image side qm lexacangry = "side_image/side_qm_lexacangry.png"
image side qm lexacangry2 = "side_image/side_qm_lexacangry2.png"
image side qm lexacworried = "side_image/side_qm_lexacworried.png"
image side qm lexacpain = "side_image/side_qm_lexacpain.png"

image side qm edistalk = "side_image/side_qm_edistalk.png"

image side qm ingridtalk = "side_image/side_qm_ingridtalk.png"
image side qm miratalk = "side_image/side_qm_miratalk.png"

image side qm merchanttalk = "side_image/side_qm_merchanttalk.png"


define walter = Character("Walter",
        color = "#E1A588", 
        image = "walter",
        what_color= "#E1A588")
image side walter talk = "side_image/side_walter_talk.png"
image side walter nudetalk = "side_image/side_walter_nudetalk.png"

define ivy = Character("Ivy",
        color = "#822100", 
        image = "ivy",
        what_color= "#822100")
image side ivy talk = "side_image/side_ivy_talk.png"

define ingrid = Character("Ingrid",
        color = "#624720", 
        image = "ingrid",
        what_color= "#624720")
image side ingrid talk = "side_image/side_ingrid_talk.png"
image side ingrid ntalk = "side_image/side_ingrid_ntalk.png"
image side ingrid talk2 = "side_image/side_ingrid_talk2.png"
image side ingrid talk3 = "side_image/side_ingrid_talk3.png"

define mira = Character("Mira",
        color = "#55332B", 
        image = "mira",
        what_color= "#55332B")
image side mira talk = "side_image/side_mira_talk.png"
image side mira nudetalk = "side_image/side_mira_nudetalk.png"

define luna = Character("Luna",
        color = "#CACAD9", 
        image = "luna",
        what_color= "#CACAD9")
image side luna talk = "side_image/side_luna_talk.png"
image side luna nudetalk = "side_image/side_luna_nudetalk.png"


define dany = Character("Dany",
        color = "#F5E483", 
        image = "dany",
        what_color= "#F5E483")
image side dany talk = "side_image/side_dany_talk.png"
image side dany nudetalk = "side_image/side_dany_nudetalk.png"
image side dany gowntalk = "side_image/side_dany_gowntalk.png"

define ramsay = Character("Ramsay",
        color = "#C2C2BA", 
        image = "ramsay",
        what_color= "#C2C2BA")
image side ramsay talk = "side_image/side_ramsay_talk.png"


define r = Character("Ruby",
        color = "#FF9999", 
        image = "ruby",
        what_color= "#FF9999")

image side ruby concentrate = "side_image/side_ruby_concentrate.png"
image side ruby smile = "side_image/side_ruby_smile.png"
image side ruby talk = "side_image/side_ruby_talk.png"
image side ruby talk2 = "side_image/side_ruby_talk2.png"

image side ruby ttalk = "side_image/side_ruby_ttalk.png"
image side ruby ttalk2 = "side_image/side_ruby_ttalk2.png"
image side ruby nudettalk = "side_image/side_ruby_nudettalk.png"
image side ruby nudettalk2 = "side_image/side_ruby_nudettalk2.png"

image side ruby nudetalk = "side_image/side_ruby_nudetalk.png"
image side ruby nudesmile = "side_image/side_ruby_nudesmile.png"
image side ruby nudeconcentrate = "side_image/side_ruby_nudeconcentrate.png"


define z = Character("Zoey", 
        color = "#DFBFFF", 
        image = "zoey",
        what_color= "#DFBFFF")

image side zoey desire = "side_image/side_zoey_desire.png"
image side zoey happy = "side_image/side_zoey_happy.png"
image side zoey flirting = "side_image/side_zoey_flirting.png"
image side zoey pleased = "side_image/side_zoey_pleased.png"
image side zoey pleasure = "side_image/side_zoey_pleasure.png"
image side zoey talk = "side_image/side_zoey_talk.png"
image side zoey talk2 = "side_image/side_zoey_talk2.png"
image side zoey wink = "side_image/side_zoey_wink.png"

image side zoey pyjamatalk = "side_image/side_zoey_pyjamatalk.png"
image side zoey pyjamatalk2 = "side_image/side_zoey_pyjamatalk2.png"
image side zoey pyjamadesire = "side_image/side_zoey_pyjamadesire.png"
image side zoey pyjamaflirting = "side_image/side_zoey_pyjamaflirting.png"
image side zoey pyjamapleased = "side_image/side_zoey_pyjamapleased.png"
image side zoey pyjamawink = "side_image/side_zoey_pyjamawink.png"
image side zoey pyjamahappy = "side_image/side_zoey_pyjamahappy.png"

image side zoey nudewink = "side_image/side_zoey_nudewink.png"
image side zoey nudetalk = "side_image/side_zoey_nudetalk.png"
image side zoey nudetalk2 = "side_image/side_zoey_nudetalk2.png"
image side zoey nudepleased = "side_image/side_zoey_nudepleased.png"
image side zoey nudeflirting = "side_image/side_zoey_nudeflirting.png"
image side zoey nudehappy = "side_image/side_zoey_nudehappy.png"
image side zoey nudedesire = "side_image/side_zoey_nudedesire.png"
image side zoey nudepleasure = "side_image/side_zoey_nudepleasure.png"

image side zoey desirebb = "side_image/side_zoey_desirebb.png"
image side zoey happybb = "side_image/side_zoey_happybb.png"
image side zoey flirtingbb = "side_image/side_zoey_flirtingbb.png"
image side zoey pleasedbb = "side_image/side_zoey_pleasedbb.png"
image side zoey talkbb = "side_image/side_zoey_talkbb.png"
image side zoey talk2bb = "side_image/side_zoey_talk2bb.png"
image side zoey winkbb = "side_image/side_zoey_winkbb.png"



define jack = Character("Jack",
        color = "#999999", 
        image="jack",
        what_color="#999999")

image side jack angry = "side_image/side_jack_angry.png"
image side jack angry2 = "side_image/side_jack_angry2.png"
image side jack laugh = "side_image/side_jack_laugh.png"
image side jack laugh2 = "side_image/side_jack_laugh2.png"
image side jack stare = "side_image/side_jack_stare.png"
image side jack talk = "side_image/side_jack_talk.png"
image side jack talk2 = "side_image/side_jack_talk2.png"

image side jack nudetalk = "side_image/side_jack_nudetalk.png"
image side jack nudetalk2 = "side_image/side_jack_nudetalk2.png"
image side jack nudestare = "side_image/side_jack_nudestare.png"
image side jack nudelaugh = "side_image/side_jack_nudelaugh.png"
image side jack nudeangry = "side_image/side_jack_nudeangry.png"
image side jack nudeangry2 = "side_image/side_jack_nudeangry2.png"

define e = Character("Elyse", 
        color = "#4DFFA6", 
        image = "elyse",
        what_color= "#4DFFA6")

image side elyse sad = "side_image/side_elyse_sad.png"
image side elyse kiss = "side_image/side_elyse_kiss.png"
image side elyse happy = "side_image/side_elyse_happy.png"
image side elyse jealous = "side_image/side_elyse_jealous.png"
image side elyse talk = "side_image/side_elyse_talk.png"
image side elyse talk2 = "side_image/side_elyse_talk2.png"
image side elyse talk3 = "side_image/side_elyse_talk3.png"
image side elyse skeptical = "side_image/side_elyse_skeptical.png"

image side elyse drunktalk2 = "side_image/side_elyse_drunktalk2.png"
image side elyse drunktalk3 = "side_image/side_elyse_drunktalk3.png"

image side elyse nudedrunktalk2 = "side_image/side_elyse_nudedrunktalk2.png"
image side elyse nudedrunktalk3 = "side_image/side_elyse_nudedrunktalk3.png"

image side elyse nudeskeptical = "side_image/side_elyse_nudeskeptical.png"
image side elyse nudetalk = "side_image/side_elyse_nudetalk.png"
image side elyse nudetalk2 = "side_image/side_elyse_nudetalk2.png"
image side elyse nudetalk3 = "side_image/side_elyse_nudetalk3.png"
image side elyse nudesad = "side_image/side_elyse_nudesad.png"
image side elyse nudekiss = "side_image/side_elyse_nudekiss.png"
image side elyse nudepleasure = "side_image/side_elyse_nudepleasure.png"
image side elyse nudejealous = "side_image/side_elyse_nudejealous.png"
image side elyse nudehappy = "side_image/side_elyse_nudehappy.png"

define j = Character("Jane", 
        color = "#007095", 
        image = "jane",
        what_color= "#007095")

image side jane angry = "side_image/side_jane_angry.png"
image side jane blow = "side_image/side_jane_blow.png"
image side jane pouty = "side_image/side_jane_pouty.png"
image side jane talk = "side_image/side_jane_talk.png"
image side jane talk2 = "side_image/side_jane_talk2.png"
image side jane skeptical = "side_image/side_jane_skeptical.png"

image side jane sslayer = "side_image/side_jane_sslayer.png"
image side jane sslayer2 = "side_image/side_jane_sslayer2.png"
image side jane sslayer3 = "side_image/side_jane_sslayer3.png"
image side jane sslayer4 = "side_image/side_jane_sslayer4.png"
image side jane sslayer5 = "side_image/side_jane_sslayer5.png"

image side jane gymangry = "side_image/side_jane_gymangry.png"
image side jane gympouty = "side_image/side_jane_gympouty.png"
image side jane gymskeptical = "side_image/side_jane_gymskeptical.png"
image side jane gymtalk = "side_image/side_jane_gymtalk.png"
image side jane gymtalk2 = "side_image/side_jane_gymtalk2.png"

image side jane dblow = "side_image/side_jane_dblow.png"
image side jane dpouty = "side_image/side_jane_dpouty.png"
image side jane dtalk = "side_image/side_jane_dtalk.png"
image side jane dtalk2 = "side_image/side_jane_dtalk2.png"
image side jane dpleasure1 = "side_image/side_jane_dpleasure1.png"
image side jane dpleasure2 = "side_image/side_jane_dpleasure2.png"
image side jane dskeptical = "side_image/side_jane_dskeptical.png"
image side jane dangry = "side_image/side_jane_dangry.png"

image side jane nudetalk = "side_image/side_jane_nudetalk.png"
image side jane nudetalk2 = "side_image/side_jane_nudetalk2.png"
image side jane nudepleasure1 = "side_image/side_jane_nudepleasure1.png"
image side jane nudepleasure2 = "side_image/side_jane_nudepleasure2.png"
image side jane nudeskeptical = "side_image/side_jane_nudeskeptical.png"
image side jane nudepouty = "side_image/side_jane_nudepouty.png"
image side jane nudeblow = "side_image/side_jane_nudeblow.png"
image side jane nudeangry = "side_image/side_jane_nudeangry.png"
image side jane nudeyummy = "side_image/side_jane_nudeyummy.png"



define a = Character("Andre", 
        color = "#FFFF00", 
        image = "andre",
        what_color= "#FFFF00")

image side andre angry = "side_image/side_andre_angry.png"
image side andre talk = "side_image/side_andre_talk.png"
image side andre talk2 = "side_image/side_andre_talk2.png"
image side andre sulk = "side_image/side_andre_sulk.png"
image side andre tongue = "side_image/side_andre_tongue.png"


image side andre njtalk = "side_image/side_andre_NJtalk.png"
image side andre njtalk2 = "side_image/side_andre_NJtalk2.png"

image side andre gymtongue = "side_image/side_andre_gymtongue.png"
image side andre gymtalk = "side_image/side_andre_gymtalk.png"
image side andre gymtalk2 = "side_image/side_andre_gymtalk2.png"
image side andre gymsulk = "side_image/side_andre_gymsulk.png"
image side andre gymangry = "side_image/side_andre_gymangry.png"

image side andre nudesulk = "side_image/side_andre_nudesulk.png"
image side andre nudetalk = "side_image/side_andre_nudetalk.png"
image side andre nudetalk2 = "side_image/side_andre_nudetalk2.png"
image side andre nudeangry = "side_image/side_andre_nudeangry.png"
image side andre nudepleasure1 = "side_image/side_andre_nudepleasure1.png"
image side andre nudepleasure2 = "side_image/side_andre_nudepleasure2.png"
image side andre nudetongue = "side_image/side_andre_nudetongue.png"

image side andre shirttalk = "side_image/side_andre_shirttalk.png"
image side andre shirttalk2 = "side_image/side_andre_shirttalk2.png"
image side andre shirtsulk = "side_image/side_andre_shirtsulk.png"
image side andre shirttongue = "side_image/side_andre_shirttongue.png"
image side andre shirtangry = "side_image/side_andre_shirtangry.png"


define edis = Character("Edis", 
        color = "#F34E52", 
        image = "edis",
        what_color= "#F34E52")

image side edis talk = "side_image/side_edis_talk.png"
image side edis smirk = "side_image/side_edis_smirk.png"
image side edis laugh = "side_image/side_edis_laugh.png"

image side edis nudelaugh = "side_image/side_edis_nudelaugh.png"
image side edis nudesmirk = "side_image/side_edis_nudesmirk.png"
image side edis nudetalk = "side_image/side_edis_nudetalk.png"

image side edis ttalk = "side_image/side_edis_ttalk.png"
image side edis ttalk2 = "side_image/side_edis_ttalk2.png"
image side edis scream = "side_image/side_edis_scream.png"
image side edis insane = "side_image/side_edis_insane.png"
image side edis aangry = "side_image/side_edis_aangry.png"
image side edis aangry2 = "side_image/side_edis_aangry2.png"

define amir = Character("Amir", 
        color = "#B25900", 
        image = "amir",
        what_color= "#B25900")

image side amir angry = "side_image/side_amir_angry.png"
image side amir pleasure = "side_image/side_amir_pleasure.png"
image side amir talk = "side_image/side_amir_talk.png"
image side amir smile = "side_image/side_amir_smile.png"

image side amir nudetalk = "side_image/side_amir_nudetalk.png"
image side amir nudesmile = "side_image/side_amir_nudesmile.png"
image side amir nudepleasure = "side_image/side_amir_nudepleasure.png"
image side amir nudeangry = "side_image/side_amir_nudeangry.png"



define d = Character("Dahlia", 
        color = "#FF2626", 
        image = "dahlia",
        what_color= "#FF2626")
image side dahlia talk = "side_image/side_dahlia_talk.png"
image side dahlia talk2 = "side_image/side_dahlia_talk.png"
image side dahlia surprised = "side_image/side_dahlia_surprised.png"
image side dahlia pleasure = "side_image/side_dahlia_pleasure.png"

image side dahlia angry = "side_image/side_dahlia_angry.png"
image side dahlia angry2 = "side_image/side_dahlia_angry2.png"
image side dahlia angry3 = "side_image/side_dahlia_angry3.png"


define shp = Character("Karin",
        color = "#8C0000", 
        image = "karin",
        what_color= "#8C0000")
image side karin talk = "side_image/side_karin_talk.png"
image side karin nudetalk = "side_image/side_karin_nudetalk.png"

define aur = Character("Aurora",
        color = "#486DA2", 
        image = "aurora",
        what_color= "#486DA2")
image side aurora talk = "side_image/side_aurora_talk.png"
image side aurora nudetalk = "side_image/side_aurora_nudetalk.png"
image side aurora ctalk = "side_image/side_aurora_ctalk.png"

define l = Character("Lexa", 
        color = "#008C00", 
        image = "lexa",
        what_color= "#008C00")

image side lexa cangry = "side_image/side_lexa_cangry.png"
image side lexa cangry2 = "side_image/side_lexa_cangry2.png"
image side lexa cworried = "side_image/side_lexa_cworried.png"
image side lexa cpain = "side_image/side_lexa_cpain.png"

image side lexa angry = "side_image/side_lexa_angry.png"
image side lexa doubt = "side_image/side_lexa_doubt.png"
image side lexa eyebrow = "side_image/side_lexa_eyebrow.png"
image side lexa pain = "side_image/side_lexa_pain.png"
image side lexa talk = "side_image/side_lexa_talk.png"
image side lexa closedeyes = "side_image/side_lexa_closedeyes.png"
image side lexa pleasure = "side_image/side_lexa_pleasure.png"


image side lexa aangry = "side_image/side_lexa_aangry.png"
image side lexa adoubt = "side_image/side_lexa_adoubt.png"
image side lexa aeyebrow = "side_image/side_lexa_aeyebrow.png"
image side lexa apain = "side_image/side_lexa_apain.png"
image side lexa atalk = "side_image/side_lexa_atalk.png"
image side lexa aclosedeyes = "side_image/side_lexa_aclosedeyes.png"
image side lexa apleasure = "side_image/side_lexa_apleasure.png"

image side lexa utalk = "side_image/side_lexa_utalk.png"


define chloe = Character("Chloe", 
        color = "#006DD9", 
        image = "chloe",
        what_color= "#006DD9")

image side chloe sigh = "side_image/side_chloe_sigh.png"
image side chloe kiss = "side_image/side_chloe_kiss.png"
image side chloe yummy2 = "side_image/side_chloe_yummy2.png"
image side chloe talk = "side_image/side_chloe_talk.png"
image side chloe talk2 = "side_image/side_chloe_talk2.png"
image side chloe talk2x = "side_image/side_chloe_talk2x.png"
image side chloe angry = "side_image/side_chloe_angry.png"

image side chloe nudesigh = "side_image/side_chloe_nudesigh.png"
image side chloe nudekiss = "side_image/side_chloe_nudekiss.png"
image side chloe nudetalk = "side_image/side_chloe_nudetalk.png"
image side chloe nudetalk2 = "side_image/side_chloe_nudetalk2.png"
image side chloe nudetalk2x = "side_image/side_chloe_nudetalk2x.png"
image side chloe nudepleasure = "side_image/side_chloe_nudepleasure.png"
image side chloe nudeyummy = "side_image/side_chloe_nudeyummy.png"
image side chloe nudeyummy2 = "side_image/side_chloe_nudeyummy2.png"

image side chloe snsigh = "side_image/side_chloe_snsigh.png"
image side chloe sntalk = "side_image/side_chloe_sntalk.png"
image side chloe snpleasure = "side_image/side_chloe_snpleasure.png"
image side chloe snkiss = "side_image/side_chloe_snkiss.png"
image side chloe sntalk2 = "side_image/side_chloe_sntalk2.png"
image side chloe sntalk2x = "side_image/side_chloe_sntalk2x.png"
image side chloe snangry = "side_image/side_chloe_snangry.png"
image side chloe snyummy2 = "side_image/side_chloe_snyummy2.png"


define m = Character("Melisa", 
        color = "#FFC926", 
        image = "melisa",
        what_color= "#FFC926")

image side melisa angry = "side_image/side_melisa_angry.png"
image side melisa pleasure = "side_image/side_melisa_pleasure.png"
image side melisa talk = "side_image/side_melisa_talk.png"
image side melisa talk2 = "side_image/side_melisa_talk2.png"
image side melisa openmouth = "side_image/side_melisa_openmouth.png"
image side melisa smile = "side_image/side_melisa_smile.png"
image side melisa yummy = "side_image/side_melisa_yummy.png"

image side melisa nudeangry = "side_image/side_melisa_nudeangry.png"
image side melisa nudepleasure = "side_image/side_melisa_nudepleasure.png"
image side melisa nudetalk = "side_image/side_melisa_nudetalk.png"
image side melisa nudeyummy = "side_image/side_melisa_nudeyummy.png"
image side melisa nudesmile = "side_image/side_melisa_nudesmile.png"
image side melisa nudeopenmouth = "side_image/side_melisa_nudeopenmouth.png"
image side melisa nudetalk2 = "side_image/side_melisa_nudetalk2.png"


define v = Character("Victor", 
        color = "#BFFFDF", 
        image = "victor",
        what_color= "#BFFFDF")

image side victor dream = "side_image/side_victor_dream.png"
image side victor talk = "side_image/side_victor_talk.png"
image side victor observing = "side_image/side_victor_observing.png"

image side victor nudedream = "side_image/side_victor_nudedream.png"
image side victor nudetalk = "side_image/side_victor_nudetalk.png"
image side victor nudeobserving = "side_image/side_victor_nudeobserving.png"


define cass = Character("Cassandra",
        color = "#A64DFF",
        image="cass",
        what_color="#A64DFF")

image side cass angry = "side_image/side_cass_angry.png"
image side cass considering = "side_image/side_cass_considering.png"
image side cass talk = "side_image/side_cass_talk.png"
image side cass talk2 = "side_image/side_cass_talk2.png"
image side cass yummy = "side_image/side_cass_yummy.png"
image side cass unhappy = "side_image/side_cass_unhappy.png"

image side cass pangry = "side_image/side_cass_pangry.png"
image side cass ptalk = "side_image/side_cass_ptalk.png"
image side cass pthinking = "side_image/side_cass_pthinking.png"
image side cass punhappy = "side_image/side_cass_punhappy.png"
image side cass ppleasure = "side_image/side_cass_ppleasure.png"
image side cass ppleasure2 = "side_image/side_cass_ppleasure2.png"


image side cass undythinking = "side_image/side_cass_thinking.png"
image side cass undytalk = "side_image/side_cass_undytalk.png"
image side cass undytalk2 = "side_image/side_cass_undytalk2.png"
image side cass undyangry = "side_image/side_cass_undyangry.png"
image side cass undypleasure = "side_image/side_cass_undypleasure.png"
image side cass undypleasure2 = "side_image/side_cass_undypleasure2.png"

image side cass nudeangry = "side_image/side_cass_nudeangry.png"
image side cass nudetalk = "side_image/side_cass_nudetalk.png"
image side cass nudetalk2 = "side_image/side_cass_nudetalk2.png"
image side cass nudeconsidering = "side_image/side_cass_nudeconsidering.png"
image side cass nudethinking = "side_image/side_cass_nudethinking.png"
image side cass nudeunhappy = "side_image/side_cass_nudeunhappy.png"
image side cass nudepleasure = "side_image/side_cass_nudepleasure.png"
image side cass nudepleasure2 = "side_image/side_cass_nudepleasure2.png"

image side cass dressangry = "side_image/side_cass_dressangry.png"
image side cass dressconsidering = "side_image/side_cass_dressconsidering.png"
image side cass dresstalk = "side_image/side_cass_dresstalk.png"
image side cass dresstalk2 = "side_image/side_cass_dresstalk2.png"
image side cass dressyummy = "side_image/side_cass_dressyummy.png"
image side cass dressunhappy = "side_image/side_cass_dressunhappy.png"
image side cass dresspleasure = "side_image/side_cass_dresspleasure.png"
image side cass dresspleasure2 = "side_image/side_cass_dresspleasure2.png"


#Chapter 2 & 3 images-----------------------------------------------------------------------------------
image janedinnerfeet1c = "chapter 2/janedinnerfeet1.jpg"
image janedinnerfeet2d = "chapter 2/janedinnerfeet2.jpg"

image elysebreakfasteating = "chapter 3/elysebreakfasteating.jpg"
image elysebreakfast0x = "chapter 3/elysebreakfast0x.jpg"
image elyse breakfast 1 = "chapter 3/elysebreakfast1.jpg"
image elyse breakfast 2 = "chapter 3/elyse breakfast 2.jpg"
image elyse breakfast 3 = "chapter 3/elysebreakfast3.jpg"
image elyse breakfast 4 = "chapter 3/elysebreakfast4.jpg"
image elyse breakfast 5 = "chapter 3/elysebreakfast5.jpg"











#------------------------------------------------------------------------------------------------------

image bjdoc1 = "chapter 1/melisa undress 1.jpg"
image bjdoc2 = "chapter 1/melisa bj 1.jpg"
image bjdoc3 = "chapter 1/melisa bj 2.jpg"
image bjdoc3x = "chapter 1/melisa bj 2x.jpg"
image bjdoc4 = "chapter 1/melisa bj 3.jpg"
image bjdoc5 = "chapter 1/melisa bj 4.jpg"
image bjdoc6 = "chapter 1/melisa bj 5.jpg"
image bjdoc7 = "chapter 1/melisa bj 6.jpg"
image bjdoc8 = "chapter 1/melisa bj 7.jpg"
image bjdoc9 = "chapter 1/melisa bj 8.jpg"
image bjdoc10 = "chapter 1/melisa bj 9.jpg"
image bjdoc11 = "chapter 1/melisa bj 10.jpg"
image bjdoc12 = "chapter 1/melisa bj 11.jpg"
image bjdoc13 = "chapter 1/melisa bj 12.jpg"
image bjdoc14 = "chapter 1/melisa bj 2.jpg"
image bjdoc14x = "chapter 1/melisa bj 2x.jpg"

image feetdoc1 = "chapter 1/melisa feet 1.jpg"
image feetdoc2 = "chapter 1/melisa feet 2.jpg"
image feetdoc3 = "chapter 1/melisa feet 3.jpg"
image feetdoc4 = "chapter 1/melisa feet 4.jpg"
image feetdoc5 = "chapter 1/melisa feet 5.jpg"
image feetdoc6 = "chapter 1/melisa feet 6.jpg"
image feetdoc7 = "chapter 1/melisa feet 7.jpg"
image feetdoc8 = "chapter 1/melisa feet 8.jpg"
image feetdoc9 = "chapter 1/melisa feet 9.jpg"
image feetdoc10 = "chapter 1/melisa feet 10.jpg"
image feetdoc11 = "chapter 1/melisa feet 11.jpg"
image feetdoc12 = "chapter 1/melisa feet 12.jpg"

image mcstretching = "chapter 4/mc stretching.jpg"
image chloecumming = "chapter 4/chloe cumming.jpg"
image hallwaylistening = "chapter 4/hallway listening.jpg"

#define flash = Fade(0.1, 0.0, 0.2, color="#fff")
define slowfade = Fade(1.0, 0.5, 1.0)
define fadehold = Fade(0.5, 1.0, 0.5)
define fasterfadeout = Fade(0.5, 0.5, -1)
define slowfadeout = Fade(0.5, 0.5, 1)
define fadein = Fade(1.8, 1.0, -0.5)
define fadeout = Fade(0.0, 0.5, 1.0)

define fasterfadein = Fade(0.6, 1.0, -0.5)

define flash = Fade(.25, 0, .75, color="#fff")
init:
    image white = Solid((255, 255, 255, 255))
    
define flashlong = Fade(4.95, 0.0, .75, color="#fff")

image choice_overlay = "gui/choice_overlay.png"

define pushright = PushMove(0.3, "pushright")
define pushleft = PushMove(0.3, "pushleft")
define pushup = PushMove(0.3, "pushup")
define pushdown = PushMove(0.3, "pushdown")

#animations
image backalley_animated:
    "chapter 1/back alley 6.jpg" with Dissolve(0.5)
    1
    "chapter 1/back alley 5.jpg" with Dissolve(0.5)
    1
    repeat

image melisaoffice_animated:
    "chapter 1/melisa bj 5.jpg" with Dissolve(0.5)
    1
    "chapter 1/melisa bj 6.jpg" with Dissolve(0.5)
    2
    repeat
    
image melisaoffice2_animated:
    "chapter 1/melisa bj 6.jpg" with Dissolve(0.5)
    1
    "chapter 1/melisa bj 7.jpg" with Dissolve(0.5)
    2
    repeat
    
image melisaoffice3_animated:
    "chapter 1/melisa feet 4.jpg" with Dissolve(0.5)
    1
    "chapter 1/melisa feet 5.jpg" with Dissolve(0.5)
    2
    repeat
    
image melisaoffice4_animated:
    "chapter 1/melisa feet 5.jpg" with Dissolve(0.5)
    0.6
    "chapter 1/melisa feet 6.jpg" with Dissolve(0.5)
    1.3
    repeat
    
image melisaoffice5_animated:
    "chapter 1/melisa feet 12.jpg" with Dissolve(0.4)
    0.4
    "chapter 1/melisa feet 11.jpg" with Dissolve(0.4)
    0.4
    "chapter 1/melisa feet 10.jpg" with Dissolve(0.4)
    0.4
    "chapter 1/melisa feet 11.jpg" with Dissolve(0.4)
    0.4
    repeat


    
init:
    $ renpy.music.register_channel("ambient","sfx",True,tight=True)
#This code is registering a sound channel named "ambient". You can use it for sound effects that you will want to play in a continuous loop (like rain, wind or a clock ticking). You can use it with


#animations
# The game starts here.
label start:
    $ change_cursor("1")
    scene black
    stop music fadeout 5.0
    
    play music "music/crystal hunter.mp3" fadein 10.0
    
    $ player_name = renpy.input("Karakterinizin adını girin \n(veya entera basıp varsayılan ismi seçin.)", length=10, with_none=None, pixel_width=None)
# The .strip() instruction removes any extra spaces the player 
# may have typed by accident.

#  If the player can't be bothered to choose a name, then we
#  choose a suitable one for them:
    if player_name == "":
        $ player_name="Peter"

    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    "Location: United States \nYear: 2080"

    #A ntr scene is about to start

   # if persistent.show_ntr:
   #     #Ntr scene
   #     "NTR enabled scene"
   #     "Sex, sex, sex..."

    #Here continues the non ntr scene
   # "At the next day..."
    #...

    "Earth has advanced incredibly in technology the past decades and humans became intergalactic species. Other races and creatures emerged and made Earth their new home."

    "You and your family have been selected to participate in a social space program that lasts from a few months up to a year. Everyone who makes it until the end will receive a handsome reward for participating. For you that reward will be multiplied since
     your whole family will participate."

    "You still feel extremely lucky to be given the chance to participate though, and so is your family. Today is the day. A briefing and quick medical examination awaits you before arriving on the spaceship."

    "This is where your story begins."
    
    z "\"Dad...\""
    z "\"Wake up.\""

# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.

    $ quick_menu = False
    menu:
        "Open your eyes":
            jump wakingup1

    label wakingup1:
        
    $ quick_menu = True
    
    scene waking up 1
    with slowfade
    
    z pyjamatalk"\"Dad, wake up.\""
    
    
    scene waking up 2
    with slowfade
    
    z pyjamatalk "\"Dad!\""
    
    
    scene waking up 3 with vpunch
    
    mc nudeshocked "\"What??\""
    mc nudetalk "\"What are you doing, Zoey!?\""
    
    
    scene waking up 4
    with dissolve
    
    z pyjamahappy "\"Daddy!\""
    
    
    scene waking up 6
    with dissolve
    
    z pyjamawink "\"Rough night?\"" 
    z pyjamawink "\"Hahaha.\""
    
    
    scene waking up 7
    with dissolve
    
    mc nudetalk3 "\"Keep it quiet, you will wake your mom.\""
    mc nudetalk2 "\"Anyway, why are you up so early?\""
    
    
    scene waking up 5
    with dissolve
    
    z pyjamatalk "\"Did you forget?\""
    z pyjamatalk "\"We have to get ready and prepare to leave! We shouldn't be late.\""
    
    mc nudetalk "\"I didn't forget, of course. But, we still have about an hour more to sleep...\"" 
    "..."
    "..."
    "..."
    mc nudetalk2 "\"You will bug me until we start preparing won't you?\""
    
    z pyjamahappy "\"Yup!\""
    
    mc nudetalk3 "\"Sigh...\""
    mc nudetalk "\"Fine... Go and wake your sister up. I will start preparing too.\""
    
    z pyjamahappy "\"Yay! Sounds like a plan. Don't forget to wake up mom.\""
    
    
    scene waking up 8
    with dissolve
    
    mc nudethinking "{i}Oh...{/i}"
    
    $ quick_menu = False
    
    menu:
        "Look closer":
            $ quick_menu = True
            scene waking up 9
            with dissolve
            $ watched_zoey1 = True
            mc nudethinking "{i}My little girl sure has grown... She will be breaking hearts in no time.{/i}"
            mc nudethinking "{i}She has her mother's...{/i}"
            mc nudethinking "{i}assets.{/i}"
            mc nudethinking "{i}I wonder how much she has really grown...{/i}"
            
            $ quick_menu = False
            menu:
                "Imagine":
                    $ quick_menu = True
                    scene waking up 9 nude
                    with dissolve
                    mc nudethinking "{i}If I had to guess how much she has really grown...{/i}"
                    mc nudethinking "{i}It will be nothing less than perfection.{/i}"
                    mc nudethinking "{i}After all, she has my genes.{/i}"
                    "Zoey leaves the room."
                    
                    
        "It's wrong":
            $ quick_menu = True
            scene waking up 8
            with dissolve
            $ watched_zoey1 = False
            mc nudethinking "{i}I shouldn't look...{/i}"
            mc nudethinking "{i}I can't believe I was even considering that. She is my daughter...{/i}"
            
            
    scene a few moments later
    $ quick_menu = False
    with fasterfadein
    pause 2.0
    with fasterfadeout
    
    
    scene waking up 10
    $ quick_menu = True
    with fasterfadein
    
    
    mc nudethinking "{i}What was she thinking sitting on me like that...{/i}"
    mc nudethinking "{i}I have a boner and I am not sure if it's because of the morning...{/i}"
    mc nudethinking "{i}This is wrong... Even having thoughts about this concerns me.{/i}"
    mc nudethinking "{i}Let's forget this ever happened and move on.{/i}"
    mc nudethinking "{i}I will go take a shower and dress up.{/i}"
    mc nudethinking "{i}But before that I should wake up Cass, just in case. She does like to sleep in late.{/i}"
    
    scene waking up 11
    with dissolve
    
    mc nudetalk2 "\"Hey, hun.\""
    mc nudetalk "\"We should start preparing to leave soon. I will go and take a shower.\""
    
    
    scene waking up 11x2
    with dissolve
    
    cass undytalk "\"5 more mins and I am up.\""
    cass undythinking "\"Promise.\""
    
    
    scene waking up 11
    with dissolve
    
    mc nudethinking "{i}Why am I not convinced?{/i}"
    mc nudetalk2 "\"Sure, hun. I will get the remaining luggage ready as well.\""
    cass undytalk2 "\"Thank you, dear.\""
    

    scene waking up 12
    with fade
    
    mc nudethinking "{i}Look at me, even when I am going in my 40's I have the body of a teenager.{/i}"
    mc nudethinking "{i}Although my wife is 5 years older than me, she still looks amazing as well.{/i}"
    mc nudethinking "{i}I gotta say, I am very lucky in many ways.{/i}"
    mc nudethinking "{i}I have 2 beautiful daughters, beautiful wife, we got chosen for this space social program. Which is actually really well paid, if we last until the end.{/i}"
    mc nudethinking "{i}I know right? A space vacation that you get paid to go to.{/i}"
    mc nudethinking "{i}I couldn't even imagine such a thing 20 years ago.{/i}"
    mc nudethinking "{i}Everything seems to be going great so far.{/i}"
    mc nudethinking "{i}Anyway, enough about that, time to get a shower and dress up.{/i}"
    
    $ quick_menu = False
    
    menu:
        "Take a shower":
            jump twentyfiveminslater

    label twentyfiveminslater:
        
    $ quick_menu = True
    
    with fasterfadein
    
    scene 25 mins later
    $ quick_menu = False
    pause 2.5
    with fasterfadeout
    
    scene waking up 13
    $ quick_menu = True
    with fasterfadein
    
    mc milthinking "{i}I think I will use my military uniform. I want to make good first impressions.{/i}"
    mc milthinking "{i}My military accomplishments alongside Zoey's involvment in helping with that cryosleep experiment program that lasted a few years, really helped our family's chances of being picked.{/i}"
    mc milthinking "{i}I think we are also the only full family that will be going.{/i}"
    mc milthinking "{i}Even though there won't be that many people to begin with.{/i}"
    mc milthinking "{i}I should go and check on Elyse and see if Zoey actually woke her up.{/i}"
    
    
    scene waking up 14
    with fade
    
    mc milthinking "{i}This is Elyse's room.{/i}"
    mc milthinking "{i}Should I knock or just enter?{/i}"
    $ quick_menu = False
    menu:
        "Knock":
            $ quick_menu = True
            scene waking up 15
            with dissolve
            $ watched_elyse1 = False
            "*knock* *knock*"
            mc miltalk "\"El, are you up?\""

            e "\"I am dressing! I will be out in a few minutes.\""

            mc miltalk2 "\"Okay!\""
            mc milthinking "{i}Well I guess that's that...{/i}"
        "Enter ":
            scene waking up 16
            with dissolve
            scene elyse close up with fade:
                subpixel True
                yalign 1.0
                pause 2.0
                linear 7.0 yalign 0.0
            pause
            scene waking up 16
            with dissolve
            $ quick_menu = True
            $ watched_elyse1 = True
            mc milthinking "{i}Oh... my... god...{/i}"
            mc milthinking "{i}She is...{/i}"
            mc milthinking "{i}definitely...{/i}"
            mc milthinking "{i}up...{/i}"
            if watched_zoey1:
                mc milthinking "{i}I can't decide whether she has grown to have better 'backside' ... or my younger daughter has.{/i}" 
                mc milthinking "{i}I guess that is to be decided some other day, as I haven't actually seen Zoey... this much, outside of my mind that is.{/i}" 
                mc milthinking "{i}Anyway... I should bolt and get the hell out of here before she notices.{/i}"
            else:
                mc milthinking "{i}I should bolt and get the hell out of here before she notices.{/i}"
                jump wakingup10

    label wakingup10:
    scene waking up 17
    with fadein
    mc milthinking "{i}I wonder how long I will have to wait now...{/i}"
    mc milthinking "{i}It's not like I didn't expect this though.{/i}"
    
    with fasterfadein
    scene one eternity later
    $ quick_menu = False
    pause 2.5
    with fasterfadeout
    
    scene waking up 18
    with fasterfadein
    $ quick_menu = True
    cass talk "\"So How do I look?\""
    mc miltalk3 "\"Wow...\""
    mc miltalk2 "\"You look ravishing, Cass.\""
    cass talk2 "\"Mmm... I do like compliments like that.\""
    mc miltalk "\"Men might look at you a lot and I might get jealous.\""
    cass talk "\"Haha. Don't joke like that. I am out of fashion.\""
    mc miltalk2 "\"Well, you don't look out of fashion to me.\""
    
    scene waking up 19
    with dissolve
    cass talk2 "\"I certainly hope not!\""
    mc milsmileshocked "\"All things considered, I still can't believe they let all 4 of us participate.\""
    cass considering "\"I know right?\""
    cass talk "\"It's kind of weird, considering there is already so few spots, but I guess they had to include a family in?\""
    cass talk2 "\"We shouldn't question it. Let's just be glad.\""
    mc miltalk3 "\"I totally agree with you.\""
    mc miltalk2 "\"They said they will come and pick us up 1 by 1 too which is a bit strange, but I guess that's their policy.\""
    cass talk "\"Yeah, I think so.\""
    scene waking up 20
    with dissolve
    z happy "\"Ready!\""
    mc miltalk "\"Great. Only Elyse is left then.\""
    scene waking up 21
    with dissolve
    e talk "\"Surprise!!\""
    scene waking up 22
    with dissolve
    mc milsmileshocked "\"Oh, that was fast.\""
    mc miltalk2 "\"Good morning, El!\""
    e talk2 "\"Morning.\""
    scene waking up 21
    with dissolve
    mc miltalk "\"So you guys prepared everything?\""
    e talk3 "\"Yeah.\""
    z talk "\"Yup!\""
    cass considering "\"The question is, did you?\""
    mc miltalk3 "\"I think so, but even if I didn't I don't need as much stuff as you girls do.\""
    "*knock* *knock* *knock*"
    qm "\"[mc]? Your ride has arrived!\""
    mc miltalk2 "\"Oh... already? I guess it's time to go.\""
    scene waking up 23
    with dissolve
    pause 2.5
    with fasterfadeout
    
    scene waking up 24
    with fasterfadein
    
    mc miltalk "\"Okay, girls. We will meet again in a few hours.\""
    mc miltalk "\"Listen carefully to their instructions, be good and everything will be alright.\""
    mc miltalk "\"Love you all.\""
    e talk "\"See you soon, dad. Love you.\""
    z desire "\"Stay safe, daddy!\""
    cass talk "\"I love you too, hun. Don't worry about anything. The girls know how to take care of themselves now.\""
    mc miltalk "\"I know and they will have us if anything happens. Gotta go now, I don't want to keep the driver waiting.\""
    
    scene car outside 1
    with fadein
    qm drivertalk2 "\"Good day. My name is Alex and I was assigned to be your driver today.\""

    scene car outside 2
    alex talk "\"Please, let me take care of the luggage and you get comfortable.\""
    mc miltalk3 "\"Nice to meet you, Alex and wow\""
    mc miltalk2 "\"That is quite the ride you got.\""
    scene car outside 1
    with dissolve
    alex talk3 "\"Glad you like it, mister.\""
    alex talk "\"I am taking you to a quick briefing after which you'd get an examination from a doctor and then I will take you straight to the ship itself.\""
    alex talk2 "\"We'll be there in approximately 10 minutes.\""
    mc miltalk2 "\"Sounds good to me.\""

    scene driver 2
    pause 2.5
    with fasterfadein
    
    scene 10 mins later
    $ quick_menu = False
    pause 2.5
    with fasterfadeout

    
    scene driver 3
    with fasterfadein
    $ quick_menu = True
    alex talk "\"I will be waiting for you outside the doc's office whenever you're done.\""
    mc miltalk "\"Alright, sounds good.\""
    with fasterfadeout
    
    scene door knock 1
    with fadein
    "You arrive at the office for the briefing"
    $ quick_menu = False
    menu:
        "Knock":
            jump knockondoor

    label knockondoor:
    $ quick_menu = True
    scene door knock 2
    "You knock on the door."
            
    qm "\"Come on in.\""
    scene office
    qm "\"You must be [mc].  Please, sit down. My name is Jack. I am here to give you a brief
    explanation of what you can expect in the next few months.\""
   
    
    scene office 1
   
    mc miltalk3 "\"Nice to meet you, Jack. Me and my family are really excited to be a part of this.\""
    
    jack talk "\"I am really glad to hear that, [mc]. I am here to give you a quick rundown of what's to come.\""
    jack stare "\"I see from your profile and clothing that you were in the military and even your younger daugther,
               Zoey, was a part of the test group in the cryosleep technology we were developing.\""

    mc miltalk2 "\"That's correct. My younger daughter was a part of that...\""

    scene vessel chloe
    with fadein


    mc miltalk3 "\"Even though she is 18 now, she looks way younger than she should because of the few years spent in there.\""
    mc miltalk2 "\"She was really brave and happy to be able to help out with something.\""
    mc miltalk "\"I am just glad she will be with me on the cruise.\""

    
    scene office 1
    with fadein
    jack talk "\"I am also happy for you and your family.\""
    jack stare "\"As you might be aware, we had a lot of candidates for this.\""
    jack stare "\"So we had to kind of make a priority list and people with at least some kind of contribution will have a slightly better chance.\""
    jack talk "\"We also needed at least one full family to be participating, so you were the lucky ones!\""
    jack talk "\"I am glad the program let's your whole family participate. But do remember that if one
               of you get disqualified, you all do. Which increases the risk a lot with each additional member of your family.\""
    
    
    jack stare "\"You just have to follow the general rules and there won't be any issue.
               Otherwise a disqualification might occur and you won't get any compensation for the time spent in there. And depending on your actions you might also be charged for damage caused.
                This is a multi-billion social project, so quitting is not advised, unless it's a matter of life and death.\""

    
    jack talk "\"The ship itself is called 'Paradise 1337-69' and for the most part it will feel like home to you. We made sure a lot of the rooms
                look very similar to what you'd be used to here on Earth. Although, at first, you will all be in a common sleeping area. You will be briefed
                further on that topic when you arrive there.\""

    jack talk "\"I will also be on board to make sure everything goes smoothly, as well as the doctor that will give you the mandatory medical examination in a few minutes from now.\""

    jack stare "\"If you have any questions you can ask me now or later either me, Melisa which is our doctor or Ruby, our android.\""
    
    mc miltalk "\"I don't have any questions right now, Jack. Thanks.\""
    
    jack talk "\"You're free to proceed to your examination then. You know the location, correct?\""
    
    scene office 2
    with dissolve
    mc miltalk2 "\"Yup. I got the coordinates. It's 2 blocks away from here.\""
    
    jack talk "\"That's correct. Well, good luck and I will see you on Paradise.\""
    
    mc miltalk3 "\"Thanks, see you.\""

    scene black
    with fadein
    "You leave and start walking towards the doc."
    
    scene homeless 1
    with fadein
    qm strangertalk2 "\"Hey, mister.\""
    scene homeless 2
    with dissolve
    
    qm strangertalk "\"Can you spare 2 minutes of your time?\""
    $ quick_menu = False
    menu:
        "Yes":
            $ quick_menu = True
            mc miltalk2 "\"Sure, what is it?\""
            qm strangertalk "\"You might be thinking that I am just a beggar.\""
            qm strangertalk2 "\"But I actually want to offer you something.\""
            qm strangertalk2 "\"You see...\""
            qm strangertalk "\"I know where you're going and what will mostly occur.\""
            "..."
            mc miltalk "\"I don't understand?\""
        "No":
            $ quick_menu = True
            mc miltalk2 "\"Sorry, man. I don't have any change.\""
            "You start to walk away"
            qm strangertalk2 "\"I will make it worth your while, [mc]. I promise.\""
            mc milshocked2 "\"What the hell? How do you know my name?\""
            
    qm strangertalk "\"Let me explain.\""
    qm strangertalk2 "\"Let's say that I know the people who are offering you this 'wonderful' way to make a lot of money by vising space on a tourist trip for a few months.\""
    qm strangertalk2 "\"Something unheard of, sure.\""
    qm strangertalk2 "\"I can tell you that they are not telling you the whole truth.\""
    qm strangertalk2 "\"That this is not just another social program.\""
    qm strangertalk "\"I can also tell you what will happen once you enter that doctor's office.\""
    mc milshocked2 "\"What!?\""
    qm strangertalk2 "\"You will be given an examination, sure. But that won't be the only thing. She will give you an injection and she will say it will be to 'help' your immune system in space.\""
    qm strangertalk2 "\"Which isn't the case. She will inject you with a new serum they've developed that temporarily causes amnesia on the part of the brain which stores memories of relatives and loved ones.\""
    mc milshocked2 "\"What the hell?\""
    qm strangertalk2 "\"She will also offer to give you a pill for the headache that you might get after she injects you with it.\""
    qm strangertalk2 "\"It's an experimental serum that is used to wipe and mind control captured enemy troops in giving out secrets of their homeland. The most prime example would be Russia.\""
    qm strangertalk2 "\"You mustn't worry though. Your family won't lose their memories permanently. They will be stored. I am unfamiliar with how the whole process works, but I know the effect lasts only a particular set of time.\""
    qm strangertalk2 "\"Which most likely will be the duration of your stay up there.\""
    qm strangertalk "\"I can offer you and only you an alternative though. I have a special pill that will negate the effect of that serum. It also helps reduce headache which you will get once the serum has been injected.\""
    mc miltalk2 "\"You're delusional. You have to be. I can't believe what I am hearing.\""
    qm strangertalk2 "\"Am I really, [mc]? You want more proof?\""
    qm strangertalk2 "\"How about this:\""
    qm strangertalk "\"I know your deepest secrets. I know all your preferences... I know you don't like mushrooms. I know your wife Cassandra of 15 years is 5 years older than you, I know you didn't get to pick your children's names
        and that you really need this money to get your children through college. Your job is not paid well enough to support your family that much. You still have mortgage to pay and I also know you get horny watc-\""
    mc milshocked2 "\"Okay! That's enough. Jesus Christ. I don't know how the hell you know all of this, but this is getting creepy.\""
    mc milshocked2 "\"What the hell do you get out of all of this?\""
    qm strangertalk2 "\"Well... I was going to ask for a $100. I think my precious information and my pill costs at least that much.\""
    qm strangertalk2 "\"I also like to help out someone in need, of course.\""
    scene homeless 3
    with dissolve
    qm strangertalk "\"If you take this red pill, you stay in Wonderland, and you will see how deep the rabbit hole goes.\""
    qm strangertalk2 "\"Or you don't and continue being an experimental sheep.\""
    $ quick_menu = False
    menu:
        "Pay him":
            $ quick_menu = True
            mc miltalk3 "\"Here's the money, give me this pill.\""
            scene homeless 4
            with dissolve
            qm strangertalk2 "\"Here, take it. You can swallow it whole as is right now.\""
            scene homeless 5
            with dissolve
            qm strangertalk "\"Or you can wait and see for yourself when everything I said happen.\""
            jump paidforpill
        "Leave":
            $ quick_menu = True
            mc milshocked "\"No thanks. I rather not waste $100 on what seems to be a fictional story.\""
            "You start to walk away"
            qm strangertalk2 "\"Hold on.\""
            qm strangertalk "\"How about this then...\""
            qm strangertalk2 "\"I will give you the pill without asking you to pay a cent right now.\""
            qm strangertalk2 "\"And if it does work you can find me back here and pay me back whenever you decide.\""
            qm strangertalk "\"You don't lose anything in the process.\""
            mc milthinking "{i}Well... he does have a point.{/i}"
            mc miltalk "\"Fine, old man. Give me the damn pill.\""
            scene homeless 5
            with dissolve
            qm strangertalk2 "\"Here, take it. You can swallow it whole as is right now.\""
            qm strangertalk "\"Or you can wait and see for yourself if you still doubt me.\""
            jump nopayforpill
            
    label paidforpill:
        $ quick_menu = False
        menu:
            "Take the pill now":
                $ quick_menu = True
                $ took_pill = True
                scene homeless 6
                with dissolve
                pause 2.0
                scene homeless 7
                with dissolve
                pause 2.0
                scene homeless 2
                with dissolve
                qm strangertalk "\"Wise choice.\""
                scene homeless 2
                with dissolve
                mc miltalk3 "\"I am not so sure about that.\""
                mc miltalk2 "\"For all I know you could've drugged me.\""
                qm strangerlaugh "\"Hahahahaha. Why would I waste a good drug on you?\""
                mc miltalk "\"Why would you waste a super special pill that can help fight against the amnesia you described?\""
                qm strangertalk "\"Why not? No one would need this as it fights only the serum I told you about. And I could make a few dollars with it from you.\""
                mc miltalk2 "\"I don't even know how you obtained it and I don't even want to know. I am already late for my appointment. Goodbye.\""
                qm strangertalk2 "\"Thanks for the cash and I hope it serves you well.\""
                qm strangertalk2 "\"Oh, another word of advice...\""
                qm strangertalk "\"When you are in dire need and believe me, you will know when that is, search for the witch Elisande. She will help you out.\""
                mc miltalk "\"... I will keep that in mind.\""
                jump afteroldman
                
            "Save it for later":
                $ quick_menu = True
                $ took_pill = False
                scene homeless 2
                with dissolve
                mc miltalk3 "\"I will decide later if you're even telling the truth.\""
                qm strangertalk2 "\"As you wish.\""
                qm strangertalk2 "\"Good luck on your adventure then.\""
                qm strangertalk "\"Don't forget about me if it helps you out.\""
                mc miltalk2 "\"Sure, whatever. We'll see if this is even true, old man.\""
                qm strangertalk2 "\"Oh, another word of advice...\""
                qm strangertalk "\"When you are in dire need and believe me, you will know when that is, search for the witch Elisande. She will help you out.\""
                mc miltalk "\"... I will keep that in mind.\""
                jump afteroldman
                
    label nopayforpill:
        $ quick_menu = False
        menu:
            "Take the pill now":
                $ quick_menu = True
                $ took_pill = True
                scene homeless 6
                with dissolve
                pause 2.0
                scene homeless 7
                with dissolve
                qm strangertalk "\"Wise choice.\""
                scene homeless 2
                with dissolve
                mc miltalk2 "\"I am not so sure about that.\""
                mc miltalk "\"For all I know you could've drugged me.\""
                qm strangerlaugh "\"Hahahahaha. Why would I waste a good drug on you?\""
                mc miltalk3 "\"Why would you waste a super special pill that can help fight against the amnesia you described?\""
                qm strangertalk2 "\"Why not? No one would need this as it fights only the serum I told you about. And I could make a few dollars with it from you.\""
                mc miltalk2 "\"I don't even know how you obtained it and I don't even want to know. I am already late for my appointment. Goodbye.\""
                qm strangertalk2 "\"Good luck and don't forget about me if it helps you on your journey.\""
                qm strangertalk2 "\"Oh, another word of advice...\""
                qm strangertalk "\"When you are in dire need and believe me, you will know when that is, search for the witch Elisande. She will help you out.\""
                mc miltalk "\"... I will keep that in mind.\""
                jump afteroldman
                
            "Save it for later":
                $ quick_menu = True
                $ took_pill = False
                scene homeless 2
                with dissolve
                mc miltalk3 "\"I will decide later if you're even telling the truth.\""
                qm strangertalk2 "\"As you wish.\""
                qm strangertalk2 "\"Good luck on your adventure then.\""
                qm strangertalk "\"Don't forget about me if it helps you out.\""
                mc miltalk2 "\"Sure, whatever. We'll see if this is even true, old man.\""
                qm strangertalk2 "\"Oh, another word of advice...\""
                qm strangertalk "\"When you are in dire need, and believe me you will know when that is, search for the witch Elisande. She will help you out.\""
                mc miltalk "\"... I will keep that in mind.\""
                jump afteroldman
                
    label afteroldman:
    mc milthinking "{i}Fuck... I took too long here. I must go right now.{/i}"            
    scene black
    with fadein
    "You leave in a hurry."
    
    scene back alley 1
    with fadein
    mc milthinking "{i}I will take this shortcut through this back alley which should lead me straight there.{w}{/i}"
    scene back alley 2
    with dissolve
    pause 2.5
    qm  "\"Ah... yes... bitch.\""
    qm "\"Suck it just like that...\""
    qm "\"Take it deeper.\""
    scene back alley 3
    with dissolve
    pause 2.5
    mc milthinking "What the hell is that?"
    $ quick_menu = False
    menu:
        "Investigate":
            $ quick_menu = True
            mc milthinking "{i}I  will check really quick...{/i}"
            $ watched_jane = True
            scene back alley 6
            with dissolve
            mc milthinking "{i}What the fuck?{/i}"
            qm amirpleasure"\"Ah...\""
            qm amirtalk"\"You are real good cock sleeve, you know that?\""
            qm janeblow"\"MM-MGH!\""
            qm amirtalk"\"What was that? You want it deeper?\""
            scene back alley 5
            with dissolve
            qm amirangry"\"Take it, you slut!\""
            qm janeblow"\"BUH-FUUH!\""
            
            $ quick_menu = False
            show screen my_skip
            $ renpy.show("backalley_animated")
            $ renpy.transition(Dissolve(1))
            $ renpy.pause(12, hard=True)

            label afterbackalley:
            hide screen my_skip
            
            $ quick_menu = True
            qm amirtalk"\"Time for you to eat your lunch, bitch.\""
            qm amirpleasure"\"Ahh-\""
            
            scene back alley 7
            with dissolve
            
            qm janepouty"\"MMGH...\""
            qm janeblow"\"GUHH...\""
            qm amirtalk"\"Ah, that was nice.\""
            
            scene back alley 4
            with dissolve
            
            qm amirangry"\"Why the fuck didn't you swallow?\""
            qm amirangry"\"Next time you better do it.\""
            
            mc milthinking "{i}Holy shit... I better get the hell out of here.{/i}"

        "Ignore and continue":
            $ quick_menu = True
            $ watched_jane = False
            mc milthinking "{i}It's probably nothing.{/i}"
            scene back alley 2
            with dissolve
            mc milthinking "{i}I don't have any time to lose either.{/i}"
            

    scene doc office 1
    with fadein
    "You arrive outside the doctor's office"
    $ quick_menu = False
    menu:
        "Knock":
            jump docknock
            
    label docknock:
    $ quick_menu = True
    scene doc office 2
    with dissolve
    qm "\"Come in!!\""
    scene doc office 3
    with dissolve
    pause 2.5
    "You approach the doctor"
    scene doc office 7
    with dissolve
    qm melisatalk"\"Hi there. I am Melisa and you must be [mc], I presume?\""
    scene doc office 8
    with dissolve
    m smile "\"I hope you don't mind me resting my feet a bit since I had a long day...\""
    mc miltalk2 "\"Oh not at all. Nice to meet you Melisa, yes that's me and I think I am a bit late, sorry about that.\""
    scene doc office 9
    with dissolve
    m talk "\"You are actually my last patient that I have to check and don't worry about that.\""
    mc miltalk "\"Oh? My family already passed through?\""
    scene doc office 7
    with dissolve
    m talk"\"Ah, yes I think your older daughter just left a few moments ago. I thought you met them on the way.\""
    mc miltalk2 "\"I didn't, but I will be seeing them soon enough.\""
    m smile "\"That's right!\""
    m talk "\"So, you ready to start?\""
    mc miltalk "\"Of course. What do I have to do?\""
    m smile "\"Just take off your jacket and shirt and give me your right arm.\""
    mc miltalk2 "\"Sure.\""
    mc milthinking "{i}Time to see if that old man was right.{/i}"
    m talk "\"I am gonna have to give you a quick injection to boost up your immune system.\""
    m smile "\"After all, we are going in space and this is mandatory procedure.\""
    mc milthinking "{i}What the fuck? He was actually right? No fucking way.{/i}"
    mc milthinking "{i}What do I do now? I have to continue playing dumb.{/i}"
    mc milthinking "{i}She can't find out that I know what I know.{/i}"
    scene doc office 7
    with dissolve
    m talk "\"[mc]?\""
    mc miltalk2 "\"Yes?\""
    m talk "\"Your arm please.\""
    scene doc office 4xx
    with dissolve
    pause 2.0
    mc miltalk "\"Oh... right, sorry about that.\""
    m smile "\"Don't worry about it.\""
    scene doc office 4x
    with dissolve
    pause 2.0
    "..."
    scene doc office 4
    with dissolve
    pause 2.0
    m talk "\"And... done!\""
    m talk "\"Now, you might get a small headache.\""
    m smile "\"I can give you a pill to help with that.\""
    mc milthinking "{i}Again... the old man was correct after all.{/i}"
    if took_pill:
        mc miltalk3 "\"No thanks. I already had a headache before coming here, so I took one. I will be fine.\""
        m talk"\"Oh. I see. That's fine then.\""
        m talk "\"I will continue with my examination then...\""
        scene doc office 5
        with dissolve
        m smile "\"You seem to be very healthy and in a good shape.\""
        mc miltalk2 "\"Haha. Thanks. I try to be.\""
        m yummy "\"Mmm... yes... indeed.\""
        m yummy "\"I wonder how healthy you are down there though...\""
        scene doc office 6
        with dissolve
        mc milthinking "{i}What the fuck?{/i}"
        mc milthinking "{i}What do I do now?{/i}"
        mc milthinking "{i}The old man didn't tell me how long it takes for the serum to take effect.{/i}"
        mc milthinking "{i}So she might suspect I already lost some of my memories.{/i}"
        mc milthinking "{i}Do I play along?{/i}"
        jump doctor_sequence1
    else:
        mc miltalk3 "\"Thanks. But I have a pill on me. I will take it right now.\""
        m smile "\"Sure. Here's a glass of water.\""
        mc miltalk2 "\"Thanks.\""
        scene melisa pill 1
        with dissolve
        pause 1.0
        scene melisa pill 2
        with dissolve
        pause 1.0
        scene melisa pill 3
        with dissolve
        pause 1.0
        scene melisa pill 4
        with dissolve
        pause 2.0
        scene doc office 5
        with dissolve
        mc miltalk "\"Thanks for the water.\""
        m talk "\"You're welcome.\""
        m smile "\"Now... to continue with my examination.\""
        scene doc office 5
        with dissolve
        m smile "\"You seem to be very healthy and in a good shape.\""
        mc miltalk2 "\"Haha. Thanks. I try to be.\""
        m yummy "\"Mmm... yes... indeed.\""
        m yummy "\"I wonder how healthy you are down there though...\""
        scene doc office 6
        with dissolve
        mc milthinking "{i}What the fuck?{/i}"
        mc milthinking "{i}What do I do now?{/i}"
        mc milthinking "{i}The old man didn't tell me how long it takes for the serum to take effect.{/i}"
        mc milthinking "{i}So she might suspect I already lost some of my memories.{/i}"
        mc milthinking "{i}Do I play along?{/i}"
        jump doctor_sequence1
    label doctor_sequence1:
        $ quick_menu = False
        menu:
            "Go along with it":
                $ quick_menu = True
                $ sex_melisa = True
                mc miltalk "\"Why don't you find out?\""
                scene black
                with fadeout
                m yummy "\"Mmm... Don't mind if I do.\""
                "Melisa removes her coat and you take off your pants"
                show bjdoc1
                with dissolve
                m smile "\"How about this:\""
                m talk "\"I will give you a choice between my pretty little mouth and my feet.\""
                m smile "\"There is no wrong choice here.\""
                mc milthinking "{i}I might as well 'pretend' to enjoy this I don't have a choice either way.{/i}"
                jump doctor_sequencechoice
            "Stop her":
                $ quick_menu = True
                $ sex_melisa = False
                mc miltalk "\"Sorry... I can't do this.\""
                scene doc office 10x
                with dissolve
                m talk "\"Oh...\""
                m talk "\"Um...\""
                mc milthinking "{i}For some reason she seems really surprised I turned her down.{/i}"
                mc milthinking "{i}I hope I didn't give myself out.{/i}"
                m angry "\"Of course... what was I thinking?\""
                m angry "\"You're all done with your examination.\""
                m angry "\"You can leave now.\""
                mc milthinking " I hope she doesn't suspect anything...\""
                mc miltalk2 "\"Thanks, Melisa and don't worry about it.\""
                jump doctor_sequencefinal
    label doctor_sequencechoice:
        $ quick_menu = False
        menu:
            "Use her mouth":
                $ quick_menu = True
                $ melisa_mouth1 = True
                $ melisa_feet1 = False
                mc nudetalk "\"Your mouth. Please.\""
                m smile "\"Good choice, babe.\""
                show bjdoc2
                with dissolve
                m smile "\"This will only get in the way.\""
                m talk "\"And I don't want to dirty my working clothes.\""
                mc nudetalk2 "\"No objections from me.\""
                m smile "\"Good. I wasn't going to take any.\""
                show bjdoc3
                with dissolve
                m nudesmile "\"So?\""
                m nudetalk "\"What do you think?\""
                mc nudetalk2 "\"Wow.\""
                mc nudetalk "\"Just wow.\""
                m nudesmile"\"Haha.\""
                show bjdoc3x
                with dissolve
                m nudetalk "\"Any girlfriend that might be jealous?\""
                mc nudethinking "{i}This has to be a test...{/i}"
                mc nudethinking "{i}I have to play dumb...{/i}"
                mc nudetalk "\"Nope! I am single currently.\""
                m nudeyummy "\"Oh goodie. I can eat you all up then.\""
                "Melisa reaches for your cock and takes a good look at it."
                show bjdoc5
                with dissolve
                m nudeyummy "\"Mmm...I wonder how it tastes.\""
                "She starts licking your shaft"
                m nudeyummy "\"MMM~\""
                m nudesmile "\"Not bad.\""
                m nudesmile "\"Time to dive in.\""
                show bjdoc6
                with dissolve
                m nudepleasure"\"MM-BBH\""
                
                $ quick_menu = False
                show screen my_skip2
                $ renpy.show("melisaoffice_animated")
                $ renpy.transition(Dissolve(1))
                $ renpy.pause(12, hard=True)
                label melbj1:
                hide screen my_skip2
                
                $ quick_menu = True
                mc nudethinking "{i}I have to act like I am getting into this.{/i}"
                jump doctor_sequencechoice2
            "Play with her feet":
                $ quick_menu = True
                $ melisa_feet1 = True
                $ melisa_mouth1 = False
                mc nudetalk "\"Y-Your feet...Please.\""
                m smile "\"You don't have to be nervous about it.\""
                show feetdoc1
                with dissolve
                m talk "\"Do you like my feet?\""
                mc nudetalk3 "\"Hahh...\""
                mc nudetalk2 "\"Yes...\""
                mc nudetalk "\"Yes, I do.\""
                m yummy "\"Mmm... I see you're already excited.\""
                m yummy "\"How about you lick my soles?\""
                mc nudetalk2 "\"Yes...\""
                "You kneel down in front of her"
                show feetdoc3
                with dissolve
                m pleasure "\"Hahh...\""
                m openmouth "\"That's nice.\""
                show feetdoc9
                with dissolve
                m yummy "\"Keep going just like that.\""

                
                $ quick_menu = False
                show screen my_skip3
                $ renpy.show("melisaoffice5_animated")
                $ renpy.transition(Dissolve(0.1))
                $ renpy.pause(12, hard=True)   

                label melfeet1:
                hide screen my_skip3
                
                $ quick_menu = True
                "You lick her sole and toes clean"
                m smile "\"Good. I think you deserve a reward.\""
                m talk "\"Put your cock between my toes.\""
                show feetdoc4
                with dissolve
                "You do as you were told."
                m talk "\"Good boy. Stay still and enjoy now.\""
                
                $ quick_menu = False
                show screen my_skip4
                $ renpy.show("melisaoffice3_animated")
                $ renpy.transition(Dissolve(1))
                $ renpy.pause(12, hard=True)

                label melfeet2:
                hide screen my_skip4
                
                $ quick_menu = True
                m "\"Time to speed up.\""
                
                $ quick_menu = False
                show screen my_skip5
                $ renpy.show("melisaoffice4_animated")
                $ renpy.transition(Dissolve(1))
                $ renpy.pause(12, hard=True)

                label melfeet3:
                hide screen my_skip5
                
                $ quick_menu = True
                "You feel yourself getting close"
                mc nudepleasure "\"Hah...\""
                m talk "\"Are you close?\""
                m yummy "\"Cum.\""
                m yummy "\"Dirty the feet you just cleaned with your cum.\""
                mc nudetalk3 "\"Hahh...\""
                mc nudepleasure "\"I am cumming...\""
                show feetdoc7
                with flash
                show feetdoc7
                with flash
                show feetdoc7
                with flash
                "You spray her feet with everything you've got."
                m yummy "\"Woah. You let out a lot. Mmm...\""
                show feetdoc8
                with dissolve
                m smile "\"Look how dirty they are now.\""
                m yummy "\"Mmm...\""
                m yummy "\"You want to clean them up again?\""
                mc nudeshocked2 "\"What!?\""
                m smile "\"Hahaha.\""
                m talk "\"Relax. I am just joking.\""
                m talk "\"Give me a moment to clean myself.\""
                scene a few minutes later
                $ quick_menu = False
                with fasterfadein
                pause 2.0
                with fasterfadeout                                                                
                                                        
                scene doc office 10
                $ quick_menu = True
                with fasterfadein                                
                m smile "\"Well, I sincerely hope you enjoyed that.\""
                m talk "\"I sure did.\""
                mc miltalk2 "\"I did. Thanks.\""
                m smile "\"No need to thank me. Thank you, actually. I needed that.\""
                m talk "\"I usually don't do this with just anyone, but I had a really long day...\""
                m talk "\"Hopefully you understand.\""
                mc miltalk "\"I do. Don't worry about it at all.\""
                m talk "\"Well, I guess you are free to go!\""
                m smile "\"You were healthy... in all departments.\""
                mc miltalk2 "\"Haha... I am glad to hear that.\""
                mc miltalk3 "\"Thanks and see you... soon?\""
                m smile "\"Yup. See you on the ship.\""
                jump doctor_sequencefinal
    label doctor_sequencechoice2:
        $ quick_menu = False
        menu:
            "Go deeper":
                $ quick_menu = True
                show bjdoc6
                with dissolve
                mc nudepleasure "\"Ahh...\""
                m nudeopenmouth "\"Gghhhm--\""
                mc nudethinking "{i}Take it, you whore.{/i}"
                mc nudethinking "{i}You think you can make me lose my memories?{/i}"
                mc nudethinking "{i}Take this.{/i}"
                
                $ quick_menu = False
                show screen my_skip6
                $ renpy.show("melisaoffice2_animated")
                $ renpy.pause(7, hard=True)

                label melbj2:
                hide screen my_skip6

                $ quick_menu = True
                mc nudethinking "{i}Uhh...{/i}"
                mc nudethinking "{i}I am getting close...{/i}"
                mc nudethinking "{i}Where should I finish?{/i}"
                jump doctor_sequencechoice3
    label doctor_sequencechoice3:
        $ quick_menu = False
        menu:
            "Inside her mouth":
                $ quick_menu = True
                show bjdoc8
                with dissolve
                mc nudepleasure "\"Ughh... I am cumming!\""
                show bjdoc8
                with flash
                show bjdoc8
                with flash
                show bjdoc8
                with flash
                "You hold down her head to make sure she swallow everything"
                show bjdoc13
                with flash
                show bjdoc13
                with flash
                m nudepleasure "\"HGHH\""
                m nudeopenmouth "\"GUH\""
                mc nudepleasure "\"Ah...\""
                "Melisa gulps down all of your semen"
                mc nudetalk "\"Sorry about that...\""
                show bjdoc14
                with dissolve
                m nudetalk "\"It's fine.\""
                m nudesmile "\"I am glad you got into it.\""
                m nudetalk "\"And I do like to swallow.\""
                m nudesmile "\"Yours was delicious by the way.\""
                mc nudetalk "\"Um, thanks?\""
                m nudetalk "\"I usually don't do this with just anyone, but I had a really long day...\""
                m nudetalk "\"Hopefully you understand.\""
                mc nudetalk "\"I do. Don't worry about it at all.\""
                show bjdoc14x
                with dissolve
                m nudetalk "\"Well, I guess you are free to go!\""
                m nudesmile "\"You were healthy in all departments.\""
                mc nudetalk2 "\"Haha... I am glad to hear that.\""
                mc nudetalk3 "\"Thanks and see you... soon?\""
                m nudesmile "\"Yup. See you on the ship.\""
                                        
            "On her face":
                $ quick_menu = True
                show bjdoc9
                with dissolve
                m nudeyummy "\"Give it to me... baby.\""
                mc nudepleasure "\"Ah... I am cumming!\""
                show bjdoc10
                with flash
                show bjdoc10
                with flash
                show bjdoc10
                with flash
                "You start covering her face with your thick cum"
                show bjdoc11
                with dissolve
                $ renpy.pause(1, hard=True)
                show bjdoc12
                with dissolve
                $ renpy.pause(3, hard=True)
                m nudepleasure "\"Hahh...\""
                m nudetalk "\"You sure came a lot.\""
                mc nudetalk "\"Sorry... I think I got some in your eye.\""
                m nudeyummy "\"Ha. You sure did.\""
                show bjdoc4
                with dissolve
                m nudetalk "\"Let me get cleaned up. I will be right back.\""
                mc nudetalk2 "\"Of course. Take your time.\""
                                        
                scene a few minutes later
                $ quick_menu = False
                with fasterfadein
                pause 2.0
                with fasterfadeout                                                                
                                        
                scene doc office 10
                $ quick_menu = True
                with fasterfadein
                m talk "\"Well, I sincerely hope you enjoyed that.\""
                m smile "\"I sure did.\""
                mc miltalk "\"I did. Thanks.\""
                scene doc office 10x
                with dissolve
                m talk "\"No need to thank me. Thank you, actually. I needed that.\""
                m talk "\"I usually don't do this with just anyone, but I had a really long day...\""
                m talk "\"Hopefully you understand.\""
                mc miltalk2 "\"I do. Don't worry about it at all.\""
                scene doc office 10
                with dissolve
                m talk "\"Well, I guess you are free to go!\""
                m smile "\"You were healthy... in all departments.\""
                mc miltalk3 "\"Haha... I am glad to hear that.\""
                mc miltalk2 "\"Thanks and see you... soon?\""
                m talk "\"Yup. See you on the ship.\""
                jump doctor_sequencefinal


    label doctor_sequencefinal:
    scene black
    with fasterfadein
    "As you leave the building you see Alex, your personal driver, and you make your way towards him."
    scene driver4
    with dissolve
    alex talk "\"Hi again, [mc]. All done and ready to go?\""
    mc miltalk "\"Yeah. I am ready to leave.\""
    alex talk2 "\"Awesome. I will drop you off at the ship in that case.\""
    mc miltalk "\"Alright.\""
    scene a few minutes later
    $ quick_menu = False
    with fasterfadein
    pause 2.0
    with fasterfadeout        

    scene black
    with fasterfadein
    $ quick_menu = True
    alex talk "\"This is your final stop.\""
    alex talk "\"Best of luck to you out there.\""
    mc miltalk2 "\"Thanks. Take care of yourself too. Goodbye.\""
    
    scene ship leave
    with dissolve
    "You leave and start walking towards the entrance of the ship."
    
    scene entering ship ruby2
    with dissolve
    
    qm rubytalk "\"Welcome aboard Paradise 1337-69, [mc].\""
    
    scene entering ship ruby
    with dissolve
    
    qm rubytalk "\"I am called Ruby, the assisting AI aboard the ship.\""
    mc miltalk2 "\"Pleased to meet you, Ruby. I hope you weren't waiting too long for me.\""
    r talk "\"You have arrived in the specified time frame.\""
    r talk2 "\"Give me a moment to start the engines and set the coordinates.\""
    mc miltalk3 "\"Of course. Take your time.\""
    r talk "\"Thank you for your compliance.\""
    
    scene entering ship ruby3
    with dissolve
    
    "\"Authorized Access Granted.\""
    "\"System startup initiated.\""
    "\"Engine started.\""
    "\"Launch sequence initiated.\""

    scene entering ship ruby
    with dissolve
    r talk "\"Everything is ready and the liftoff should be in a minute.\""
    mc miltalk "\"That is pretty cool. You can control the ship through your mind?\""
    r talk "\"Yes. I am connected to the ship system and thus no pilot is needed as I can control the ship automatically and all the systems aboard it.\""
    mc miltalk "\"But what if something happens to you? No one else can get us down?\""
    r talk2 "\"The engineer -- Jane, is also trained to evacuate the ship in a last resort.\""
    mc miltalk2 "\"I see. That makes sense.\""
    r talk2 "\"In the meantime, could you please follow me so you can meet the other participants?\""
    mc miltalk2 "\"Of course. Lead the way.\""
    
    scene entering ship ruby5
    with dissolve
    r smile "\"Before we continue, do you have any questions?\""
    $ quick_menu = False
    menu:
        "No questions":
            $ quick_menu = True
            mc miltalk3 "\"Nope. No questions.\""
            scene entering ship ruby4
            with dissolve
            r talk2 "\"Understood. Please, follow me then.\""
            jump afterruby
        "Weapons":
            $ quick_menu = True
            mc miltalk2 "\"I was actually curious...\""
            mc miltalk "\"I saw the ship outside and I saw that it was equipped with quite a few weapons as if we are going to a battle or something?\""
            mc miltalk2 "\"What's up with that?\""
            scene entering ship ruby4
            with dissolve
            r talk "\"Assurance, mostly.\""
            r talk2 "\"We don't know what could happen at any given time, so having precautions is mandatory.\""
            r talk "\"It's for your own protection in the end.\""
            scene entering ship ruby5
            with dissolve
            mc miltalk3 "\"I see. Don't get me wrong, I am happy for being 'protected' but isn't this whole operation a bit... too expensive to be funded?\""
            mc miltalk2 "\"Who wins from this and what?\""
            mc milthinking "{i}I already know their real agenda with all of this... but maybe I can get some extra information.{/i}"
            scene entering ship ruby4
            with dissolve
            r talk "\"This whole trip is sponsored greatly by the generous Amir from Saudi Arabia.\""
            r talk2 "\"What he gains from this? I couldn't tell you.\""
            r talk "\"He is one of the participants though.\""
            scene entering ship ruby5
            with dissolve
            mc miltalk "\"Wait... so he sponsored all of this with his own money and he is a participant in it?\""
            scene entering ship ruby4
            with dissolve
            r talk "\"That's correct.\""
            scene entering ship ruby5
            with dissolve
            mc miltalk2 "\"Weird...\""
            scene entering ship ruby4
            with dissolve
            r talk "\"Any other questions?\""
            jump noweaponsquestion
        "Sex":
            $ quick_menu = True
            mc miltalk "\"This might sound weird, but...\""
            scene entering ship ruby4
            with dissolve
            r talk "\"I am an android, [mc]. Nothing will be weird for me. I have no feelings like you do after all.\""
            scene entering ship ruby5
            with dissolve
            mc miltalk "\"Ah... right...\""
            mc miltalk2 "\"How will sex work here exactly?\""
            mc miltalk "\"There is quite a few people and genders vary, so I am only assuming it will happen.\""
            mc miltalk2 "\"What if a girl gets pregnant?\""
            scene entering ship ruby4
            with dissolve
            r talk "\"Not a problem for our ship. We have the newest technology possible for this sort of thing and the gravity is quite improved for a spaceship.\""
            r talk2 "\"If a woman gets pregnant while on board, then she will have a perfectly healthy baby to bring back home on Earth.\""
            scene entering ship ruby5
            with dissolve
            mc miltalk "\"O-Okay. I see. That's good to hear, I guess?\""
            scene entering ship ruby4
            with dissolve
            r talk "\"Any other questions?\""
            jump nosexquestion
            
    label noweaponsquestion:
    $ quick_menu = False
    menu:
        "No questions":
            $ quick_menu = True
            mc miltalk3 "\"Nope. No questions.\""
            scene entering ship ruby4
            with dissolve
            r talk2 "\"Understood. Please, follow me then.\""
            jump afterruby
        "Sex":
            $ quick_menu = True
            mc miltalk "\"This might sound weird, but...\""
            scene entering ship ruby4
            with dissolve
            r talk "\"I am an android, [mc]. Nothing will be weird for me. I have no feelings like you do after all.\""
            scene entering ship ruby5
            with dissolve
            mc miltalk "\"Ah... right...\""
            mc miltalk2 "\"How will sex work here exactly?\""
            mc miltalk3 "\"I mean...\""
            mc miltalk "\"There is quite a few people and genders vary, so I am only assuming it will happen.\""
            mc miltalk2 "\"What if a girl gets pregnant?\""
            scene entering ship ruby4
            with dissolve
            r talk "\"Not a problem for our ship. We have the newest technology possible for this sort of thing and the gravity is quite improved for a spaceship.\""
            r talk2 "\"If a woman gets pregnant while on board, then she will have a perfectly healthy baby to bring back home on Earth.\""
            scene entering ship ruby5
            with dissolve
            mc miltalk "\"O-Okay. I see. That's good to hear, I guess?\""
            scene entering ship ruby4
            with dissolve
            r talk "\"Any other questions?\""
            jump noquestions
            
    label nosexquestion:
    $ quick_menu = False
    menu:
        "No questions":
            $ quick_menu = True
            mc miltalk3 "\"Nope. No questions.\""
            scene entering ship ruby4
            with dissolve
            r talk2 "\"Understood. Please, follow me then.\""
            jump afterruby
        "Weapons":
            $ quick_menu = True
            mc miltalk2 "\"I was actually curious...\""
            mc miltalk "\"I saw the ship outside and I saw that it was equipped with quite a few weapons as if we are going to a battle or something?\""
            mc miltalk2 "\"What's up with that?\""
            scene entering ship ruby4
            with dissolve
            r talk "\"Assurance, mostly.\""
            r talk2 "\"We don't know what could happen at any given time, so having precautions is mandatory.\""
            r talk "\"It's for your own protection in the end.\""
            scene entering ship ruby5
            with dissolve
            mc miltalk3 "\"I see. Don't get me wrong, I am happy for being 'protected' but isn't this whole operation a bit... too expensive to be funded?\""
            mc miltalk2 "\"Who wins from this and what?\""
            mc milthinking "{i}I already know their real agenda with all of this... but maybe I can get some extra information.{/i}"
            scene entering ship ruby4
            with dissolve
            r talk "\"This whole trip is sponsored greatly by the generous Amir from Saudi Arabia.\""
            r talk2 "\"What he gains from this? I couldn't tell you.\""
            r talk "\"He is one of the participants though.\""
            scene entering ship ruby5
            with dissolve
            mc miltalk "\"Wait... so he sponsored all of this with his own money and he is a participant in it?\""
            scene entering ship ruby4
            with dissolve
            r talk "\"That's correct.\""
            scene entering ship ruby5
            with dissolve
            mc miltalk2 "\"Weird...\""
            scene entering ship ruby4
            with dissolve
            r talk "\"Any other questions?\""
            jump noquestions
    label noquestions:
    $ quick_menu = False
    menu:
        "No questions":
            $ quick_menu = True
            mc miltalk3 "\"Nope. No questions.\""
            scene entering ship ruby4
            with dissolve
            r talk2 "\"Understood. Please, follow me then.\""
            jump afterruby
            
    label afterruby:    
    "You continue to follow Ruby."
    
    scene entering ship ruby6
    with dissolve
    pause 1.0
    scene black
    with dissolve
    "\"Countdown to liftoff...\""
    "\"3...\""
    "\"3...\n 2...\""
    "\"3...\n  2...\n 1...\""
    scene ship leave1
    with flash
    pause 2.5
    scene black
    with dissolve
    pause 1.0
    scene ship leave2
    with dissolve
    pause 2.5
    
    scene black
    with dissolve
    pause 2.5
    jump chapter2

label thanks:
    $ change_cursor("1")
    $ _game_menu_screen = None

    $ quick_menu = False
    $ credits_speed = 60 #scrolling speed in seconds
    stop music fadeout 7.0
    show screen disable_Credit
    scene credits2
    with fadein

    play music [ "music/Journey of King.mp3" ] noloop fadein 5.0

    show cred at Move((0.5, 5.6), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom") onlayer static_layer2
    show screen credit_button
    show screen skipcredits
    with renpy.pause(credits_speed, hard=True)
    stop music fadeout 4.0
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    $ _game_menu_screen = "save_screen"
    hide screen disable_Credit
    with fasterfadein
    return

init python: #
    credits = ('{size=70}{color=#B7B7B7}GUI and Renders{/color}', 'Void Star'),('{size=70}{color=#B7B7B7}Story and Characters{/color}', 'Void Star'), ('{size=70}{color=#B7B7B7}Music{/color}', 'Moon Garden\nJourney of King by Bisou\nCrystal Hunter\nQuest for Glory by Giovanni\nEastern Thought by Bruce Zimmerman\nSpread the Word by Neil Cross\nAmbient Thriller Motif & Modern Horror Film Music by Bobby Cole'), ('{size=70}{color=#B7B7B7}Programming{/color}', 'Void Star'), ('{size=60}{color=#B7B7B7}Special thanks to my PATRONS:{/color}',''), ('{size=70}{color=#BD8A20}Legend:{/color}', '{color=#E0AF49}Joey\ngerrit flipse\nMark\nusa93\nCalladin\nPaul Schmidt\ndarrel hotchkin\nmarclung\nCsm\nali kaiba\nGelon\n<matt\nZacharyk{/color}'), ('{size=70}{color=#366092}Hardcore:{/color}', '{color=#5C8AC2}John Foster\nstephen sheppard\nChris Frazier\nWim\nJeremy Bowman\nPhillip \'Gedion\' K.\nParadox3164\nVladimir Timofeev\nMr. Chase Sin\nGeoff Goodenough\nI.W.\nMarcus Depth\nDaniel Lynch\nUKGAMER\nNeoma\njay\nKilroy\nswartxide\nCraigoss\ntommy\nMidukill{/color}'), ('{size=40}And everyone else who pledged!', '{size=40}This was possible thanks to you!')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}" + renpy.version()

init:
    image cred = Text(credits_s, text_align=0.5,color="#DDDDDD",outlines = [(2, "#000", 0, 0)],bold=True, drop_shadow = (2, 2), drop_shadow_color = "#000000")
    image thanks = Text("{size=80}Thank you for\n playing!", text_align=0.5,color="#DDDDDD",outlines = [(2, "#000", 0, 0)],bold=True, drop_shadow = (4, 4), drop_shadow_color = "#000000")
    screen credit_button: #Patreon Button in Thanks screen
        imagebutton auto "gui/support_button_%s.png" xpos 0 ypos 1003 focus_mask None action OpenURL("https://www.patreon.com/VoidStar") hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
        imagebutton auto "gui/credit_ad_%s.png" xpos 0 ypos 0 focus_mask True action NullAction() hovered [Function(set_cursor_hover)], Show("the_img", img="gui/credits2nude.png"), Show("the_patreonlogo", img="gui/support_button_idle.png") unhovered [Function(set_cursor_default)], Hide("the_img"), Hide("the_patreonlogo")

label thanksmainmenu:
    $ change_cursor("1")
    $ _game_menu_screen = None
    stop music fadeout 1.0
    show screen disable_Credit
    $ quick_menu = False
    $ credits_speed = 60 #scrolling speed in seconds
    scene credits2
    with fasterfadein

    play music [ "music/Journey of King.mp3" ] noloop fadein 5.0

    show cred at Move((0.5, 5.6), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom") onlayer static_layer2
    show screen credit_button
    with Pause(credits_speed)
    stop music fadeout 4.0
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    $ _game_menu_screen = "save_screen"
    hide screen disable_Credit
    with fasterfadein
    return

init python: #
    credits = ('{size=70}{color=#B7B7B7}GUI and Renders{/color}', 'Void Star'),('{size=70}{color=#B7B7B7}Story and Characters{/color}', 'Void Star'), ('{size=70}{color=#B7B7B7}Music{/color}', 'Moon Garden\nJourney of King by Bisou\nCrystal Hunter\nQuest for Glory by Giovanni\nEastern Thought by Bruce Zimmerman\nSpread the Word by Neil Cross\nAmbient Thriller Motif & Modern Horror Film Music by Bobby Cole'), ('{size=70}{color=#B7B7B7}Programming{/color}', 'Void Star'), ('{size=60}{color=#B7B7B7}Special thanks to my PATRONS:{/color}',''), ('{size=70}{color=#BD8A20}Legend:{/color}', '{color=#E0AF49}Joey\ngerrit flipse\nMark\nusa93\nCalladin\nPaul Schmidt\ndarrel hotchkin\nmarclung\nCsm\nali kaiba\nGelon\n<matt\nZacharyk{/color}'), ('{size=70}{color=#366092}Hardcore:{/color}', '{color=#5C8AC2}John Foster\nstephen sheppard\nChris Frazier\nWim\nJeremy Bowman\nPhillip \'Gedion\' K.\nParadox3164\nVladimir Timofeev\nMr. Chase Sin\nGeoff Goodenough\nI.W.\nMarcus Depth\nDaniel Lynch\nUKGAMER\nNeoma\njay\nKilroy\nswartxide\nCraigoss\ntommy\nMidukill{/color}'), ('{size=40}And everyone else who pledged!', '{size=40}This was possible thanks to you!')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}" + renpy.version()

init:
    image cred = Text(credits_s, text_align=0.5,color="#DDDDDD",outlines = [(2, "#000", 0, 0)],bold=True, drop_shadow = (2, 2), drop_shadow_color = "#000000")
    image thanks = Text("{size=80}Thank you for\n playing!", text_align=0.5,color="#DDDDDD",outlines = [(2, "#000", 0, 0)],bold=True, drop_shadow = (4, 4), drop_shadow_color = "#000000")
    screen credit_button: #Patreon Button in Thanks screen
        imagebutton auto "gui/support_button_%s.png" xpos 0 ypos 1003 focus_mask None action OpenURL("https://www.patreon.com/VoidStar") hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
        imagebutton auto "gui/credit_ad_%s.png" xpos 0 ypos 0 focus_mask True action NullAction() hovered [Function(set_cursor_hover)], Show("the_img", img="gui/credits2nude.png"), Show("the_patreonlogo", img="gui/support_button_idle.png") unhovered [Function(set_cursor_default)], Hide("the_img"), Hide("the_patreonlogo")

