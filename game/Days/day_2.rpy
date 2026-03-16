label day_2:
    $ day_count += 1

    centered "DAY [day_count]"

    # ── NGÃ BA ĐƯỜNG → nền đen ──
    scene black with fade
    play music audio.music_royal fadein 1.5

    show hero_normal

    "Ngã ba đường."
    "Ánh nắng ban mai. Bụi đường. Tiếng chim."
    "..."
    "Chính xác là ngã ba này."

    hero "Hả...?"
    hero "Đây là... chỗ ta đứng hôm qua?"
    hero "Không. Chắc ta đi lạc. Hay bị ảo giác."
    hero "...Ừ chắc vậy. Đừng nghĩ nhiều."

    "Đứng giữa ngã ba đường với túi lương thực đã cạn, [hero_name] buộc phải đưa ra lựa chọn."
    jump again_or_change

label next_day_2:

    # ── TRONG THÀNH → nền đen ──
    scene black with fade
    hide hero_normal

    "Dũng sĩ bước vào thành. Tờ thông báo vẫn còn đó."

    hero "..."
    hero "Phải tìm hiểu chuyện này thôi."

    # ── CUNG ĐIỆN → palace hall ──
    scene bg_palace_hall with fade
    play music audio.music_royal fadein 1.0

    show king_normal

    king "Ồ, dũng sĩ! Ngươi đến nhận nhiệm vụ giải cứu công chúa?"
    king "Đứa con khốn khổ của ta vẫn đang bị giam cầm. Ngươi là hy vọng duy nhất."
    hero "Vâng. Nhưng phần thưởng — phải là vàng."
    king "..."
    king "Được, được! Ta hứa thưởng vàng xứng đáng!"

    # ── NGÃ BA ĐƯỜNG → nền đen ──
    scene black with fade
    hide king_normal

    "[hero_name] lên đường. Mọi thứ trông quen đến kỳ lạ."
    "Đi đến ngã ba đường."
    jump long_or_short_road

label next_day_2_2:
    # ── LÂU ĐÀI ÁC MA (nội thất) → dungeon ──
    scene bg_dungeon with fade
    play music audio.music_myst fadein 1.5

    show devil_normal

    devil "Lại đến rồi. Vẫn câu đó, vẫn bộ mặt đó."
    devil "Ta tưởng ngươi sẽ mang lại gì đó khác chứ."
    hero "Im. Đâu là công chúa."

    show princess_normal

    princess "Ngươi... lại đến."
    princess "(nhỏ giọng) Ngươi có nhớ gì không? Về ngày hôm qua?"
    devil "Câu hỏi thú vị đấy, công chúa ơi. Nhưng chưa phải lúc."
    devil "Nào dũng sĩ, ta đang chờ."
    jump attack

label next_day_2_3:
    # ── SAU CHIẾN ĐẤU → dungeon ──
    "Dũng sĩ cứu được công chúa."
    "Phía sau cánh cửa — vàng, vẫn còn đó."

    show princess_normal

    princess "Ngươi nhớ vàng đó không?"
    hero "Nhớ. Hôm qua—"
    princess "(dừng lại) Hôm qua?"
    hero "..."
    princess "Không quan trọng. Đưa ta về thành đi."

    # ── CUNG ĐIỆN → palace hall ──
    scene bg_palace_hall with fade
    play music audio.music_royal fadein 1.0

    show king_normal

    king "Dũng sĩ trở về! Ta đã nói mà, ngươi nhất định sẽ thành công!"
    king "Vàng — ta sẽ thưởng vàng như đã hứa. Và thêm một điều nữa—"
    king "Ta gả công chúa cho ngươi!"
    hero "Thần đã nói—"
    king "Hãy mở tiệc! Đêm nay ta sẽ không nghe từ chối!"

    "Dũng sĩ bị cuốn vào bữa tiệc."
    "Cố không ngủ. Cố gắng hết sức."
    "Không có tác dụng."

    # ── MÀN ĐÊM → đen ──
    scene black with dissolve

    "..."
    "Biến số này đang nhận ra. Nhanh hơn những lần trước."
    "Xem tiếp thôi."

    jump day_3
