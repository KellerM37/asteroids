import pygame
import pygame.gfxdraw
from circleshape import CircleShape
from data.constants import *

class Shot(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)

	def draw(self, screen):
		pygame.gfxdraw.filled_circle(screen, int(self.position.x), int(self.position.y), self.radius, (255, 255, 255))

	def update(self, dt):
		self.position += self.velocity * dt