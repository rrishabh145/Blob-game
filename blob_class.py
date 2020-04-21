import random

class Blob:
    """docstring for Blob"""
    def __init__(self, color, x_boundary, y_boundary, size_range = (4,8), movement_range = (-1,2)):
        self.x_boundary = x_boundary # window size of the 
        self.y_boundary = y_boundary
        self.x = random.randrange(0,self.x_boundary)  #size of game window
        self.y = random.randrange(0,self.y_boundary)
        self.size = random.randrange(size_range[0],size_range[1]) # size of the blob
        self.color = color  #color of the blob
        self.movement_range = movement_range
        
    def move(self):
        self.move_x = random.randrange(self.movement_range[0],self.movement_range[1]) #moving 1 step randomly
        self.move_y = random.randrange(self.movement_range[0],self.movement_range[1])
        self.x += self.move_x
        self.y += self.move_y

    #to prevent the blob from running off the game screen
    def check_bounds(self):
        if self.x < 0: self.x = 0
        elif self.x > self.x_boundary: self.x = self.x_boundary

        if self.y<0: self.y = 0
        elif self.y > self.y_boundary: self.y = self.y_boundary
