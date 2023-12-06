import pygame
import random
from game_parameters import *

class Goat(pygame.sprite.Sprite):
    # While initializing, have "top_bottom" to distinguish the two goats
    def __init__(self, x, y, top_bottom):
        super().__init__()

        # Initialize the x and y positions
        self.x = x
        self.y = y

        # Load the top got
        if top_bottom == 1:
            self.image = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/new_goat_top.png").convert()
            self.image.set_colorkey((0, 0, 0))

        # Load the bottom goat
        else:
            self.image = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/new_goat.png").convert()
            self.image.set_colorkey((255, 255, 255))

        # Get the size of the goat in order to scale it properly for game play
        self.goat_size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.goat_size[0] * 1.75, self.goat_size[1] * 1.75))

        # Create a rectangle to represent the goats
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Set their speed
        self.speed = random.uniform(GOAT_SPEED_MIN, GOAT_SPEED_MAX)

    # Update both of the goats positions
    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    # Draw the goats onto the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Create two groups for each of the goats to be stored in
goats1 = pygame.sprite.Group()
goats2 = pygame.sprite.Group()
