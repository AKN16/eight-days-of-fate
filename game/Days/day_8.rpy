label day_8:
    $ day_count += 1
    centered "DAY [day_count]"

    # ── NGÃ BA ĐƯỜNG → nền đen ──
    scene black with fade
    play music audio.music_royal fadein 1.5

    show hero_normal

    menu:
        "Đi vào rừng":
            jump true
        "đi vào thành":
            jump day_8_next

label day_8_next:
    hide hero_normal
    if kill >= 1:
        jump terrible

    elif investigated_king >= 2 and princess_affection < 3:
        jump ending_normal

    elif princess_affection >= 3 and helped_princess_escape >= 1:
        if investigated_king >= 2:
            jump happy
        else:
            jump good

    else:
        jump bad
