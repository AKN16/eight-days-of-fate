label run_away:
    # ── RỪNG ──
    scene bg_forest with fade
    play music audio.music_myst fadein 2.0

    "[hero_name] chọn đi vào rừng."
    "Cây cối rậm rạp. Tiếng chim. Bình yên lạ thường."
    "Rồi — mùi khói."

    # ── LÂU ĐÀI ÁC MA (ngoài trời) → nhìn ra ──
    scene bg_devil_castle with fade

    "Nhìn qua kẽ lá — tòa thành đang bốc lửa."

    hero "...Cháy?"
    "Ác ma không cần ai đánh bại nó mới gây ra hậu quả."
    "Trốn tránh chưa bao giờ là cách giải quyết vấn đề."

    # ── MÀN ĐÊM → đen ──
    scene black with dissolve

    "..."
    "Ngày hôm đó kết thúc trong im lặng."

    $ next_day = "day_" + str(day_count)
    jump expression next_day
