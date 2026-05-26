# =============================================
# FILE: Platforming/skill_manager.rpy
# MỤC ĐÍCH: Nơi tập trung để TẠO SKILL MỚI và NÂNG CẤP SKILL
#
# ── TẠI SAO CÓ FILE NÀY? ──
#   skills.rpy chứa logic kỹ thuật (hàm Python, biến).
#   File này là "giao diện quản lý" dành cho việc thêm/sửa skill
#   dễ dàng hơn, không cần đụng vào code Python phức tạp.
#
# ── FILE NÀY LÀM GÌ? ──
#   1. Hướng dẫn từng bước để tạo skill mới (slot 4, 5, ...)
#   2. Cung cấp label sẵn dùng cho mọi tình huống nâng cấp
#   3. Cung cấp label để reset, ẩn/hiện skill
#   4. Screen "skill_menu" để xem toàn bộ skill trong game
#
# ── PHÂN BIỆT VỚI skills.rpy ──
#   skills.rpy     → định nghĩa biến + hàm Python (ĐỪNG SỬA NẾU KHÔNG CHẮC)
#   skill_manager  → dùng các biến/hàm đó để tạo gameplay (SỬA TẠI ĐÂY)
# =============================================


# =============================================
# PHẦN 1: HƯỚNG DẪN TẠO SKILL MỚI
# =============================================
#
# Để tạo SKILL 4 (hoặc bất kỳ slot mới nào), làm theo thứ tự:
#
# BƯỚC 1 – Thêm biến vào skills.rpy (phần PHẦN 1):
# ─────────────────────────────────────────────────
#   default skill_4_name      = "Tên Skill"
#   default skill_4_key       = "[M]"          ← phím hiển thị HUD
#   default skill_4_desc      = "Mô tả ngắn."
#   default skill_4_level     = 1
#   default skill_4_max_level = 3
#   default skill_4_damage    = 15             ← nếu skill gây damage
#   default skill_4_cooldown  = 2.0
#   default skill_4_unlocked  = False          ← True nếu mở ngay từ đầu
#
# BƯỚC 2 – Thêm hàm vào skills.rpy (phần init python, PHẦN 2):
# ──────────────────────────────────────────────────────────────
#   def use_skill_4():
#       if not renpy.store.skill_4_unlocked:
#           renpy.notify("Skill 4 chưa mở khóa!")
#           return
#       # TODO: logic skill tại đây
#       renpy.notify("[M] {} kích hoạt!".format(renpy.store.skill_4_name))
#
# BƯỚC 3 – Bind phím vào player_controls.rpy:
# ─────────────────────────────────────────────
#   Tìm dòng "key "K_l"" và thêm NGAY SAU:
#   key "K_m"  action Function(use_skill_4) repeat False
#   (K_m = phím M, thay bằng phím bạn muốn)
#
# BƯỚC 4 – Thêm slot HUD vào player_controls.rpy:
# ─────────────────────────────────────────────────
#   Trong hbox hiển thị skill HUD, thêm vbox mới:
#   vbox:
#       xalign 0.5
#       text "[skill_4_name]" xalign 0.5 size 16 color "#aaffaa" outlines [(1,"#000",0,0)]
#       text "[skill_4_key]"  xalign 0.5 size 14 color "#aaaaaa" outlines [(1,"#000",0,0)]
#
# BƯỚC 5 (TÙY CHỌN) – Thêm label upgrade vào file NÀY (phần dưới):
# ──────────────────────────────────────────────────────────────────
#   label upgrade_skill_4:
#       ...
#
# =============================================


# =============================================
# PHẦN 2: LABEL MỞ KHÓA SKILL
# Gọi các label này trong story khi player đạt điều kiện.
# =============================================

label skill_mgr_unlock_1:
    # Mở khóa lại Skill 1 nếu trước đó bị khóa
    # Gọi: "call skill_mgr_unlock_1"
    $ skill_1_unlocked = True
    "[hero_name] đã mở khóa Skill 1: [skill_1_name]!"
    "Nhấn [J] để sử dụng."
    return

label skill_mgr_unlock_2:
    # Mở khóa Skill 2
    $ skill_2_unlocked = True
    "[hero_name] đã mở khóa Skill 2: [skill_2_name]!"
    "Nhấn [K] để sử dụng."
    return

label skill_mgr_unlock_3:
    # Mở khóa Skill 3 (tương tự unlock_skill_3 trong skills.rpy nhưng không thay tên)
    # Dùng label này nếu bạn đã đặt tên skill_3 trước rồi.
    $ skill_3_unlocked = True
    $ skill_3_level    = 1
    "[hero_name] đã mở khóa Skill 3: [skill_3_name]!"
    "Nhấn [L] để sử dụng."
    return


# =============================================
# PHẦN 3: LABEL NÂNG CẤP LINH HOẠT
# Nâng cấp có kèm dialogue tùy chỉnh.
# Khác với upgrade_skill_X trong skills.rpy (chỉ tăng số),
# ở đây bạn có thể thêm scene, nhạc, cutscene tùy ý.
# =============================================

label skill_mgr_upgrade_1_with_scene:
    # ── NÂNG CẤP SKILL 1 CÓ CUTSCENE ──
    # Ví dụ: sau khi đánh boss, hero học được chiêu mạnh hơn.
    # Chỉnh đoạn này tùy ý.

    # [TÙY CHỌN] Thêm scene/âm nhạc trước khi nâng cấp:
    # scene bg_palace_hall with fade
    # play music audio.music_royal fadein 1.0

    if skill_1_level < skill_1_max_level:
        $ skill_1_level  += 1
        $ skill_1_damage += 5      # ← Đổi công thức tăng damage tại đây
        "[hero_name] cảm nhận sức mạnh mới trỗi dậy trong lưỡi kiếm."
        "[skill_1_name] đã lên Cấp [skill_1_level]!  Sát thương: [skill_1_damage]."
    else:
        "[skill_1_name] đã đạt đỉnh giới hạn. Không thể mạnh hơn nữa."
    return

label skill_mgr_upgrade_2_with_scene:
    # ── NÂNG CẤP SKILL 2 CÓ CUTSCENE ──
    if skill_2_level < skill_2_max_level:
        $ skill_2_level    += 1
        $ skill_2_distance += 50   # ← Đổi khoảng cách tăng tại đây
        "[hero_name] tập luyện thêm vũ bộ. Bước lướt dài hơn và nhanh hơn."
        "[skill_2_name] lên Cấp [skill_2_level]!  Khoảng cách: [skill_2_distance] px."
    else:
        "[skill_2_name] đã đạt đỉnh giới hạn."
    return

label skill_mgr_upgrade_3_with_scene:
    # ── NÂNG CẤP SKILL 3 CÓ CUTSCENE ──
    if not skill_3_unlocked:
        "Skill 3 chưa được mở khóa. Hãy khám phá thêm cốt truyện."
        return
    if skill_3_level < skill_3_max_level:
        $ skill_3_level += 1
        "[hero_name] kiểm soát [skill_3_name] tốt hơn trước."
        "Cấp độ [skill_3_name]: [skill_3_level] / [skill_3_max_level]."
    else:
        "[skill_3_name] đã đạt đỉnh giới hạn."
    return


# =============================================
# PHẦN 4: LABEL RESET SKILL
# Dùng khi cần đặt lại tất cả skill về mặc định.
# Ví dụ: khi bắt đầu vòng lặp mới (loop mechanic).
# =============================================

label skill_mgr_reset_all:
    # ── RESET TOÀN BỘ SKILL VỀ MẶC ĐỊNH ──
    # Sau khi gọi label này, tất cả skill trở về như lúc bắt đầu game.

    $ skill_1_level    = 1
    $ skill_1_damage   = 10
    $ skill_1_unlocked = True

    $ skill_2_level    = 1
    $ skill_2_distance = 200
    $ skill_2_unlocked = True

    $ skill_3_level    = 0
    $ skill_3_unlocked = False
    $ skill_3_name     = "???"
    $ skill_3_desc     = "Chưa mở khóa. Tiếp tục hành trình để khám phá."

    # Không có dialogue – label âm thầm reset và return.
    # Thêm dialogue bên dưới nếu muốn thông báo cho player.
    return

label skill_mgr_reset_for_new_loop:
    # ── RESET DÀNH RIÊNG CHO VÒNG LẶP ──
    # Khác reset_all: chỉ reset level, giữ lại tên và trạng thái unlock.
    # Dùng khi game có cơ chế "vòng lặp" (loop) nhưng hero nhớ kỹ năng.

    $ skill_1_level  = 1
    $ skill_1_damage = 10
    $ skill_2_level  = 1
    $ skill_2_distance = 200
    if skill_3_unlocked:
        $ skill_3_level = 1
    return


# =============================================
# PHẦN 5: SCREEN XEM SKILL (SKILL MENU)
# Hiển thị toàn bộ skill hiện có, level, mô tả.
# Gọi: "call screen skill_menu_screen"
# Thoát: Nhấn Escape hoặc nút "Đóng"
# =============================================

screen skill_menu_screen():

    # Nền mờ
    add Solid("#000000cc") xsize 1920 ysize 1080

    frame:
        xalign  0.5
        yalign  0.5
        xsize   800
        padding (40, 30)
        background Frame("#12122acc", 14, 14)

        vbox:
            spacing 20
            xalign  0.5

            # Tiêu đề
            text "── SKILL CỦA [hero_name] ──":
                xalign 0.5
                size   26
                color  "#f5e6c8"
                bold   True

            null height 6

            # ── SLOT SKILL 1 ──
            frame:
                xsize   680
                padding (16, 12)
                background "#1e1e3ecc"
                hbox:
                    spacing 20
                    # Phím
                    frame:
                        background "#3a2a0e"
                        padding (10, 8)
                        text "[skill_1_key]" size 20 color "#ffdd88" bold True yalign 0.5
                    vbox:
                        spacing 4
                        hbox:
                            spacing 12
                            text "[skill_1_name]" size 20 color "#ffdd88" bold True yalign 0.5
                            # Hiện trạng thái khóa
                            if skill_1_unlocked:
                                text "✓ Đã mở" size 14 color "#88ff88" yalign 0.5
                            else:
                                text "✗ Chưa mở" size 14 color "#ff8888" yalign 0.5
                        text "Cấp: [skill_1_level] / [skill_1_max_level]  |  Sát thương: [skill_1_damage]" size 14 color "#aaaaaa"
                        text "[skill_1_desc]" size 14 color "#cccccc"

            # ── SLOT SKILL 2 ──
            frame:
                xsize   680
                padding (16, 12)
                background "#1e1e3ecc"
                hbox:
                    spacing 20
                    frame:
                        background "#0e1e3a"
                        padding (10, 8)
                        text "[skill_2_key]" size 20 color "#88ddff" bold True yalign 0.5
                    vbox:
                        spacing 4
                        hbox:
                            spacing 12
                            text "[skill_2_name]" size 20 color "#88ddff" bold True yalign 0.5
                            if skill_2_unlocked:
                                text "✓ Đã mở" size 14 color "#88ff88" yalign 0.5
                            else:
                                text "✗ Chưa mở" size 14 color "#ff8888" yalign 0.5
                        text "Cấp: [skill_2_level] / [skill_2_max_level]  |  Khoảng cách lướt: [skill_2_distance]px" size 14 color "#aaaaaa"
                        text "[skill_2_desc]" size 14 color "#cccccc"

            # ── SLOT SKILL 3 ──
            frame:
                xsize   680
                padding (16, 12)
                background "#1e1e3ecc"
                hbox:
                    spacing 20
                    frame:
                        background "#2a0e2a"
                        padding (10, 8)
                        text "[skill_3_key]" size 20 color "#ff88aa" bold True yalign 0.5
                    vbox:
                        spacing 4
                        hbox:
                            spacing 12
                            text "[skill_3_name]" size 20 color "#ff88aa" bold True yalign 0.5
                            if skill_3_unlocked:
                                text "✓ Đã mở" size 14 color "#88ff88" yalign 0.5
                            else:
                                text "✗ Chưa mở" size 14 color "#ff8888" yalign 0.5
                        if skill_3_unlocked:
                            text "Cấp: [skill_3_level] / [skill_3_max_level]" size 14 color "#aaaaaa"
                        text "[skill_3_desc]" size 14 color "#cccccc"

            null height 8

            # Nút đóng
            textbutton "Đóng [X]":
                xalign  0.5
                action  Hide("skill_menu_screen")
                text_size  20
                text_color "#ffffff"
                background  "#2a1a1a"
                hover_background "#4a2a2a"
                padding (20, 8)
