import pygame, sys

def draw_floor():
	screen.blit(floor_surface,(floor_x_pos,620)) #put surface
	screen.blit(floor_surface,(floor_x_pos + 400,620)) #put surface


pygame.init()
screen = pygame.display.set_mode((400, 711))
clock = pygame.time.Clock()

bg_surface = pygame.transform.scale2x(pygame.image.load('assets/background-day.png').convert())

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0
# floor_y_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,355))


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	screen.blit(bg_surface,(0,0)) #put surface
	screen.blit(bird_surface, bird_rect)
	floor_x_pos -=1
	draw_floor()
	if floor_x_pos <= -400:
		floor_x_pos = 0
	pygame.display.update()
	clock.tick(120)
