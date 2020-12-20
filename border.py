# ---IMPORTS---
from turtle import Turtle
from constants import *


# ---CLASSES---
class Border(Turtle):
    def __init__(self):
        super(Border, self).__init__()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()

    def createBorder(self):
        x_pos = SCREEN_HEIGHT / 2 - SNAKE_SEGMENT_SIZE
        y_pos = SCREEN_WIDTH / 2 - SNAKE_SEGMENT_SIZE
        self.goto(x_pos, y_pos)
        self.pendown()
        self.goto(-x_pos, y_pos)
        self.goto(-x_pos, -y_pos)
        self.goto(x_pos, -y_pos)
        self.goto(x_pos, -y_pos)
        self.goto(x_pos, y_pos)
        self.penup()
