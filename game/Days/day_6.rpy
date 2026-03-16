label day_6:
    $ day_count += 1

    centered "DAY [day_count]"

    # ── NGÃ BA ĐƯỜNG → nền đen ──
    scene black with fade
    play music audio.music_royal fadein 1.5

    show hero_normal

    "Ngã ba đường."
    "[hero_name] không nói gì. Chỉ nhìn."
    jump again_or_change

label next_day_6:

    # ── TRONG THÀNH → nền đen ──
    scene black with fade
    hide hero_normal

    "[hero_name] vào thành. Quen đến mức buồn nôn."
    hero "Lần này phải khác."

    menu:
        "Điều tra vua":
            jump to_king
        "Điều tra công chúa":
            jump to_princess
