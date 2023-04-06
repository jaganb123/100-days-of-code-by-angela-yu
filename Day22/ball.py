from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        speed = ( 100 / 25 )
        self.refresh_rate = (1 / 25)
        self.x_move = speed
        self.y_move = speed
        self.move_speed = self.refresh_rate

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def bouce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = self.refresh_rate
        self.bounce_x()

