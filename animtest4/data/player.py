#A rework of the player class in an attempt to make everything more streamlined

import pygame
import sys

from data import constants

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, game):
		super().__init__()
		self.game = game
		self.image = constants.pngPlayer[0]
		self.rect = self.image.get_rect()
		self.rect.x = x * constants.TILE_SIZE
		self.rect.y = y * constants.TILE_SIZE
		self.velocityX = 0
		self.velocityY = 0
		self.facingRight = True
		self.moving = False
		self.jumping = False 
		self.landed = True
		self.animCounter = 0
		self.frameTicker = 0
		
	def update(self):
		#clear variables
		self.moving = False
		self.jumping = False
		self.velocityX = 0
		
		self.gravity()
		
		self.event()
		#pygame.event.clear(pygame.KEYDOWN)
		self.update_physics()
		self.rect.x += self.velocityX
		self.check_collisions_x()
		self.rect.y += self.velocityY
		self.check_collisions_y()
		self.draw()
		
		#repeat
		
	def gravity(self):
		if self.velocityY == 0:
			self.velocityY = 5
		else:
			self.velocityY += 0.35
	
	def event(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			self.moving = True
			self.facingRight = True
		elif keys[pygame.K_a]:
			self.moving = True
			self.facingRight = False
		if keys[pygame.K_SPACE]:
			self.jumping = True
		if keys[pygame.K_ESCAPE]:
			self.game.running = False
					
	def update_physics(self):
		if self.moving == True:
			if self.facingRight == True:
				self.velocityX = 4
				self.frameTicker += 1
			else:
				self.velocityX = -4
				self.frameTicker += 1
				
		if self.jumping == True:
			self.rect.y += 1
			collisionY = pygame.sprite.spritecollide(self, self.game.platformSprites, False)
			self.rect.y -=1
			if len(collisionY) or self.rect.bottom >= constants.WINDOW_HEIGHT:
				self.velocityY = -10
				
		if self.velocityY != 0:
			self.landed = False
				
	def check_collisions_x(self):
		collisionX = pygame.sprite.spritecollide(self, self.game.platformSprites, False)
		for collision in collisionX:
			if self.velocityX > 0:
				self.rect.right = collision.rect.left
			elif self.velocityX < 0:
				self.rect.left = collision.rect.right
			self.velocityX = 0
			
	def check_collisions_y(self):
		collisionY = pygame.sprite.spritecollide(self, self.game.platformSprites, False)
		for collision in collisionY:
			if self.velocityY > 0:
				self.rect.bottom = collision.rect.top
			elif self.velocityY < 0:
				self.rect.top = collision.rect.bottom
			self.velocityY = 0
			self.landed = True
			
	def draw(self):
		if self.landed == False:
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
