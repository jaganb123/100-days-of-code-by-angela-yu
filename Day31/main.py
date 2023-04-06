from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"

#Pick random words from the data csv
try:
    data = pandas.read_csv("words_to_learn.csv")
    data_list = data.to_dict(orient="records")
    print(data_list)
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_list = data.to_dict(orient="records")
    print(data_list)

random_word_current = None
french_word = None
english_word = None


def random_word():
    global french_word
    global english_word
    global random_word_current
    random_word_current = random.choice(data_list)
    french_word = random_word_current.get("French")
    english_word = random_word_current.get("English")
random_word()


def change_flash_card():
    global after_1
    window.after_cancel(after_1)
    canvas.itemconfig(card_bg_canvas, image=card_back_image)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")
    after_1 = window.after(3000, reset_flash_card)


def reset_flash_card():
    global after_1
    window.after_cancel(after_1)
    random_word()
    canvas.itemconfig(card_bg_canvas, image=card_front_image)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=french_word, fill="black")
    after_1 = window.after(3000, change_flash_card)


def user_know():
    global after_1
    window.after_cancel(after_1)
    data_list.remove(random_word_current)
    data = pandas.DataFrame(data_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    print(random_word_current, len(data_list))
    reset_flash_card()


# def user_remembered():
#     index = 0
#     for i in data_list:
#         if i.get('French') == french_word:
#             data_list.pop(index)
#             print(data_list[index], len(data_list))
#         index += 1


#Creating UI
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash card - Learn french")

#Canvas
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_bg_canvas = canvas.create_image(400, 263, image=card_front_image)
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text=french_word, font=("Ariel", 40, "italic"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
right_button_image = PhotoImage(file="images/right.png")
right_button = Button(width=100, height=99,image=right_button_image, borderwidth=0, highlightthickness=0, command=user_know)
right_button.grid(row=1, column=1)
left_button_image = PhotoImage(file="images/wrong.png")
left_button = Button(width=100, height=99, image=left_button_image, borderwidth=0, highlightthickness=0, command=reset_flash_card)
left_button.grid(row=1, column=0)

after_1 = window.after(3000, change_flash_card)

window.mainloop()