from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 275)
        self.replace_score()

    def replace_score(self):
        self.write(f"Scoreboard: {self.score}", font=("Time New Roman", 15), align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Time New Roman", 15))

    def score_up(self):
        self.score += 1
        self.clear()
        self.replace_score()
