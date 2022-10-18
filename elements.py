import pygame
import random
from hitbox import *


class Shield(object):
    def __init__(self, screen):
        self.screen = screen
        self.x = -25
        self.y = 375
        self.speed = 0
        self.cooldown = 0
        self.image = pygame.image.load("img/Shield.png")

    def spawn(self, luck):
        if luck == 0:
            self.x = 864 + random.randint(25, 150)
            self.cooldown = 4
            return True
        else:
            self.cooldown = 0
            self.x = -25

    def update(self):
        self.x += - self.speed
        if self.x <= -25:
            self.x = -25

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def getHitBox(self):
        return Hitbox(self.screen, self.x, self.y, 25, 25)

    def collision(self, tuyau):
        if self.getHitBox().collision(tuyau.getHitBox()):
            return True
        return False


class Star():
    def __init__(self, screen):
        self.screen = screen
        self.x = 45
        self.y = 1000
        self.speed = 0
        self.min = 30
        self.max = 250
        self.bool = True
        self.cooldown = 1
        self.image = pygame.image.load("img/star.png")
        self.visible = True

    def update(self):
        if self.visible:
            self.x += - self.speed
            if self.x <= -25:
                self.x = 864 + 27

            if self.y == self.min or self.y == self.min + 1:
                self.bool = True
            if self.y == self.max or self.y == self.max + 1:
                self.bool = False

            if self.bool == True:
                self.y += 2
            if self.bool == False:
                self.y += -2
        else:
            self.y = 1000

    def luck(self, x):
        if x == 0:
            self.y = 50
            self.cooldown = 2
            self.visible = True
        else:
            self.cooldown = 1
            self.visible = False

    def getHitBox(self):
        return Hitbox(self.screen, self.x, self.y, 25, 25)

    def collision(self, oiseau):
        if self.getHitBox().collision(oiseau.getHitBox()):
            return True
        return False

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        # pygame.draw.rect(self.screen, (255,0,0), (self.x,self.y,25,25), 1)


class Coin(object):
    """docstring for Coin"""

    def __init__(self, screen, speed):
        self.screen = screen
        self.x = 864 + random.randint(-25, 25)
        self.y = 375
        self.speed = speed
        self.image = pygame.image.load("img/coin.png")

    def update(self):
        self.x += - self.speed

    def draw(self):
        # pygame.draw.rect(self.screen, (255,0,0), (self.x,self.y,25,35), 1)
        self.screen.blit(self.image, (self.x, self.y))

    def getHitBox(self):
        return Hitbox(self.screen, self.x, self.y, 25, 35)

    def collision(self, tuyau):
        if self.getHitBox().collision(tuyau.getHitBox()):
            return True
        return False
