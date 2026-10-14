def dog_collision_detection(player_x, player_y, player, Falling_dog_x, Falling_dog_y, Falling_dog):
    return (player_x <= Falling_dog_x + Falling_dog.width and
            player_x + player.width >= Falling_dog_x and
            player_y <= Falling_dog_y + Falling_dog.height and
            player_y + player.height >= Falling_dog_y)