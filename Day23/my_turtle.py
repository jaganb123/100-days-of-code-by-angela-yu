from turtle import Turtle
MOVE_SPEED = 10
START_POSITION = (0, -260)
BORDER_BOTTOM = -250
BORDER_TOP = 250


def start_end_lines():
    line_runner = Turtle()
    line_runner.ht()
    draw_line(line_runner, BORDER_BOTTOM, "red")
    draw_line(line_runner, BORDER_TOP, "green")


def draw_line(drawer, y_position, color):
    drawer.penup()
    drawer.color(color)
    drawer.pensize(5)
    drawer.goto(-100, y_position)
    drawer.pendown()
    drawer.goto(100, y_position)
    drawer.penup()


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()
        start_end_lines()

    def create_turtle(self):
        self.speed(0)
        self.penup()
        self.shape("turtle")
        self.color("blue")
        self.setheading(90)
        self.goto(START_POSITION)

    def move(self):
        self.forward(10)
