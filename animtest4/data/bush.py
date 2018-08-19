class Bush(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pngBush
		self.rect = self.image.get_rect()
		self.rect.x = x * TILE_SIZE
		self.rect.y = y * TILE_SIZE - 224

