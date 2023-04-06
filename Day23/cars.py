from turtle import Turtle
from random import randrange, choice
COLORS = [ "blue", "midnight blue", "sienna", "orange", "lime green", "slate gray", "dark cyan", "sea green"]
CAR_STARTING_X = 320
CAR_SPEED = 0.1
#START Y range -220 to 220


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.car_list = []
        self.car_speed = CAR_SPEED
        self.starting_cars()

    def span_car(self, x_pos=CAR_STARTING_X):
        self.car_list.append(Turtle(shape="square"))
        self.car_list[-1].penup()
        self.car_list[-1].shape("square")
        self.car_list[-1].shapesize(stretch_len=2, stretch_wid=1)
        self.car_list[-1].setheading(180)
        self.car_list[-1].color(choice(COLORS))
        y_pos = randrange(-210, 210, 30)
        for i in self.car_list:
            diff = x_pos - i.xcor()
            if diff <= 20:
                x_pos += 80

        self.car_list[-1].goto(x_pos, y_pos)

    def starting_cars(self):
        for i in range(20):
            x_position = randrange(-210, 210, 20)
            self.span_car(x_position)

