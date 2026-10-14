import pygame
import random
import time
from Cat import Falling_cat, Falling_cat_x, Falling_cat_y, Falling_cat_vel_x, Falling_cat_vel_y
from PlayerSystem import player, player_x, player_y, player_vel_x, player_vel_y
from Dog import Falling_dog, Falling_dog_x, Falling_dog_y, Falling_dog_vel_x, Falling_dog_vel_y
from cat_collision import cat_collision_detection
from dog_collision import dog_collision_detection
pygame.init()

window = pygame.display.set_mode((800, 600))

background = pygame.image.load("img/Background.png").convert_alpha()
background = pygame.transform.scale(background, (800, 600))

white_background = pygame.Surface((800, 600))
white_background.fill((255, 255, 255))
white_background.blit(background, (0, 0))

background = white_background

player = pygame.image.load("img/PlayerFrame1.png").convert_alpha()
player = pygame.transform.scale(player, (150, 150))
# made the player look like a person rather than just a boring box
Falling_cat = pygame.image.load("img/Kitty.png").convert_alpha()
Falling_cat = pygame.transform.scale(Falling_cat, (100, 100))
# Gave the kitty an image so it wont look like a box
Falling_dog = pygame.image.load("img/Doggy.png").convert_alpha()
Falling_dog = pygame.transform.scale(Falling_dog, (100, 100))

game_state = 1

cats_spawned = []
dogs_spawned = []

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
        if cat_collision_detection(player_x, player_y, player, Falling_cat_x, Falling_cat_y, Falling_cat):
            game_state = 2
        elif dog_collision_detection(player_x, player_y, player, Falling_dog_x, Falling_dog_y, Falling_dog):
            game_state = 2

        window_height = window.get_height()
        if Falling_cat_y > window_height:
            Falling_cat_y = -50
            Falling_cat_x = random.randint(0, 700)

        if Falling_dog_y > window_height:
            Falling_dog_y = -50
            Falling_dog_x = random.randint(0, 700)        

        player_x += player_vel_x # Updates the Player X pos
        player_y += player_vel_y # Updates the Player Y Pos

        Falling_cat_x += Falling_cat_vel_x
        Falling_cat_y += Falling_cat_vel_y

        Falling_dog_x += Falling_dog_vel_x
        Falling_dog_y += Falling_dog_vel_y
        
        window.blit(background, (0, 0))
        window.blit(player, (player_x, player_y))
        window.blit(Falling_cat, (Falling_cat_x, Falling_cat_y))
        window.blit(Falling_dog, (Falling_dog_x, Falling_dog_y))

    elif game_state == 2:
        window.fill((200, 0, 0))
        player_vel_x = 0
        player_vel_y = 0
        Falling_cat_vel_x = 0
        Falling_cat_vel_y = 0
        Falling_dog_vel_x = 0
        Falling_dog_vel_y = 0
    
    pygame.display.flip()

