label short_road:
    if day_count == 1:
        # Tutorial + bật platforming đúng lúc player cần di chuyển
        if not tutorial_done:
            call tutorial_platforming
        $ p_reset_position()
        show screen platforming_screen


        
    "Vượt qua một số thử thách"
    
    jump next_2