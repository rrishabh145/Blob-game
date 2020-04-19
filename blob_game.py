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

		if self.x < 0: self.x = 0
		elif self.x > WIDTH: self.x = WIDTH

		if self.y<0: self.y = 0
		elif self.y > HEIGHT: self.y = HEIGHT