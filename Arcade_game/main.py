import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scoreboard
WIDTH = 1200
HEIGHT = 800
BGCOLOR = "Black"
TITLE = "The Arcade Game"


def main():
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor(BGCOLOR)
    screen.title(TITLE)
    screen.tracer(0)

    paddle = Paddle()
    ball = Ball()
    scoreboard = Scoreboard()
    screen.update()

    screen.listen()
    screen.onkey(key="Up", fun=paddle.move_right_puddle_up)
    screen.onkey(key="Down", fun=paddle.move_right_puddle_down)
    screen.onkey(key="w", fun=paddle.move_left_puddle_up)
    screen.onkey(key="s", fun=paddle.move_left_puddle_down)

    while True:
        time.sleep(0.1)
        if not ball.move(paddle,scoreboard):
            print("Game Over")
            break

        screen.update()






    screen.exitonclick()


if __name__ == "__main__":
    main()
