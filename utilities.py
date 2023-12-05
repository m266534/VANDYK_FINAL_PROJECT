import pygame
import random
from game_parameters import *
from missile import Missile, missiles

def draw_background(screen):
    clouds = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/small_clouds.png").convert()
    ground = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/try_better_hills.png").convert()
    sky = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/sky.png").convert()

    clouds.set_colorkey((0,0,0))
    ground.set_colorkey((0,0,0))
    sky.set_colorkey((0,0,0))

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(sky, (x, y))

    for x in range(0, screen_width, tile_size):
        screen.blit(ground, (x, screen_height - tile_size))

    for _ in range(10):
        x = random.randint(0, screen_width)
        screen.blit(clouds, (x, screen_height / 16))

def add_missiles(num_missiles, pos, angle):
    for _ in range(num_missiles):
        missiles.add(Missile(pos[0], pos[1], angle))

