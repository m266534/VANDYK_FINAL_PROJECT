import time
import sys
import random
from game_parameters import *
from utilities import draw_background, add_missiles
from player import Jet, jets
from goats2 import Goat, goats1, goats2
from bad_jet import Bad, bad_guys
from missile import Missile, missiles
from math import atan2
import pygame.mixer

# Initializing Pygame
pygame.init()

# Loading background music and play an a loop
pygame.mixer.music.load("../VANDYK_FINAL_PROJECT/assets/sounds/DangerZone.mp3")
pygame.mixer.music.play(-1)

# Creating the game window and setting tile window value
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Jet")

# Creating a copy of the screen for background and drawing the background
background = screen.copy()
draw_background(background)

# Creating a Pygame clock object to control frame rate
clock = pygame.time.Clock()

# Loading fonts, creating text, and loading sounds for game
welcome_font = pygame.font.Font("../VANDYK_FINAL_PROJECT/assets/fonts/FlappyBirdy.ttf",size = 75)
welcome_text = welcome_font.render("Welcome to Flappy Jet", True, (0, 128, 0))
welcome_rect = welcome_text.get_rect(center = (screen_width//2, screen_height//2))
starting_text = welcome_font.render("Press Space Bar to Start", True, (0, 128, 0))
starting_rect = starting_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
score_font = pygame.font.Font("../VANDYK_FINAL_PROJECT/assets/fonts/Arcade.ttf", size = 35)
score_sound = pygame.mixer.Sound("../VANDYK_FINAL_PROJECT/assets/sounds/score.wav")
crash_sound = pygame.mixer.Sound("../VANDYK_FINAL_PROJECT/assets/sounds/crash.wav")
missile_sound = pygame.mixer.Sound("../VANDYK_FINAL_PROJECT/assets/sounds/missle.wav")
explosion_sound = pygame.mixer.Sound("../VANDYK_FINAL_PROJECT/assets/sounds/explosion.wav")
clock_font = pygame.font.Font("../VANDYK_FINAL_PROJECT/assets/fonts/Arcade.ttf", size = 35)

# Created the player and added to the jets group
player = Jet(screen_width / 2, screen_height / 2)
jets.add(player)

#Create and store the top Goat
goat1 = Goat(screen_width, 0, 1 )
goats1.add(goat1)

#Create and store the bottom
goat_size = goat1.image.get_size()
goat2 = Goat(screen_width, screen_height - goat_size[1], 0)
goats2.add(goat2)


#Initialize the score and the lives of the player
score = 0
lives = number_lives

# Flag to control main game loop and welcome_screen
running = True
welcome_screen = True

while welcome_screen:
    # Check for events in game
    for event in pygame.event.get():
        # If the user closes the window, quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # If the user presses the spacebar, move past the welcome screen
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            welcome_screen = False

    # Render the welcome screen elements
    screen.blit(background, (0, 0))
    screen.blit(welcome_text, welcome_rect)
    screen.blit(starting_text, starting_rect)
    pygame.display.flip()
    clock.tick(60) #Control the FPS to 60

# Begin recording the start time
start_time = pygame.time.get_ticks()
# Create the time delays to add the bad guys as time goes on making the game progressively harder
time_to_add_first_bad_guy = 15000
time_to_add_second_bad_guy = 30000
time_to_add_third_bad_guy = 60000

# Create main game loop as long as the player is alive
while lives > 0:
    for event in pygame.event.get():
        # Quit the game if the window is closed
        if event.type == pygame.QUIT:
            running = False
        # Stop player movement if closed
        player.stop()

        if event.type == pygame.KEYDOWN:
            # Move the player upwards when the "Up" key is pressed
            if event.key == pygame.K_UP:
                player.y_velocity = 1.7*(PLAYER_SPEED-gravity)


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: # [0] Ensures that the event will occur if the left mouse button is clicked
                pos = player.rect.midright # Get the position of the right side of the player
                mouse_x, mouse_y = pygame.mouse.get_pos() # Get the position of where the mouse was clicked
                angle = - atan2(mouse_y - pos[1], mouse_x - pos[0])# Calculate the angle between the player and mouse click
                add_missiles(1, pos, angle)# Add the missile to fire it with the position and angle
                pygame.mixer.Sound.play(missile_sound)# Add the missile sound effect


    else:
        # If there's no welcome screen, draw the background
        screen.blit(background, (0,0))

        # Update the move-able game objects
        player.update()
        goats1.update()
        goats2.update()
        missiles.update(player)

        # Calculate the total time since the game has started
        current_time = pygame.time.get_ticks()
        time_elapsed = current_time - start_time

        # Check if it's time to add the first bad_guy
        if time_elapsed >= time_to_add_first_bad_guy and len(bad_guys) == 0:
            bad_guys.add(Bad(random.randint(0, screen_width - tile_size), 0))

        # Check if it's time to add the second bad_guy
        if time_elapsed >= time_to_add_second_bad_guy and len(bad_guys) == 1:
            bad_guys.add(Bad(random.randint(0, screen_width - tile_size), 0))

        # Check if it's time to add the third bad_guy
        if time_elapsed >= time_to_add_third_bad_guy and len(bad_guys) == 2:
            bad_guys.add(Bad(random.randint(0, screen_width - tile_size), 0))

        # Get the current time in seconds
        current_time_seconds = pygame.time.get_ticks() // 1000  # Convert milliseconds to seconds

        # Format the time as HH:MM:SS
        formatted_time = time.strftime('%H:%M:%S', time.gmtime(current_time_seconds))

        # Render the time onto the screen
        clock_text = clock_font.render(formatted_time, True, (255, 69, 0))
        screen.blit(clock_text, (10, 10))

        # Update the movement of the bad guys based on the position of the player
        for bad in bad_guys:
            theta = atan2(player.y - bad.y, player.x - bad.x)
            bad.update(theta)


        death1 = pygame.sprite.spritecollide(player, goats1, True)
        death2 = pygame.sprite.spritecollide(player, goats2, True)

        if death1 or death2:
            player.stop()
            pygame.mixer.Sound.play(crash_sound)
            lives -= 1


        crash = pygame.sprite.spritecollide(player, bad_guys, True)
        if crash:
            lives -= 1

        for missile in missiles:
            if missile.rect.y > screen_height:
                missiles.remove(missile)

            for bad_guy in bad_guys:
                missile_enemy = pygame.sprite.spritecollide(missile, bad_guys, True)
                if missile_enemy:
                    score += len(missile_enemy)
                    pygame.mixer.Sound.play(explosion_sound)
                    bad_guys.remove(missile_enemy)
                    bad_guys.add(Bad(random.randint(0, screen_width - tile_size),  0))
                    missiles.remove(missile)


        for goat1 in goats1:
            if goat1.rect.x < -goat1.rect.width:
                goats1.remove(goat1)
                goat1 = Goat(screen_width, 0, 1 )
                goats1.add(goat1)
                score += 1
                pygame.mixer.Sound.play(score_sound)

        for goat2 in goats2:
            if goat2.rect.x < -goat2.rect.width:
                goats2.remove(goat2)
                goat2 = Goat(screen_width, screen_height - goat_size[1], 0)
                goats2.add(goat2)
                score += 1
                pygame.mixer.Sound.play(score_sound)

        player.draw(screen)
        goats1.draw(screen)
        goats2.draw(screen)
        bad_guys.draw(screen)

        for missile in missiles:
            missile.draw_missile(screen)

        text = score_font.render(f"{score}", True, (255, 69, 0))
        screen.blit(text, (screen_width - text.get_width() - 10, 0))

        pygame.display.flip()



screen.blit(background, (0,0))
player.draw(screen)
message = score_font.render("Game Over", True, (0,0,0))
screen.blit(message, (screen_width / 2 - message.get_width() / 2, screen_height / 2 - message.get_height() / 2))

score_text = score_font.render(f"Score: {score}", True, (0,0,0))
screen.blit(score_text, (screen_width / 2 -score_text.get_width() / 2, screen_height /2 + message.get_height()))

time_text = clock_font.render(f"Time: {formatted_time}", True, (0, 0, 0))
screen.blit(time_text, (screen_width / 2 - time_text.get_width() / 2, screen_height / 2 + score_text.get_height() + message.get_height()))
pygame.display.flip()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()





