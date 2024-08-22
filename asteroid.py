import pygame
import pygame.gfxdraw
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

		self.random_r = random.uniform(78, 90)
		self.random_g = random.uniform(65, 72)
		self.random_b = random.uniform(28, 36)
		self.random_angle = random.uniform(20, 50)

	def draw(self, screen):
		pygame.gfxdraw.filled_circle(screen, int(self.position.x), int(self.position.y), self.radius, (self.random_r, self.random_g, self.random_b))

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		v1 = self.velocity.rotate(self.random_angle)
		v2 = self.velocity.rotate(-self.random_angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		n1 = Asteroid(self.position.x, self.position.y, new_radius)
		n2 = Asteroid(self.position.x, self.position.y, new_radius)

		n1.velocity = v1 * 1.2
		n2.velocity = v2 * 1.2