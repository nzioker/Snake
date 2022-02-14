from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

import time

my_screen = Screen()
snake = Snake()
food = Food()
my_score = Score()

my_screen.setup(500, 400)
my_screen.bgcolor("black")
is_game_on = True
my_screen.tracer(0)

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")


while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        my_score.increase_score()

    # detect collision with walls

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        my_score.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            my_score.reset()


my_screen.exitonclick()
