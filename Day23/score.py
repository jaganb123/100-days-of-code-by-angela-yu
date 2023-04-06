from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 260)
        self.write(f"LEVEL: {self.score}", align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Courier", 15, "normal"))

    def score_add(self):
        self.score += 1
        self.update_scoreboard()