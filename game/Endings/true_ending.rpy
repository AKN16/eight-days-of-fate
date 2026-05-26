label true:
    # ── RỪNG → dẫn vào lâu đài ──
    scene bg_forest with fade
    play music audio.music_myst fadein 2.0
    hide hero_normal

    "Con đường xuyên rừng dẫn đến một nơi không ngờ tới."
    "Lâu đài ác ma. Nhưng không có công chúa, không có tiếng kêu cứu."

    # ── LÂU ĐÀI ÁC MA → dungeon ──
    scene bg_dungeon with fade

    "Chỉ có Zagan — đang ngồi trên ngai, trước mặt là vô số mảnh hình ảnh từ những vòng lặp trước."

    show devil_see_and_drink_tea

    devil "Cùng uống một ly trà nhé, dũng sĩ."
    hero "Tất cả...tất cả là do ngươi?"
    devil "Ta chưa từng phủ nhận....hmm...ta cũng chưa từng thừa nhận."
    devil "Con đường này là do nhân loại cấc ngươi từ lựa chọn, đừng có mà đỗ lỗi cho ta."
    hero "...."
    devil "Ừ đúng rồi đó. Những thứ ngươi đang nghĩ đều là thật...dũng sĩ... à không phải là "The Fool"."
    hero "...Có ý gì đây?"
    devil "...(không quan tâm)"

    hero "Ta sẽ kết thúc chuyện này."
    devil "Được thôi."

    jump attack


    "Trận chiến cuối cùng."
    "Lần này không phải để cứu công chúa. Lần này là để thoát thật sự."
    hero "Ta thắng rôi...Không...ta tự do rồi.."

    "[hero_name] chạy đi khỏi vùng đất này. Không quan tâm bất kì điều gì khác nữa."

    # ── VÙNG ĐẤT MỚI → đen rồi fade ──
    scene black with dissolve

    "Ngày hôm sau, [hero_name] tỉnh dậy."
    "Không phải ngã ba đường."
    "Một vùng đất mới. Thật sự mới."

    show devil_smirk

    "..."
    "Tạm biệt... và hẹn gặp lại...[hero_name]"


    "END."
    return
