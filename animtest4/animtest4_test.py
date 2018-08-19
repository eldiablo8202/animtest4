import pygame

from data import constants

class Test:
	def __init__(self):
		pygame.init()
		self.constants = constants
		pygame.display.set_icon(self.constants.WINDOW_LOGO)
		pygame.display.set_caption('animtest4_test')
		screen = pygame.display.set_mode(self.constants.WINDOW_DIMENSIONS)

test = Test()
		
