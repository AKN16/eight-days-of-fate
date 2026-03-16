label helped_princess_escape_1:
    $ helped_princess_escape += 1
    $ princess_affection += 1

    # ── LÂU ĐÀI ÁC MA (nội thất) → dungeon ──
    scene bg_dungeon with fade

    show princess_normal

    hero "Ngươi có muốn rời khỏi đây không — vĩnh viễn?"
    princess "(nhìn hero một lúc dài) Ngươi hỏi thật không?"
    hero "Ta chia đôi số vàng này với ngươi. Đi đi. Đừng quay lại vùng đất này."
    princess "..."
    princess "Ngươi không sợ ta là nguyên nhân của vòng lặp sao?"
    hero "Nếu ngươi là nguyên nhân, vòng lặp đã tự kết thúc từ lâu rồi."

    "Công chúa nhìn về phía cửa. Nhìn lại hero."
    princess "Cảm ơn."
    hide princess_normal

    "Cô ấy đi. Không ngoảnh đầu lại."

    # ── RỪNG → forest ──
    scene bg_forest with fade
    play music audio.music_myst fadein 2.0

    "Đêm đó [hero_name] ngủ dưới gốc cây trong rừng."
    hero "Không... ta phải tỉnh... phải..."

    scene black with dissolve

    "Không có tác dụng."

    $ next_day = "day_" + str(day_count + 1)
    jump expression next_day
