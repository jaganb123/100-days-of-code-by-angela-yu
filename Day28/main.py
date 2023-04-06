from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✓"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    timer_lable.config(text="Timer")
    checkmark_lable.config(text="")
    canvas.itemconfig(canvas_text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    reps += 1
    if reps > 8:
        pass
    elif reps == 8:
        timer_lable.config(text="Break", fg=RED)
        count_down(long_break_seconds)
    elif reps % 2:
        timer_lable.config(text="Work", fg=GREEN)
        count_down(work_seconds)
    else:
        timer_lable.config(text="Break", fg=PINK)
        count_down(short_break_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minutes = math.floor( count / 60 )
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(canvas_text, text=f"{minutes}:{seconds}")
    if count > 0 :
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()
        check_mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            check_mark += "✓"
        checkmark_lable.config(text=f"{check_mark}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
#Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

#Button
start_button = Button(text="Start", font=(FONT_NAME, 16, "bold"), highlightthickness=0, borderwidth=0, command=start_count)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", font=(FONT_NAME, 16, "bold"), highlightthickness=0, borderwidth=0, command=timer_reset)
reset_button.grid(row=2, column=2)

#Lable
timer_lable = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW, pady=10)
timer_lable.grid(row=0, column=1)
checkmark_lable = Label(font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
checkmark_lable.grid(row=3, column=1)


window.mainloop()
