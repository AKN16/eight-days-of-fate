label king_is_dead_1:
    # ── CUNG ĐIỆN → palace hall ──
    scene bg_palace_hall with fade

    "Dũng sĩ không cần suy nghĩ nhiều."
    show king_normal
    king "Ngươi muốn—"
    "Xong."
    hide king_normal

    # ── TRONG THÀNH / PHÁP TRƯỜNG → đen ──
    scene black with fade
    play music audio.music_myst fadein 1.0

    "Lính ập vào từ khắp hướng."
    "Dũng sĩ chạy. Không thoát được."

    "Dũng sĩ nhắm mắt chờ."
    "Thay vì đau — là cơn buồn ngủ quen thuộc."

    scene black with dissolve

    "..."
    "Giết vua thì vòng lặp vẫn chạy."
    "Vì vua không phải nguyên nhân — ông ta chỉ là một phần của sân khấu."

    $ next_day = "day_" + str(day_count + 1)
    jump expression next_day
