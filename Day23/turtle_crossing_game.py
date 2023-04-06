from turtle import Screen
import time
from my_turtle import MyTurtle
import random
from cars import Cars
from score import ScoreBoard



#setup turtle screen
screen = Screen()
screen.tracer(0)
screen.title("TURTLE RACING")
screen.bgcolor("white")
screen.setup(width=600, height=600)

#initialize game objects
tom = MyTurtle()
cars = Cars()
score = ScoreBoard()

#exit game function
def exit_game():
    global is_game_on
    is_game_on = False

#key presses and actions
screen.listen()
screen.onkey(exit_game, "q")
screen.onkeypress(tom.move, "w")



is_game_on = True
while is_game_on:
    time.sleep(cars.car_speed)
    screen.update()
    if len(cars.car_list) < 20:
        cars.span_car()
    for i in cars.car_list:
        i.fd(10)
        if tom.distance(i) < 25:
            is_game_on = False
            score.game_over()
        if i.xcor() < -320:
            index = cars.car_list.index(i)
            cars.car_list.pop(index)
    if tom.ycor() > 250:
        score.score_add()
        cars.car_speed *= 0.9
        tom.goto((0, -260))

screen.exitonclick()