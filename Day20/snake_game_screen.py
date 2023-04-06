from turtle import  Screen
from snake import Snake
from food import Food
from score import Score
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# snake_position = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
snake = Snake()
score = Score()
food = Food()


def exit_game():
    global is_game_on
    is_game_on = False

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(exit_game, "q")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    snake.move()
    screen.update()

    #detect collision with food
    if snake.head.distance(food) < 15 :
        score.add_score()
        food.refresh()
        snake.snake_grow()

    #detect collition with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        score.reset1()
        snake.reset_snake()

    #detect collition with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 1:
            score.reset1()
            snake.reset_snake()
screen.exitonclick()