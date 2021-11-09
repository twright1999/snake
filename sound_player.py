import pygame as pg
import random
from os import walk

class SoundPlayer:
	def __init__(self):
		eat_file_names = next(walk('sounds/eat'), (None, None, []))[2]
		death_file_names = next(walk('sounds/death'), (None, None, []))[2]
		move_file_names = next(walk('sounds/move'), (None, None, []))[2]

		self.eat_sound_files = list(map(lambda x: pg.mixer.Sound('sounds/eat/'+x), eat_file_names))
		self.death_sound_files = list(map(lambda x: pg.mixer.Sound('sounds/death/'+x), death_file_names))
		self.move_sound_files = list(map(lambda x: pg.mixer.Sound('sounds/move/'+x), move_file_names))

	def eat(self):
		sound_index = random.randint(0,len(self.eat_sound_files)-1)

		pg.mixer.Sound.play(self.eat_sound_files[sound_index])

	def death(self):
		sound_index = random.randint(0,len(self.death_sound_files)-1)

		pg.mixer.Sound.play(self.death_sound_files[sound_index])

	def move(self, direction):
		if direction == "LEFT":
			pg.mixer.Sound.play(self.move_sound_files[0])
		if direction == "RIGHT":
			pg.mixer.Sound.play(self.move_sound_files[1])
		if direction == "UP":
			pg.mixer.Sound.play(self.move_sound_files[2])
		if direction == "DOWN":
			pg.mixer.Sound.play(self.move_sound_files[3])