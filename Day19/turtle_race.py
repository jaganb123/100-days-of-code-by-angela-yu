from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
width = 1000
height = 1000
start_pos = (width / 2) * -1
end_pos = (width / 2)
screen.setup(width=width, height=height)
colors = ['red', "orange", "yellow", "green", "blue", "purple"]

turtles = []
y_coordinate = -75
for i in range(0, 6):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto((start_pos + 20), y_coordinate)
    y_coordinate += 30


def draw_finish_line(start_pos):
    draw = Turtle()
    draw.speed("slowest")
    draw.ht()
    draw.penup()
    draw.goto(start_pos, 90)
    draw.pendown()
    draw.goto(start_pos, -90)

draw_finish_line(start_pos + 40)
draw_finish_line(end_pos - 20)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color")


if user_bet:
    is_race_on = True


def turtle_move(turtle):
    turtle_distance = random.randint(0, 10)
    turtle.forward(turtle_distance)


finish_line = start_pos + 40
is_turned = False
while is_race_on:
    for i in range(0, 6):
        turtle_move(turtles[i])
        if turtles[i].xcor() >= (end_pos - 20):
            turtles[i].setheading(180)
            is_turned = True
        if turtles[i].xcor() < finish_line and is_turned:
            turtle_won = turtles[i].pencolor()
            is_race_on = False
            continue
if user_bet == turtle_won:
    print(f"You Won!!! {turtle_won} turtle reached the finish line first.")
else:
    print(f"Aah!!! {turtle_won} turtle reached the finish line first.")
screen.exitonclick()
