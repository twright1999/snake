import pygame as pg
import sys

class InputHandler:
	def __init__(self):
		self.left = False
		self.right = False
		self.up = False
		self.down = False
		self.enter = False

		self.presses = []

		self.most_recent = None

	def input(self):
		for event in pg.event.get():

			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_LEFT:
					self.presses.append("LEFT")
					self.most_recent = "LEFT"
					self.left = True
				if event.key == pg.K_RIGHT:
					self.presses.append("RIGHT")
					self.most_recent = "RIGHT"
					self.right = True
				if event.key == pg.K_UP:
					self.presses.append("UP")
					self.most_recent = "UP"
					self.up = True
				if event.key == pg.K_DOWN:
					self.presses.append("DOWN")
					self.most_recent = "DOWN"
					self.down = True
				if event.key == pg.K_RETURN:
					self.enter = True

			if event.type == pg.KEYUP:
				if event.key == pg.K_LEFT:
					self.presses.remove("LEFT")
					self.left = False
				if event.key == pg.K_RIGHT:
					self.presses.remove("RIGHT")
					self.right = False
				if event.key == pg.K_UP:
					self.presses.remove("UP")
					self.up = False
				if event.key == pg.K_DOWN:
					self.presses.remove("DOWN")
					self.down = False
