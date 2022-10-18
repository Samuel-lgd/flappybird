# Créé par CHALULB, le 11/02/2021 en Python 3.7
import pygame

class Hitbox():
    def __init__(self, screen, x, y, largeur, hauteur):
        self.x = x
        self.y = y
        self.screen = screen
        self.largeur = largeur
        self.hauteur = hauteur

    def collision(self, h):
        colX = (h.x < self.x + self.largeur) and (self.x < h.x + h.largeur)
        colY = (h.y < self.y + self.hauteur) and (self.y < h.y + h.hauteur)
        return colX and colY

    def draw(self):
        pygame.draw.rect(self.screen, (255,0,0), (self.x,self.y,self.largeur,self.hauteur), 10)
