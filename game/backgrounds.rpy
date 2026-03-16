# =============================================
# BACKGROUNDS & MUSIC DEFINITIONS
# =============================================
# Tất cả background đã được scale 1920x1080
#
# BẢNG PHÂN CẢNH:
#   bg_palace_hall   → CUNG ĐIỆN (gặp vua, phòng ngai vàng)
#   bg_palace_inner  → CUNG ĐIỆN (phòng riêng, hành lang trong)
#   bg_forest        → RỪNG (hành trình, thoát khỏi vòng lặp)
#   bg_devil_castle  → LÂU ĐÀI ÁC MA (ngoài trời, sân)
#   bg_dungeon       → LÂU ĐÀI ÁC MA (nội thất, gặp Zagan & công chúa)
#   (ngã ba đường)   → KHÔNG CÓ SCENE → nền đen mặc định Ren'Py
# =============================================

# ── CUNG ĐIỆN ──
# Nguồn: craftpix castle interior background 2 (cột đá, cờ vàng, cửa sổ gothic)
image bg_palace_hall  = "images/backgrounds/palace_hall_1920.png"

# Nguồn: craftpix castle interior background 4 (nội thất chạm khắc, hoa văn hồng)
image bg_palace_inner = "images/backgrounds/palace_inner_1920.png"

# ── RỪNG ──
# Nguồn: Free Pixel Art Forest (cây cổ thụ tối, tia sáng huyền bí)
image bg_forest = "images/backgrounds/forest_1920.png"

# ── LÂU ĐÀI ÁC MA (ngoài trời) ──
# Nguồn: Fort of Illusion (thành tối, đuốc vàng, núi xanh lam)
image bg_devil_castle = "images/backgrounds/devil_castle_1920.png"

# ── LÂU ĐÀI ÁC MA (nội thất / hầm ngục) ──
# Nguồn: Cold Corridors (hành lang xanh tối, cột đá, đuốc)
image bg_dungeon = "images/backgrounds/dungeon_1920.png"

# ── NHẠC NỀN ──
# myst.ogg        → huyền bí / tối → dùng cho lâu đài ác ma & rừng
# royal_theme.ogg → fantasy hoành tráng → dùng cho cung điện & ngày mới
define audio.music_myst  = "audio/music/myst.ogg"
define audio.music_royal = "audio/music/royal_theme.ogg"
