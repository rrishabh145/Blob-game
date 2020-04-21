import pygame
import random
from blob_class import Blob
import numpy as np

STARTING_BLUE_BLOBS = 15
STARTING_RED_BLOBS = 15
STARTING_GREEN_BLOBS = 15

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

#initial game environment setup
game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

# inheritance class
class BlueBlob(Blob):
    # when we inherit, we take all of the methods from parent class
    # we can overwrite those methods
    # or we can create new methods
    def __init__(self, x_boundary, y_boundary): # rewriting the init method
        super().__init__((0, 0, 255), x_boundary, y_boundary)

    # operator overloading of '+' when two blobs collide
    def __add__(self, other_blob):
        if other_blob.color== (255,0,0):
            self.size -= other_blob.size
            other_blob.size -= self.size
        elif other_blob.color == (0,255,0):
            self.size += other_blob.size
            other_blob.size = 0
        elif other_blob.color == (0,0,255):
            pass
        else:
            raise Exception('Tried to combine one or multiple blobs of unsupported colors.')

class RedBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        super().__init__((255, 0, 0), x_boundary, y_boundary)

class GreenBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        super().__init__((0, 255, 0), x_boundary, y_boundary)

#to check if two circular blobs are touching each other or not
def is_touching(b1,b2):
    return np.linalg.norm(np.array([b1.x, b1.y])-np.array([b2.x, b2.y])) < (b1.size + b2.size)

#to iterate through all of the blobs and check for collition
def handle_collision(blob_list):
    blues, reds, greens = blob_list
    for blue_id, blue_blob in blues.copy().items(): #we do copy().items() if we wish to modify the same item
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                if blue_blob == other_blob:
                    pass
                else:
                    if is_touching(blue_blob, other_blob):
                        blue_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        if blue_blob.size <= 0:
                            del blues[blue_id]

    return blues, reds, greens

# fn to draw the gameboard
def draw_environment(blob_list):
    blues, reds, greens = handle_collision(blob_list)
    game_display.fill(WHITE) # clear and redraw after very frame
    for blob_dict in blob_list:    
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display,blob.color, [blob.x, blob.y], blob.size) # circle( where to display, what to display)
            blob.move()
            blob.check_bounds() #checks if blob doesnt run out of screen

    pygame.display.update() # this step brings the previous step in action
    return blues, reds, greens

def main():
    blue_blobs = dict(enumerate([BlueBlob(WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)])) #giving the blobs an id each
    red_blobs = dict(enumerate([RedBlob(WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)])) #giving the blobs an id each
    green_blobs = dict(enumerate([GreenBlob(WIDTH,HEIGHT) for i in range(STARTING_GREEN_BLOBS)])) #giving the blobs an id each

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if the game is quit by user
                pygame.quit()
                quit()

        blue_blobs, red_blobs, green_blobs = draw_environment([blue_blobs,red_blobs,green_blobs])
        clock.tick(60) #to limit FPS

if __name__ == '__main__':
    main()