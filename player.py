import pygame
import random
from game_parameters import *


class Jet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Load image and set its transparency color
        self.image = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/sized_jet.png").convert()
        self.image.set_colorkey((0,0,0))

        # Create a rectangle to represent the player
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)

        # Set the player's velocity to 0
        self.y_velocity = 0

    # Apply the effect of gravity to the player's movement
    def gravity_effect(self):
        self.y_velocity = gravity

    # Move the player upwards
    def move_up(self):
        self.y_velocity = PLAYER_SPEED - gravity
        self.y += self.y_velocity
        self.rect.y = self.y

    # Stop the player's movement
    def stop(self):
        self.y_velocity = gravity

    # Update the player's position
    def update(self):
        self.y += self.y_velocity
        self.y = max(0, min(self.y, screen_height - self.rect.height)) # Keep the player on the screen
        self.rect.y = self.y

    # Draw the jet onto the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Create a group to store the player
jets = pygame.sprite.Group()