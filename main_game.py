import pygame
import sys
import random
from game_parameters import *
from utilities import draw_background
from player import Jet, jets

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Using blit to draw tiles")

background = screen.copy()
draw_background(background)

player = Jet(screen_width / 2, screen_height / 2)
jets.add(player)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.move_up()

    screen.blit(background, (0, 0))

    # jets.update()
    player.update()

    # jets.draw(screen)
    player.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()