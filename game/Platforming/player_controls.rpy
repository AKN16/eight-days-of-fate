# =============================================
# FILE: Platforming/player_controls.rpy
# MỤC ĐÍCH: Xử lý toàn bộ điều khiển của player trong màn platforming
#
# ── CÁCH HOẠT ĐỘNG ──
#   - File này định nghĩa 2 thứ:
#       1. Variables (biến) lưu trạng thái player
#       2. Screen "platforming_screen" hiển thị player và nhận input phím
#
# ── PHÍM ĐIỀU KHIỂN ──
#   A         = di chuyển trái
#   D         = di chuyển phải
#   W         = di chuyển lên (dùng khi có thang / leo)
#   S         = di chuyển xuống / cúi
#   SPACE     = nhảy (chỉ nhảy được khi đang đứng trên mặt đất)
#   J         = Skill 1 (xem skills.rpy để chỉnh)
#   K         = Skill 2
#   L         = Skill 3
#
# ── CÁCH GỌI MÀNG PLATFORMING ──
#   Trong label bất kỳ, dùng:
#       call screen platforming_screen
#   hoặc show/hide thủ công nếu muốn kết hợp với dialogue.
#
# ── CÁCH CHỈNH TỐC ĐỘ / VẬT LÝ ──
#   Tất cả hằng số vật lý nằm trong init python block bên dưới.
#   Tìm dòng "# === CÓ THỂ CHỈNH ===" để biết chỗ nào an toàn để sửa.
# =============================================


# ── BIẾN TRẠNG THÁI PLAYER ──
# Các biến này lưu vị trí, tốc độ, và trạng thái player trong platforming.
# Dùng 'default' thay vì 'define' để có thể reset khi cần.
default px = 200           # Vị trí X của player (tính từ trái màn hình, pixel)
default py = 400           # Vị trí Y của player (tính từ trên xuống, pixel)
default pvy = 0            # Tốc độ dọc (velocity Y): dương = rơi xuống, âm = bay lên
default pvx = 0            # Tốc độ ngang (velocity X): dùng cho momentum nếu muốn
default p_on_ground = True # True nếu player đang đứng trên mặt đất
default p_facing = "right" # Hướng player đang nhìn: "left" hoặc "right"
default p_moving = False   # True nếu player đang di chuyển ngang

# ── BIẾN KIỂM SOÁT VÒNG LẶP PLATFORMING ──
# Dùng để thoát khỏi màn platforming khi đạt điều kiện (đến đích, chết, v.v.)
default platforming_active = False  # True = đang chạy platforming loop
default platforming_result = ""     # Kết quả: "win", "lose", "exit", v.v.


init python:
    # =============================================
    # CÀI ĐẶT VẬT LÝ VÀ TỐC ĐỘ
    # Chỉnh các giá trị trong phần này để thay đổi cảm giác điều khiển.
    # =============================================

    # === CÓ THỂ CHỈNH ===
    P_SPEED       = 20      # Tốc độ chạy ngang (pixel/frame). Tăng = chạy nhanh hơn.
    P_JUMP_FORCE  = -22    # Lực nhảy (âm vì Y tăng xuống dưới). -22 = nhảy cao vừa.
    P_GRAVITY     = 10    # Gia tốc rơi mỗi frame. Tăng = rơi nhanh hơn.
    P_MAX_FALL    = 20     # Tốc độ rơi tối đa (giới hạn để không xuyên đất).
    GROUND_Y      = 480    # Tọa độ Y của mặt đất. Điều chỉnh theo background.
    PLAYER_H      = 96     # Chiều cao sprite player (pixel). Dùng để tính va chạm đất.
    SCREEN_LEFT   = 0      # Giới hạn trái màn hình (player không ra ngoài đây).
    SCREEN_RIGHT  = 1820   # Giới hạn phải màn hình (1920 - độ rộng sprite ~100px).
    # === KẾT THÚC PHẦN CÓ THỂ CHỈNH ===

    def p_update_physics():
        """
        Hàm vật lý chính. Gọi mỗi frame trong game loop platforming.
        Cập nhật: trọng lực, va chạm đất, giới hạn màn hình.
        """
        global py, pvy, p_on_ground

        # Cộng trọng lực vào tốc độ dọc
        pvy += P_GRAVITY

        # Giới hạn tốc độ rơi tối đa
        if pvy > P_MAX_FALL:
            pvy = P_MAX_FALL

        # Cập nhật vị trí Y
        py += pvy

        # Kiểm tra va chạm với mặt đất
        if py + PLAYER_H >= GROUND_Y:
            py = GROUND_Y - PLAYER_H  # Đặt player trên mặt đất
            pvy = 0
            p_on_ground = True
        else:
            p_on_ground = False

        renpy.restart_interaction()

    def p_move_left():
        """
        Di chuyển player sang trái.
        Cập nhật vị trí X và hướng nhìn.
        """
        global px, p_facing, p_moving
        px -= P_SPEED
        if px < SCREEN_LEFT:
            px = SCREEN_LEFT
        p_facing = "left"
        p_moving = True

    def p_move_right():
        """
        Di chuyển player sang phải.
        Cập nhật vị trí X và hướng nhìn.
        """
        global px, p_facing, p_moving
        px += P_SPEED
        if px > SCREEN_RIGHT:
            px = SCREEN_RIGHT
        p_facing = "right"
        p_moving = True

    def p_move_up():
        """
        Di chuyển player lên (dùng cho thang leo, không phải nhảy).
        Nếu muốn nhảy, dùng p_jump() thay vào.
        """
        global py
        py -= P_SPEED
        if py < 0:
            py = 0

    def p_move_down():
        """
        Di chuyển player xuống (cúi xuống / leo xuống thang).
        """
        global py
        py += P_SPEED

    def p_jump():
        """
        Nhảy. Chỉ thực hiện khi player đang đứng trên mặt đất (p_on_ground = True).
        Để điều chỉnh độ cao nhảy: thay đổi P_JUMP_FORCE ở trên.
        """
        global pvy, p_on_ground
        if p_on_ground:
            pvy = P_JUMP_FORCE
            p_on_ground = False

    def p_stop_moving():
        """Đặt lại trạng thái đang di chuyển về False."""
        global p_moving
        p_moving = False

    def p_reset_position():
        """
        Reset player về vị trí ban đầu.
        Gọi hàm này khi bắt đầu một màn mới hoặc khi player chết.
        """
        global px, py, pvy, p_on_ground, p_facing, p_moving
        px = 200
        py = GROUND_Y - PLAYER_H
        pvy = 0
        p_on_ground = True
        p_facing = "right"
        p_moving = False


# ── SCREEN CHÍNH CỦA PLATFORMING ──
# Screen này hiển thị player và lắng nghe input phím.
# Để dùng screen này: "call screen platforming_screen" trong label.
#
# LƯU Ý VỀ key ACTION:
#   - "K_a" = phím A (Ren'Py dùng tên SDL key, viết thường)
#   - repeat=True = giữ phím = lặp lại action (cần thiết cho di chuyển)
#   - repeat=False = chỉ kích hoạt 1 lần khi nhấn (dùng cho nhảy, skill)

screen platforming_screen():
    # Hiển thị sprite player tại vị trí (px, py)
    # Sprite sẽ thay đổi dựa trên hướng đang nhìn và trạng thái di chuyển.
    # Hiện tại dùng hero_normal làm mặc định.
    # TODO: Thay bằng Animation sprite khi có đủ frame.
    add "hero_normal" xpos px ypos py

    # ── PHÍM DI CHUYỂN ──
    # W và S đã bỏ theo yêu cầu. Chỉ giữ A (trái), D (phải), SPACE (nhảy), J/K/L (skill).
    key "K_a"      action [Function(p_move_left),  Function(p_update_physics)]
    key "K_d"      action [Function(p_move_right), Function(p_update_physics)]

    # ── NHẢY ──
    key "K_SPACE"  action Function(p_jump)

    # ── SKILL ──
    key "K_j"      action Function(use_skill_1)
    key "K_k"      action Function(use_skill_2)
    key "K_l"      action Function(use_skill_3)

    # ── HUD: Phím tắt ──
    hbox:
        xalign 0.5
        yalign 0.98
        spacing 20
        text "A/D: Di chuyển" size 18 color "#ffffff" outlines [(1,"#000",0,0)]
        text "SPACE: Nhảy" size 18 color "#ffffff" outlines [(1,"#000",0,0)]
        text "J/K/L: Skill" size 18 color "#ffffff" outlines [(1,"#000",0,0)]

    # ── HUD: Hiển thị skill cooldown / tên skill (lấy từ skills.rpy) ──
    hbox:
        xalign 0.5
        yalign 0.93
        spacing 30
        vbox:
            xalign 0.5
            text "[skill_1_name]" xalign 0.5 size 16 color "#ffdd88" outlines [(1,"#000",0,0)]
            text "[skill_1_key]" xalign 0.5 size 14 color "#aaaaaa" outlines [(1,"#000",0,0)]
        vbox:
            xalign 0.5
            text "[skill_2_name]" xalign 0.5 size 16 color "#88ddff" outlines [(1,"#000",0,0)]
            text "[skill_2_key]" xalign 0.5 size 14 color "#aaaaaa" outlines [(1,"#000",0,0)]
        vbox:
            xalign 0.5
            text "[skill_3_name]" xalign 0.5 size 16 color "#ff88aa" outlines [(1,"#000",0,0)]
            text "[skill_3_key]" xalign 0.5 size 14 color "#aaaaaa" outlines [(1,"#000",0,0)]
