# ---IMPORTS---
from turtle import Turtle
from constants import *


# ---FUNCTIONS---
def getHighestScore():
    with open(file="data.txt", mode="r") as file:
        highest_score = int(file.read())
    return highest_score


# ---CLASSES---
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(SCOREBOARD_SPEED)
        self.penup()
        self.hideturtle()
        self.score = 0
        self.highest_score = getHighestScore()
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(SCOREBOARD_X_POSITION, SCOREBOARD_Y_POSITION)
        self.color(SCOREBOARD_TEXT_COLOR)
        text_arg = f"Score: {self.score} Highest Score: {self.highest_score}"
        self.write(arg=text_arg, move=True,
                   align=SCOREBOARD_TEXT_ALIGN, font=SCOREBOARD_TEXT_TUPLE)

    def endgame(self):
        self.home()
        self.write(arg=SCOREBOARD_GAME_OVER_TEXT, move=True,
                   align=SCOREBOARD_TEXT_ALIGN, font=SCOREBOARD_GAME_OVER_TEXT_TUPLE)

    def resetHighestScore(self):
        if self.score > self.highest_score:
            with open(file="data.txt", mode="w") as file:
                file.write(str(self.score))
        self.highest_score = getHighestScore()
        self.score = 0
        self.refresh()
