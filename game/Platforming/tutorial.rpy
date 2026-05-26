# =============================================
# FILE: Platforming/tutorial.rpy
# MỤC ĐÍCH: Hiển thị màn hướng dẫn (tutorial) trước khi vào platforming
#
# ── VỊ TRÍ GỌI TUTORIAL ──
#   Tutorial này được thiết kế để gọi TRƯỚC lần đầu tiên player
#   vào màn platforming. Có 2 cách gọi:
#
#   CÁCH 1 – Gọi trực tiếp từ story (khuyến nghị):
#       Trong label bất kỳ (ví dụ day_1.rpy, trước khi vào platforming):
#           call tutorial_platforming
#       Sau đó gọi màn chơi như bình thường.
#
#   CÁCH 2 – Gọi có điều kiện (chỉ hiện lần đầu):
#       if not tutorial_done:
#           call tutorial_platforming
#       call screen platforming_screen
#
# ── NỘI DUNG TUTORIAL ──
#   Gồm 2 phần:
#     A. Màn dialogue giải thích câu chuyện / lý do phải platforming
#     B. Screen hướng dẫn phím bấm (hiển thị bảng điều khiển trực quan)
#
# ── CÁCH CHỈNH NỘI DUNG ──
#   - Sửa text trong label tutorial_platforming để đổi lời thoại
#   - Sửa screen tutorial_controls_screen để đổi layout bảng phím
#   - Thêm/bớt skill hint bằng cách sửa vbox "skill_hint" bên dưới
# =============================================


# ── BIẾN TRẠNG THÁI TUTORIAL ──
# Dùng để kiểm tra xem player đã xem tutorial chưa.
# Khi tutorial_done = True → không hiện lại nữa (nếu dùng Cách 2 ở trên).
default tutorial_done = False


# =============================================
# SCREEN HIỂN THỊ BẢNG PHÍM (gọi từ label tutorial_platforming)
# Hiển thị overlay trong suốt với bảng hướng dẫn phím bấm.
# Player bấm bất kỳ phím nào để tiếp tục.
# =============================================

screen tutorial_controls_screen():

    # ── NỀN MỜ ──
    # Một lớp đen trong suốt phủ lên toàn màn hình.
    # alpha=0.75 = 75% mờ. Tăng để tối hơn, giảm để thấy background hơn.
    add Solid("#000000bb") xsize 1920 ysize 1080

    # ── KHUNG TRUNG TÂM ──
    frame:
        xalign 0.5
        yalign 0.45
        xsize  860
        padding (40, 30)
        background Frame("#1a1a2ecc", 12, 12)

        vbox:
            spacing 22
            xalign 0.5

            # ── TIÊU ĐỀ ──
            text "── HƯỚNG DẪN ĐIỀU KHIỂN ──":
                xalign  0.5
                size    28
                color   "#f5e6c8"
                bold    True

            null height 4

            # ── PHẦN DI CHUYỂN ──
            # Mỗi hbox = 1 dòng hướng dẫn: [phím] → [mô tả]
            text "DI CHUYỂN":
                size   18
                color  "#aaddff"
                bold   True

            hbox:
                spacing 14
                xalign  0.5
                # Phím A
                frame:
                    background "#2d2d4e"
                    padding (10, 6)
                    text "  A  " size 22 color "#ffffff" bold True
                text "← Di chuyển trái" yalign 0.5 size 18 color "#dddddd"

            hbox:
                spacing 14
                xalign  0.5
                frame:
                    background "#2d2d4e"
                    padding (10, 6)
                    text "  D  " size 22 color "#ffffff" bold True
                text "→ Di chuyển phải" yalign 0.5 size 18 color "#dddddd"

            hbox:
                spacing 14
                xalign  0.5
                frame:
                    background "#2d2d4e"
                    padding (10, 6)
                    text "  W  " size 22 color "#ffffff" bold True
                text "↑ Di chuyển lên / leo thang" yalign 0.5 size 18 color "#dddddd"

            hbox:
                spacing 14
                xalign  0.5
                frame:
                    background "#2d2d4e"
                    padding (10, 6)
                    text "  S  " size 22 color "#ffffff" bold True
                text "↓ Di chuyển xuống / cúi" yalign 0.5 size 18 color "#dddddd"

            hbox:
                spacing 14
                xalign  0.5
                frame:
                    background "#2d2d4e"
                    padding (10, 6)
                    text " SPACE " size 22 color "#ffe066" bold True
                text "⬆ Nhảy  (chỉ khi đứng trên đất)" yalign 0.5 size 18 color "#dddddd"

            null height 6

            # ── PHẦN SKILL ──
            text "SKILL":
                size  18
                color "#ffaa55"
                bold  True

            hbox:
                spacing 14
                xalign  0.5
                frame:
                    background "#3d2d1e"
                    padding (10, 6)
                    text "  J  " size 22 color "#ffdd88" bold True
                # Tên skill lấy từ biến skill_1_name trong skills.rpy
                text "Skill 1 – [skill_1_name]  |  [skill_1_desc]" yalign 0.5 size 16 color "#ffdd88"

            hbox:
                spacing 14
                xalign  0.5
                frame:
                    background "#1e2d3d"
                    padding (10, 6)
                    text "  K  " size 22 color "#88ddff" bold True
                text "Skill 2 – [skill_2_name]  |  [skill_2_desc]" yalign 0.5 size 16 color "#88ddff"

            hbox:
                spacing 14
                xalign  0.5
                frame:
                    background "#2d1e2d"
                    padding (10, 6)
                    text "  L  " size 22 color "#ff88aa" bold True
                text "Skill 3 – [skill_3_name]  |  [skill_3_desc]" yalign 0.5 size 16 color "#ff88aa"

            null height 10

            # ── NÚT TIẾP TỤC ──
            # Player bấm nút này (hoặc nhấn Enter/Space) để đóng tutorial
            textbutton "Bắt đầu! →":
                xalign  0.5
                action  Return()  # Đóng tutorial và quay lại chỗ đã gọi
                text_size  22
                text_color "#ffffff"
                text_bold  True
                background  "#4a3a1e"
                hover_background "#6a5a2e"
                padding (24, 10)

    # ── GÓC DƯỚI: Gợi ý bấm phím tắt ──
    text "(hoặc nhấn Enter / Chuột trái để tiếp tục)":
        xalign 0.5
        yalign 0.97
        size   15
        color  "#888888"


# =============================================
# LABEL CHÍNH CỦA TUTORIAL
# Gọi: "call tutorial_platforming" từ bất kỳ đâu trong story.
# =============================================

label tutorial_platforming:

    # ── PHẦN A: DIALOGUE DẪN NHẬP ──
    # Đây là lời thoại xuất hiện TRƯỚC bảng phím.
    # Chỉnh sửa hoặc thêm bớt các dòng này tùy ý.
    # Nếu không muốn có dialogue, xóa từ dòng này đến "# END DIALOGUE"

    "Phía trước là con đường chưa ai đặt chân..."
    "[hero_name] hít một hơi dài. Chuyến hành trình thật sự bắt đầu từ đây."
    "Đây là lúc [hero_name] phải tự điều khiển mọi thứ."

    # ── GỢI Ý: Thêm dialogue nhân vật tại đây ──
    # Ví dụ:
    #   hero "Được rồi. Ta hiểu cách này rồi."
    #   princess "Hãy cẩn thận. Con đường không đơn giản đâu."

    # END DIALOGUE

    # ── PHẦN B: HIỂN THỊ BẢNG PHÍM ──
    # Gọi screen tutorial và chờ player bấm nút "Bắt đầu!"
    call screen tutorial_controls_screen

    # ── ĐÁNH DẤU ĐÃ XEM TUTORIAL ──
    # Sau khi xem xong, đặt tutorial_done = True.
    # Nếu muốn tutorial chỉ hiện 1 lần, dùng điều kiện "if not tutorial_done"
    # khi gọi label này (xem phần CÁCH GỌI TUTORIAL ở đầu file).
    $ tutorial_done = True

    return
    # ── KẾT THÚC LABEL ──
    # Sau return, code sẽ quay lại chỗ đã gọi "call tutorial_platforming"
    # và tiếp tục chạy dòng tiếp theo (thường là gọi platforming_screen).
