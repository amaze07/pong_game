from turtle import Turtle
ALIGNMENT = "center"
FONT1 = ("Courier", 80, "normal")
FONT2 = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-10, -290)
        self.write("Press r to reset the match.",align=ALIGNMENT, font=FONT2)
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT1)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT1)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()