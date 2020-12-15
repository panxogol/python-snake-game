# ---IMPORTS---
from turtle import Turtle, Screen
from time import sleep
from snake import Snake

# ---CONSTANTS---
# SCREEN CONFIG
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_BACKGROUND_COLOR = "black"
SLEEP_TIME = 0.1

# TODO 1: Configure screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BACKGROUND_COLOR)
screen.tracer(0)

# TODO 2: Configure initial snake
snake = Snake()

# TODO 3: Move the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    sleep(SLEEP_TIME)
    snake.move()



# Stop the screen from exit
screen.exitonclick()
