import pygame
from os import path

from data import map
from data import camera
from data import cloud
from data import bush
from data import ground

#initialise pygame
pygame.init()

#initialise clock
gameClock = pygame.time.Clock()

#initialise window
pygame.display.set_icon(WINDOW_LOGO)
pygame.display.set_caption('animtest3')
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)


