import pygame
import random
from game_parameters import *


class Jet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/sized_jet.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.y_velocity = 0

    def gravity_effect(self):
        if self.y_velocity == 0:
            self.y_velocity = gravity

    def move_up(self):
        self.y_velocity = - player_speed
