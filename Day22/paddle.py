from turtle import Turtle

MOVE_SPEED = 20

class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.location = location
        self.paddle_init()

    def paddle_init(self):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.location)

    def paddle_up(self):
        y = self.ycor() + MOVE_SPEED
        self.sety(y)

    def paddle_down(self):
        y = self.ycor() - MOVE_SPEED
        self.sety(y)
