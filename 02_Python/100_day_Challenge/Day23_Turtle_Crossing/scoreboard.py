from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_level = 1
        self.goto(-200, 250)
        self.write(f"Level:  {self.player_level}", align="Center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="Center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level:  {self.player_level}", align="Center", font=FONT)

    def increase_score(self):
        self.player_level += 1
        self.update_scoreboard()
