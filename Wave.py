import random

import pygame
from pygame.constants import QUIT, K_F11, K_SPACE, K_LCTRL

pygame.init()

# Константи ширини та висоти
window_width = 800
window_height = 600

FONT = pygame.font.SysFont('Verdana', 20)


#FPS гри
FPS = pygame.time.Clock()

#Константи кольорів
COLOR_DARK_RED = (200, 50, 0)
COLOR_BLACK = (0, 0 ,0)
COLOR_BLUE = (53, 137, 175)
COLOR_WHITE = (255, 255, 255)

#Створення екрану
main_display = pygame.display.set_mode((window_width, window_height))

bg = pygame.transform.scale(pygame.image.load('Fon.png'), (window_width, window_height))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

#Гравець
player_size = (30, 30)
player = pygame.image.load('Wave4-40.png').convert_alpha()  #pygame.Surface((player_size))         
player_rect = pygame.Rect(0, 300, *player_size)
player_speed = [0, 1]
player_move_up = [0, -2]


def create_obstacle():
    Obstacle_size = (30, 30)
    Obstacle = pygame.Surface(Obstacle_size)
    Obstacle.fill(COLOR_WHITE)
    Obstacle_rect = pygame.Rect(window_width, random.randint(0, window_height), *Obstacle_size)
    Obstacle_move = [-3, -0]
    return [Obstacle, Obstacle_rect, Obstacle_move]

CREATE_OBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_OBSTACLE, 100)

Obstacles = []

score = 0

#Головний цикл гри
playing = True

while playing:
    FPS.tick(240)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_OBSTACLE:
            Obstacles.append(create_obstacle())

    # main_display.fill(COLOR_BLACK)

    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width() 


    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

    keys = pygame.key.get_pressed()

    if keys[K_SPACE] and player_rect.bottom > 0:
        player_rect = player_rect.move(player_move_up)

    if keys[K_F11]:
        playing = False

    for Obstacle in Obstacles:
        Obstacle[1] = Obstacle[1].move(Obstacle[2])
        main_display.blit(Obstacle[0], Obstacle[1])
    
        if player_rect.colliderect(Obstacle[1]):
            playing = False

    #main_display.blit(FONT.render(str(score), True, COLOR_WHITE), (20, window_height-50))
    main_display.blit(player, player_rect)  
    
    player_rect = player_rect.move(player_speed)

    print(len(Obstacles))

    pygame.display.flip()

    for Obstacle in Obstacles:
        if Obstacle[1].left < 0:
            Obstacles.pop(Obstacles.index(Obstacle))
          