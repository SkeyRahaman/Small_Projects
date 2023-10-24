from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 24, "normal")


class Scoreboard():

    def __init__(self):
        self.left = Turtle()
        self.left_score = 0
        self.left.color("white")
        self.left.penup()
        self.left.goto(-100, 350)
        self.left.hideturtle()
        self.left.write(self.left_score, align=ALIGNMENT, font=FONT)

        self.right = Turtle()
        self.right_score = 0
        self.right.color("white")
        self.right.penup()
        self.right.goto(100, 350)
        self.right.hideturtle()
        self.right.write(self.right_score, align=ALIGNMENT, font=FONT)

    def increase_score_left(self):
        self.left_score += 1
        self.left.clear()
        self.left.write(self.left_score, align=ALIGNMENT, font=FONT)

    def increase_score_right(self):
        self.right_score += 1
        self.right.clear()
        self.right.write(self.right_score, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.left.goto(0, 0)
        self.left.write("GAME OVER", align=ALIGNMENT, font=FONT)
        if self.left_score == self.right_score:
            self.left.goto(0, -50 )
            self.left.write("GAME draw", align=ALIGNMENT, font=FONT)
        else:
            self.left.goto(0, -50)
            self.left.write(f"{'Left' if self.left_score>self.right_score else 'Right'} won", align=ALIGNMENT, font=FONT)

