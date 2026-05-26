# =============================================
# CHARACTER SPRITE DEFINITIONS
# =============================================
# Nguồn: character-pack-full_version
#   hero     = character #1  (tóc cam, chiến binh)
#   princess = character #5  (tóc hồng, váy đỏ)
#   king     = character #20 (mũ vương miện, râu bạc)
#   devil    = character #24 (ngọn lửa đỏ, quái vật)

# ── IDLE (đứng yên, nhìn xuống / ra phía trước) ──
image hero_normal     = "images/hero/hero.png"
image king_normal     = "images/king/king.png"
image princess_normal = "images/princess/princess.png"
image devil_normal    = "images/devil/devil.png"

# ── HERO ANIMATION (walk down) ──
image hero_walk_down = Animation(
    "images/hero/hero_down_1.png", 0.15,
    "images/hero/hero_down_2.png", 0.15,
    "images/hero/hero_down_3.png", 0.15)

# Dùng frame cụ thể trong scene nếu cần
image hero_down_1  = "images/hero/hero_down_1.png"
image hero_down_2  = "images/hero/hero_down_2.png"
image hero_down_3  = "images/hero/hero_down_3.png"
image hero_left_1  = "images/hero/hero_left_1.png"
image hero_left_2  = "images/hero/hero_left_2.png"
image hero_right_1 = "images/hero/hero_right_1.png"
image hero_right_2 = "images/hero/hero_right_2.png"
# ── PRINCESS ANIMATION FRAMES ──
image princess_down_1  = "images/princess/princess_down_1.png"
image princess_down_2  = "images/princess/princess_down_2.png"
image princess_left_1  = "images/princess/princess_left_1.png"
image princess_right_1 = "images/princess/princess_right_1.png"

# ── KING ANIMATION FRAMES ──
image king_down_1 = "images/king/king_down_1.png"
image king_down_2 = "images/king/king_down_2.png"
image king_left_1 = "images/king/king_left_1.png"

# ── DEVIL ANIMATION FRAMES ──
image devil_down_1  = "images/devil/devil_down_1.png"
image devil_down_2  = "images/devil/devil_down_2.png"
image devil_left_1  = "images/devil/devil_left_1.png"
image devil_right_1 = "images/devil/devil_right_1.png"

# ── PLACEHOLDER EXPRESSIONS (map về idle cho đến khi có sprite riêng) ──
image devil_see_and_drink_tea  = "images/devil/devil.png"
image devil_smirk              = "images/devil/devil.png"
image devil_laugh              = "images/devil/devil.png"
image devil_excited            = "images/devil/devil.png"
image devil_ignore             = "images/devil/devil.png"
image devil_commend            = "images/devil/devil.png"
image devil_boring             = "images/devil/devil.png"
image princess_crazy           = "images/princess/princess.png"
image princess_kill_hero       = "images/princess/princess.png"
image princess_happy           = "images/princess/princess.png"
image princess_brave           = "images/princess/princess.png"
image princess_smirk           = "images/princess/princess.png"
image hero_surprise            = "images/hero/hero.png"
image hero_carry_out_execution = "images/hero/hero.png"
image queen                    = "images/princess/princess.png"
image happy_wedding            = "images/hero/hero.png"
