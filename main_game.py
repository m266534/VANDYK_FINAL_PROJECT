import pygame
import sys
import random
from game_parameters import *
from utilities import draw_background

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Using blit to draw tiles")

background = screen.copy()
draw_background(background)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()