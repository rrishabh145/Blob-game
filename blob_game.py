import pygame
import random

WIDTH = 800
HEIGHT = 600
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

#initial game environment setup
game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

class Blob:
	"""docstring for Blob"""
	def __init__(self, color):
		self.x = random.randrange(0,WIDTH)	#size of game window
		self.y = random.randrange(0,HEIGHT)
		self.size = random.randrange(4,8) # size of the blob
		self.color = color	#color of the blob
		
	def move(self):
		self.move_x = random.randrange(-1,2) #moving 1 step randomly
		self.move_y = random.randrange(-1,2)
		self.x += self.move_x
		self.y += self.move_y

		#to prevent the blob from running off the creen
		if self.x < 0: self.x = 0
		elif self.x > WIDTH: self.x = WIDTH

		if self.y<0: self.y = 0
		elif self.y > HEIGHT: self.y = HEIGHT


def draw_environment(blob):
	game_display.fill(WHITE) # clear and redraw after very frame
	pygame.draw.circle(game_display,blob.color, [blob.x, blob.y], blob.size) # circle( where to display, what to display)
	pygame.display.update() # this step brings the previous step in action
	blob.move()

def main():
	red_blob = Blob(color=RED)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # if the game is quit by user
				pygame.quit()
				quit()

		draw_environment(red_blob)
		clock.tick(60) #to limit FPS

if __name__ == '__main__':
	main()