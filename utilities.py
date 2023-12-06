import pygame
import random
from game_parameters import *
from missile import Missile, missiles

# Function to draw the background onto the screen
def draw_background(screen):
    # Load the images used for the background
    clouds = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/small_clouds.png").convert()
    ground = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/try_better_hills.png").convert()
    sky = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/sky.png").convert()

    # Set the transparency color of the images
    clouds.set_colorkey((0,0,0))
    ground.set_colorkey((0,0,0))
    sky.set_colorkey((0,0,0))

    # Draw the sky as a tile
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(sky, (x, y))

    # Draw the ground as tiles
    for x in range(0, screen_width, tile_size):
        screen.blit(ground, (x, screen_height - tile_size))

    # Draw the clouds randomly as tiles
    for _ in range(10):
        x = random.randint(0, screen_width)
        screen.blit(clouds, (x, screen_height / 16))

# Function to add more missiles to the missile group
def add_missiles(num_missiles, pos, angle):
    for _ in range(num_missiles):
        missiles.add(Missile(pos[0], pos[1], angle)) # Add the missiles based off position and angle

