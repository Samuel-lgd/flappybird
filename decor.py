import pygame


class Decor:
    def __init__(self, screen):
        # print("Init decor")
        self.screen = screen
        self.image = pygame.image.load("img/background-day.png")
        self.x = 0
        self.speed = 0

    def update(self):
        self.x += - self.speed
        if self.x <= -287:
            self.x = 0

    def draw(self):
        self.screen.blit(self.image, (self.x + 0, 0))
        self.screen.blit(self.image, (self.x + 288, 0))
        self.screen.blit(self.image, (self.x + 576, 0))
        self.screen.blit(self.image, (self.x + 864, 0))
