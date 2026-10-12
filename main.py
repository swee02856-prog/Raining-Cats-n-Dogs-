import pygame
import random
pygame.init()

window = pygame.display.set_mode((800, 600))

player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0

player = pygame.Surface((75, 75))
player.fill((0, 0, 0))
player = pygame.image.load("Player.png").convert_alpha()
player = pygame.transform.scale(player, (150, 150))

Falling_cat_x = 500
Falling_cat_y = -100
Falling_cat_vel_x = 0
Falling_cat_vel_y = 0.1

Falling_cat = pygame.Surface((50, 50))
Falling_cat.fill((0, 0, 0))
Falling_cat = pygame.image.load("Kitty.png").convert_alpha()
Falling_cat = pygame.transform.scale(Falling_cat, (100, 100))


game_state = 1

def collision_detection():
    return (player_x <= (Falling_cat_x + int(Falling_cat.width)) and
            (player_x + player.width) >= Falling_cat_x and
            player_y <= (Falling_cat_y + Falling_cat.height + 5) and
            (player_y + player.height) >= Falling_cat_y)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_vel_x = -0.3
            if event.key == pygame.K_RIGHT:
                player_vel_x = 0.3
            if event.key == pygame.K_UP:
                player_vel_y = -0.3
            if event.key == pygame.K_DOWN:
                player_vel_y = 0.3

        else:
            player_vel_x = 0
            player_vel_y = 0

    if game_state == 1:
        if collision_detection():
            game_state = 2


        window_height = window.get_height()
        if Falling_cat_y > window_height:
            Falling_cat_y = -50
            Falling_cat_x = random.randint(0, 700)

        player_x += player_vel_x # Updates the Player X pos
        player_y += player_vel_y # Updates the Player Y Pos

        Falling_cat_x += Falling_cat_vel_x
        Falling_cat_y += Falling_cat_vel_y

        window.fill((255, 255, 255))
        window.blit(player, (player_x, player_y))
        window.blit(Falling_cat, (Falling_cat_x, Falling_cat_y))

    elif game_state == 2:
        window.fill((200, 0, 0))
        player_vel_x = 0
        player_vel_y = 0
        Falling_cat_vel_x = 0
        Falling_cat_vel_y = 0
    
    pygame.display.flip()

