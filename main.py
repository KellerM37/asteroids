import pygame
import pygame_gui
from pygame_gui.elements import UILabel
from pygame_gui.elements import UIPanel
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	# Basic pygame and window initialization. UI manager loaded. Delta_time loaded.
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	ui_manager = pygame_gui.UIManager(screen.get_size(), "ui_theme.json")
	background = pygame.image.load("stars.jpg").convert()
	pygame.display.set_caption("Klar's game")
	clock = pygame.time.Clock()
	is_running = True
	dt = 0
	
	# Object groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	# Score initialiazation
	score = 0
	score_box = pygame.Rect((0, 0), (100, 30))
	score_text = UILabel(relative_rect=score_box, text=(f"Score: {score}"), manager=ui_manager)

	# Object group assignment
	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, shots)

	# Player and enviro start
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroidField = AsteroidField()


	while is_running:
		# 60 fps max
		dt = clock.tick(60) / 1000
		score = player.score

		# Check for events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_running = False
			ui_manager.process_events(event)
		
		ui_manager.update(dt)

		for x in updatable:
			x.update(dt)

		for x in asteroids:
			if x.collision(player) == True:
				print("Game over!")
#				exit()
			for shot in shots:
				if x.collision(shot) == True:
					shot.kill()
					x.split()




#		screen.fill(("black"))
		screen.blit(background, (0, 0))

		for x in drawable:
			x.draw(screen)
			
		ui_manager.draw_ui(screen)

		pygame.display.update()

if __name__ == "__main__":
	main()