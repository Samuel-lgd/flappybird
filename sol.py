import pygame
from hitbox import *


class Sol:
    def __init__(self, screen):
        print("Init sol")
        self.screen = screen
        self.x = 0
        self.y = 400
        self.speed = 0
        self.image = pygame.image.load("img/base.png")

    def update(self):
        self.x = self.x - self.speed
        if self.x < -self.image.get_width():
            self.x = 0

    def getHitBox(self):
        return Hitbox(self.screen, self.x, self.y, 1000, 1000)

    def collision(self, oiseau):
        if self.getHitBox().collision(oiseau.getHitBox()):
            return True
        return False

    def draw(self):
        # print("Sol draw")
        self.screen.blit(self.image, (self.x, self.y))
        self.screen.blit(self.image, (self.x + self.image.get_width(), self.y))
        self.screen.blit(
            self.image, (self.x + 2*self.image.get_width(), self.y))
        self.screen.blit(
            self.image, (self.x + 3*self.image.get_width(), self.y))

# bird = Oiseau()
