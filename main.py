# ---IMPORTS---
from turtle import Screen
from scoreboard import Scoreboard
from time import sleep
from snake import Snake
from food import Food
from constants import *
from border import Border

# ---GLOBAL---
paused = False


# ---FUNCTIONS---
def main():
    # TODO 1: Configure screen
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_BACKGROUND_COLOR)
    screen.tracer(0)

    # Add borders
    border = Border()
    border.createBorder()

    # TODO 2: Configure initial snake
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # TODO 3: Move the snake
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    #global paused

    #def unpause():
    #    global paused
    #    paused = not paused

    #screen.onkey(unpause, "p")

    game_is_on = True
    while game_is_on:
        #while paused:
        #    sleep(0.2)
        screen.update()
        sleep(SLEEP_TIME)
        snake.move()

        # TODO 4: Detect collision with food
        snake_food_collision_distance = (food.width() + snake.head.width()) / 2 - COLLISION_ERROR
        if snake.head.distance(food) < snake_food_collision_distance:
            scoreboard.score += 1
            snake.add_segment()
            food.refresh()
            for segment in snake.tail:
                while segment.position() == food.position():
                    food.clear()
                    food.refresh()
            scoreboard.refresh()

        # TODO 5: Detect collision with walls
        pass_x_wall = (snake.head.xcor() < -SCREEN_WIDTH / 2 + snake.head.width()
                       or
                       snake.head.xcor() > SCREEN_WIDTH / 2 - snake.head.width())
        pass_y_wall = (snake.head.ycor() < -SCREEN_HEIGHT / 2 + snake.head.width()
                       or
                       snake.head.ycor() > SCREEN_HEIGHT / 2 - snake.head.width())
        wall_collision = pass_x_wall or pass_y_wall
        if wall_collision:
            scoreboard.resetHighestScore()
            snake.resetSnake()

        # TODO 6: Detect collision with tail
        tail_head_collision_distance = snake.head.width() - COLLISION_ERROR
        for segment in snake.tail[1:]:
            if segment.distance(snake.head) < tail_head_collision_distance:
                scoreboard.resetHighestScore()
                snake.resetSnake()

    screen.exitonclick()


# ---RUN---
if __name__ == "__main__":
    main()
