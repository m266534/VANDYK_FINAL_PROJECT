import pygame
import random
from game_parameters import *

class Goat(pygame.sprite.Sprite):
    def __init__(self, x, y, top_bottom):
        super().__init__()
        self.x = x
        self.y = y
        if top_bottom == 1:
            self.image = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/new_goat_top.png").convert()
            self.image.set_colorkey((0, 0, 0))
        else:
            self.image = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/new_goat.png").convert()
            self.image.set_colorkey((255, 255, 255))

        self.goat_size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.goat_size[0] * 2, self.goat_size[1] * 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.uniform(GOAT_SPEED_MIN, GOAT_SPEED_MAX)
        # self.speed_increase_interval = 20
        # self.timer = 0



        # self.upper_goat = pygame.transform.flip(self.image, False, True)
    def update(self):
        self.x -= self.speed
        self.rect.x = self.x


    def draw(self, screen):
        screen.blit(self.image, self.rect)


goats1 = pygame.sprite.Group()
goats2 = pygame.sprite.Group()
