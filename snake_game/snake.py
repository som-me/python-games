import pygame
import time
import random
pygame.init()
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

#Colors
black = (0,0,0)
white = (255,255,255)
red = (213,50,80)
green = (0,255,0)

#snake set_up
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)

def our_snake(snake_black, snake_list):
	for x in snake_list:
		pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
	mesg = font_style.render(msg, True, color)
	window.blit(mesg, [width / 6, height / 3])

def gameLoop():
	game_over = False
	game_close = False
	
	x1 = width/2
	y1 = height/2

	x1_change = 0
	y1_change = 0
	
	snake_list = []
	length_of_snake = 1

	#food Postition..

	foodx =	round(random.randrange(0, width - snake_block) / 10.0)* 10.0
	foody = round(random.randrange(0, height - snake_block) / 10.0)* 10.0

	while not game_over:
		while game_close:
			window.fill(black)
			message("YOU LOST! Press C-Play Again or Q-Quit", red)
			pygame.display.update()
			
			for event in pygame.event.get():
                		if event.type == pygame.KEYDOWN:
                    			if event.key == pygame.K_q:
                        			game_over = True
                        			game_close = False
                    			if event.key == pygame.K_c:
                        			gameLoop()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x1_change = -snake_block
					y1_change = 0
				if event.key == pygame.K_RIGHT:
					x1_change = snake_block
					y1_change = 0
				if event.key == pygame.K_UP:
					x1_change = 0
					y1_change = -snake_block
				if event.key == pygame.K_DOWN:
					x1_change = 0
					y1_change = snake_block
	
		if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
			game_close = True 
		x1 += x1_change
		y1 += y1_change
		window.fill(black)
		pygame.draw.rect(window, white, [foodx, foody, snake_block, snake_block])
		snake_head = []
		snake_head.append(x1)
		snake_head.append(y1)
		snake_list.append(snake_head)
		if len(snake_list) > length_of_snake:
			del snake_list[0]
			
		for x in snake_list[:-1]:
			if x == snake_head:
				game_close = True 
				
		our_snake(snake_block, snake_list)
		pygame.display.update()
		
		if x1 == foodx and y1 == foody:
			foodx = round(randam.randrange(0, width - snake_block) / 10.0)*10.0
			foody = round(random.randrange(0, height - snake_block) / 10.0)*10.0
			length_of_snake += 1

		clock.tick(snake_speed)
	pygame.quit()
	quit()
gameLoop()