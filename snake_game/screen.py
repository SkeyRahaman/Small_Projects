from turtle import Screen

WIDTH = 600
HEIGHT = 600
BGCOLOR = 'Black'


class Game_Screen:

    def __init__(self, width=WIDTH, height=HEIGHT, bgcolor=BGCOLOR, title="My Snake Game"):
        self.screen = Screen()
        self.screen.setup(width=width, height=height)
        self.screen.bgcolor(bgcolor)
        self.screen.title(title)
        self.screen.tracer(0)
