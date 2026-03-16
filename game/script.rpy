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

# ===== PLATFORM GAME VARIABLES =====
default player_x = 300
default player_y = 0
default v_y = 0
default gravity = 2
default on_ground = False

define ground_y = 420
define player_h = 120


define hero = Character("[hero_name]")
define king = Character("Nexia", color="#f0e32d")
define princess = Character("Công chúa", color="#ff65a5")
define devil = Character("Zagan", color="#D73535")


# Image definitions đã chuyển sang characters.rpy và backgrounds.rpy


init python:
    def update_player():
        global player_y, v_y, on_ground

        v_y += gravity
        player_y += v_y

        if player_y + player_h >= ground_y:
            player_y = ground_y - player_h
            v_y = 0
            on_ground = True
        else:
            on_ground = False

        renpy.restart_interaction()

    def jump():
        global v_y, on_ground
        if on_ground:
            v_y = -20
            on_ground = False


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
