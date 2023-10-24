from turtle import Turtle

BODY_LENGTH = 5


class Paddle:

    def __init__(self):
        self.left_body = []
        for i in range(BODY_LENGTH):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(x=-550, y=i * 20)
            tim.left(90)
            self.left_body.append(tim)
        self.right_body = []
        for i in range(BODY_LENGTH):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(x=550, y=i * 20)
            tim.left(90)
            self.right_body.append(tim)

    def move_left_puddle_up(self):
        if self.left_body[-1].ycor() < 390:
            for tim in self.left_body:
                tim.forward(20)

    def move_left_puddle_down(self):
        if self.left_body[0].ycor() > -390:
            for tim in self.left_body:
                tim.back(20)

    def move_right_puddle_up(self):
        if self.right_body[-1].ycor() < 390:
            for tim in self.right_body:
                tim.forward(20)

    def move_right_puddle_down(self):
        if self.right_body[0].ycor() > -390:
            for tim in self.right_body:
                tim.back(20)
