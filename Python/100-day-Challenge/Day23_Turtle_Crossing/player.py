from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.player_level = 1

    def up(self):
        self.forward(MOVE_DISTANCE)

    # Detect the top edge
    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    # Go to the original
    def go_to_start(self):
        self.goto(STARTING_POSITION)
        self.player_level += 1



