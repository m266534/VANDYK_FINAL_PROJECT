import pygame
import random
from game_parameters import *

class Goat(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("../VANDYK_FINAL_PROJECT/assets/sprites/new_goat.png").convert()
        self.image.set_colorkey((0,0,0))
        self.image= pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.speed = GOAT_SPEED
        max_goat_height = y  - 2 * self.image.get_height()
        self.goat_height = random.randint(gap, max_goat_height)

        self.y_top = self.goat_height - self.image.get_height()
        self.y_bottom = self.goat_height + gap

        self.rect_top = self.image.get_rect(topleft=(x, self.y_top))
        self.rect_bottom = self.image.get_rect(topleft=(x, self.y_bottom))


        self.upper_goat = pygame.transform.flip(self.image, False, True)
    def update(self):
        self.x -= self.speed
        self.rect_top.x = self.x
        self.rect_bottom.x = self.x

    def off_screen(self):
        return self.x + self.image.get_width() < 0

    def draw(self, screen):
        screen.blit(self.image, self.rect_top)
        screen.blit(pygame.tansform.flip(self.image, False, True), self.rect_bottom)

goats = pygame.sprite.Group()
