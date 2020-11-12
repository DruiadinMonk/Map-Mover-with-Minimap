# Player class to create images able to be modified of their (x, y).

# MODULES
import pygame



# CLASS: Player
class Player:

	# INITIALIZE
	def __init__(self, window, color, x, y, r):
		self.window = window
		self.color = color
		self.x = x
		self.y = y
		self.r = r


	# DRAW BACKGROUND
	def draw(self):

		# OUTLINE ONLY SQUARES
		pygame.draw.circle(self.window, self.color, (self.x, self.y), self.r)
