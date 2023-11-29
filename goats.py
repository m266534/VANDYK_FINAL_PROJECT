import pygame
import random
from game_parameters import *

class Goat(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/new_goat.png").convert()
        self.image.set_colorkey((0,0,0))
        self.image= pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.gap = 100
        y = random.randint()
        self.x = x
        self.y = y
        self.speed = GOAT_SPEED
        self.rect.center = (x,y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)

goats = pygame.sprite.Group()
