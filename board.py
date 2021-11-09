import numpy as np
import pygame as pg
import random
import math

class Board:
	def __init__(self, w, h):
		self.x_pos = 0
		self.y_pos = 0
		self.width = w
		self.height = h
		self.cell_size = 50

		self.snake = [[int(self.height/2),int(self.width/2)]]*3
		self.board = np.zeros((self.height,self.width))
		self.board[int(self.height/2),int(self.width/2)] = 1

		self.facing = "LEFT"

		self.generate_fruit()

	def draw(self, screen):
		for x in range(self.width):
			for y in range(self.height):
				pg.draw.rect(screen, pg.Color("gray"), (self.x_pos+(self.cell_size*x),
					self.y_pos+(self.cell_size*y),self.cell_size,self.cell_size), 1)

				cell_color = None

				if self.board[y,x] == 1:
					cell_color = pg.Color("green")

				if self.board[y,x] == 2:
					cell_color = pg.Color("red")

				if cell_color != None:
					pg.draw.rect(screen, cell_color, (self.x_pos+(self.cell_size*x),
					self.y_pos+(self.cell_size*y),self.cell_size,self.cell_size))


					# white, white, black, black
					eye_coords = [(0,0), (0,0), (0,0), (0,0)]

					if [y,x] == self.snake[0]:
						if self.facing == "LEFT" or self.facing == "RIGHT":
							eye_coords[0] = (self.x_pos+(self.cell_size*x)+(self.cell_size/2),
											self.y_pos+(self.cell_size*y)+(self.cell_size/5))

							eye_coords[1] = (self.x_pos+(self.cell_size*x)+(self.cell_size/2),
											self.y_pos+(self.cell_size*y)+(self.cell_size*4/5))

							if self.facing == "LEFT":
								eye_coords[2] = (self.x_pos+(self.cell_size*x)+(self.cell_size/2)-self.cell_size/10,
												self.y_pos+(self.cell_size*y)+(self.cell_size/5))

								eye_coords[3] = (self.x_pos+(self.cell_size*x)+(self.cell_size/2)-self.cell_size/10,
												self.y_pos+(self.cell_size*y)+(self.cell_size*4/5))
							else:
								eye_coords[2] = (self.x_pos+(self.cell_size*x)+(self.cell_size/2)+self.cell_size/10,
												self.y_pos+(self.cell_size*y)+(self.cell_size/5))

								eye_coords[3] = (self.x_pos+(self.cell_size*x)+(self.cell_size/2)+self.cell_size/10,
												self.y_pos+(self.cell_size*y)+(self.cell_size*4/5))

						else:
							eye_coords[0] = (self.x_pos+(self.cell_size*x)+(self.cell_size/5),
											self.y_pos+(self.cell_size*y)+(self.cell_size/2))

							eye_coords[1] = (self.x_pos+(self.cell_size*x)+(self.cell_size*4/5),
											self.y_pos+(self.cell_size*y)+(self.cell_size/2))

							if self.facing == "UP":
								eye_coords[2] = (self.x_pos+(self.cell_size*x)+(self.cell_size/5),
												self.y_pos+(self.cell_size*y)+(self.cell_size/2)-self.cell_size/10)

								eye_coords[3] = (self.x_pos+(self.cell_size*x)+(self.cell_size*4/5),
												self.y_pos+(self.cell_size*y)+(self.cell_size/2)-self.cell_size/10)
							else:
								eye_coords[2] = (self.x_pos+(self.cell_size*x)+(self.cell_size/5),
												self.y_pos+(self.cell_size*y)+(self.cell_size/2)+self.cell_size/10)

								eye_coords[3] = (self.x_pos+(self.cell_size*x)+(self.cell_size*4/5),
												self.y_pos+(self.cell_size*y)+(self.cell_size/2)+self.cell_size/10)


						pg.draw.circle(screen, pg.Color("white"),eye_coords[0],self.cell_size/5)
						pg.draw.circle(screen, pg.Color("white"),eye_coords[1],self.cell_size/5)
						pg.draw.circle(screen, pg.Color("black"),eye_coords[2],self.cell_size/10)
						pg.draw.circle(screen, pg.Color("black"),eye_coords[3],self.cell_size/10)


	def update(self, input, score, sound):
		current_direction = self.facing

		if input.left or input.right or input.up or input.down:
			if not self.new_facing_backwards(input.presses[-1]):
				self.facing = input.presses[-1]
				if self.facing != current_direction:
					sound.move(input.presses[-1])

		elif input.most_recent != None:
			if not self.new_facing_backwards(input.most_recent):
				self.facing = input.most_recent
				if self.facing != current_direction:
					sound.move(input.most_recent)

		next_coord = self.snake[0].copy()

		if self.facing == "LEFT":
			next_coord[1] -= 1
		elif self.facing == "RIGHT":
			next_coord[1] += 1
		elif self.facing == "UP":
			next_coord[0] -= 1
		elif self.facing == "DOWN":
			next_coord[0] += 1

		next_coord[0] = next_coord[0] % self.height
		next_coord[1] = next_coord[1] % self.width

		eat = False

		if self.board[next_coord[0],next_coord[1]] == 1:	# snake	
			if next_coord == self.snake[-1]:
				self.board[self.snake[-1][0],self.snake[-1][1]] = 0
			else:
				return False, eat

		elif self.board[next_coord[0],next_coord[1]] == 2:
			self.snake.append([self.snake[-1][0],self.snake[-1][1]])
			self.generate_fruit()

			eat = True

		else:
			self.board[self.snake[-1][0],self.snake[-1][1]] = 0

		for s in range(len(self.snake)-1,0,-1):
			self.snake[s] = self.snake[s-1].copy()

		self.board[next_coord[0],next_coord[1]] = 1

		self.snake[0] = next_coord

		return True, eat

	def new_facing_backwards(self, new_facing):
		new_left = self.facing == "RIGHT" and new_facing == "LEFT"
		new_right = self.facing == "LEFT" and new_facing == "RIGHT"
		new_up = self.facing == "DOWN" and new_facing == "UP"
		new_down = self.facing == "UP" and new_facing == "DOWN"

		if new_left or new_right or new_up or new_down:
			return True
		else:
			return False

	def generate_fruit(self):
		flat = self.board.copy().ravel()
		free_indices = []

		for i in range(len(flat)):
			if flat[i] == 0.0:
				free_indices.append(i)

		random_index = free_indices[random.randint(0,len(free_indices)-1)]

		x_index = random_index % self.width
		y_index = math.floor(random_index/self.width)

		self.board[y_index,x_index] = 2
