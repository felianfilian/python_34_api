from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Trivial Quiz")

        self.window.config(width=400, height=600, padx=20, pady=20, bg=THEME_COLOR)
        txt_score = Label(text="Score: 0", fg="white", font=("Arial", 18, "normal"), bg=THEME_COLOR, highlightthickness=0,  padx=20, pady=20)
        txt_score.grid(row=0, column=1)
        txt_quest = Label(text="the question", fg="black", font=("Arial", 18, "normal"), bg="white", padx=20, pady=20)
        txt_quest.grid(row=1, column=0, columnspan=2)

        self.window.mainloop()