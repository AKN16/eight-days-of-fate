label day_1:
    $ day_count += 1

    centered "DAY [day_count]"

    # ── NGÃ BA ĐƯỜNG → nền đen mặc định Ren'Py ──
    scene black with fade
    play music audio.music_royal fadein 1.5

    show hero_normal
    "Dũng sĩ [hero_name] từ phương xa, sau nhiều ngày rong ruổi, cuối cùng đặt chân đến vùng đất lạ."
    "Trước mắt hắn là một ngã ba đường. Bụi đường còn vương trên đôi giày mòn gót."
    "Nắng chiều vàng óng đổ dài. Gió thổi nhẹ, mang theo mùi của cánh rừng xa."
    "Đứng giữa ngã ba đường với túi lương thực đã cạn, [hero_name] buộc phải đưa ra lựa chọn."
    jump luck_or_next

label next_day_1:

    # ── TRONG THÀNH → nền đen ──
    scene black with fade
    hide hero_normal

    "[hero_name] bước vào thành. Một tờ thông báo dán trên cổng chính."
    hero "Giải cứu công chúa bị ác ma bắt giữ. Phần thưởng hậu hĩ."
    hero "...Hậu hĩ."
    "Nhìn vào túi tiền chỉ còn 1 đồng vàng."

    # ── CUNG ĐIỆN → palace hall ──
    scene bg_palace_hall with fade
    play music audio.music_royal fadein 1.0

    show king_normal

    king "Hỡi dũng sĩ phương xa! Ngươi đến vào đúng lúc."
    king "Đứa con tội nghiệp của ta đang bị tên ác ma giam cầm. Mỗi ngày trôi qua, ta chỉ biết cầu trời..."
    king "Hãy cứu lấy con ta. Phần thưởng sẽ xứng đáng với công sức."
    hero "Thần xin nhận lệnh."

    # ── NGÃ BA ĐƯỜNG → nền đen ──
    scene black with fade
    hide king_normal

    "[hero_name] lên đường đến lâu đài ác ma."
    "Đi đến ngã ba đường."
    jump long_or_short_road

label next_day_1_2:
    # ── LÂU ĐÀI ÁC MA (nội thất) → dungeon ──
    scene bg_dungeon with fade
    play music audio.music_myst fadein 1.5

    show devil_normal

    devil "Ồ? Khách mới."
    devil "Lâu lắm rồi ta không gặp kiểu này. Biến số thú vị."
    hero "Ta đến để đưa Công Chúa về."

    show princess_normal

    princess "Ngươi... ngươi thật sự đến đây?"
    princess "Cứu ta đi. Làm ơn — cứu ta ra khỏi chỗ này!"
    devil "Muốn mang cô ấy đi thì phải qua ta trước."
    jump attack

label next_day_1_3:
    # ── LÂU ĐÀI ÁC MA (sau chiến đấu) → dungeon ──
    "Dũng sĩ cứu được công chúa."
    "Phía sau ngai của ác ma là một cánh cửa hé mở — bên trong, vàng chất thành đống."

    show princess_normal

    princess "..."
    princess "Ở đất nước này, có hai cách sở hữu tài sản của người khác."
    princess "Cách thứ nhất — chiến thắng họ trong chiến đấu. Như ngươi vừa làm."
    princess "(khẽ nhìn về phía cửa vàng) Cách thứ hai... sau này ngươi sẽ biết."

    # ── CUNG ĐIỆN → palace hall ──
    scene bg_palace_hall with fade
    play music audio.music_royal fadein 1.0

    show king_normal

    king "Ha! Dũng sĩ quả nhiên không phụ lòng ta! Xuất sắc, xuất sắc lắm!"
    king "Phần thưởng xứng đáng nhất mà ta có thể ban — ngươi sẽ được cưới công chúa!"
    hero "Thần không—"
    king "Không cần khiêm tốn! Đây là vinh dự tột bậc! Hãy mở tiệc!"

    show princess_normal

    princess "(thì thầm) Còn nhớ cách thứ hai ta nói không?"
    princess "(thì thầm) Kết hôn với người đang sở hữu tài sản đó."
    princess "(nhìn thẳng) Chào mừng đến vùng đất này."

    "Dũng sĩ tức giận nhưng không thoát được buổi tiệc."
    "Định bụng mai sẽ tính. Nhắm mắt chỉ một chút..."

    # ── MÀN ĐÊM → đen ──
    scene black with dissolve

    "..."
    "Biến số đầu tiên. Chưa biết sẽ đi đến đâu."
    "Cũng thú vị."

    jump day_2
