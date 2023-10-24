import random
from turtle import Turtle

FOOD_LIMIT = 250


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x, random_y = self.generate_new_cord()
        self.goto(random_x, random_y)

    def refresh(self):
        random_x, random_y = self.generate_new_cord()
        self.goto(random_x, random_y)

    def generate_new_cord(self):
        return (random.randint(-FOOD_LIMIT, FOOD_LIMIT) // 20) * 20, (
                    random.randint(-FOOD_LIMIT, FOOD_LIMIT) // 20) * 20
