default hero_name = ""
default kill = 0
default princess_affection = 0
default day_count = 0
default hero_dead = 0
default name_try = 0
default investigated_king = 0
default helped_princess_escape = 0
default passed_crossroad = False
default royal_area = False




init python:
    def make_sfx_callback(sfx_path):
        def cb(event, interact=True, **kwargs):
            if event == "begin":
                renpy.sound.play(sfx_path, channel="voice")
        return cb

define hero     = Character("[hero_name]",                  callback=make_sfx_callback("audio/sfx/sfx_hero.ogg"))
define king     = Character("Nexia",     color="#f0e32d",   callback=make_sfx_callback("audio/sfx/sfx_king.ogg"))
define princess = Character("Công chúa", color="#ff65a5",   callback=make_sfx_callback("audio/sfx/sfx_princess.ogg"))
define devil    = Character("Zagan",     color="#D73535",    callback=make_sfx_callback("audio/sfx/sfx_devil.ogg"))



screen platform_game():
    add "hero_normal" xpos player_x ypos player_y
    key "K_SPACE" action Function(jump)


label start:
    while hero_name.strip() == "":
        $ hero_name = renpy.input("Nhập tên của bạn:")
        $ hero_name = hero_name.strip()
        $ name_try += 1

        if hero_name == "":
            if name_try > 10:
                "Giỡn mặt hả??? "
            else:
                "Bạn chưa nhập tên. Vui lòng nhập tên để tiếp tục."

    jump day_1


label show_day:
    show screen day_screen
    pause 1.5
    hide screen day_screen
    return


label crossroad_minigame:
    show screen platform_game

    while not passed_crossroad:
        $ update_player()
        pause 0.03

    hide screen platform_game
    return
