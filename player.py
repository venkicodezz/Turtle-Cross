from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("cornflower blue")
        self.penup()
        self.reset()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)

    def player_is_reached(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def move_side_left(self):
        new_Y = 10
        self.goto(self.xcor(), new_Y)
