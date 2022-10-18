import random
import pygame
from hitbox import *


class Tuyau:
    def __init__(self, screen, x):
        self.screen = screen
        self.x = x
        self.largeur = 52
        self.hauteur = 150
        self.speed = 0
        self.randomMin = 30
        self.randomMax = 250
        self.y = random.randint(100, 200)
        self.imageHaut = pygame.image.load("img/pipe-green-down.png")
        self.imageBas = pygame.image.load("img/pipe-green.png")

    def update(self):
        self.x += - self.speed
        if self.x < - self.largeur:
            self.x = 864
            self.y = random.randint(self.randomMin, self.randomMax)

    def getHitBoxes(self):
        hbs = []
        hbs.append(Hitbox(self.screen, self.x, 0, self.largeur, self.y))
        hbs.append(Hitbox(self.screen, self.x, self.y +
                   self.hauteur, self.largeur, 512))
        return hbs

    def collision(self, oiseau):
        hbs = self.getHitBoxes()
        for hb in hbs:
            if hb.collision(oiseau.getHitBox()):
                return True
        return False

    def point(self, oiseau):
        hbScore = Hitbox(self.screen, self.x + 50, self.y, 1, self.hauteur)
        if hbScore.collision(oiseau.getHitBox()):
            return True

    def draw(self):
        self.screen.blit(self.imageHaut, (self.x, self.y - 320))
        self.screen.blit(self.imageBas, (self.x, self.y + self.hauteur))
