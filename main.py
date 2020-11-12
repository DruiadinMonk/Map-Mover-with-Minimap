# Map Mover with a character that moves, by moving the background.

# MODULES
import pygame
import sys
from background import Background
from border import Border
from player import Player



# INITIALIZE
pygame.init()
WIN_X, WIN_Y = 400, 400
window = pygame.display.set_mode((WIN_X, WIN_Y))
pygame.display.set_caption("Map Mover")
clock = pygame.time.Clock()
run = True
FPS = 60
p_speed = 4



# COLORS
WHITE = (255, 255, 255)
GRAY  = (127, 127, 127)
BLACK = (  0,   0,   0)



# INITIALIZE, MAIN PRIMARY MAP
# Background Map
main_background = []
x = y = 0
sq = 20
for col in range(20): 	# 40 tiles per column.
	for row in range(20): 	# 40 tiles per row.

		# CREATE: Object
		b = Background(window, GRAY, x, y, sq, sq)
		main_background.append(b)

		# UPDATE: (x, y)
		x += 20

	# After row is complete, reset 'X' (like a typewriter), and add to 'Y'.
	x  =  0
	y += 20

# Character: ALWAYS in middle of window.
main_player = Player(window, WHITE, 200, 200, 25)

# BOARDERS: border[left, right, top, bottom]
main_border = []

left = Border(window, GRAY, 0, 0, 0, 400, 5)
main_border.append(left)

right = Border(window, GRAY, 400, 0, 400, 400, 5)
main_border.append(right)

top = Border(window, GRAY, 0, 0, 400, 0, 5)
main_border.append(top)

bottom = Border(window, GRAY, 0, 400, 400, 400, 5)
main_border.append(bottom)



# INITIALIZE, MINI PRIMARY MAP: 1/4 size of main map.

# Background Map
mini_background = []
x = y = 300 			# Starting point
sq = 5
for col in range(20): 	# 40 tiles per column.
	for row in range(20): 	# 40 tiles per row.

		# CREATE: Object
		b = Background(window, GRAY, x, y, sq, sq)
		mini_background.append(b)

		# UPDATE: (x, y)
		x += 5

	# After row is complete, reset 'X' (like a typewriter), and add to 'Y'.
	x  =  300
	y += 5

# Character: ALWAYS in middle of window.
mini_player = Player(window, WHITE, 350, 350, 6)

# BOARDERS: border[left, right, top, bottom]
mini_border = []

left = Border(window, GRAY, 300, 300, 300, 400, 2)
mini_border.append(left)

right = Border(window, GRAY, 400, 300, 400, 400, 2)
mini_border.append(right)

top = Border(window, GRAY, 300, 300, 400, 300, 2)
mini_border.append(top)

bottom = Border(window, GRAY, 300, 400, 400, 400, 2)
mini_border.append(bottom)



# MAIN LOOP
while run:


	# INITIALIZE
	clock.tick(FPS)
	keys = pygame.key.get_pressed()
	window.fill(BLACK)


	# FOR EACH EVENT...
	for event in pygame.event.get():

		# IF QUIT...
		if event.type == pygame.QUIT:

			pygame.quit()
			sys.exit()



	# MAIN BACKGROUND:

	# mini background does NOT move.
	# mini border do NOT move.


	# IF PLAYER IS WITHIN border...
	# ALL FOUR border must be independent.

	# Border Index - 0 = left, 1 = right, 2, = top, 3 = bottom

	# BOUNDARY: Left, using top border[2] as reference.
	if main_border[2].x1 < main_player.y - main_player.r:

		# MOVE: Left
		if keys[pygame.K_LEFT]:
			# MOVE: Background
			for i in range(len(main_background)):
				main_background[i].x += p_speed
				# mini_background[i]
			# MOVE: Border
			for i in range(len(main_border)):
				main_border[i].x1 += p_speed
				main_border[i].x2 += p_speed

			# Since, 1/4 size of main, Have a counter BEFORE moving, based on main_player.
			# ALSO, formula is based off 'p_speed' AND ratio (1/4).

			# MOVE: Mini-Player
			mini_player.x -= 1

	# BOUNDARY: Right, using top border[2] as reference.
	if main_player.y + main_player.r < main_border[2].x2:

		# MOVE: Right
		if keys[pygame.K_RIGHT]:
			# MOVE: Background
			for i in range(len(main_background)):
				main_background[i].x -= p_speed
			# MOVE: Border
			for i in range(len(main_border)):
				main_border[i].x1 -= p_speed
				main_border[i].x2 -= p_speed

			# MOVE: Mini-Player
			mini_player.x += 1

	# BOUNDARY: Top, using left border as reference.
	if main_border[0].y1 < main_player.y - main_player.r:

		# MOVE: Up
		if keys[pygame.K_UP]:
			# MOVE: Background
			for i in range(len(main_background)):
				main_background[i].y += p_speed
			# MOVE: Border
			for i in range(len(main_border)):
				main_border[i].y1 += p_speed
				main_border[i].y2 += p_speed


			# MOVE: Mini-Player
			mini_player.y -= 1

	# BOUNDARY: Bottom, using left border[0] as reference.
	if main_player.y + main_player.r < main_border[0].y2:

		# MOVE: Down
		if keys[pygame.K_DOWN]:
			# MOVE: Background
			for i in range(len(main_background)):
				main_background[i].y -= p_speed
			# MOVE: Border
			for i in range(len(main_border)):
				main_border[i].y1 -= p_speed
				main_border[i].y2 -= p_speed

			# MOVE: Mini-Player
			mini_player.y += 1



	# MAIN DRAW: Background
	for i in range(len(main_background)):
		main_background[i].draw()

	# MAIN DRAW: Border
	for i in range(len(main_border)):
		main_border[i].draw()

	# MAIN DRAW: Player
	main_player.draw()



	# MINI DRAW: Background
	pygame.draw.rect(window, BLACK, (300, 300, 100, 100)) 	# Solid background.
	for i in range(len(mini_background)):
		mini_background[i].draw()

	# MINI DRAW: Border
	for i in range(len(mini_border)):
		mini_border[i].draw()

	# MINI DRAW: Player
	mini_player.draw()



	# UPDATE
	pygame.display.update()
