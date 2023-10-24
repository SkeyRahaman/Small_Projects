import time
from screen import Game_Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def main():
    sn = Game_Screen()
    snake = Snake()
    food = Food()
    score = Scoreboard()

    sn.screen.listen()
    sn.screen.onkey(key="Up", fun=snake.set_direction_up)
    sn.screen.onkey(key="Down", fun=snake.set_direction_down)
    sn.screen.onkey(key="Left", fun=snake.set_direction_left)
    sn.screen.onkey(key="Right", fun=snake.set_direction_right)

    while True:
        time.sleep(0.2)
        snake.move()

        # check collision with food
        if 15 > snake.body[-1][2].distance(food):
            snake.got_food()
            food.refresh()
            score.increase_score()
        sn.screen.update()
        if not snake.check_if_inside():
            score.game_over()
            break

    sn.screen.exitonclick()


if __name__ == "__main__":
    main()
