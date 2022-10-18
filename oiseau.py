import pygame
from hitbox import *


class Oiseau:
    def __init__(self, screen):
        self.screen = screen
        self.x = 40
        self.y = 40

        self.image = []
        self.image.append(pygame.image.load("img/yellowbird-downflap.png"))
        self.image.append(pygame.image.load("img/yellowbird-midflap.png"))
        self.image.append(pygame.image.load("img/yellowbird-upflap.png"))

        self.frame = 0
        self.blinking = 0

        self.vitesse = 0
        self.acceleration = 0.10

        self.maxSaut = 12

    def jump(self):
        self.vitesse = (self.vitesse - 35) * 0.5
        if self.vitesse < -self.maxSaut:
            self.vitesse = -self.maxSaut

    def update(self):
        self.frame = self.frame + 1
        self.vitesse = self.vitesse + self.acceleration
        self.vitesse = self.vitesse * 0.965
        self.y = self.y + self.vitesse
        if self.y > 500:
            self.y = 0
            self.vitesse = 0

    def getHitBox(self):
        return Hitbox(self.screen, self.x, self.y, 28, 18)

    def blink(self):
        self.blinking += 1
        if self.blinking <= 5:
            self.screen.blit(
                self.image[(self.frame // 30) % 2], (self.x, self.y))
        elif self.blinking == 10:
            self.blinking = 0

    def draw(self):
        self.screen.blit(self.image[(self.frame // 30) % 2], (self.x, self.y))
