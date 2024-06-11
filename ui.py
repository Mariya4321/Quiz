from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score = Label(text="score = 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self.q_text = self.canvas.create_text(150, 125, width=250, text="something", fill=THEME_COLOR,
                                              font=("Ariel", 15, "italic"))

        self.right_img = PhotoImage(file="images/true.png")
        self.true = Button(image=self.right_img, highlightthickness=0, bd=0, command=self.true_pressed)
        self.true.grid(column=0, row=2)

        self.wrong_img = PhotoImage(file="images/false.png")
        self.false = Button(image=self.wrong_img, highlightthickness=0, bd=0, command=self.false_pressed)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=question)
        else:
            self.canvas.itemconfig(self.q_text, text="you've reached the end of quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
