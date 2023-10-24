# Arcade Pong Game

The Arcade Pong Game is a simple arcade-style game where two players control paddles to bounce a ball back and forth. The goal is to prevent the ball from reaching the player's side, and each time the ball passes a player's paddle, the opponent scores a point. The game continues until one player reaches a set number of points or the game is manually exited.

## Gameplay

- Player 1 controls their paddle using the "Up" and "Down" arrow keys.
- Player 2 controls their paddle using the "W" and "S" keys.
- The game continues until a set number of points are scored, or players decide to exit the game.

## Features

- **Two-Player Mode**: Enjoy head-to-head gameplay with a friend or family member.
- **Simple Controls**: Easy-to-use controls for both players, enhancing accessibility.
- **Score Tracking**: Keep track of scores on the screen with a scoreboard.
- **Game Over Message**: Displays a "Game Over" message and the winner when the game ends.
- **Customizable**: You can customize the game by changing the winning score limit or adding more features.

## Dependencies

The game is built using the Python programming language and relies on the Turtle graphics library for graphics and the game's display. No external dependencies are required to run the game.

## Usage

1. Ensure that you have Python installed on your computer.
2. Clone the project from GitHub or download the source code files.
3. Run the game by executing the `main.py` script.
4. Follow the on-screen instructions to play the game.

```bash
python main.py
```

## Customization

You can customize the game by:

- Changing the winning score limit: In the `main.py` file, adjust the value in the `while` loop to change the score limit for winning the game.

```python
while True:
    if not ball.move(paddle, scoreboard):
        print("Game Over")
        break
    if scoreboard.left_score >= 5:  # Change the score limit here
        print("Player 1 wins!")
        break
    elif scoreboard.right_score >= 5:  # Change the score limit here
        print("Player 2 wins!")
        break
    screen.update()
```

- Adding more features: Extend the game by introducing power-ups, sound effects, or additional gameplay elements.

## Contributions

This game was developed by [Your Name]. You can contribute to its improvement by submitting pull requests, reporting issues, or suggesting enhancements.

Enjoy playing the Arcade Pong Game and have fun with your friends!

