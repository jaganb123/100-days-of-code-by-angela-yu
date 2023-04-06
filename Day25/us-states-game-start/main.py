from turtle import Turtle, Screen
import turtle
import pandas

screen = Screen()

image = "blank_states_img.gif"
turtle.addshape(image)
img = Turtle(shape=image)

state_write = Turtle()
state_write.ht()
state_write.penup()
state_write.speed("fast")

def write_screen(letter, x_axis, y_axis):
    state_write.goto(x_axis, y_axis)
    state_write.write(arg=letter, align="center", font=("Aerial", 8, "normal"))


data = pandas.read_csv("50_states.csv")
all_states_list = data.state.to_list()
is_game_on = True
user_score = 0
guessed_state = []
while len(guessed_state) < 50:
    user_answer = screen.textinput(title=f"score: {user_score}/50 Enter an US State", prompt="Choose another state").title()
    if user_answer == "Exit":
        need_to_learn = [state for state in all_states_list if state not in guessed_state]
        dt = pandas.DataFrame(need_to_learn)
        dt.to_csv("Learn_these_states.csv")
        screen.exitonclick()
        break
    if user_answer in all_states_list:
        row = data[data.state == user_answer]
        x_axis = float(row["x"])
        y_axis = float(row["y"])
        print(row)
        write_screen(user_answer, x_axis, y_axis)
        user_score += 1
        guessed_state.append(user_answer)


screen.mainloop()