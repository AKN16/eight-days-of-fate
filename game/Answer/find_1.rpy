label find_1:
    # ── CUNG ĐIỆN / KHO VÀNG → palace inner ──
    scene bg_palace_inner with fade
    play music audio.music_royal fadein 1.0

    "Dũng sĩ lẻn vào kho vàng hoàng gia."
    "Không có lính canh. Bên trong — trống rỗng."
    hero "Không có gì?"
    "Sổ sách. Thuế thu vào — nhiều. Chi tiêu — kỳ lạ."
    "Quần áo. Tiệc tùng. Và một khoản chi mà dũng sĩ không thể tin là có thật."
    hero "(thấp giọng) Ông ta đã dùng tiền thuế của dân để..."

    # ── TRONG THÀNH → đen ──
    scene black with fade

    "Dũng sĩ trộm hai quyển sổ rồi lẻn ra."
    "Trong thành có một nhóm đã nghi ngờ vua từ lâu — chưa có bằng chứng."
    "Đến gặp họ. Đặt hai quyển sổ xuống bàn."
    "Không cần nói gì thêm."

    "Đêm đó bằng chứng được công bố."
    "Vua bị trục xuất khỏi thành trước bình minh."

    hero "Công chúa—"
    "Dũng sĩ chợt nhớ ra. Đã quên mất công chúa."

    # ── NHÌN VỀ LÂU ĐÀI ÁC MA → devil castle ──
    scene bg_devil_castle with fade
    play music audio.music_myst fadein 1.5

    "Nhìn về phía lâu đài ác ma. Có ánh lửa."
    hero "..."

    scene black with dissolve

    "Cơn buồn ngủ ập đến. Mạnh hơn mọi lần."

    $ next_day = "day_" + str(day_count + 1)
    jump expression next_day
