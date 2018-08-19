import pygame

from data import constants

class Cloud(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = constants.pngCloud
		self.rect = self.image.get_rect()
		self.rect.x = x * constants.TILE_SIZE
		self.rect.y = y * constants.TILE_SIZE

