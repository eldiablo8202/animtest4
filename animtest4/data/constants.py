import pygame
from os import path


WHITE = (255,255,255)
BLACK = (0,0,0)
SKYBLUE = (0,128,255)
GREENSCREEN = (76,255,0)
PINKSCREEN = (255,0,170)

ASSETS_FOLDER = path.join(path.dirname(__file__), 'assets')
WINDOW_DIMENSIONS = WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480	
WINDOW_LOGO = pygame.image.load(path.join(ASSETS_FOLDER, 'tri.png'))
GAME_FPS = 60
TILE_SIZE = 32
MOVE_DISTANCE = 4		#Use constants for these so I dont have to keep changing numbers
FRAME_TICKER_MAX = 4	#for left/right movements				

pngTile = pygame.image.load(path.join(ASSETS_FOLDER, 'tile.png'))
pngBush = pygame.transform.scale2x(pygame.image.load(path.join(ASSETS_FOLDER, 'bush.png')))
pngBush.set_colorkey(PINKSCREEN)
pngCloud = pygame.transform.scale2x(pygame.image.load(path.join(ASSETS_FOLDER,'cloud.png')))
pngCloud.set_colorkey(GREENSCREEN)
#pngSnake = pygame.transform.scale2x(pygame.image.load(path.join(ASSETS_FOLDER, 'wboy_snake.png')))
#pngSnake.set_colorkey(PINKSCREEN)
pngPlayer = [pygame.image.load(path.join(ASSETS_FOLDER, 'wboy' + str(i) + '.png')) for i in range(1,5)]

for i in range(0,4):
	pngPlayer[i].set_colorkey(PINKSCREEN)

