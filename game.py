import pygame as pg

import board, input_handler, score, sound_player

class Game:
	def __init__(self):
		pg.init()

		self.done = False
		self.end_game = True

		self.board = board.Board(11,11)
		self.input_handler = input_handler.InputHandler()
		self.sound_player = sound_player.SoundPlayer()
		self.score = score.Score(self.board)

		self.caption = "Snake"
		self.screen_size = (800,800)
		self.screen = pg.display.set_mode(self.screen_size)
		self.clock = pg.time.Clock()

	def main(self):
		pg.display.set_caption(self.caption)


		count = 0
		while not self.done:
			self.input()

			if count == self.score.speed:
				if not self.update():
					self.sound_player.death()
					self.done = True

				self.draw()
				self.input_handler.most_recent = None
				count = 0

			count += 1
			self.clock.tick(60)

		while self.end_game:
			self.input()

			if self.input_handler.enter:
				self.end_game = False

		pg.quit()

	def input(self):
		self.input_handler.input()

	def update(self):
		dead, eat = self.board.update(self.input_handler, self.score, self.sound_player)

		if eat:
			self.score.update()
			self.sound_player.eat()

		return dead

	def draw(self):
		self.screen.fill(pg.Color("white"))

		self.board.draw(self.screen)
		self.score.draw(self.screen)


		pg.display.flip()

