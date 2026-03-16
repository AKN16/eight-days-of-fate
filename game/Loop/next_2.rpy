label next_2:
    if day_count == 1:
        jump next_day_1_2
    elif day_count == 2:
        jump next_day_2_2
    elif day_count <= 6:
        jump next_day_3_2
    else:
        jump next_day_7_2
