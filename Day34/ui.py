from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = Label(text=f"score : {0}", background=THEME_COLOR)
        self.score.grid(row=0, column=1)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0, borderwidth=0, command=self.answered_true)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, borderwidth=0, command=self.answered_false)
        self.false_button.grid(row=2, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, background="white")
        self.canvas_text = self.canvas.create_text(150, 125, text="Quote here", fill="black",
                                                   font=('Aerial', 20, 'italic'), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.display_question()

        self.window.mainloop()

    def display_question(self):
        self.canvas.config(background="white")
        self.score.config(text=f"score : {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"You have reached end of the quiz, "
                                                          f"Your score is {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answered_true(self):
        self.give_feedback(self.quiz.check_answer('True'))
        # self.score.config(text=f"score : {score}")

    def answered_false(self):
        self.give_feedback(self.quiz.check_answer('False'))
        # self.score.config(text=f"score : {score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
            self.window.after(1000, self.display_question)
        else:
            self.canvas.config(background="red")
            self.window.after(1000, self.display_question)