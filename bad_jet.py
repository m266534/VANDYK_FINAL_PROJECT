import pygame
import random
from game_parameters import *
from math import cos, sin


class Bad(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Load the image of the bad guys and set their transparency color
        self.image = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/enemy.png").convert()
        self.image.set_colorkey((0,0,0))

        # Create a rectangle to represent the bad guys
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

        # Set their speeds and center their position
        self.speed = random.uniform(BAD_SPEED_MIN, BAD_SPEED_MAX)
        self.rect.center = (x, y)

    # Update the position of the bad guys based on the angle calculated in the main code
    def update(self, theta):
        self.x += self.speed * cos(theta)
        self.rect.x = self.x
        self.y += self.speed * sin(theta)
        self.rect.y = self.y

    # Draw the bad guys onto the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Create a group to store the bad guys
bad_guys = pygame.sprite.Group()