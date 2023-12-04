import pygame
import sys
import random
from game_parameters import *
from utilities import draw_background
from player import Jet, jets
from goats2 import Goat, goats1, goats2

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Jet")

background = screen.copy()
draw_background(background)

clock = pygame.time.Clock()
welcome_font = pygame.font.Font("../VANDYK_FINAL_PROJECT/assets/fonts/FlappyBirdy.ttf",size = 75)
welcome_text = welcome_font.render("Welcome to Flappy Jet", True, (255, 69, 0))
welcome_rect = welcome_text.get_rect(center = (screen_width//2, screen_height//2))
welcome_timer = 15 * 60

player = Jet(screen_width / 2, screen_height / 2)
jets.add(player)

goat1 = Goat(screen_width, 0, 1 )
goats1.add(goat1)

goat_size = goat1.image.get_size()
goat2 = Goat(screen_width, screen_height - goat_size[1], 0)
goats2.add(goat2)

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.y_velocity = 1.5*(PLAYER_SPEED - gravity)
        else:
            player.gravity_effect()

    if welcome_timer > 0:
        screen.blit(background, (0, 0))
        screen.blit(welcome_text, welcome_rect)
        pygame.display.flip()
        welcome_timer -= 1

    else:
        screen.blit(background, (0,0))


        goats1.update()
        goats2.update()
        player.update()

        for goat1 in goats1:
            if goat1.rect.x < -goat1.rect.width:
                goats1.remove(goat1)
                goat1 = Goat(screen_width, 0, 1 )
                goats1.add(goat1)

        for goat2 in goats2:
            if goat2.rect.x < -goat2.rect.width:
                goats2.remove(goat2)
                goat2 = Goat(screen_width, screen_height - goat_size[1], 0)
                goats2.add(goat2)


        goats1.draw(screen)
        goats2.draw(screen)
        player.draw(screen)

        pygame.display.flip()



pygame.quit()
sys.exit()