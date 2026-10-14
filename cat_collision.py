def cat_collision_detection(player_x, player_y, player, Falling_cat_x, Falling_cat_y, Falling_cat):
    return (player_x <= Falling_cat_x + Falling_cat.width and
            player_x + player.width >= Falling_cat_x and
            player_y <= Falling_cat_y + Falling_cat.height and
            player_y + player.height >= Falling_cat_y)