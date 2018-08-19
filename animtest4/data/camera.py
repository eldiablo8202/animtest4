import pygame

from data import constants

class Camera:
	def __init__(self, width, height):
		self.camera = pygame.Rect(0, 0, width, height)
		self.width = width
		self.height = height
		
	def apply(self, entity):
		return entity.rect.move(self.camera.topleft)
	
	def update(self, target):
		x =- target.rect.x + int(constants.WINDOW_WIDTH / 4)
		x = min(0, x)
		x = max(-(self.width - constants.WINDOW_WIDTH), x)
		self.camera = pygame.Rect(x, 0, self.width, self.height)
