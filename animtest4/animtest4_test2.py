import pygame
from os import path

from data import constants
from data import map
from data import camera
from data import ground
from data import cloud
from data import player

pygame.init()
pygame.display.set_icon(constants.WINDOW_LOGO)
pygame.display.set_caption('animtest4_test2')
screen = pygame.display.set_mode(constants.WINDOW_DIMENSIONS)
#screen = pygame.display.set_mode(constants.WINDOW_DIMENSIONS, pygame.FULLSCREEN)

gameClock = pygame.time.Clock()

class Game:
	def __init__(self):
		self.running = True

	def new(self):
		self.mapGrid = map.Map(path.join(constants.ASSETS_FOLDER, 'map.dat'))
		self.allSprites = pygame.sprite.Group()
		self.platformSprites = pygame.sprite.Group()
		self.decorationSprites = pygame.sprite.Group()
		for row, tiles in enumerate(self.mapGrid.mapData):
			for col, tile in enumerate(tiles):
				if tile == 'g':
					self.ground = ground.Ground(col, row)
					self.allSprites.add(self.ground)
					self.platformSprites.add(self.ground)
				if tile == 'c':
					self.cloud = cloud.Cloud(col, row)
					self.allSprites.add(self.cloud)
					self.decorationSprites.add(self.cloud)
				if tile == 'P':
					self.player = player.Player(col, row, game)
					self.allSprites.add(self.player)
					
		self.camera = camera.Camera(self.mapGrid.mapWidth, self.mapGrid.mapHeight)
		
	def draw(self):
		self.testFont = pygame.font.SysFont('monospace', 15)
		self.testFont.set_bold(True)
		self.lblVelocityX = self.testFont.render('VelocityX: ' + str(self.player.velocityX), 1, constants.BLACK)
		self.lblVelocityY = self.testFont.render('VelocityY: ' + str(self.player.velocityY), 1, constants.BLACK)
		self.lblRectX = self.testFont.render('RectX: ' + str(self.player.rect.x), 1, constants.BLACK)
		self.lblRectY = self.testFont.render('RectY: ' + str(self.player.rect.y), 1, constants.BLACK)
		self.lblLanded = self.testFont.render('Landed: ' + str(self.player.landed), 1, constants.BLACK)
		self.lblMoving = self.testFont.render('Moving: ' + str(self.player.moving), 1, constants.BLACK)
		self.lblJumping = self.testFont.render('Jumping: ' + str(self.player.jumping), 1, constants.BLACK)
		self.lblFacingRight = self.testFont.render('FacingRight: ' + str(self.player.facingRight), 1, constants.BLACK)
		screen.fill(constants.SKYBLUE)
		for sprite in self.allSprites:
			screen.blit(sprite.image, self.camera.apply(sprite))
		screen.blit(self.lblVelocityX, (20,20))
		screen.blit(self.lblVelocityY, (20,40))
		screen.blit(self.lblRectX, (20, 60))
		screen.blit(self.lblRectY, (20, 80))
		screen.blit(self.lblLanded, (400, 20))
		screen.blit(self.lblMoving, (400, 40))
		screen.blit(self.lblJumping, (400,60))
		screen.blit(self.lblFacingRight, (400, 80))
				
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
				pygame.quit()
				quit()
			if event.type == pygame.KEYUP:
				self.player.moving = False
				self.player.frameTicker = constants.FRAME_TICKER_MAX - 1
			
	def update(self):
		self.allSprites.update()
		self.camera.update(self.player)
		
	def run(self):
		while self.running == True:
			gameClock.tick(constants.GAME_FPS)
			self.events()
			self.update()
			self.draw()
			pygame.display.flip()
			
game = Game()

game.new()
game.run()
				
