import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.angles_ = {"upleft": 135, "upright": 45, "downleft": 225, "downright": 315}
        self.direction = random.choice(list(self.angles_.keys()))

    def move(self, paddle, scoreboard):
        if not self.set_direction(paddle,scoreboard):
            return False
        self.setheading(self.angles_[self.direction])
        self.forward(20)
        return True

    def set_direction(self, paddle, scoreboard):
        if self.ycor() >= 380:
            self.direction = "downright" if self.direction == "upright" else "downleft"
        elif self.ycor() <= -380:
            self.direction = "upright" if self.direction == "downright" else "upleft"
        elif self.xcor() >= 550:
            for tim in paddle.right_body:
                if self.distance(tim) < 10:
                    self.direction = "upleft" if self.direction == "upright" else "downleft"
                    scoreboard.increase_score_right()
                    return True
            scoreboard.game_over()
            return False
        elif self.xcor() <= -550:
            for tim in paddle.left_body:
                if self.distance(tim) < 10:
                    self.direction = "upright" if self.direction == "upleft" else "downright"
                    scoreboard.increase_score_left()
                    return True
            scoreboard.game_over()
            return False
        return True
