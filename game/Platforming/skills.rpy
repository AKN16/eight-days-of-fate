# =============================================
# FILE: Platforming/skills.rpy
# MỤC ĐÍCH: Định nghĩa và quản lý toàn bộ skill của player
#
# ── CÁCH ĐỌC FILE NÀY ──
#   File gồm 3 phần chính:
#     PHẦN 1 – Biến lưu thông tin skill (tên, cooldown, level, v.v.)
#     PHẦN 2 – Hàm thực thi skill (logic xảy ra khi nhấn J/K/L)
#     PHẦN 3 – Hàm nâng cấp skill (upgrade system)
#
# ── CÁCH THÊM SKILL MỚI ──
#   1. Thêm biến mô tả skill ở PHẦN 1 (tên, key, mô tả)
#   2. Viết hàm logic skill ở PHẦN 2 (use_skill_X)
#   3. Nếu có nâng cấp, thêm hàm upgrade ở PHẦN 3
#   4. Bind phím mới trong player_controls.rpy (thêm dòng key "K_m" action ...)
#
# ── CÁCH THÊM COOLDOWN ──
#   Hiện tại chưa có cooldown timer thật.
#   Để thêm: dùng biến "skill_X_cd_remaining" đếm ngược mỗi frame trong game loop.
#   Ví dụ: if skill_1_cd_remaining > 0: skill_1_cd_remaining -= 1
# =============================================


# =============================================
# PHẦN 1: BIẾN MÔ TẢ SKILL
# Thay đổi tên, mô tả ở đây sẽ tự cập nhật HUD trên màn hình.
# =============================================

# ── SKILL 1 – Phím J ──
# Dùng cho kỹ năng tấn công cơ bản / skill chiến đấu đầu tiên.
default skill_1_name         = "Chém"           # Tên hiển thị trên HUD
default skill_1_key          = "[J]"             # Phím hiển thị trên HUD
default skill_1_desc         = "Chém mạnh về phía trước. Gây sát thương cơ bản." # Mô tả dài (dùng trong menu)
default skill_1_level        = 1                 # Level hiện tại (bắt đầu từ 1)
default skill_1_max_level    = 3                 # Level tối đa có thể nâng
default skill_1_damage       = 10               # Sát thương cơ bản (chỉnh theo game balance)
default skill_1_cooldown     = 1.5              # Thời gian hồi chiêu (giây, chỉ để tham khảo hiện tại)
default skill_1_unlocked     = True             # True = đã mở khóa, False = chưa

# ── SKILL 2 – Phím K ──
# Dùng cho kỹ năng phòng thủ / di chuyển đặc biệt.
default skill_2_name         = "Lướt"
default skill_2_key          = "[K]"
default skill_2_desc         = "Lướt nhanh về phía đang nhìn. Né tránh đòn tấn công."
default skill_2_level        = 1
default skill_2_max_level    = 3
default skill_2_distance     = 200              # Khoảng cách lướt (pixel)
default skill_2_cooldown     = 2.0
default skill_2_unlocked     = True

# ── SKILL 3 – Phím L ──
# Dùng cho kỹ năng đặc biệt / mạnh nhất, thường mở khóa sau.
default skill_3_name         = "???"
default skill_3_key          = "[L]"
default skill_3_desc         = "Chưa mở khóa. Tiếp tục hành trình để khám phá."
default skill_3_level        = 0
default skill_3_max_level    = 3
default skill_3_cooldown     = 5.0
default skill_3_unlocked     = False            # Mặc định chưa mở khóa


# =============================================
# PHẦN 2: HÀM THỰC THI SKILL
# Đây là logic xảy ra khi player nhấn phím J/K/L.
# Thay đổi code trong từng hàm để thay đổi hiệu ứng skill.
# =============================================

init python:

    def use_skill_1():
        """
        SKILL 1 – Chém (phím J)
        Logic hiện tại: hiển thị thông báo debug trên console.
        
        ── CÁCH MỞ RỘNG ──
        - Kiểm tra có enemy trong range không → giảm HP enemy
        - Phát animation chém
        - Phát sound effect
        
        Ví dụ tương lai:
            if enemy_in_range():
                enemy_hp -= skill_1_damage
                renpy.sound.play("audio/sfx/slash.ogg")
        """
        if not renpy.store.skill_1_unlocked:
            renpy.notify("Skill 1 chưa được mở khóa!")
            return

        # ── LOGIC SKILL 1 ──
        # TODO: Thêm animation, kiểm tra va chạm enemy, gây damage tại đây
        renpy.notify("[J] Chém! Sát thương: {}".format(renpy.store.skill_1_damage))

    def use_skill_2():
        """
        SKILL 2 – Lướt (phím K)
        Logic hiện tại: dịch chuyển player theo hướng đang nhìn.
        
        ── CÁCH MỞ RỘNG ──
        - Thêm trạng thái invincible trong lúc lướt
        - Phát particle effect
        - Cooldown timer thật
        """
        if not renpy.store.skill_2_unlocked:
            renpy.notify("Skill 2 chưa được mở khóa!")
            return

        # ── LOGIC SKILL 2: Lướt về phía đang nhìn ──
        dist = renpy.store.skill_2_distance
        if renpy.store.p_facing == "right":
            renpy.store.px += dist
            # Giới hạn không ra ngoài màn hình
            if renpy.store.px > 1820:
                renpy.store.px = 1820
        else:
            renpy.store.px -= dist
            if renpy.store.px < 0:
                renpy.store.px = 0

        renpy.notify("[K] Lướt {} px!".format(dist))
        renpy.restart_interaction()

    def use_skill_3():
        """
        SKILL 3 – Skill bí ẩn (phím L)
        Logic hiện tại: chỉ hoạt động khi đã mở khóa.
        
        ── GỢI Ý CHO SKILL 3 ──
        - Có thể là: AoE damage, hồi máu, triệu hồi, v.v.
        - Mở khóa bằng cách gọi unlock_skill_3() trong story
        """
        if not renpy.store.skill_3_unlocked:
            renpy.notify("Skill 3 chưa mở khóa. Tiếp tục hành trình!")
            return

        # ── LOGIC SKILL 3 ──
        # TODO: Thêm logic khi đã thiết kế skill
        renpy.notify("[L] {} kích hoạt!".format(renpy.store.skill_3_name))


# =============================================
# PHẦN 3: HÀM NÂNG CẤP SKILL (UPGRADE SYSTEM)
# Gọi các hàm này trong story khi player đạt điều kiện nâng cấp.
# Ví dụ: "call upgrade_skill_1" sau khi nhân vật học được kỹ năng mới.
# =============================================

label upgrade_skill_1:
    # ── NÂNG CẤP SKILL 1 ──
    # Gọi label này khi muốn nâng cấp Skill 1.
    # Tăng level, tăng sát thương theo công thức (có thể tùy chỉnh).
    # Gửi thông báo cho player biết.
    
    if skill_1_level < skill_1_max_level:
        $ skill_1_level += 1
        # Công thức tăng damage: +5 mỗi level. Thay đổi tùy ý.
        $ skill_1_damage += 5
        "[hero_name] đã nâng cấp Skill 1 – [skill_1_name] lên Level [skill_1_level]!"
        "Sát thương tăng lên [skill_1_damage]."
    else:
        "[skill_1_name] đã đạt cấp độ tối đa (Level [skill_1_max_level])!"
    return

label upgrade_skill_2:
    # ── NÂNG CẤP SKILL 2 ──
    # Tăng khoảng cách lướt mỗi level nâng cấp.
    
    if skill_2_level < skill_2_max_level:
        $ skill_2_level += 1
        # Công thức tăng distance: +50px mỗi level. Thay đổi tùy ý.
        $ skill_2_distance += 50
        "[hero_name] đã nâng cấp Skill 2 – [skill_2_name] lên Level [skill_2_level]!"
        "Khoảng cách lướt tăng lên [skill_2_distance] pixel."
    else:
        "[skill_2_name] đã đạt cấp độ tối đa!"
    return

label unlock_skill_3:
    # ── MỞ KHÓA SKILL 3 ──
    # Gọi label này tại điểm trong story khi player học được skill bí ẩn.
    # Đổi tên skill trước khi gọi nếu muốn tên riêng.
    
    $ skill_3_unlocked = True
    $ skill_3_level = 1
    $ skill_3_name = "Bùng Nổ"    # ← Đổi tên skill 3 tại đây khi đã quyết định
    $ skill_3_key = "[L]"
    $ skill_3_desc = "Tung ra một vụ nổ năng lượng. Đẩy lùi tất cả kẻ thù xung quanh."
    "[hero_name] đã học được Skill mới: [skill_3_name]!"
    "Nhấn [L] để sử dụng."
    return

label upgrade_skill_3:
    # ── NÂNG CẤP SKILL 3 ──
    if not skill_3_unlocked:
        "Skill 3 chưa được mở khóa."
        return
    if skill_3_level < skill_3_max_level:
        $ skill_3_level += 1
        "[hero_name] đã nâng cấp [skill_3_name] lên Level [skill_3_level]!"
    else:
        "[skill_3_name] đã đạt cấp độ tối đa!"
    return
