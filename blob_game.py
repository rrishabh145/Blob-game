import pygame
import random
from blob_class import Blob

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3

WIDTH = 800
HEIGHT = 600
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

#initial game environment setup
game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

def draw_environment(blob_list):
    game_display.fill(WHITE) # clear and redraw after very frame
    for blob_dict in blob_list:    
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display,blob.color, [blob.x, blob.y], blob.size) # circle( where to display, what to display)
            blob.move()
            blob.check_bounds() #checks if blob doesnt run out of screen

    pygame.display.update() # this step brings the previous step in action
    

def main():

    blue_blobs = dict(enumerate([Blob(BLUE,WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)])) #giving the blobs an id each
    red_blobs = dict(enumerate([Blob(RED,WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)])) #giving the blobs an id each

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if the game is quit by user
                pygame.quit()
                quit()

        draw_environment([blue_blobs,red_blobs])
        clock.tick(60) #to limit FPS

if __name__ == '__main__':
    main()