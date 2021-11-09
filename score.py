import pygame as pg
import math

class Score:
	def __init__(self,board):
		self.text_size = board.cell_size
		self.x_pos = board.x_pos + board.cell_size*board.width + 25
		self.y_pos = board.y_pos + board.cell_size
		self.points = 0
		self.max_points = board.width*board.height - 3

		self.speed = 10
		self.max_speed = 100

	def update(self):
		self.points += 1

	def draw(self,screen):
		font = pg.font.Font('freesansbold.ttf',self.text_size)

		string = "score: " + str(self.points)
		textsurface = font.render(string, False, (0, 0, 0))
		screen.blit(textsurface,(self.x_pos,self.y_pos))