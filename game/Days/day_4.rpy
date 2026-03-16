label day_4:
    $ day_count += 1

    centered "DAY [day_count]"

    # ── NGÃ BA ĐƯỜNG → nền đen ──
    scene black with fade
    play music audio.music_royal fadein 1.5

    show hero_normal

    "[hero_name] mở mắt. Ngã ba đường. Lần nữa."
    "Không có gì bất ngờ nữa — chỉ có mệt mỏi."
    jump again_or_change

label next_day_4:

    # ── TRONG THÀNH → nền đen ──
    scene black with fade
    hide hero_normal

    "[hero_name] nhìn tờ thông báo. Không buồn đọc nữa."
    hero "Vua hay công chúa. Ai mới là người giữ vòng lặp này."

    menu:
        "Điều tra vua":
            jump to_king
        "Điều tra công chúa":
            jump to_princess

label to_princess:
    # ── CUNG ĐIỆN → palace hall (lướt qua) ──
    scene bg_palace_hall with fade
    play music audio.music_royal fadein 0.5

    show king_normal

    king "Hỡi dũng sĩ phương x—"
    hero "Tôi nhận nhiệm vụ."
    hide king_normal

    "Dũng sĩ rời đi trước khi vua kịp nói hết câu."

    # ── LÂU ĐÀI ÁC MA (nội thất) → dungeon ──
    scene bg_dungeon with fade
    play music audio.music_myst fadein 1.5

    show devil_normal

    devil "(không buồn đứng dậy) À, đến rồi."
    hero "Hôm nay ta cần nói chuyện với công chúa."
    devil "Đánh ta trước. Sau đó muốn làm gì thì làm."

    show princess_normal

    "Sau trận chiến."

    princess "Ngươi nhìn ta như thể đang tìm kiếm gì đó."
    hero "Ta cần biết — ngươi có phải nguyên nhân của vòng lặp không?"
    princess "(im lặng dài) Nếu ta là nguyên nhân, ta đã không mắc kẹt trong đó."
    princess "Ta bị kẹt ở đây từ trước khi ngươi đặt chân vào vùng đất này, dũng sĩ."
    hero "Bao lâu?"
    princess "Lâu hơn ngươi nghĩ."

    menu:
        "Giết công chúa":
            jump princess_is_dead_1
        "Giúp công chúa trốn thoát":
            jump helped_princess_escape_1

label to_king:
    $ investigated_king += 1

    # ── CUNG ĐIỆN → palace hall ──
    scene bg_palace_hall with fade
    play music audio.music_royal fadein 1.0

    show king_normal

    king "Hỡi dũng sĩ phương xa, đứa con tội nghiệp—"
    hero "Tôi muốn hỏi thêm về công chúa trước khi nhận lệnh."
    king "Ồ? Ừ... tất nhiên. Hỏi đi."
    hero "Ngài lo lắng cho công chúa đến mức nào?"
    king "Lo lắng? Ta — ta là cha của con bé! Ta lo lắng từng ngày từng đêm!"
    king "Mỗi buổi sáng thức dậy ta chỉ cầu mong có người đủ dũng cảm mang con ta về."
    hero "..."

    menu:
        "Giết vua":
            jump king_is_dead_1
        "Điều tra xem ông ta có phải chủ vòng lặp không":
            jump find_1
