from turtle import Turtle, Screen


tor = Turtle()
screen = Screen()


def move_forward():
    tor.fd(10)


def move_backward():
    tor.bk(10)


def turn_left():
    tor.left(15)


def turn_right():
    tor.right(15)

def reset_turtle():
    tor.reset()

tor.shape("turtle")
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset_turtle)
screen.exitonclick()