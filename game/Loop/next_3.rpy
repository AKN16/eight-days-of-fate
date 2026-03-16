label next_3:
    if day_count == 1:
        jump next_day_1_3
    elif day_count == 2:
        jump next_day_2_3
    elif day_count <= 6:
        jump next_day_3_3
    else:
        jump next_day_7_3
