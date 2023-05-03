from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
turtles = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    
    snake.move()

    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    if snake.turtles[0].xcor() > 290 or snake.turtles[0].xcor() < -290 or snake.turtles[0].ycor() > 290 or snake.turtles[0].ycor() < -290:
        scoreboard.reset()
        snake.reset()
    
    for turtle in snake.turtles[1:]:
        if snake.turtles[0].distance(turtle) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()