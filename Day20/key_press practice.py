from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
#tim.hideturtle()
tim.write("Hello Turtle", False , align="center", font=('Arial',16, 'normal'))

screen.exitonclick()

#
# def up():
#     tim.setheading(90)
#
#
# def down():
#     tim.setheading(270)
#
# tim = Turtle(shape="turtle")
# screen = Screen()
#
# screen.listen()
# screen.onkey(up, "Up")
# screen.onkey(down, "Down")
#
#
#
# screen.exitonclick()

# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, Exhale")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def move(self):
#         print("I am moving")
#
#     def breathe(self):
#         super().breathe()
#         print("I am under water")
#
#
# fish = Fish()
# fish.move()
# fish.breathe()


