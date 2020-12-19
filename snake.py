# ---IMPORTS---
from turtle import Turtle
from constants import *

# ---CONSTANTS---
# DIRECTIONS
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# ---CLASSES---
class Snake:
    def __init__(self, color=SNAKE_COLOR, init_size=SNAKE_INITIAL_SIZE, shape=SNAKE_SHAPE,
                 speed=SNAKE_SPEED, segment_size=SNAKE_SEGMENT_SIZE):
        self.tail = []
        self.color = color
        self.initial_size = init_size
        self.speed = speed
        self.shape = shape
        self.segment_size = segment_size
        self.create_tail()
        self.head = self.tail[0]
        self.moved = True

    def create_tail(self):
        """
        Create the initial snake body
        """
        for turtle_index in range(self.initial_size):
            x_pos = -turtle_index * self.segment_size - self.segment_size / 2
            y_pos = -self.segment_size / 2
            self.add_segment(x_pos, y_pos)

    def add_segment(self, x_position=None, y_position=None):
        if x_position is None:
            x_position = self.tail[-1].xcor()
        if y_position is None:
            y_position = self.tail[-1].ycor()
        new_turtle = Turtle(shape=self.shape)
        new_turtle.penup()
        new_turtle.goto(x_position, y_position)
        new_turtle.color(self.color)
        new_turtle.speed(self.speed)
        new_turtle.width(self.segment_size)
        self.tail.append(new_turtle)

    def move(self):
        for segment in self.tail[::-1]:
            current_index = self.tail.index(segment)
            if current_index == 0:
                segment.forward(self.segment_size)
                self.moved = True
            else:
                segment.goto(self.tail[current_index - 1].pos())

    def up(self):
        if self.tail[0].heading() not in [90, 270] and self.moved:
            self.head.setheading(UP)
            self.moved = False

    def down(self):
        if self.tail[0].heading() not in [90, 270] and self.moved:
            self.head.setheading(DOWN)
            self.moved = False

    def left(self):
        if self.tail[0].heading() not in [0, 180] and self.moved:
            self.head.setheading(LEFT)
            self.moved = False

    def right(self):
        if self.tail[0].heading() not in [0, 180] and self.moved:
            self.head.setheading(RIGHT)
            self.moved = False
