from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Trivial Quiz")

        self.window.config(width=400, height=600, padx=20, pady=20, bg=THEME_COLOR)
        self.txt_score = Label(text="Score: 0", fg="white", font=("Arial", 18, "normal"), bg=THEME_COLOR, highlightthickness=0,  padx=20, pady=20)
        self.txt_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.txt_question = self.canvas.create_text(150, 125, text="The question", fill=THEME_COLOR, font=("Arial", 18, "normal"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        btn_img_true = PhotoImage(file="images/true.png")
        self.btn_true = Button(image=btn_img_true, highlightthickness=0)
        self.btn_true.grid(row=2, column=0)

        btn_img_false = PhotoImage(file="images/false.png")
        self.btn_true = Button(image=btn_img_false, highlightthickness=0)
        self.btn_true.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.txt_question, text=q_text)