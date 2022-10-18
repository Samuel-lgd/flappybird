import pygame


class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.speed = 0

        self.largHb = 250
        self.hautHb = 75
        self.xBtn = 864/2 - self.largHb/2
        self.yBtn = - 50

        self.xLogo = 864/2 - 200
        self.yLogo = -210

        self.startButton = pygame.image.load("img/start.png")
        self.logo = pygame.image.load("img/logo.png")

    def show(self):
        pass

    def update(self, show):
        if show:
            self.yBtn += 2
            self.yLogo += 2
            if self.yBtn >= 250:
                self.yBtn = 250
            if self.yLogo >= 60:
                self.yLogo = 60
        if not show:
            self.xBtn += -self.speed * 1.30
            self.xLogo += -self.speed * 1.30

    def draw(self):
        # pygame.draw.rect(self.screen, (255,0,0), (self.xBtn,self.yBtn,self.largHb,self.hautHb), 1)
        # pygame.draw.rect(self.screen, (255,0,0), (self.xLogo,self.yLogo,400,150), 1)

        self.screen.blit(self.startButton, (self.xBtn, self.yBtn))
        self.screen.blit(self.logo, (self.xLogo, self.yLogo))
