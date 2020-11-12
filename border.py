# Background class to create images able to be modified of their (x, y).

# MODULES
import pygame



# CLASS: Background
class Border:

	# INITIALIZE
	def __init__(self, window, color, x1, y1, x2, y2, size):
		self.window = window
		self.color = color
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.size = size


	# DRAW BACKGROUND
	def draw(self):

		# OUTLINE ONLY SQUARES
		pygame.draw.line(self.window, self.color, (self.x1, self.y1), (self.x2, self.y2), self.size)
