import pygame
from game_parameters import *
from math import cos, sin

# Sublcassing the Sprite by calling the base initializer before adding the Sprite to Groups
class Missile(pygame.sprite.Sprite):
    # Constructor. Pass in its x and y position and/or the color and dimensions of the block
    def __init__(self, x, y, angle):
        #inherit from the parent class (Sprite)
        super().__init__()

        # Represent the missile with an area of the rectangle
        self.rect = pygame.Rect(0,0, MISSILE_WIDTH, MISSILE_HEIGHT)

        # Set the initial position and angle
        self.x = x
        self.y = y
        self.angle = angle


    # Update object position based on missile speed and the angle determined in the main code
    def update(self, player):
        self.x += MISSILE_SPEED * cos(self.angle)
        self.y -= MISSILE_SPEED * sin(self.angle)
        self.rect.x, self.rect.y = self.x, self.y

    # Draw the missile on the screen
    def draw_missile(self, screen):
        pygame.draw.rect(screen, MISSILE_COLOR, self.rect)

# Create a group to store the missiles
missiles = pygame.sprite.Group()