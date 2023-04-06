from turtle import Turtle
ALIGN = "center"
FONT = ("Aerial", 16, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.high_score_get())
        self.init_score()

    def init_score(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write(f"Current score : {self.score}   High score : {self.high_score}", move=False, align=ALIGN, font=FONT)

    def high_score_get(self):
        with open("/Users/jegan.babu/Downloads/PyCharm projects/Hundred_Days_of_Code/Day20/high_score.txt", mode="r") as score:
            return score.read()

    def high_score_update(self):
        with open("/Users/jegan.babu/Downloads/PyCharm projects/Hundred_Days_of_Code/Day20/high_score.txt", mode="w") as score:
            value = str(self.high_score)
            score.write(value)

    def scored(self):
        self.clear()
        self.write(f"Current score : {self.score}   High score : {self.high_score}", move=False, align=ALIGN, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", move=False, align=ALIGN, font=FONT)
    def add_score(self):
        self.score += 1
        self.scored()

    def reset1(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.scored()
        self.high_score_update()