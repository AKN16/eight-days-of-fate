label day_3:
    $ day_count += 1

    centered "DAY [day_count]"

    # ── NGÃ BA ĐƯỜNG → nền đen ──
    scene black with fade
    play music audio.music_royal fadein 1.5

    show hero_normal

    "Ngã ba đường."
    "Vẫn ngã ba này."
    hero "(nghiến răng) Đây không phải ảo giác."

    "Đứng giữa ngã ba đường, [hero_name] buộc phải đưa ra lựa chọn."
    jump again_or_change

label next_day_3:

    # ── CUNG ĐIỆN → palace hall ──
    scene bg_palace_hall with fade
    play music audio.music_royal fadein 1.0
    hide hero_normal

    show king_normal

    king "Hỡi dũng sĩ phương xa, hãy cứu lấy đứa con tội nghiệp—"
    hero "Thần hiểu rồi. Thần sẽ đi."
    king "À... ừ, tốt lắm. Phần thưởng—"
    hero "Biết rồi."

    # ── CUNG ĐIỆN / THƯ VIỆN → palace inner ──
    scene bg_palace_inner with fade
    hide king_normal

    "[hero_name] đi thẳng đến thư viện hoàng gia."
    "Phải tìm ra nguyên nhân của vòng lặp này."
    jump libary

label next_day_3_1:
    # ── NGÃ BA ĐƯỜNG → nền đen ──
    scene black with fade
    play music audio.music_royal fadein 1.0

    "[hero_name] lên đường đến lâu đài ác ma."
    "Đi đến ngã ba đường."
    jump long_or_short_road

label next_day_3_2:
    # ── LÂU ĐÀI ÁC MA (nội thất) → dungeon ──
    scene bg_dungeon with fade
    play music audio.music_myst fadein 1.5

    show devil_normal

    devil "Ngày thứ ba. Ngươi đang tiến bộ đấy — ít nhất là về tốc độ."
    hero "Công chúa đâu."

    show princess_normal

    princess "..."
    princess "Lần này ngươi có vẻ... khác."
    princess "(quan sát) Ngươi biết mình đang lặp lại không?"
    devil "Ah. Câu chuyện bắt đầu thú vị rồi. Nào, đừng để ta chờ."
    jump attack

label next_day_3_3:
    # ── SAU CHIẾN ĐẤU → dungeon ──
    "Dũng sĩ cứu được công chúa."

    show princess_normal

    princess "Ngươi vào thư viện hôm nay."
    hero "Ngươi biết?"
    princess "Ta biết mọi thứ ngươi làm trong thành. Vòng lặp này — ta đã ở đây lâu hơn ngươi rất nhiều."
    hero "Bao lâu?"
    princess "(ngừng lại) Đủ lâu."

    # ── CUNG ĐIỆN → palace hall ──
    scene bg_palace_hall with fade
    play music audio.music_royal fadein 1.0

    show king_normal

    king "Xuất sắc! Dũng sĩ lại lập công! Như ta đã kỳ vọng—"
    king "Phần thưởng lần này — ngươi sẽ cưới công chúa!"
    hero "Vàng. Chỉ cần vàng."
    king "Ừ... vàng thì được. Nhưng ta vẫn muốn—"
    hero "Chỉ. Vàng."
    king "..."
    king "Được rồi, được rồi."

    # ── RA NGOÀI / MÀN ĐÊM → đen ──
    scene black with fade
    hide king_normal

    "Dũng sĩ nhận vàng, rời thành."
    "Chưa kịp ra khỏi cổng thì nhóm người lạ mặt xuất hiện."
    "Ma thuật ru ngủ. Túi vàng biến mất."

    scene black with dissolve

    "..."
    "Vòng lặp không thích bị thoát dễ dàng như vậy."
    "Dù sao — đêm nay ngươi đã biết tên ta rồi, công chúa ơi."

    jump day_4
