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
        self.y_velocity += gravity

    def move_up(self):
        self.y_velocity -= PLAYER_SPEED

    def stop(self):
        self.y_velocity = 0

    def update(self):
        self.gravity_effect()
        self.y += self.y_velocity
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

jets = pygame.sprite.Group()