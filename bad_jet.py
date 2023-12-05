import pygame
import random
from game_parameters import *
from math import cos, sin


class Bad(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/enemy.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(BAD_SPEED_MIN, BAD_SPEED_MAX)
        self.rect.center = (x, y)


    def update(self, theta):
        self.x += self.speed * cos(theta)
        self.rect.x = self.x
        self.y += self.speed * sin(theta)
        self.rect.y = self.y


    def draw(self, screen):
        screen.blit(self.image, self.rect)

bad_guys = pygame.sprite.Group()