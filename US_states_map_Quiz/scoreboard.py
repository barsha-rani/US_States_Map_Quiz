from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Helvetica", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        return self.score
        # self.update_scoreboard()

    # def update_scoreboard(self):
    #     self.clear()
    #     self.write(arg=f"Score: {self.score}/50 correct", align=ALIGNMENT, font=FONT)
