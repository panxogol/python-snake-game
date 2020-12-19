# ---IMPORTS---
from turtle import Turtle
from random import choice
from constants import *

# ---CONSTANTS---


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.width(FOOD_SIZE)
        self.color(FOOD_COLOR)
        self.speed(FOOD_SPEED)
        self.penup()
        self.refresh()

    def refresh(self):
        max_x = int(SCREEN_WIDTH / 2 - self.width() - self.width() / 2)
        max_y = int(SCREEN_HEIGHT / 2 - self.width() - self.width() / 2)
        positions_x = range(-max_x, max_x + 1, self.width())
        positions_y = range(-max_y, max_y + 1, self.width())
        random_x = choice(positions_x)
        random_y = choice(positions_y)
        self.goto(random_x, random_y)
