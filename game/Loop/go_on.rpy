label go_on:
    if day_count == 4:
        jump go_on_4
    elif day_count == 5:
        jump go_on_5
    elif day_count == 6:
        jump go_on_6
    else:
        jump go_on_7
