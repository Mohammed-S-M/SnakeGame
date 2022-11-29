# Importing files
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

# Creating the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating snake, food, and the scoreboard objects
snake = Snake()
food = Food()
food.refresh()
score = Score()

# Creating keyboard events to control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Loop to keep the game going until the user lose
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.display()

    # Detect collision with food.
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    # Detect collision with wall.
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 \
            or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
