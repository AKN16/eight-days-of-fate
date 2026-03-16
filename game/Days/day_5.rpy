label day_5:
    $ day_count += 1

    centered "DAY [day_count]"

    # ── NGÃ BA ĐƯỜNG → nền đen ──
    scene black with fade
    play music audio.music_royal fadein 1.5

    show hero_normal

    "Ngã ba đường. Ánh mắt [hero_name] mệt mỏi."
    "Không tức giận nữa. Chỉ là mệt."
    jump again_or_change

label next_day_5:

    # ── TRONG THÀNH → nền đen ──
    scene black with fade
    hide hero_normal

    "Tờ thông báo. [hero_name] không thèm nhìn."
    hero "Vua hay công chúa. Phải tìm ra mới được."

    menu:
        "Điều tra vua":
            jump to_king
        "Điều tra công chúa":
            jump to_princess
