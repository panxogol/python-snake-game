# ---IMPORTS---
from turtle import Turtle

# ---CONSTANTS---
# SNAKE CONFIG
SNAKE_COLOR = "white"
SNAKE_INITIAL_SIZE = 5
SNAKE_SPEED = "fastest"
SNAKE_SHAPE = "square"
SNAKE_SEGMENT_SIZE = 20

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

    def create_tail(self):
        """
        Create the initial snake body
        """
        for turtle_index in range(self.initial_size):
            new_turtle = Turtle(shape=self.shape)
            new_turtle.penup()
            new_turtle.goto(new_turtle.xcor() - turtle_index * self.segment_size, new_turtle.ycor())
            new_turtle.color(self.color)
            new_turtle.speed(self.speed)
            self.tail.append(new_turtle)

    def move(self):
        for segment in self.tail[::-1]:
            current_index = self.tail.index(segment)
            if current_index == 0:
                segment.forward(self.segment_size)
            else:
                segment.goto(self.tail[current_index - 1].pos())

    def up(self):
        if self.tail[0].heading() not in [90, 270]:
            self.head.setheading(UP)

    def down(self):
        if self.tail[0].heading() not in [90, 270]:
            self.head.setheading(DOWN)

    def left(self):
        if self.tail[0].heading() not in [0, 180]:
            self.head.setheading(LEFT)

    def right(self):
        if self.tail[0].heading() not in [0, 180]:
            self.head.setheading(RIGHT)
