import pygame

from data import constants

class Ground(pygame.sprite.Sprite):
	def __init__(self, x, y):						#
		super().__init__()							#
		self.image = constants.pngTile				#Same for all static objects. Load image file, set object rect
		self.rect = self.image.get_rect()			#and set x and y dimensions
		self.rect.x = x * constants.TILE_SIZE		#
		self.rect.y = y * constants.TILE_SIZE		#

