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
white_background.fill((104, 205, 242))
white_background.blit(background, (0, 0))

background = white_background

playerFrame1 = pygame.image.load("img/PlayerFrame1.png").convert_alpha()
playerFrame1 = pygame.transform.scale(playerFrame1, (200, 200))
playerFrame2 = pygame.image.load("img/PlayerFrame2.png").convert_alpha() 
playerFrame2 = pygame.transform.scale(playerFrame2, (200, 200))

player = pygame.transform.scale(player, (300, 300))
# made the player look like a person rather than just a boring box
Falling_cat = random.choice([pygame.image.load("img/Kitty1.png").convert_alpha(), pygame.image.load("img/Kitty2.png").convert_alpha(), pygame.image.load("img/Kitty3.png").convert_alpha()])
Falling_cat = pygame.transform.scale(Falling_cat, (100, 100))
# Gave the kitty an image so it wont look like a box
Falling_dog = random.choice([pygame.image.load("img/Doggy1.png").convert_alpha(), pygame.image.load("img/Doggy2.png").convert_alpha(), pygame.image.load("img/Doggy3.png").convert_alpha()])
Falling_dog = pygame.transform.scale(Falling_dog, (100, 100))

game_state = 1

frames = [playerFrame1, playerFrame2]
frame = 0
timer = 0

font = pygame.font.SysFont("Arial", 36)
start_time = pygame.time.get_ticks()

Quotes = ["Game Sucks, Not you..", "Watch your head next time!", "Ay, you good bro?", "Sucks to be you...", "You died... Shocker..", "Skill issue", "The Game cheated..Lol", "Try again.. If you dare"]

Jumping = False
while True:
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_vel_x = -0.2
            if event.key == pygame.K_RIGHT:
                player_vel_x = 0.2

        else:
            player_vel_x = 0
            player_vel_y = 0

    if game_state == 1:

        window_height = window.get_height()
        if Falling_cat_y > window_height:
            Falling_cat_y = -50
            Falling_cat_x = random.randint(0, 700)

        if Falling_dog_y > window_height:
            Falling_dog_y = -50
            Falling_dog_x = random.randint(0, 700)        

        player_x += player_vel_x # Updates the Player X pos (Need to place this note here cuz i keep losing it haha)
        player_y += player_vel_y # Updates the Player Y Pos

        PlayerHitbox = pygame.Rect(player_x, player_y, 75, 75)

        Falling_cat_x += Falling_cat_vel_x
        Falling_cat_y += Falling_cat_vel_y

        FallingCatHitbox = pygame.Rect(Falling_cat_x, Falling_cat_y, 40, 40)

        Falling_dog_x += Falling_dog_vel_x
        Falling_dog_y += Falling_dog_vel_y

        FallingDogHitbox = pygame.Rect(Falling_dog_x, Falling_dog_y, 40, 40)

        if dog_collision_detection(PlayerHitbox, FallingDogHitbox):
            game_state = 2
                
        elif cat_collision_detection(PlayerHitbox, FallingCatHitbox):
            game_state = 2
        
        window.blit(background, (0, 0))
        window.blit(frames[frame], (player_x, player_y))
        window.blit(Falling_cat, (Falling_cat_x, Falling_cat_y))
        window.blit(Falling_dog, (Falling_dog_x, Falling_dog_y))

    elif game_state == 2:
        window.fill((200, 0, 0)) # Game over red background
        Game_over_text = font.render("Game over", True, (255, 255, 255))
        Random_Game_over_quote  = random.choice(Quotes)
        Chosen_quote = font.render(Random_Game_over_quote, True, (255, 255, 255))
        window.blit(Chosen_quote, (250, 300))
        window.blit(Game_over_text, (300, 250))
        player_vel_x = 0
        player_vel_y = 0
        Falling_cat_vel_x = 0
        Falling_cat_vel_y = 0
        Falling_dog_vel_x = 0
        Falling_dog_vel_y = 0

    timer += 1

    if timer >= 450:
        frame = 1 - frame
        timer = 0

    pygame.display.flip()

