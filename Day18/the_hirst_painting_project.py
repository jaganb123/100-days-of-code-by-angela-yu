import random

import colorgram
from turtle import Turtle, Screen
import turtle as tr

tr.colormode(255)
pet = Turtle()
# extracted = colorgram.extract('damien-hirst-lactulose.webp', 30)
# color_list = []
# for i in extracted:
#     rgb_color = i.rgb
#     color_list.append(rgb_color)
#     print(rgb_color.Rgb)
# print(color_list)
# def convert_colors(colorgram_object):
#     color_list = []
#     for color in colorgram_object:
#         this_color = color.rgb
#         color_list.append((this_color.r, this_color.g, this_color.b))
#     return color_list
#
# print(convert_colors(extracted))
color_list = [(26, 109, 164), (194, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (222, 137, 176), (143, 109, 57), (101, 197, 219), (206, 166, 29), (21, 58, 132), (212, 75, 91), (238, 89, 49), (141, 208, 227), (119, 192, 141), (6, 160, 87), (4, 186, 179), (106, 108, 198), (136, 29, 72), (98, 51, 37), (25, 153, 211), (228, 168, 188), (153, 213, 195), (173, 186, 221), (234, 174, 162), (30, 91, 95), (87, 47, 34), (34, 46, 84)]

pet.speed("fastest")
def draw_circle():
    size = 20
    pet.dot(size, random.choice(color_list))


def vertical_dots():
    current_pos = pet.position()
    current_pos_y = current_pos[1]
    for _ in range(10):
        horizontal_dots()
        current_pos_y += 50
        pet.setx(-300)
        pet.sety(current_pos_y)


def horizontal_dots():
    current_pos = pet.position()
    current_pos_x = current_pos[0]
    for _ in range(10):
        draw_circle()
        current_pos_x += 50
        pet.setx((current_pos_x))


def set_initial_position():
    pet.penup()
    pet.hideturtle()
    x_position = -300
    y_position = -300
    pet.setx(x_position)
    pet.sety(y_position)
    vertical_dots()


set_initial_position()
screen = Screen()
screen.exitonclick()