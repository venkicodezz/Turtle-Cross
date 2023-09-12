from turtle import Turtle

FONT = ("Times New Roman", 22, "bold")
FONT2 = ("Times New Roman", 23, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-230, 255)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level}", align="Center", font=FONT)

    def update_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.hideturtle()
        self.write(f"GAME OVER!", align="Center", font=FONT2)
