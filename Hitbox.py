import pygame
pygame.init()


def DogHitbox(Falling_dog_x, Falling_dog_y):
    return pygame.Rect(Falling_dog_x, Falling_dog_y, 40, 40)

def CatHitbox(Falling_cat_x, Falling_cat_y):
    return pygame.Rect(Falling_cat_x, Falling_cat_y, 40, 40)

def PlayersHitbox(player_x, player_y):
    return pygame.Rect(player_x, player_y, 75, 75)

