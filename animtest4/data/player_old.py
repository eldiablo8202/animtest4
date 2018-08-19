import pygame
import sys

#sys.path.append('..') #<- this was need to make the call to Game() work

#import animtest4_test2 #<- removed for now as it doesn't work, animtest3 Player class uses no reference to the game class anyway
from data import constants

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, game):
		super().__init__()
		self.game = game
		self.image = constants.pngPlayer[0]
		self.rect = self.image.get_rect()
		self.rect.x = x * constants.TILE_SIZE
		self.rect.y = y * constants.TILE_SIZE - 64
		self.velocityX = 0
		self.velocityY = 0
		self.facingRight = True
		self.moving = False
		self.jumping = False 						#don't think this is used at all yet
		self.animCounter = 0
		self.frameTicker = 0
		self.jumpTimer = 0
		
	def gravity(self):
		if self.velocityY == 0:
			self.velocityY = 5
		else:
			self.velocityY += 0.35
			
	def walkRight(self):
		self.velocityX = 4
		self.moving = True
		self.facingRight = True
		self.frameTicker += 1
			
	def walkLeft(self):
		self.velocityX = -4
		self.moving = True
		self.facingRight = False
		self.frameTicker += 1
			
	def jump(self):
		self.jumping = True
		self.rect.y += 1
		collisionY = pygame.sprite.spritecollide(self, self.game.platformSprites, False)
		self.rect.y -= 1
		if len(collisionY) or self.rect.bottom >= constants.WINDOW_HEIGHT:
			self.velocityY = -10
			
	def draw(self):
		if self.velocityY != 0:
			if self.facingRight == True:
				self.image = constants.pngPlayer[3]
				self.animCounter = 0
			else:
				self.image = pygame.transform.flip(constants.pngPlayer[3], True, False)
				self.animCounter = 0
		else:
			if self.moving == False:
				if self.facingRight == True:
					self.image = constants.pngPlayer[0]
					self.animCounter = 0
				else:
					self.image = pygame.transform.flip(constants.pngPlayer[0], True, False)
					self.animCounter = 0
			else:
				if self.frameTicker == constants.FRAME_TICKER_MAX:
					if self.facingRight == True:
						self.image = constants.pngPlayer[self.animCounter]
					else:
						self.image = pygame.transform.flip(constants.pngPlayer[self.animCounter], True, False)
					self.animCounter = (self.animCounter + 1) % len(constants.pngPlayer)
					self.frameTicker = 0
					
		
			
	def update(self):			#maybe re-organise the code in this module so the keypress checks come first
		self.gravity()
		
		
		if self.jumping == True:
			self.jumpTimer += 1
			
		if self.jumpTimer == 50:
			self.jumping = False
			self.jumpTimer = 0
			
		
			
		now = pygame.time.get_ticks() #is this actually used anywhere?
		self.velocityX = 0
		#self.velocityY = 0	#this might break something <- it did, leave out for now
		#pygame.key.set_repeat(100, 75)
		keys = pygame.key.get_pressed()
		#catch key presses
		if keys[pygame.K_d]:
			self.walkRight()
		if keys[pygame.K_a]:
			self.walkLeft()
		if keys[pygame.K_SPACE]:
			if self.jumping == False:
				self.jump()
		
			
		self.rect.x += self.velocityX
		collisionX = pygame.sprite.spritecollide(self, self.game.platformSprites, False)
		for collision in collisionX:
			if self.velocityX > 0:
				self.rect.right = collision.rect.left
			elif self.velocityX < 0:
				self.rect.left = collision.rect.right
			self.velocityX = 0
		
		self.rect.y += self.velocityY
		collisionY = pygame.sprite.spritecollide(self, self.game.platformSprites, False)
		for collision in collisionY:
			if self.velocityY > 0:
				self.rect.bottom = collision.rect.top
			elif self.velocityY < 0:
				self.rect.top = collision.rect.bottom
			self.velocityY = 0
		
		self.draw()
			
		
                
