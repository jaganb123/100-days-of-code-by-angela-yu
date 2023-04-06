import turtle
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG")

turtle.listen()

turtle.tracer(0)
left_pad = Paddle((-350, 0))
right_pad = Paddle((350, 0))
ball = Ball()
score = ScoreBoard()
def exit_game():
    global is_game_on
    is_game_on = False

screen.onkeypress(left_pad.paddle_up, "w")
screen.onkeypress(left_pad.paddle_down, "s")
screen.onkeypress(right_pad.paddle_up, "Up")
screen.onkeypress(right_pad.paddle_down, "Down")
screen.onkey(exit_game, "q")

is_game_on = True
while is_game_on:
    turtle.update()
    time.sleep(ball.move_speed)
    ball.move()
    #collition with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouce_y()
    #collition with paddle
    if ball.distance(right_pad) < 50 and ball.xcor() >= 340 or ball.distance(left_pad) < 50 and ball.xcor() <= -340:
        ball.bounce_x()
    #if ball miss on right pad
    if ball.xcor() > 350:
        score.score_add_left()
        ball.reset_position()
    #if ball miss on left pad
    if ball.xcor() < -350 :
        score.score_add_right()
        ball.reset_position()



screen.exitonclick()