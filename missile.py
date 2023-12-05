import pygame
from game_parameters import *
from math import cos, sin

#sublcassing the Sprite by calling the base initializer before adding the Sprite to Groups
class Missile(pygame.sprite.Sprite):
    #constructor. Pass in its x and y position and/or the color and dimensions of the block
    def __init__(self, x, y, angle):
        #inherit from the parent class (Sprite)
        super().__init__()
        self.rect = pygame.Rect(0,0, MISSILE_WIDTH, MISSILE_HEIGHT)
        self.x = x
        self.y = y
        self.angle = angle


    #update object position
    def update(self, player):
        self.x += MISSILE_SPEED * cos(self.angle)
        self.y -= MISSILE_SPEED * sin(self.angle)
        self.rect.x, self.rect.y = self.x, self.y

    def draw_missile(self, screen):
        pygame.draw.rect(screen, MISSILE_COLOR, self.rect)

missiles = pygame.sprite.Group()