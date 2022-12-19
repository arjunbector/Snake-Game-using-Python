from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard
import time


#Setting up the screen.
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')

screen.title('Snake Game')
screen.tracer(0)

# Defining snake, food and score
snake = Snake()
food = Food()
score = ScoreBoard()


# To use user inputs to make the snake move.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update() # Used to update the screen.

game_is_on = True # Flag to know whether the game is still on or off.

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15: # To check whether the snake head is close enough to the food. 
        food.refresh()
        snake.extend()    
        score.increase_score()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()