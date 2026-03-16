label princess_is_dead_1:
    $ kill += 1

    # ── LÂU ĐÀI ÁC MA (nội thất) → dungeon ──
    scene bg_dungeon with fade

    show princess_normal

    "Công chúa nhìn dũng sĩ tiến lại gần."
    princess "(thấp giọng, không kinh hãi — chỉ mệt mỏi) Ngươi cũng chọn cách này."
    princess "Ta đã thấy điều này... vài lần rồi."
    "Cô ấy không chạy. Không kêu cứu."
    "Chỉ nhắm mắt."
    hide princess_normal

    # ── MÀN ĐÊM → đen ──
    scene black with dissolve

    "Dũng sĩ mang vàng đi."
    "Màn đêm buông xuống nhanh hơn bình thường."
    "Cơn buồn ngủ ép xuống."

    "..."
    "Ah. Lại kết cục này."
    "Ta không phán xét. Ta chỉ ghi lại."

    $ next_day = "day_" + str(day_count + 1)
    jump expression next_day
