label true:
    # ── RỪNG → dẫn vào lâu đài ──
    scene bg_forest with fade
    play music audio.music_myst fadein 2.0
    hide hero_normal

    "Con đường xuyên rừng dẫn đến một nơi không ngờ tới."
    "Lâu đài ác ma. Nhưng không có công chúa, không có tiếng kêu cứu."

    # ── LÂU ĐÀI ÁC MA (nội thất) → dungeon ──
    scene bg_dungeon with fade

    "Chỉ có Zagan — đang ngồi trên ngai, trước mặt là vô số mảnh hình ảnh lung linh."

    show devil_see_and_drink_tea

    devil "À. Ngươi chọn đúng con đường rồi."
    hero "Tất cả — vòng lặp, công chúa, vua — tất cả là do ngươi?"
    devil "Ta không nói dối bao giờ."
    devil "Ta chỉ tạo ra sân khấu. Còn diễn như thế nào là do các ngươi tự chọn."
    hero "Công chúa. Cô ấy không bị bắt. Vua đã bán cô ấy cho ngươi."
    devil "(không phủ nhận) Vua muốn vàng. Ta muốn xem. Mọi người đều có được điều mình muốn."
    hero "Trừ công chúa."
    devil "..."
    devil "(lần đầu tiên ngừng lại) Đó là điều thú vị nhất trong vòng này."

    hero "Ta sẽ kết thúc chuyện này."
    devil "Được thôi. Ta đã xem đủ vòng này rồi."

    "Trận chiến cuối cùng."
    "Lần này không phải để cứu công chúa. Lần này là để thoát thật sự."
    "Zagan thua — hoặc chọn thua."

    # ── VÙNG ĐẤT MỚI → đen rồi fade ──
    scene black with dissolve

    "Ngày hôm sau, [hero_name] tỉnh dậy."
    "Không phải ngã ba đường."
    "Một vùng đất mới. Thật sự mới."

    show devil_smirk

    "..."
    "Biến số thú vị nhất từ trước đến giờ."
    "Nhưng mọi vòng lặp đều sẽ có biến số tiếp theo."
    "Ta sẽ không vội."

    "END."
    return
