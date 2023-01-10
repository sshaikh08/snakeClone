from random import randint
from tkinter import Canvas
from game_window.canvas_constants import GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE

COLOR = '#FF36E9'
TAG = 'food'


class Food:
    def __init__(self, canvas):
        x = randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = randint(0, (GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]
        self.canvas = canvas

        self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=COLOR, tag=TAG)
