import pygame

class Stencil():

	def __init__(self, screen):
		"""Initialize the stencil and set its starting position."""
		self.screen = screen

		# Load the stencil image and get its rect.
		self.image = pygame.image.load('images/Andrea Spiral.BMP')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Start each stencil center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

	def blitme(self):
		"""Draw the stecil at its current location."""
		self.screen.blit(self.image, self.rect)
