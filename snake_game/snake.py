from collections import deque
from turtle import Turtle

INITIAL_LENGTH = 5


class Snake:

    def __init__(self):
        self.body = deque()
        self.path = {"up": [0, 20],
                     "right": [20, 0],
                     "down": [0, -20],
                     "left": [-20, 0]
                     }
        self.direction = "right"
        self.initialize_snake()

    def initialize_snake(self):
        for i in range(INITIAL_LENGTH):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(x=(i * 20), y=0)
            self.body.append([i * 20, 0, tim])

    def move(self):
        mouth = [self.body[-1][0], self.body[-1][1]]
        x, y, tim = self.body.popleft()
        new_x = mouth[0] + self.path[self.direction][0]
        new_y = mouth[1] + self.path[self.direction][1]
        tim.goto(new_x, new_y)
        self.body.append([new_x, new_y, tim])

    def got_food(self):
        mouth = [self.body[-1][0], self.body[-1][1]]
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        new_x = mouth[0] + self.path[self.direction][0]
        new_y = mouth[1] + self.path[self.direction][1]
        tim.goto(new_x, new_y)
        self.body.append([new_x, new_y, tim])

    def set_direction_left(self):
        if self.direction != 'right':
            self.direction = "left"

    def set_direction_right(self):
        if self.direction != 'left':
            self.direction = 'right'

    def set_direction_up(self):
        if self.direction != 'down':
            self.direction = 'up'

    def set_direction_down(self):
        if self.direction != 'up':
            self.direction = 'down'

    def check_if_inside(self):
        head = self.body[-1][:2]
        body = [[a, b] for a, b, _ in self.body][:-1]
        return (-290 <= head[0] <= 290) and (-290 <= head[1] <= 290) and head not in body
