# HƯỚNG DẪN CHI TIẾT – PROJECT 1 PLATFORMING SYSTEM
# ======================================================
# File này giải thích toàn bộ hệ thống đã tạo để bạn
# dễ dàng chỉnh sửa theo ý muốn.
# ======================================================


## MỤC LỤC
1. Cấu trúc file tổng quan
2. Điều khiển Player (player_controls.rpy)
3. Hệ thống Skill (skills.rpy)
4. Tutorial (tutorial.rpy) ← FILE MỚI
5. Quản lý Skill (skill_manager.rpy) ← FILE MỚI
6. Cách gọi từ story
7. Checklist khi thêm skill mới
8. Lỗi thường gặp


---
## 1. CẤU TRÚC FILE
---

```
game/Platforming/
│
├── player_controls.rpy   ← Vật lý + phím bấm + HUD
├── skills.rpy            ← Biến skill + hàm Python + label upgrade
├── tutorial.rpy          ← (MỚI) Tutorial hướng dẫn đầu game
├── skill_manager.rpy     ← (MỚI) Quản lý / tạo / up skill
│
├── attack.rpy            ← Label battle (chưa hoàn thiện)
├── libary.rpy            ← Label thư viện
├── long.rpy              ← Label đường dài
└── short.rpy             ← Label đường ngắn
```

**Nguyên tắc:**
- `player_controls.rpy` + `skills.rpy` = lõi kỹ thuật → sửa cẩn thận
- `tutorial.rpy` + `skill_manager.rpy` = lớp gameplay → sửa thoải mái
- Các file `day_X.rpy` trong `/Days` → nơi gọi tất cả label trên


---
## 2. ĐIỀU KHIỂN PLAYER (player_controls.rpy)
---

### Phím bấm
| Phím  | Hàm được gọi    | Mô tả                              |
|-------|-----------------|-------------------------------------|
| A     | p_move_left()   | Di chuyển trái 8px/frame            |
| D     | p_move_right()  | Di chuyển phải 8px/frame            |
| W     | p_move_up()     | Di chuyển lên (leo thang)           |
| S     | p_move_down()   | Di chuyển xuống                     |
| SPACE | p_jump()        | Nhảy (chỉ khi đứng trên đất)       |
| J     | use_skill_1()   | Skill 1 – Chém                      |
| K     | use_skill_2()   | Skill 2 – Lướt                      |
| L     | use_skill_3()   | Skill 3 – Bí ẩn                     |

### Chỉnh tốc độ / vật lý
Mở `player_controls.rpy`, tìm phần `# === CÓ THỂ CHỈNH ===`:

```python
P_SPEED      = 8      # Tốc độ chạy. Tăng số → chạy nhanh hơn.
P_JUMP_FORCE = -22    # Lực nhảy. Số âm càng lớn → nhảy cao hơn (VD: -30).
P_GRAVITY    = 1.2    # Trọng lực. Tăng → rơi nhanh hơn.
P_MAX_FALL   = 20     # Tốc độ rơi tối đa.
GROUND_Y     = 480    # Tọa độ Y của mặt đất. Đổi theo background.
PLAYER_H     = 96     # Chiều cao sprite player (px).
SCREEN_LEFT  = 0      # Giới hạn trái.
SCREEN_RIGHT = 1820   # Giới hạn phải (1920 - khoảng sprite).
```

### Thêm phím mới
Trong `screen platforming_screen()`, thêm dòng:
```renpy
key "K_m"  action Function(use_skill_4) repeat False
# K_m = phím M. repeat False = chỉ kích hoạt 1 lần khi nhấn.
# repeat True  = giữ phím = lặp liên tục (dùng cho di chuyển).
```

### Tên phím Ren'Py
| Muốn dùng | Viết trong code |
|-----------|-----------------|
| A–Z       | K_a ... K_z     |
| 1–9       | K_1 ... K_9     |
| Space     | K_SPACE         |
| Enter     | K_RETURN        |
| Shift     | K_LSHIFT        |
| F1–F12    | K_F1 ... K_F12  |


---
## 3. HỆ THỐNG SKILL (skills.rpy)
---

### Cấu trúc mỗi skill
```python
# Biến (default = có thể thay đổi lúc chạy game)
default skill_X_name     = "Tên"       # Hiển thị trên HUD
default skill_X_key      = "[J]"       # Phím hiển thị trên HUD
default skill_X_desc     = "Mô tả."    # Dùng trong skill_menu
default skill_X_level    = 1           # Level hiện tại
default skill_X_max_level= 3           # Level tối đa
default skill_X_damage   = 10          # Sát thương (nếu có)
default skill_X_cooldown = 1.5         # Cooldown (giây, tham khảo)
default skill_X_unlocked = True        # True = mở, False = khóa
```

### Hàm use_skill_X()
Đây là code chạy khi player nhấn phím:
```python
def use_skill_1():
    # Kiểm tra khóa
    if not renpy.store.skill_1_unlocked:
        renpy.notify("Chưa mở khóa!")
        return
    # Logic skill tại đây
    renpy.notify("[J] Chém!")
```

**Để thêm sound:**
```python
renpy.sound.play("audio/sfx/slash.ogg")
```

**Để di chuyển player:**
```python
renpy.store.px += 100   # Dịch phải 100px
renpy.restart_interaction()  # Cập nhật màn hình
```

### Label upgrade
Trong `skills.rpy` có sẵn:
- `upgrade_skill_1` → tăng level + damage
- `upgrade_skill_2` → tăng level + distance
- `unlock_skill_3`  → mở khóa + đặt tên Skill 3
- `upgrade_skill_3` → tăng level

Trong `skill_manager.rpy` có thêm version có cutscene:
- `skill_mgr_upgrade_1_with_scene` (có dialogue tùy chỉnh)
- `skill_mgr_upgrade_2_with_scene`
- `skill_mgr_upgrade_3_with_scene`


---
## 4. TUTORIAL (tutorial.rpy) – FILE MỚI
---

### Gọi tutorial ở đâu?

**Cách A – Gọi 1 lần duy nhất (khuyến nghị):**
Mở `Days/day_1.rpy` (hoặc file bất kỳ trước khi platforming đầu tiên),
thêm ngay trước dòng `show screen platform_game` hoặc `call screen platforming_screen`:

```renpy
label crossroad_minigame:          # label đã có sẵn trong script.rpy
    if not tutorial_done:          # chỉ hiện nếu chưa xem
        call tutorial_platforming
    show screen platform_game
    ...
```

**Cách B – Gọi trực tiếp, không điều kiện:**
```renpy
call tutorial_platforming
call screen platforming_screen
```

**Cách C – Gọi từ một điểm story cụ thể:**
Ví dụ thêm vào cuối day_1.rpy trước `jump long_or_short_road`:
```renpy
if not tutorial_done:
    call tutorial_platforming
jump long_or_short_road
```

### Chỉnh nội dung tutorial

**Đổi lời thoại dẫn nhập:**
Mở `tutorial.rpy`, phần `# PHẦN A: DIALOGUE DẪN NHẬP`:
```renpy
"Phía trước là con đường chưa ai đặt chân..."     ← đổi dòng này
"[hero_name] hít một hơi dài..."                  ← hoặc dòng này
hero "Được rồi. Ta sẵn sàng."                     ← thêm lời nhân vật
```

**Đổi layout bảng phím:**
Trong `screen tutorial_controls_screen()`, mỗi `hbox` là 1 dòng hướng dẫn:
```renpy
hbox:
    spacing 14
    xalign  0.5
    frame:
        background "#2d2d4e"
        padding (10, 6)
        text "  A  " size 22 color "#ffffff" bold True  ← tên phím
    text "← Di chuyển trái" yalign 0.5 size 18 color "#dddddd"  ← mô tả
```
Sao chép/xóa hbox để thêm/bớt dòng.

**Biến `tutorial_done`:**
- Mặc định = False
- Sau khi xem tutorial lần đầu → tự động = True
- Dùng `$ tutorial_done = False` để reset (ví dụ: khi vòng lặp mới)


---
## 5. QUẢN LÝ SKILL (skill_manager.rpy) – FILE MỚI
---

### Labels sẵn có để dùng trong story

| Label                           | Dùng khi nào                              |
|---------------------------------|-------------------------------------------|
| skill_mgr_unlock_1              | Mở khóa lại Skill 1 có dialogue          |
| skill_mgr_unlock_2              | Mở khóa Skill 2 có dialogue              |
| skill_mgr_unlock_3              | Mở khóa Skill 3 (giữ tên đã đặt)        |
| skill_mgr_upgrade_1_with_scene  | Nâng Skill 1, có thể thêm scene          |
| skill_mgr_upgrade_2_with_scene  | Nâng Skill 2, có thể thêm scene          |
| skill_mgr_upgrade_3_with_scene  | Nâng Skill 3, có thể thêm scene          |
| skill_mgr_reset_all             | Reset toàn bộ (vòng lặp mới)             |
| skill_mgr_reset_for_new_loop    | Reset level, giữ unlock (loop nhớ skill) |

Cách gọi:
```renpy
# Trong bất kỳ label nào trong story:
call skill_mgr_upgrade_1_with_scene
call skill_mgr_unlock_3
```

### Screen skill_menu_screen
Hiển thị tất cả skill với thông tin đầy đủ.
```renpy
# Gọi trong story:
call screen skill_menu_screen

# Hoặc thêm nút vào HUD platforming:
# (trong player_controls.rpy, screen platforming_screen)
textbutton "Skill" action ShowTransient("skill_menu_screen")
```

### Tạo Skill 4 (hướng dẫn nhanh)
1. Mở `skills.rpy` → thêm biến `skill_4_*` ở PHẦN 1
2. Mở `skills.rpy` → thêm hàm `use_skill_4()` trong `init python` PHẦN 2
3. Mở `player_controls.rpy` → thêm `key "K_m"` trong screen
4. Mở `player_controls.rpy` → thêm vbox vào HUD hbox skill
5. (Tùy chọn) Mở `skill_manager.rpy` → thêm label upgrade/unlock cho skill 4


---
## 6. CÁCH GỌI TỪ STORY (tóm tắt nhanh)
---

```renpy
# Hiện tutorial (lần đầu):
if not tutorial_done:
    call tutorial_platforming

# Chạy màn platforming:
call screen platforming_screen

# Mở khóa skill:
call unlock_skill_3          # từ skills.rpy (có dialogue mặc định)
call skill_mgr_unlock_3      # từ skill_manager.rpy (dialogue tùy chỉnh hơn)

# Nâng cấp skill:
call upgrade_skill_1         # ngắn gọn
call skill_mgr_upgrade_1_with_scene  # có thể thêm cảnh

# Xem skill menu:
call screen skill_menu_screen

# Reset khi vòng lặp mới:
call skill_mgr_reset_all
$ tutorial_done = False      # nếu muốn hiện tutorial lại
```


---
## 7. CHECKLIST KHI THÊM SKILL MỚI
---

```
[ ] 1. Thêm biến skill_X_* vào skills.rpy (PHẦN 1)
[ ] 2. Thêm hàm use_skill_X() vào init python trong skills.rpy (PHẦN 2)
[ ] 3. Thêm key "K_?" vào screen platforming_screen trong player_controls.rpy
[ ] 4. Thêm vbox hiển thị tên + phím vào hbox skill HUD trong player_controls.rpy
[ ] 5. (Tùy chọn) Thêm label upgrade/unlock vào skill_manager.rpy
[ ] 6. (Tùy chọn) Thêm slot mới vào screen skill_menu_screen trong skill_manager.rpy
[ ] 7. (Tùy chọn) Thêm hàng mới vào screen tutorial_controls_screen trong tutorial.rpy
```


---
## 8. LỖI THƯỜNG GẶP
---

**Lỗi: "name 'use_skill_4' is not defined"**
→ Quên thêm hàm `use_skill_4()` vào `init python` trong `skills.rpy`.

**Lỗi: "Unknown image 'hero_normal'"**
→ File `characters.rpy` chưa define image, hoặc file ảnh không tồn tại.

**Player không di chuyển khi nhấn phím**
→ Kiểm tra `call screen platforming_screen` đã được gọi chưa.
→ Tên phím sai: phải là `K_a` (chữ thường), không phải `K_A`.

**Tutorial hiện mãi không tắt**
→ Kiểm tra nút "Bắt đầu!" trong `tutorial_controls_screen` có action `Hide(...)` không.

**Skill 3 không hoạt động**
→ Mặc định `skill_3_unlocked = False`. Phải gọi `call unlock_skill_3` trước.

**`renpy.restart_interaction()` báo lỗi**
→ Phải gọi trong `init python` block, không gọi trong label Ren'Py thông thường.
→ Nếu muốn gọi trong label: `$ renpy.restart_interaction()`
