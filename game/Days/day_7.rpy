label day_7:
    $ day_count += 1

    centered "DAY [day_count]"

    # ── NGÃ BA ĐƯỜNG → nền đen ──
    scene black with fade
    play music audio.music_royal fadein 1.5

    show hero_normal

    "Ngã ba đường."
    "[hero_name] nhìn hai con đường."
    "Không còn cảm giác gì đặc biệt nữa."
    jump again_or_change

label next_day_7:

    # ── TRONG THÀNH → nền đen ──
    scene black with fade
    hide hero_normal

    "Ngày cuối. [hero_name] bước vào thành lần cuối."
    hero "Hôm nay phải kết thúc chuyện này."

    menu:
        "Điều tra vua":
            jump to_king
        "Điều tra công chúa":
            jump to_princess
