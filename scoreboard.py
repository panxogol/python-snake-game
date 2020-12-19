# ---IMPORTS---
from turtle import Turtle
from constants import *


# ---CLASSES---
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(SCOREBOARD_SPEED)
        self.penup()
        self.hideturtle()
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(SCOREBOARD_X_POSITION, SCOREBOARD_Y_POSITION)
        self.color(SCOREBOARD_TEXT_COLOR)
        text_arg = f"{SCOREBOARD_TEXT_ARG}{self.score}"
        self.write(arg=text_arg, move=True,
                   align=SCOREBOARD_TEXT_ALIGN, font=SCOREBOARD_TEXT_TUPLE)

    def endgame(self):
        self.home()
        self.write(arg=SCOREBOARD_GAME_OVER_TEXT, move=True,
                   align=SCOREBOARD_TEXT_ALIGN, font=SCOREBOARD_GAME_OVER_TEXT_TUPLE)
