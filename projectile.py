import pygame
from hitbox import*
class Projectile(object):
	def __init__(self, screen, oiseau, speed):
		self.screen = screen
		self.x = oiseau.x + 10
		self.y = oiseau.y
		self.speed = speed

	def update(self):
		self.y += 13
		self.x += -1

	def draw(self):
		pygame.draw.rect(self.screen, (255,0,0), (self.x,self.y,3,10))

	def getHitBox(self):
	    return Hitbox(self.screen, self.x,self.y,3,10)

	def collision(self, shield):
		if self.getHitBox().collision(shield.getHitBox()):
			return True
		return False