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

screen disable_Credit():
    key "mouseup_3" action NullAction()
    key "K_ESCAPE" action NullAction()

screen the_img(img): #Used for Credits screen to display hovered AD correctly
    add img pos (0, 0)

screen the_patreonlogo(img): #Used for Credits screen to display patreon logo when hovering AD correctly
    add img pos (0, 1003)


screen patreonbutton():
    zorder 10
    imagebutton auto "gui/patreon_button_%s.png" xpos 860 ypos 862 focus_mask None action OpenURL("https://www.patreon.com/join/VoidStar?") hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]


screen skipcredits():
    zorder 10
    imagebutton auto "gui/skipcredits_%s.png" xpos -4 ypos 6 action MainMenu() hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]

screen my_skip():
    zorder 10
    imagebutton auto "gui/skip_%s.png" xpos -4 ypos 6 action Jump('afterbackalley')

screen my_skip2():
    zorder 10
    imagebutton auto "gui/skip_%s.png" xpos -4 ypos 6 action Jump('melbj1')

screen my_skip3():
    zorder 10
    imagebutton auto "gui/skip_%s.png" xpos -4 ypos 6 action Jump('melfeet1')

screen my_skip4():
    zorder 10
    imagebutton auto "gui/skip_%s.png" xpos -4 ypos 6 action Jump('melfeet2')

screen my_skip5():
    zorder 10
    imagebutton auto "gui/skip_%s.png" xpos -4 ypos 6 action Jump('melfeet3')

screen my_skip6():
    zorder 10
    imagebutton auto "gui/skip_%s.png" xpos -4 ypos 6 action Jump('melbj2')

screen hide_textbox():
    zorder 10
    imagebutton auto "gui/pressh_%s.png" xpos -4 ypos 6 action NullAction()

init -1 python:
    def hide_screens():
        renpy.hide_screen(say)


screen disableclick(time): #disabling CTC
    timer time action Hide("disableclick")
    key "mouseup_1" action NullAction()
    key "mousedown_1" action NullAction()
#####################################MUSIC###########################################################

screen music_screen:
    python:
            renpy.music.play("music/crystal hunter.mp3", fadeout=10.0, fadein=15.0)
            renpy.music.play("music/Moon Garden.mp3", fadeout=10.0, fadein=15.0)

screen skip_indicator():
    on 'show' action SetMute('music/crystal hunter.mp3', True)
    on 'hide' action SetMute('music/crystal hunter.mp3', False)
    
    on 'show' action SetMute('music/Quest for Glory.mp3', True)
    on 'hide' action SetMute('music/Quest for Glory.mp3', False)


#####################################MUSIC###########################################################

## ■██▓▒░ MAIN MENU ░▒▓█████████████████████████████████████■
## Screen that's used to display the main menu, when Ren'Py first starts
## http://www.renpy.org/doc/html/screen_special.html#main-menu
screen main_menu:
    tag menu # This ensures that any other menu screen is replaced.
    
    if persistent.change == "Ruby 1":
        use main_menu_1
    elif persistent.change == "Edis female":
        use main_menu_2
    elif persistent.change == "New world":
        use main_menu_3
    elif persistent.change == "New world 2":
        use main_menu_4
    elif persistent.change == "New world 3":
        use main_menu_5
    elif persistent.change == "End 1":
        use main_menu_6
    elif persistent.change == "End 2":
        use main_menu_7
    elif persistent.change == "End 3":
        use main_menu_8
        
    else:
        use main_menu_default
    
screen main_menu_default:
    tag menu
    
    add "gui/main_menu_ground.png" # Add a background image for the main menu.
#end add_image
    imagebutton auto "gui/config_andre_%s.png" xpos 690 ypos 111 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_amir_%s.png" xpos 1480 ypos 146 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_victor_%s.png" xpos 1170 ypos 166 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_elyse_%s.png" xpos 1390 ypos 120 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_chloe_%s.png" xpos 1697 ypos 189 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_zoey_%s.png" xpos 1320 ypos 255 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_melisa_%s.png" xpos 960 ypos 140 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_wife_%s.png" xpos 843 ypos 180 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_lexa_%s.png" xpos 120 ypos 120 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_jack_%s.png" xpos -160 ypos 111 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_dahlia_%s.png" xpos 99 ypos 151 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_main_%s.png" xpos 490 ypos 120 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_robot_%s.png" xpos 760 ypos 470 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_edis_%s.png" xpos 246 ypos 566 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_jane2_%s.png" xpos 590 ypos 665 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/MainMenuHoverBar_%s.png" xpos 0 ypos 957 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/PatreonLogo1_%s.png" xpos 1503 ypos -5 focus_mask None action OpenURL("https://www.patreon.com/VoidStar") hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    $ y=114 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/main_start_%s.png" xpos 217 ypos 958 focus_mask True action Start() hovered [ Play ("test_one", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_start.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff1
    on "replaced" action Hide('gui_tooltip')
    # Imagebutton documentation: http://www.renpy.org/doc/html/screens.html#imagebutton
    
    # auto - is used to automatically define the images used by this button. We could also use:
    # imagebutton idle "main_start_idle.png" hover "main_start_hover.png"
    
    # xpos 773 ypos y - are used set the coordinates to position the button at 773, 114 (y has a value of 114)
    
    # focus_mask True ensures that only non-transparent areas of the button can be focused. focus_mask defines which parts of the image can be focused, and hence clicked on. http://www.renpy.org/doc/html/style.html#button-style-properties
    
    # action - action to run when the button is activated. This also controls if the button is sensitive, and if the button is selected.
    
    # hovered - action to run when the button gains focus. Square brackets are used to run multiple actions. In this case we play a sound effect and show a tooltip.
    
    # unhovered - action to run when the button loses focus. In this case we hide a tooltip.
    
    $ y+=71 # We increase y position for the next menu item. y has a value of 185(114+81=185) now. We could also use: xpos 773 ypos 185
    imagebutton auto "gui/main_load_%s.png" xpos 514 ypos 958 focus_mask True  action ShowMenu('load'), Function(set_cursor_default) hovered [ Play ("test_two", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_load.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff2
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_config_%s.png" xpos 812 ypos 958 focus_mask True action ShowMenu('preferences'), Function(set_cursor_default) hovered [ Play ("test_three", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_config.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff3
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_thanks_%s.png" xpos 1110 ypos 958 focus_mask True action Start('thanksmainmenu'), Function(set_cursor_default) hovered [ Play ("test_four", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_credits.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff4
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_quit_%s.png" xpos 1408 ypos 958 focus_mask True action Quit(confirm=False) hovered [ Play ("test_five", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_quit.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff5
    on "replaced" action Hide('gui_tooltip')
# The code below defines the ATL transform effects for each button on the main menu. These effects are triggered when the buttons are shown.
# ATL transform properties: http://www.renpy.org/wiki/renpy/doc/reference/Animation_and_Transformation_Language#Transform_Properties
#begin main_eff
init -2:
    transform main_eff1:
        zoom 0.5
        easein 0.4 zoom 1.0
    transform main_eff2:
        zoom 0.5
        easein 0.8 zoom 1.0
    transform main_eff3:
        zoom 0.5
        easein 1.2 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.6 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 2.0 zoom 1.0
#end main_eff


screen main_menu_1:
    tag menu

    add "gui/main_menu_ground.png" # Add a background image for the main menu.
#end add_image
    imagebutton auto "gui/config_andre_%s.png" xpos 690 ypos 111 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_amir_%s.png" xpos 1480 ypos 146 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_victor_%s.png" xpos 1170 ypos 166 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_elyse_%s.png" xpos 1390 ypos 120 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_chloe_%s.png" xpos 1697 ypos 189 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_zoey_%s.png" xpos 1320 ypos 255 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_melisa_%s.png" xpos 960 ypos 140 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_wife_%s.png" xpos 843 ypos 180 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_lexa_%s.png" xpos 120 ypos 120 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_jack_%s.png" xpos -160 ypos 111 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_dahlia_%s.png" xpos 99 ypos 151 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_main_%s.png" xpos 490 ypos 120 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_robot2_%s.png" xpos 760 ypos 470 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_edis_%s.png" xpos 246 ypos 566 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_jane2_%s.png" xpos 590 ypos 665 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/MainMenuHoverBar_%s.png" xpos 0 ypos 957 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/PatreonLogo1_%s.png" xpos 1503 ypos -5 focus_mask True action OpenURL("https://www.patreon.com/VoidStar") hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    $ y=114 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/main_start_%s.png" xpos 217 ypos 958 focus_mask None action Start() hovered [ Play ("test_one", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_start.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff1
    on "replaced" action Hide('gui_tooltip')
    # Imagebutton documentation: http://www.renpy.org/doc/html/screens.html#imagebutton
    
    # auto - is used to automatically define the images used by this button. We could also use:
    # imagebutton idle "main_start_idle.png" hover "main_start_hover.png"
    
    # xpos 773 ypos y - are used set the coordinates to position the button at 773, 114 (y has a value of 114)
    
    # focus_mask True ensures that only non-transparent areas of the button can be focused. focus_mask defines which parts of the image can be focused, and hence clicked on. http://www.renpy.org/doc/html/style.html#button-style-properties
    
    # action - action to run when the button is activated. This also controls if the button is sensitive, and if the button is selected.
    
    # hovered - action to run when the button gains focus. Square brackets are used to run multiple actions. In this case we play a sound effect and show a tooltip.
    
    # unhovered - action to run when the button loses focus. In this case we hide a tooltip.
    
    $ y+=71 # We increase y position for the next menu item. y has a value of 185(114+81=185) now. We could also use: xpos 773 ypos 185
    imagebutton auto "gui/main_load_%s.png" xpos 514 ypos 958 focus_mask True  action ShowMenu('load'), Function(set_cursor_default) hovered [ Play ("test_two", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_load.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff2
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_config_%s.png" xpos 812 ypos 958 focus_mask True action ShowMenu('preferences'), Function(set_cursor_default) hovered [ Play ("test_three", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_config.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff3
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_thanks_%s.png" xpos 1110 ypos 958 focus_mask True action Start('thanksmainmenu'), Function(set_cursor_default) hovered [ Play ("test_four", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_credits.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff4
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_quit_%s.png" xpos 1408 ypos 958 focus_mask True action Quit(confirm=False) hovered [ Play ("test_five", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_quit.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff5
    on "replaced" action Hide('gui_tooltip')
# The code below defines the ATL transform effects for each button on the main menu. These effects are triggered when the buttons are shown.
# ATL transform properties: http://www.renpy.org/wiki/renpy/doc/reference/Animation_and_Transformation_Language#Transform_Properties
#begin main_eff
init -2:
    transform main_eff1:
        zoom 0.5
        easein 0.4 zoom 1.0
    transform main_eff2:
        zoom 0.5
        easein 0.8 zoom 1.0
    transform main_eff3:
        zoom 0.5
        easein 1.2 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.6 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 2.0 zoom 1.0
#end main_eff


screen main_menu_2:
    tag menu

    add "gui/main_menu_ground.png" # Add a background image for the main menu.
#end add_image
    imagebutton auto "gui/config_andre_%s.png" xpos 690 ypos 111 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_victor_%s.png" xpos 1170 ypos 166 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_chloe_%s.png" xpos 1630 ypos 189 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_elyse_%s.png" xpos 1390 ypos 120 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_zoey_%s.png" xpos 1320 ypos 255 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_melisa_%s.png" xpos 960 ypos 140 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_wife_%s.png" xpos 843 ypos 180 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_lexa2_%s.png" xpos 120 ypos 120 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_jack_%s.png" xpos -160 ypos 111 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_dahlia_%s.png" xpos 99 ypos 151 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_main_%s.png" xpos 490 ypos 120 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_robot2_%s.png" xpos 760 ypos 470 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_jane2_%s.png" xpos 590 ypos 665 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/MainMenuHoverBar_%s.png" xpos 0 ypos 957 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/PatreonLogo1_%s.png" xpos 1503 ypos -5 focus_mask True action OpenURL("https://www.patreon.com/VoidStar") hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    $ y=114 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/main_start_%s.png" xpos 217 ypos 958 focus_mask None action Start() hovered [ Play ("test_one", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_start.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff1
    on "replaced" action Hide('gui_tooltip')
    # Imagebutton documentation: http://www.renpy.org/doc/html/screens.html#imagebutton
    
    # auto - is used to automatically define the images used by this button. We could also use:
    # imagebutton idle "main_start_idle.png" hover "main_start_hover.png"
    
    # xpos 773 ypos y - are used set the coordinates to position the button at 773, 114 (y has a value of 114)
    
    # focus_mask True ensures that only non-transparent areas of the button can be focused. focus_mask defines which parts of the image can be focused, and hence clicked on. http://www.renpy.org/doc/html/style.html#button-style-properties
    
    # action - action to run when the button is activated. This also controls if the button is sensitive, and if the button is selected.
    
    # hovered - action to run when the button gains focus. Square brackets are used to run multiple actions. In this case we play a sound effect and show a tooltip.
    
    # unhovered - action to run when the button loses focus. In this case we hide a tooltip.
    
    $ y+=71 # We increase y position for the next menu item. y has a value of 185(114+81=185) now. We could also use: xpos 773 ypos 185
    imagebutton auto "gui/main_load_%s.png" xpos 514 ypos 958 focus_mask True  action ShowMenu('load'), Function(set_cursor_default) hovered [ Play ("test_two", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_load.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff2
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_config_%s.png" xpos 812 ypos 958 focus_mask True action ShowMenu('preferences'), Function(set_cursor_default) hovered [ Play ("test_three", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_config.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff3
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_thanks_%s.png" xpos 1110 ypos 958 focus_mask True action Start('thanksmainmenu'), Function(set_cursor_default) hovered [ Play ("test_four", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_credits.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff4
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_quit_%s.png" xpos 1408 ypos 958 focus_mask True action Quit(confirm=False) hovered [ Play ("test_five", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_quit.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff5
    on "replaced" action Hide('gui_tooltip')
# The code below defines the ATL transform effects for each button on the main menu. These effects are triggered when the buttons are shown.
# ATL transform properties: http://www.renpy.org/wiki/renpy/doc/reference/Animation_and_Transformation_Language#Transform_Properties
#begin main_eff
init -2:
    transform main_eff1:
        zoom 0.5
        easein 0.4 zoom 1.0
    transform main_eff2:
        zoom 0.5
        easein 0.8 zoom 1.0
    transform main_eff3:
        zoom 0.5
        easein 1.2 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.6 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 2.0 zoom 1.0
#end main_eff

screen main_menu_3:
    tag menu

    add "gui/main_menu_ground2.png" # Add a background image for the main menu.
#end add_image
    imagebutton auto "gui/config_mc3_%s.png" xpos 671 ypos 107 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_ingrid_%s.png" xpos 225 ypos 127 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_ivy_%s.png" xpos 1270 ypos 600 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_mira_%s.png" xpos 1083 ypos 121 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    
    imagebutton auto "gui/PatreonLogo1_%s.png" xpos 1503 ypos -5 focus_mask None action OpenURL("https://www.patreon.com/VoidStar") hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    $ y=114 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/main_start2_%s.png" xpos 217 ypos 958 focus_mask True action Start() hovered [ Play ("test_one", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_start.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff1
    on "replaced" action Hide('gui_tooltip')
    
    $ y+=71 # We increase y position for the next menu item. y has a value of 185(114+81=185) now. We could also use: xpos 773 ypos 185
    imagebutton auto "gui/main_load2_%s.png" xpos 514 ypos 958 focus_mask True  action ShowMenu('load'), Function(set_cursor_default) hovered [ Play ("test_two", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_load.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff2
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_config2_%s.png" xpos 812 ypos 958 focus_mask True action ShowMenu('preferences'), Function(set_cursor_default) hovered [ Play ("test_three", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_config.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff3
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_thanks2_%s.png" xpos 1110 ypos 958 focus_mask True action Start('thanksmainmenu'), Function(set_cursor_default) hovered [ Play ("test_four", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_credits.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff4
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_quit2_%s.png" xpos 1408 ypos 958 focus_mask True action Quit(confirm=False) hovered [ Play ("test_five", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_quit.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff5
    on "replaced" action Hide('gui_tooltip')
    


#begin main_eff
init -2:
    transform main_eff1:
        zoom 0.5
        easein 0.4 zoom 1.0
    transform main_eff2:
        zoom 0.5
        easein 0.8 zoom 1.0
    transform main_eff3:
        zoom 0.5
        easein 1.2 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.6 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 2.0 zoom 1.0
#end main_eff





screen main_menu_4:
    tag menu

    add "gui/main_menu_ground2.png" # Add a background image for the main menu.
#end add_image
    imagebutton auto "gui/config_mc4_%s.png" xpos 671 ypos 107 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_ingrid_%s.png" xpos 225 ypos 127 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_ivy_%s.png" xpos 1270 ypos 600 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_mira_%s.png" xpos 1083 ypos 121 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    
    imagebutton auto "gui/PatreonLogo1_%s.png" xpos 1503 ypos -5 focus_mask None action OpenURL("https://www.patreon.com/VoidStar") hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    $ y=114 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/main_start2_%s.png" xpos 217 ypos 958 focus_mask True action Start() hovered [ Play ("test_one", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_start.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff1
    on "replaced" action Hide('gui_tooltip')
    
    $ y+=71 # We increase y position for the next menu item. y has a value of 185(114+81=185) now. We could also use: xpos 773 ypos 185
    imagebutton auto "gui/main_load2_%s.png" xpos 514 ypos 958 focus_mask True  action ShowMenu('load'), Function(set_cursor_default) hovered [ Play ("test_two", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_load.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff2
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_config2_%s.png" xpos 812 ypos 958 focus_mask True action ShowMenu('preferences'), Function(set_cursor_default) hovered [ Play ("test_three", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_config.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff3
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_thanks2_%s.png" xpos 1110 ypos 958 focus_mask True action Start('thanksmainmenu'), Function(set_cursor_default) hovered [ Play ("test_four", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_credits.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff4
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_quit2_%s.png" xpos 1408 ypos 958 focus_mask True action Quit(confirm=False) hovered [ Play ("test_five", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_quit.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff5
    on "replaced" action Hide('gui_tooltip')
    


#begin main_eff
init -2:
    transform main_eff1:
        zoom 0.5
        easein 0.4 zoom 1.0
    transform main_eff2:
        zoom 0.5
        easein 0.8 zoom 1.0
    transform main_eff3:
        zoom 0.5
        easein 1.2 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.6 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 2.0 zoom 1.0
#end main_eff


screen main_menu_5:
    tag menu

    add "gui/main_menu_ground2.png" # Add a background image for the main menu.
#end add_image
    imagebutton auto "gui/config_luna_%s.png" xpos 1280 ypos 699 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_mc5_%s.png" xpos 671 ypos 107 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_ingrid_%s.png" xpos 225 ypos 127 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_ivy_%s.png" xpos 1270 ypos 600 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    imagebutton auto "gui/config_mira_%s.png" xpos 1083 ypos 121 focus_mask True action NullAction() hovered [Function(set_cursor_default)]

    imagebutton auto "gui/PatreonLogo1_%s.png" xpos 1503 ypos -5 focus_mask None action OpenURL("https://www.patreon.com/VoidStar") hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    $ y=114 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/main_start2_%s.png" xpos 217 ypos 958 focus_mask True action Start() hovered [ Play ("test_one", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_start.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff1
    on "replaced" action Hide('gui_tooltip')
    
    $ y+=71 # We increase y position for the next menu item. y has a value of 185(114+81=185) now. We could also use: xpos 773 ypos 185
    imagebutton auto "gui/main_load2_%s.png" xpos 514 ypos 958 focus_mask True  action ShowMenu('load'), Function(set_cursor_default) hovered [ Play ("test_two", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_load.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff2
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_config2_%s.png" xpos 812 ypos 958 focus_mask True action ShowMenu('preferences'), Function(set_cursor_default) hovered [ Play ("test_three", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_config.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff3
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_thanks2_%s.png" xpos 1110 ypos 958 focus_mask True action Start('thanksmainmenu'), Function(set_cursor_default) hovered [ Play ("test_four", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_credits.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff4
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_quit2_%s.png" xpos 1408 ypos 958 focus_mask True action Quit(confirm=False) hovered [ Play ("test_five", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_quit.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff5
    on "replaced" action Hide('gui_tooltip')
    


#begin main_eff
init -2:
    transform main_eff1:
        zoom 0.5
        easein 0.4 zoom 1.0
    transform main_eff2:
        zoom 0.5
        easein 0.8 zoom 1.0
    transform main_eff3:
        zoom 0.5
        easein 1.2 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.6 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 2.0 zoom 1.0
#end main_eff


screen main_menu_6:
    tag menu

    add "gui/mc alone login screen.png" # Add a background image for the main menu.
    
    imagebutton auto "gui/main_logo1_%s.png" xpos -2 ypos -3 focus_mask None action NullAction() hovered [Function(set_cursor_default)]
    
    imagebutton auto "gui/PatreonLogo3_%s.png" xpos 1503 ypos -5 focus_mask None action OpenURL("https://www.patreon.com/VoidStar") hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    $ y=114 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/main_start4_%s.png" xpos 217 ypos 958 focus_mask True action Start() hovered [ Play ("test_one", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_start.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff1
    on "replaced" action Hide('gui_tooltip')
    
    $ y+=71 # We increase y position for the next menu item. y has a value of 185(114+81=185) now. We could also use: xpos 773 ypos 185
    imagebutton auto "gui/main_load4_%s.png" xpos 514 ypos 958 focus_mask True  action ShowMenu('load'), Function(set_cursor_default) hovered [ Play ("test_two", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_load.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff2
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_config4_%s.png" xpos 812 ypos 958 focus_mask True action ShowMenu('preferences'), Function(set_cursor_default) hovered [ Play ("test_three", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_config.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff3
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_thanks4_%s.png" xpos 1110 ypos 958 focus_mask True action Start('thanksmainmenu'), Function(set_cursor_default) hovered [ Play ("test_four", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_credits.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff4
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_quit4_%s.png" xpos 1408 ypos 958 focus_mask True action Quit(confirm=False) hovered [ Play ("test_five", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_quit.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff5
    on "replaced" action Hide('gui_tooltip')
    


#begin main_eff
init -2:
    transform main_eff1:
        zoom 0.5
        easein 0.4 zoom 1.0
    transform main_eff2:
        zoom 0.5
        easein 0.8 zoom 1.0
    transform main_eff3:
        zoom 0.5
        easein 1.2 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.6 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 2.0 zoom 1.0
#end main_eff


screen main_menu_7:
    tag menu

    add "gui/mc camp login screen.png" # Add a background image for the main menu.
    
    imagebutton auto "gui/main_logo3_%s.png" xpos -1 ypos -2 focus_mask None action NullAction() hovered [Function(set_cursor_default)]
    
    imagebutton auto "gui/PatreonLogo3_%s.png" xpos 1503 ypos -5 focus_mask None action OpenURL("https://www.patreon.com/VoidStar") hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    $ y=114 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/main_start2_%s.png" xpos 217 ypos 958 focus_mask True action Start() hovered [ Play ("test_one", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_start.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff1
    on "replaced" action Hide('gui_tooltip')
    
    $ y+=71 # We increase y position for the next menu item. y has a value of 185(114+81=185) now. We could also use: xpos 773 ypos 185
    imagebutton auto "gui/main_load2_%s.png" xpos 514 ypos 958 focus_mask True  action ShowMenu('load'), Function(set_cursor_default) hovered [ Play ("test_two", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_load.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff2
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_config2_%s.png" xpos 812 ypos 958 focus_mask True action ShowMenu('preferences'), Function(set_cursor_default) hovered [ Play ("test_three", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_config.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff3
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_thanks2_%s.png" xpos 1110 ypos 958 focus_mask True action Start('thanksmainmenu'), Function(set_cursor_default) hovered [ Play ("test_four", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_credits.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff4
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_quit2_%s.png" xpos 1408 ypos 958 focus_mask True action Quit(confirm=False) hovered [ Play ("test_five", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_quit.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff5
    on "replaced" action Hide('gui_tooltip')
    


#begin main_eff
init -2:
    transform main_eff1:
        zoom 0.5
        easein 0.4 zoom 1.0
    transform main_eff2:
        zoom 0.5
        easein 0.8 zoom 1.0
    transform main_eff3:
        zoom 0.5
        easein 1.2 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.6 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 2.0 zoom 1.0
#end main_eff

screen main_menu_8:
    tag menu

    add "gui/mc ad login screen.png" # Add a background image for the main menu.
    
    imagebutton auto "gui/main_logo2_%s.png" xpos 0 ypos 0 focus_mask None action NullAction() hovered [Function(set_cursor_default)]
    
    imagebutton auto "gui/PatreonLogo3_%s.png" xpos 1503 ypos -5 focus_mask None action OpenURL("https://www.patreon.com/VoidStar") hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    $ y=114 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/main_start3_%s.png" xpos 217 ypos 958 focus_mask True action Start() hovered [ Play ("test_one", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_start.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff1
    on "replaced" action Hide('gui_tooltip')
    
    $ y+=71 # We increase y position for the next menu item. y has a value of 185(114+81=185) now. We could also use: xpos 773 ypos 185
    imagebutton auto "gui/main_load3_%s.png" xpos 514 ypos 958 focus_mask True  action ShowMenu('load'), Function(set_cursor_default) hovered [ Play ("test_two", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_load.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff2
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_config3_%s.png" xpos 812 ypos 958 focus_mask True action ShowMenu('preferences'), Function(set_cursor_default) hovered [ Play ("test_three", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_config.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff3
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_thanks3_%s.png" xpos 1110 ypos 958 focus_mask True action Start('thanksmainmenu'), Function(set_cursor_default) hovered [ Play ("test_four", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_credits.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff4
    on "replaced" action Hide('gui_tooltip')
    $ y+=71
    imagebutton auto "gui/main_quit3_%s.png" xpos 1408 ypos 958 focus_mask True action Quit(confirm=False) hovered [ Play ("test_five", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_quit.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at main_eff5
    on "replaced" action Hide('gui_tooltip')
    


#begin main_eff
init -2:
    transform main_eff1:
        zoom 0.5
        easein 0.4 zoom 1.0
    transform main_eff2:
        zoom 0.5
        easein 0.8 zoom 1.0
    transform main_eff3:
        zoom 0.5
        easein 1.2 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.6 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 2.0 zoom 1.0
#end main_eff

## ■██▓▒░ NAVIGATION ░▒▓████████████████████████████████████■
## This screen is responsible for the game menu/navigation. It's included in other screens to display the game menu navigation.
## http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():
    imagebutton auto "gui/game_menu_save_%s.png" xpos 1435 ypos 260 focus_mask True action ShowMenu('save'), Function(set_cursor_default) hovered [ Play ("test_one", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_geme_menu_save.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at nav_eff
    on "replaced" action Hide('gui_tooltip')
    imagebutton auto "gui/game_menu_load_%s.png" xpos 810 ypos 375 focus_mask True action ShowMenu('load'), Function(set_cursor_default) hovered [ Play ("test_two", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_geme_menu_load.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at nav_eff
    on "replaced" action Hide('gui_tooltip')
    imagebutton auto "gui/game_menu_config_%s.png" xpos 810 ypos 490 focus_mask True action ShowMenu('preferences'), Function(set_cursor_default) hovered [ Play ("test_three", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_geme_menu_config.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at nav_eff
    on "replaced" action Hide('gui_tooltip')
    imagebutton auto "gui/game_menu_main_%s.png" xpos 1435 ypos 605 focus_mask True action MainMenu() hovered [ Play ("test_one", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_geme_menu_main.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at nav_eff
    on "replaced" action Hide('gui_tooltip')
    imagebutton auto "gui/game_menu_return_%s.png" xpos 810 ypos 720 focus_mask True action Return(), Function(set_cursor_default) hovered [ Play ("test_two", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_geme_menu_return.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at nav_eff
    on "replaced" action Hide('gui_tooltip')
    imagebutton auto "gui/game_menu_quit_%s.png" xpos 810 ypos 835 focus_mask True action Quit() hovered [ Play ("test_three", "sfx/click.wav"), Function(set_cursor_hover), Show("gui_tooltip", my_picture="gui/tooltip_geme_menu_quit.png", my_tt_xpos=7, my_tt_ypos=964) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)] at nav_eff
    on "replaced" action Hide('gui_tooltip')
# The code below defines the ATL transform effects for the buttons on the game menu. These effects are triggered when we hover the mouse over them (hover and selected_hover). Effects that are triggered by idle and selected_idle events (when we stop hovering the mouse over them) ensure that the buttons are moved back to the initial state.
#begin nav_eff
init -2:
    transform nav_eff:
        on idle:
            easein 0.5 xpos 1435
        on selected_idle:
            easein 0.5 xpos 1435
        on hover:
            easein 0.3 xpos 1458
            easein 0.3 xpos 1418
        on selected_hover:
            easein 0.3 xpos 1458
            easein 0.3 xpos 1418
#end nav_eff

#begin choice_eff
init -2:
    transform choice_eff:
        on idle:
            easein 0.5 xpos -55
        on hover:
            easein 0.3 xpos -80
            easein 0.3 xpos -80
#end choice_eff

## ■██▓▒░ PREFERENCES ░▒▓███████████████████████████████████■
## Screen that allows the user to change the preferences.
## http://www.renpy.org/doc/html/screen_special.html#prefereces
screen preferences:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/config_ground.png" # We add the image that is shown in the background of the preferences screen.
    use navigation # We include the navigation screen (game menu)
    # Display windowed/full screen:

    imagebutton auto "gui/config_display_window_%s.png" xpos 553 ypos 355 focus_mask True action Preference('display', 'any window') at config_eff hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_windowed.png", my_tt_xpos=7, my_tt_ypos=964), Function(set_cursor_hover) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
    on "replaced" action Hide('gui_tooltip')
    imagebutton auto "gui/config_display_fullscreen_%s.png" xpos 745 ypos 355 focus_mask True action Preference('display', 'fullscreen') at config_eff hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_fullscreen.png", my_tt_xpos=7, my_tt_ypos=964), Function(set_cursor_hover) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
    on "replaced" action Hide('gui_tooltip')
    # Transitions on/off:
    imagebutton auto "gui/config_transitions_none_%s.png" xpos 930 ypos 355 focus_mask True action Preference('transitions', 'none') at config_eff hovered [ Play ("test_four", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_disable_transition.png", my_tt_xpos=7, my_tt_ypos=964), Function(set_cursor_hover) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
    on "replaced" action Hide('gui_tooltip')
    imagebutton auto "gui/config_transitions_all_%s.png" xpos 1122 ypos 355 focus_mask True action Preference('transitions', 'all') at config_eff hovered [ Play ("test_four", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_enable_transition.png", my_tt_xpos=7, my_tt_ypos=964), Function(set_cursor_hover) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
    on "replaced" action Hide('gui_tooltip')
    #Display Jane
    imagebutton auto "gui/config_jane_%s.png" xpos 500 ypos 2 focus_mask True action NullAction() hovered [Function(set_cursor_default)]
    on "replaced" action Hide('gui_tooltip')
    # Stop/continue skipping after choices
    imagebutton auto "gui/config_afterchoices_stop_%s.png" xpos 553 ypos 657 focus_mask True action Preference('after choices', 'stop') at config_eff hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_stop_skip.png", my_tt_xpos=7, my_tt_ypos=964), Function(set_cursor_hover) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
    on "replaced" action Hide('gui_tooltip')
    imagebutton auto "gui/config_afterchoices_skip_%s.png" xpos 745 ypos 657 focus_mask True action Preference('after choices', 'skip') at config_eff hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_go_skip.png", my_tt_xpos=7, my_tt_ypos=964), Function(set_cursor_hover) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
    on "replaced" action Hide('gui_tooltip')
    # Skip all/seen text
    imagebutton auto "gui/config_skip_seen_%s.png" xpos 930 ypos 657 focus_mask True action Preference('skip', 'seen') at config_eff hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip",
        my_picture="gui/tooltip_config_stop_skip.png", my_tt_xpos=7, my_tt_ypos=964), Function(set_cursor_hover) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
    on "replaced" action Hide('gui_tooltip')
    imagebutton auto "gui/config_skip_all_%s.png" xpos 1122 ypos 657 focus_mask True action Preference('skip', 'all') at config_eff hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_go_skip.png", my_tt_xpos=7, my_tt_ypos=964), Function(set_cursor_hover) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
    on "replaced" action Hide('gui_tooltip')
    # bar sliders for volume control, text speed and auto-forward time
    on "show" action Function(set_cursor_default)
    frame xpos 116 ypos 250:
        style_group "pref"
        has vbox
        bar value Preference("music volume")
    frame xpos 116 ypos 390:
        style_group "pref"
        has vbox
        bar value Preference("sound volume")
    frame xpos 116 ypos 530:
        style_group "pref"
        has vbox
        bar value Preference("voice volume")
    frame xpos 116 ypos 670:
        style_group "pref"
        has vbox
        bar value Preference("text speed")
    frame xpos 116 ypos 810:
        style_group "pref"
        has vbox
        bar value Preference("auto-forward time") bar_invert True

    imagebutton auto "gui/config_ntr_approve_%s.png" xpos 820 ypos 186 focus_mask True action ToggleField(persistent, "show_ntr") at config_eff hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip",
        my_picture="gui/tooltip_config_ntr.png", my_tt_xpos=7, my_tt_ypos=964), Function(set_cursor_hover) ] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]


init -2 python: 
    # Styling for the bar sliders:
    # Aleema's Customizing Menus tutorial: http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=9812
    # Bar style properties documentation: http://www.renpy.org/doc/html/style.html#bar-style-properties
    style.pref_frame.background = None
    style.pref_slider.left_bar = "gui/config_bar_full.png"
    style.pref_slider.right_bar = "gui/config_bar_empty.png"
    style.pref_slider.thumb = None
    style.pref_slider.xmaximum = 375
    style.pref_slider.ymaximum = 58    
init -2:
    transform config_eff:
        on idle:
            easein 0.5 rotate 0
        on selected_idle:
            easein 0.5 rotate 0
        on hover:
            easein 0.3 rotate 5
            easein 0.3 rotate -5
            repeat
        on selected_hover:
            easein 0.3 rotate 5
            easein 0.3 rotate -5
            repeat

            
## ■██▓▒░ SAVE / LOAD SLOT ░▒▓██████████████████████████████■
## This represents a load/save slot. You should customize this to ensure that the placement of the thumbnail and the slot text are as 
##desired. Positions (x1, y1, x2 and y2) are relative to the x, y parameters, that are passed when the screen is called. 
##To set the screenshot thumbnail size see options.rpy.
init -2 python: #we initialize x and y, so the load_save_slot screen below works at startup
    x=0
    y=0
screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Boş slot."), FileSaveName(number))
    $x1=x+3
    $y1=y+2
    add FileScreenshot(number) xpos x1 ypos y1
    $x2=x+10
    $y2=y+11
    text file_text xpos x2 ypos y2 size 20
init python:
    config.thumbnail_width = 406
    config.thumbnail_height = 228
## ■██▓▒░ SAVE SCREEN ░▒▓███████████████████████████████████■
screen save:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/file_picker_ground.png" # We add the file picker background image. This image is the same for save and load screens.
    imagebutton idle "gui/saveloadmenu_mousehover_idle.png" xpos 1340 ypos 0 focus_mask None action NullAction() hovered [ Function(set_cursor_default) ]
    add "gui/title_save.png" xpos 36 ypos 17 # We add the save title image on top of the background
    use file_picker # We include the file_picker screen
    on "show" action Function(set_cursor_default)

## ■██▓▒░ LOAD SCREEN ░▒▓███████████████████████████████████■
screen load:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/file_picker_ground.png"
    imagebutton idle "gui/saveloadmenu_mousehover_idle.png" xpos 1340 ypos 0 focus_mask None action NullAction() hovered [ Function(set_cursor_default) ]
    add "gui/title_load.png" xpos 36 ypos 17
    use file_picker
    on "show" action Function(set_cursor_default)
    on 'show' action SetMute('music/crystal hunter.mp3', True)

## ■██▓▒░ SAVE / LOAD FILE PICKER ░▒▓███████████████████████■
## Since saving and loading are so similar, we combine them into a single screen, file_picker. We then use the file_picker screen from simple load and save screens.
screen file_picker:
    use navigation # We include the navigation/game menu screen
    # Buttons for selecting the save/load page:
    imagebutton auto "gui/filepageback_%s.png" xpos 485 ypos 865 focus_mask True action FilePagePrevious() hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    imagebutton auto "gui/filepage1_%s.png" xpos 520 ypos 865 focus_mask True action FilePage(1) hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    imagebutton auto "gui/filepage2_%s.png" xpos 555 ypos 865 focus_mask True action FilePage(2) hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    imagebutton auto "gui/filepage3_%s.png" xpos 590 ypos 865 focus_mask True action FilePage(3) hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    imagebutton auto "gui/filepage4_%s.png" xpos 635 ypos 865 focus_mask True action FilePage(4) hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    imagebutton auto "gui/filepage5_%s.png" xpos 680 ypos 865 focus_mask True action FilePage(5) hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    imagebutton auto "gui/filepage6_%s.png" xpos 725 ypos 865 focus_mask True action FilePage(6) hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    imagebutton auto "gui/filepage7_%s.png" xpos 765 ypos 865 focus_mask True action FilePage(7) hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    imagebutton auto "gui/filepage8_%s.png" xpos 805 ypos 865 focus_mask True action FilePage(8) hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    imagebutton auto "gui/filepage9_%s.png" xpos 850 ypos 865 focus_mask True action FilePage(9) hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    imagebutton auto "gui/filepagenext_%s.png" xpos 890 ypos 865 focus_mask True action FilePageNext() hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    
    imagebutton auto "gui/fileslot_%s.png" xpos 70 ypos 114 focus_mask True action FileAction(1) hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    use load_save_slot(number=1, x=70, y=114)
    on "hide" action Function(set_cursor_default)
    imagebutton auto "gui/fileslot_%s.png" xpos 70 ypos 364 focus_mask True action FileAction(2) hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    use load_save_slot(number=2, x=70, y=364)
    on "hide" action Function(set_cursor_default)
    imagebutton auto "gui/fileslot_%s.png" xpos 70 ypos 614 focus_mask True action FileAction(3) hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    use load_save_slot(number=3, x=70, y=614)
    on "hide" action Function(set_cursor_default)
    
    imagebutton auto "gui/fileslot_%s.png" xpos 499 ypos 114 focus_mask True action FileAction(4) hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    use load_save_slot(number=4, x=499, y=114)
    on "hide" action Function(set_cursor_default)
    imagebutton auto "gui/fileslot_%s.png" xpos 499 ypos 364 focus_mask True action FileAction(5) hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    use load_save_slot(number=5, x=499, y=364)
    on "hide" action Function(set_cursor_default)
    imagebutton auto "gui/fileslot_%s.png" xpos 499 ypos 614 focus_mask True action FileAction(6) hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    use load_save_slot(number=6, x=499, y=614)
    on "hide" action Function(set_cursor_default)

    imagebutton auto "gui/fileslot_%s.png" xpos 928 ypos 114 focus_mask True action FileAction(7) hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    use load_save_slot(number=7, x=928, y=114)
    on "hide" action Function(set_cursor_default)
    imagebutton auto "gui/fileslot_%s.png" xpos 928 ypos 364 focus_mask True action FileAction(8) hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    use load_save_slot(number=8, x=928, y=364)
    on "hide" action Function(set_cursor_default)
    imagebutton auto "gui/fileslot_%s.png" xpos 928 ypos 614 focus_mask True action FileAction(9) hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    use load_save_slot(number=9, x=928, y=614)
    on "hide" action Function(set_cursor_default)
    

    
## ■██▓▒░ YES/NO PROMPT ░▒▓█████████████████████████████████■
## Screen that asks the user a yes or no question. You'll need to edit this to change the position and style of the text.
## http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:
    on "show" action Play("sound", "sfx/alert.flac")
    on "hide" action Function(set_cursor_default)
    modal True # A modal screen prevents the user from interacting with displayables below it, except for the default keymap.

    add "gui/yesno_ground.png"
    imagebutton auto "gui/yesno_yes_%s.png" xpos 620 ypos 422 action yes_action hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    imagebutton auto "gui/yesno_no_%s.png" xpos 988 ypos 422 action no_action hover_sound "sfx/click.wav" hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    
    if message == layout.ARE_YOU_SURE:
        add "gui/yesno_are_you_sure.png"
    elif message == layout.DELETE_SAVE:
        add "gui/yesno_delete_save.png"
    elif message == layout.OVERWRITE_SAVE:
        add "gui/yesno_overwrite_save.png"
    elif message == layout.LOADING:
        add "gui/yesno_loading.png"
    elif message == layout.QUIT:
        add "gui/yesno_quit.png"
    elif message == layout.MAIN_MENU:
        add "gui/yesno_main_menu.png"


screen proceed():
    on "hide" action Function(set_cursor_default)
    tag menu
    modal True
    
    add "gui/yesno_ground2.png"
    
    imagebutton auto "gui/yesno_yes2_%s.png" xpos 281 ypos 667 hover_sound "sfx/click.wav" focus_mask None action Return() hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]
    imagebutton auto "gui/yesno_no2_%s.png" xpos 1146 ypos 667 hover_sound "sfx/click.wav" focus_mask None action Quit(confirm=False) hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)]

default persistent.show_proceed = False
    


## ■██▓▒░ CUSTOM MOUSE POINTER ░▒▓██████████████████████████■
##This block is responsible for the custom mouse pointer
init python:

    def set_cursor_default():
        setattr( config, "mouse", None )

    def set_cursor_hover():
        setattr( config, "mouse", None )

    set_cursor_default()

init 1 python:
    def change_cursor(type="default"):
        persistent.mouse = type
        if type == "default":
            setattr(config, "mouse", None)
        elif type == "1":
            setattr(config, "mouse", None)
        elif type == "2":
            setattr(config, "mouse", None)
            
    if not hasattr(persistent, "mouse"):
        change_cursor()
    else:
        change_cursor(persistent.mouse)
# Configuration variables: http://www.renpy.org/doc/html/config.html
# Custom mouse pointer is commented out, to disable it for the time being, because of an issue in all recent versions of Ren'Py.
# PyTom: "There's also an issue where display latency introduced by newer Nvidia drivers makes config.mouse noticeably slow, when Maximum Pre-Rendered Frames is set (which is the default for the driver). As far as I know, this isn't fixable in the short term. For now, I strongly recommend disabling custom mouse cursors (config.mouse)." (Mar 29, 2013) http://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=19703&start=45#p259263

## ■██▓▒░ TOOLTIP ░▒▓███████████████████████████████████████■
screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos
    


## ■██▓▒░ CUSTOM SOUND CHANNEL ░▒▓██████████████████████████■
# This is the block where we declare the individual sound channels. This enables us to play several sound FX's without overlapping
init python:
    renpy.music.register_channel("test_one", "sfx", False)
    renpy.music.register_channel("test_two", "sfx", False)
    renpy.music.register_channel("test_three", "sfx", False)
    renpy.music.register_channel("test_four", "sfx", False)
    renpy.music.register_channel("test_five", "sfx", False)
    renpy.music.register_channel("test_six", "sfx", False)

## ■██▓▒░ THE TEXTBOX ░▒▓███████████████████████████████████■
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
    if not renpy.variant("medium"):
        add SideImage() xalign 0.0 yalign 1.0


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign) 
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

## ■██▓▒░ TEXTBOX DROP SHADOW ░▒▓███████████████████████████■
## This block is responsible for the text drop shadow effect for the textbox dialogue.
init:
    $ style.say_dialogue.drop_shadow = (2, 2)
    $ style.say_dialogue.drop_shadow_color = "#000000"

screen quick_menu:
    if quick_menu:
        imagebutton auto "gui/quick_back_%s.png" action Rollback() xpos 1417 ypos 1019 focus_mask True hovered [Show("gui_tooltip", my_picture="gui/tooltip_quick_back_menu.png", my_tt_xpos=0, my_tt_ypos=0), Function(set_cursor_hover)] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
        on "replaced" action Hide('gui_tooltip')
        imagebutton auto "gui/quick_auto_%s.png" action Preference("auto-forward", "toggle") xpos 1480 ypos 1019 focus_mask True hovered [Show("gui_tooltip", my_picture="gui/tooltip_quick_auto_menu.png", my_tt_xpos=0, my_tt_ypos=0), Function(set_cursor_hover)] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
        on "replaced" action Hide('gui_tooltip')
        imagebutton auto "gui/quick_skip_%s.png" action Skip() alternate Skip(fast=True, confirm=True) xpos 1542 ypos 1019 focus_mask True hovered [Show("gui_tooltip", my_picture="gui/tooltip_quick_skip_menu.png", my_tt_xpos=0, my_tt_ypos=0), Function(set_cursor_hover)] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
        on "replaced" action Hide('gui_tooltip')
        imagebutton auto "gui/quick_history_%s.png" action [SetVariable("yvalue", 1.0), ShowMenu('text_history'), Function(set_cursor_default)] xpos 1605 ypos 1019 focus_mask True hovered [Show("gui_tooltip", my_picture="gui/tooltip_quick_history_menu.png", my_tt_xpos=0, my_tt_ypos=0), Function(set_cursor_hover)] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
        on "replaced" action Hide('gui_tooltip')
        imagebutton auto "gui/quick_config_%s.png" action ShowMenu('preferences'), Function(set_cursor_default) xpos 1668 ypos 1019 focus_mask True hovered [Show("gui_tooltip", my_picture="gui/tooltip_quick_config_menu.png", my_tt_xpos=0, my_tt_ypos=0), Function(set_cursor_hover)] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
        on "replaced" action Hide('gui_tooltip')
        imagebutton auto "gui/quick_save_%s.png" action ShowMenu('save'), Function(set_cursor_default) xpos 1730 ypos 1019 focus_mask True hovered [Show("gui_tooltip", my_picture="gui/tooltip_quick_save_menu.png", my_tt_xpos=0, my_tt_ypos=0), Function(set_cursor_hover)] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
        on "replaced" action Hide('gui_tooltip')
        imagebutton auto "gui/quick_load_%s.png"action ShowMenu('load'), Function(set_cursor_default) xpos 1793 ypos 1019 focus_mask True hovered [Show("gui_tooltip", my_picture="gui/tooltip_quick_load_menu.png", my_tt_xpos=0, my_tt_ypos=0), Function(set_cursor_hover)] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
        on "replaced" action Hide('gui_tooltip')
        imagebutton auto "gui/quick_main_%s.png" action MainMenu() xpos 1857 ypos 1019 focus_mask True hovered [Show("gui_tooltip", my_picture="gui/tooltip_quick_main_menu.png", my_tt_xpos=0, my_tt_ypos=0), Function(set_cursor_hover)] unhovered [Hide("gui_tooltip"), Function(set_cursor_default)]
        on "replaced" action Hide('gui_tooltip')
## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

init -100:
    transform fade_overlay(start, end, duration):
        alpha start
        linear duration alpha end

screen choice(items):
    style_prefix "choice"
    on "show" action Function(renpy.show, "choice_overlay", at_list=[fade_overlay(0, 1, 0.5)], layer="choice_overlay")
    on "hide" action Function(renpy.show, "choice_overlay", at_list=[fade_overlay(1, 0, 0.5)], layer="choice_overlay")

    window: 
        style "menu_window"        
        
        yalign 1.9999999999999999999999999999999999999999
        if renpy.variant("small"):
            yalign 2.2329999999999999999999999999999999999999
        vbox:
            style "choice_vbox"
            spacing 0.1
            for caption, action, chosen in items:
                button:
                    action action
                    style "menu_choice_button"  xalign 0.5 hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)] at choice_eff

                    text caption style "menu_choice"

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text
style choice_button_text_hover_color is choice_button
style choice_button_text_idle_color is choice_button

style choice_vbox:
    xpos 960
    ypos -1375

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    

init python:
    #Code for customizing the in-game menu choices

    ##Code for customization of choice BG
    style.menu_choice_button.background = Frame("gui/button/choice_idle_background.png",1,1)
    style.menu_choice_button.hover_background = Frame("gui/button/choice_hover_background.png",1,1)
    style.menu_choice_button.yminimum = 69
    style.menu_choice_button.xminimum = 450

    ##Code for customization of text in the choice button
    style.menu_choice.color = "#7C7C7C"
    style.menu_choice.size = 40
    style.menu_choice.font = "Rabid Science.ttf"
    style.menu_choice.outlines = [(2, "#000", 0, 0)]
    style.menu_choice.hover_color = "#CECEBF"
    style.menu_choice.hover_outlines = [(2, "#000", 0, 0)]
    #style.menu_choice.line_spacing = 25
    style.menu_choice.slow_cps = 19
    style.menu_choice.bold = True
    
init -100:
    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        clear


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")



##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        xalign 1.0 #Centered Across
        yalign 1.0 # 75% Down from Top
        has vbox
 
        text prompt:
            yoffset 5
            style "say_dialogue"
            xoffset 0
       
        input:
            id "input"
            style "input"
            color "#85B200" # Color of Input Text
            yoffset 5
            xoffset 265
            
init -2 python:
    style.input_window.left_margin = 30
    style.input_window.right_margin = 30
    style.input_window.left_padding = 10
    style.input_window.right_padding = 10
    style.input_window.top_padding = 10
    
    style.input_text.size = 20


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False
    
    use text_history(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):
    
        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

# readback.rpy
# drop in readback module for Ren'Py by delta
# this file is licensed under the terms of the WTFPL
# see http://sam.zoy.org/wtfpl/COPYING for details

# voice_replay function added by backansi from Lemma soft forum.
# required renpy 6.12 or higher.


init 5 python:
    style.vscrollbar.xmaximum = 32
    style.vscrollbar.ymaximum = 997
    style.vscrollbar.yalign = .4
    style.vscrollbar.xpos = 60
    style.vscrollbar.ypos = 429
    style.vscrollbar.top_bar="gui/rrvscrollbar.png"
    style.vscrollbar.bottom_bar="gui/rrvscrollbar2.png"
    style.vscrollbar.thumb="gui/rrvscrollbar_thumb2.png"
    
    

init -5 python:
    config.game_menu.insert(1,( "text_history", u"Text History", ui.jumps("text_history_screen"), 'not main_menu'))

    # Styles.
    style.readback_window.background = Frame("gui/history_ground.png")
    style.readback_window.xmaximum = 1920
    style.readback_window.ymaximum = 1080
    style.readback_window.yalign = .4

    style.readback_frame.background = None 
    #Frame("frame.png", 24, 24)
    style.readback_frame.right_padding = 30
    style.readback_frame.top_padding = 24
    style.readback_frame.bottom_padding = 40
    style.readback_frame.xmargin = 5
    style.readback_frame.ymargin = 5
    style.readback_frame.xmaximum = 1920
    style.readback_frame.ymaximum = 1080
    style.readback_frame.xalign = .7
    #style.readback_frame.top_margin = 50
    #style.readback_frame.bottom_margin = 80
    style.readback_frame.xfill = True
    style.readback_frame.yfill = True
    
    style.readback_text.color = "#fff"
    
    #style.vscrollbar.xmaximum = 20
    #style.vscrollbar.top_bar=Frame("gui/rrvscrollbar.png", 5, 5)
    #style.vscrollbar.bottom_bar=Frame("gui/rrvscrollbar.png", 5, 5)
    #style.vscrollbar.thumb=Frame("gui/rrvscrollbar_thumb2.png", 5, 5)
    
    style.create("readback_button", "readback_text")
    style.readback_button.background = None
    
    style.create("readback_button_text", "readback_text")
    style.readback_button_text.selected_color = "#f12"
    style.readback_button_text.hover_color = "#f12"
    
    style.readback_label_text.bold = True
    
    # starts adding new config variables
    config.locked = False 
    
    # Configuration Variable for Text History 
    config.readback_buffer_length = 100 # number of lines stored
    config.readback_full = True # True = completely replaces rollback, False = readback accessible from game menu only (dev mode)
    config.readback_disallowed_tags = ["size"] # a list of tags that will be removed in the text history
    config.readback_choice_prefix = ">> "   # this is prefixed to the choices the user makes in readback
    
    # ends adding new config variables
    config.locked = True

init -2 python:

    # Two custom characters that store what they said
    class ReadbackADVCharacter(ADVCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            store.current_voice = ''
            return

    class ReadbackNVLCharacter(NVLCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            store.current_voice = ''
            return
            
    # this enables us to show the current line in readback without having to bother the buffer with raw shows
    def say_wrapper(who, what, **kwargs):
        store_current_line(who, what)
        return renpy.show_display_say(who, what, **kwargs)
    
    config.nvl_show_display_say = say_wrapper
    
    adv = ReadbackADVCharacter(show_function=say_wrapper)
    nvl = ReadbackNVLCharacter()
    NVLCharacter = ReadbackNVLCharacter
    
    # rewriting voice function to replay voice files when you clicked dialogues in text history screen
    def voice(file, **kwargs):
        if not config.has_voice:
            return
        
        _voice.play = file
        
        store.current_voice = file

    # overwriting standard menu handler
    # Overwriting menu functions makes Text History log choice which users choose.




        
    def nvl_screen_dialogue(): 
        """
         Returns widget_properties and dialogue for the current NVL
         mode screen.
         """

        widget_properties = { }
        dialogue = [ ]
        
        for i, entry in enumerate(nvl_list):
            if not entry:
                continue

            who, what, kwargs = entry

            if i == len(nvl_list) - 1:
                who_id = "who"
                what_id = "what"
                window_id = "window"

            else:
                who_id = "who%d" % i
                what_id = "what%d" % i
                window_id = "window%d" % i
                
            widget_properties[who_id] = kwargs["who_args"]
            widget_properties[what_id] = kwargs["what_args"]
            widget_properties[window_id] = kwargs["window_args"]

            dialogue.append((who, what, who_id, what_id, window_id))
        
        return widget_properties, dialogue
        
    # Overwriting nvl menu function
    def nvl_menu(items):

        renpy.mode('nvl_menu')
        
        if nvl_list is None:
            store.nvl_list = [ ]

        screen = None
        
        if renpy.has_screen("nvl_choice"):
            screen = "nvl_choice"
        elif renpy.has_screen("nvl"):
            screen = "nvl"
            
        if screen is not None:

            widget_properties, dialogue = nvl_screen_dialogue()        

            rv = renpy.display_menu(
                items,
                widget_properties=widget_properties,
                screen=screen,
                scope={ "dialogue" : dialogue },
                window_style=style.nvl_menu_window,
                choice_style=style.nvl_menu_choice,
                choice_chosen_style=style.nvl_menu_choice_chosen,
                choice_button_style=style.nvl_menu_choice_button,
                choice_chosen_button_style=style.nvl_menu_choice_chosen_button,
                type="nvl",                      
                )
                
            for label, val in items:
                if rv == val:
                    store.current_voice = ''
                    store_say(None, config.readback_choice_prefix + label)
            return rv
            
        # Traditional version.

        
    ## readback
    readback_buffer = []
    current_line = None
    current_voice = None
    
    def store_say(who, what):
        global readback_buffer, current_voice
        if preparse_say_for_store(what):
            new_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)
            readback_buffer = readback_buffer + [new_line]
            readback_prune()

    def store_current_line(who, what):
        global current_line, current_voice
        current_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)

    # remove text tags from dialogue lines 
    disallowed_tags_regexp = ""
    for tag in config.readback_disallowed_tags:
        if disallowed_tags_regexp != "":
            disallowed_tags_regexp += "|"
        disallowed_tags_regexp += "{"+tag+"=.*?}|{"+tag+"}|{/"+tag+"}"
    
    import re
    remove_tags_expr = re.compile(disallowed_tags_regexp) # remove tags undesirable in readback
    def preparse_say_for_store(input):
        global remove_tags_expr
        if input:
            return re.sub(remove_tags_expr, "", input)

    def readback_prune():
        global readback_buffer
        while len(readback_buffer) > config.readback_buffer_length:
            del readback_buffer[0]

    # keymap overriding to show text_history.
  
    
init python:
    yvalue = 1.0
    class NewAdj(renpy.display.behavior.Adjustment):
        def change(self,value):

            if value > self._range and self._value == self._range:
                return Return()
            else:
                return renpy.display.behavior.Adjustment.change(self, value)
                
    def store_yvalue(y):
        global yvalue
        yvalue = int(y)

screen text_history:

    #use navigation
    tag menu 
    
    if not current_line and len(readback_buffer) == 0:
        $ lines_to_show = []
        
    elif current_line and len(readback_buffer) == 0:
        $ lines_to_show = [current_line]
        
    elif current_line and not ( ( len(readback_buffer) == 3 and current_line == readback_buffer[-2]) or current_line == readback_buffer[-1]):  
        $ lines_to_show = readback_buffer + [current_line]
        
    else:
        $ lines_to_show = readback_buffer
    
    
    $ adj = NewAdj(changed = store_yvalue, step = 300)
    
    window:
        style_group "readback"

    
        side "c r":
            
            frame:
                
                has viewport:
                    mousewheel True
                    draggable True
                    yinitial yvalue
                    yadjustment adj

                vbox:
                    null height 10
                    
                    for line in lines_to_show:
                        
                        if line[0] and line[0] == "???":
                            label line[0]:
                                text_color "#FFFFFF" # name
                                text_size 41
                            label line[1]:
                                text_color "#FFFFFF"

                        elif line[0] and line[0] == "Zoey":
                            label line[0]:
                                text_color "#DFBFFF" # name
                                text_size 41
                            label line[1]:
                                text_color "#DFBFFF"
                        elif line[0] and line[0] == player_name:
                            label line[0]:
                                text_color "#85B200"
                                text_size 41
                            label line[1]:
                                text_color "#85B200"

                        elif line[0] and line[0] == "Jack":
                            label line[0]:
                                text_color "#444444"
                                text_size 41
                            label line[1]:
                                text_color "#444444"

                        elif line[0] and line[0] == "Elyse":
                            label line[0]:
                                text_color "#4DFFA6" # name
                                text_size 41
                            label line[1]:
                                text_color "#4DFFA6"

                        elif line[0] and line[0] == "Jane":
                            label line[0]:
                                text_color "#007095" # name
                                text_size 41
                            label line[1]:
                                text_color "#007095"

                        elif line[0] and line[0] == "Andre":
                            label line[0]:
                                text_color "#FFFF00" # name
                                text_size 41
                            label line[1]:
                                text_color "#FFFF00"

                        elif line[0] and line[0] == "Edis":
                            label line[0]:
                                text_color "#F34E52" # name
                                text_size 41
                            label line[1]:
                                text_color "#F34E52"

                        elif line[0] and line[0] == "Amir":
                            label line[0]:
                                text_color "#B25900" # name
                                text_size 41
                            label line[1]:
                                text_color "#B25900"

                        elif line[0] and line[0] == "Dahlia":
                            label line[0]:
                                text_color "#FF2626" # name
                                text_size 41
                            label line[1]:
                                text_color "#FF2626"

                        elif line[0] and line[0] == "Lexa":
                            label line[0]:
                                text_color "#008C00" # name
                                text_size 41
                            label line[1]:
                                text_color "#008C00"

                        elif line[0] and line[0] == "Chloe":
                            label line[0]:
                                text_color "#006DD9" # name
                                text_size 41
                            label line[1]:
                                text_color "#006DD9"

                        elif line[0] and line[0] == "Melisa":
                            label line[0]:
                                text_color "#FFC926" # name
                                text_size 41
                            label line[1]:
                                text_color "#FFC926"

                        elif line[0] and line[0] == "Victor":
                            label line[0]:
                                text_color "#BFFFDF" # name
                                text_size 41
                            label line[1]:
                                text_color "#BFFFDF"

                        elif line[0] and line[0] == "Cassandra":
                            label line[0]:
                                text_color "#A64DFF" # name
                                text_size 41
                            label line[1]:
                                text_color "#A64DFF"

                        elif line[0] and line[0] == "Ruby":
                            label line[0]:
                                text_color "#FF9999" # name
                                text_size 41
                            label line[1]:
                                text_color "#FF9999"
                                
                        elif line[0] and line[0] == "Karin":
                            label line[0]:
                                text_color "#8C0000" # name
                                text_size 41
                            label line[1]:
                                text_color "#8C0000"

                        elif line[0] and line[0] == "Aurora":
                            label line[0]:
                                text_color "#486DA2" # name
                                text_size 41
                            label line[1]:
                                text_color "#486DA2"
                        elif line[0] and line[0] == "Ingrid":
                            label line[0]:
                                text_color "#624720" # name
                                text_size 41
                            label line[1]:
                                text_color "#624720"
                        elif line[0] and line[0] == "Ivy":
                            label line[0]:
                                text_color "#822100" # name
                                text_size 41
                            label line[1]:
                                text_color "#822100"
                        elif line[0] and line[0] == "Mira":
                            label line[0]:
                                text_color "#55332B" # name
                                text_size 41
                            label line[1]:
                                text_color "#55332B"
                        elif line[0] and line[0] == "Luna":
                            label line[0]:
                                text_color "#CACAD9" # name
                                text_size 41
                            label line[1]:
                                text_color "#CACAD9"
                        elif line[0] and line[0] == "Dany":
                            label line[0]:
                                text_color "#F5E483" # name
                                text_size 41
                            label line[1]:
                                text_color "#F5E483"
                        elif line[0] and line[0] == "Ramsay":
                            label line[0]:
                                text_color "#C2C2BA" # name
                                text_size 41
                            label line[1]:
                                text_color "#C2C2BA"     
                        elif line[0] and line[0] == alien_daughter:
                            label line[0]:
                                text_color "#F1DDF7"
                                text_size 41
                            label line[1]:
                                text_color "#F1DDF7"     
                        elif line[0] and line[0] == "Elisande":
                            label line[0]:
                                text_color "#B78E7B" # name
                                text_size 41
                            label line[1]:
                                text_color "#B78E7B"   
                        elif line[0] and line[0] == "Walter":
                            label line[0]:
                                text_color "#E1A588" # name
                                text_size 41
                            label line[1]:
                                text_color "#E1A588"   
                                



                        elif line[0] and line[0] != " ":
                            label line[0]
                            


                        # if there's no voice just log a dialogue

                            
                        # else, dialogue will be saved as a button of which plays voice when clicked
                        else: 
                            textbutton line[1] action Play("voice", line[2] )
                        
                        null height 10
                
            bar adjustment adj style 'vscrollbar'
        textbutton _("Return") action Return(), Function(set_cursor_default) hovered [Function(set_cursor_hover)] unhovered [Function(set_cursor_default)] align (.97, 1.0)
    on "show" action Function(set_cursor_default)