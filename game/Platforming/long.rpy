label long_road:
    "Vượt qua thử thách"
    "Gặp loài Quoki (Quokka ngoài đời) này lag easter egg thôi"
    "Chưa kiếm được frame Quokka pixel với lại không biết vẽ"
    "bối cảnh sẽ là ở ngay đây là một bãi đất, có một con Quoki,
    nếu di chuyển dũng sĩ lại gần thì con này sẽ ném con của nó về phía dũng sĩ."
    "Cái này ám chỉ ông vua cũng có hành vi ném công chuấ về phía nguy hiểm á."
    jump next_2



label easter_egg:
    "Đây là một easter egg thôi, không có gì đâu."
    jump long


label long:
    if day_count == 1:
        # Tutorial + bật platforming đúng lúc player cần di chuyển
        if not tutorial_done:
            call tutorial_platforming
        $ p_reset_position()
        show screen platforming_screen