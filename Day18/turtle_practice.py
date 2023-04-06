import turtle as t
import random

t.colormode(255)

pet = t.Turtle()
pet.shape("turtle")
pet.color("forest green")

# for _ in range(4):
#     pet.rt(90)
#     pet.forward(100)

# for i in range(30):
#     if pet.isdown():
#         pet.penup()
#         pet.forward(10)
#     else:
#         pet.pendown()
#         pet.forward(10)
def draw(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        pet.forward(100)
        pet.right(angle)

def random_walk(distance):
    pet.color(random_color())
    angle = random.choice([0, 90, 180, 270])
    pet.forward(distance)
    pet.setheading(angle)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

#colors = ["blue", "red", "yellow", "lime green", "dark slate gray", "maroon", "orange"]
#pet.pensize(10)
pet.speed(0)
#for _ in range(200):
#    random_walk(30)

# for i in range(3, 20):
#     pet.color(random.choice(colors))
#     draw(i)

def draw_spirograph(numbers):
    step_angle = 360 / numbers
    current_angle = 0
    for i in range(numbers):
        pet.color(random_color())
        pet.circle(100)
        current_angle += step_angle
        pet.setheading(current_angle)


draw_spirograph(200)

screen = t.Screen()
screen.exitonclick()