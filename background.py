# Background class to create images able to be modified of their (x, y).

# MODULES
import pygame



# CLASS: Background
class Background:

	# INITIALIZE
	def __init__(self, window, color, x, y, w, h):
		self.window = window
		self.color = color
		self.x = x
		self.y = y
		self.w = w
		self.h = h


	# DRAW BACKGROUND
	def draw(self):

		# OUTLINE ONLY SQUARES
		pygame.draw.rect(self.window, self.color, (self.x, self.y, self.w, self.h), 1)
