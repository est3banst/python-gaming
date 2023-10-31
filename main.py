import time
from snake import Snake
from turtle import Screen
from food import Food
from score import Score

my_Screen = Screen()
my_Screen.setup(800, 600, )
my_Screen.bgcolor("black")
my_Screen.title("Welcome to the snake game")
my_Screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

my_Screen.listen()
my_Screen.onkeypress(fun=snake.go_left, key='Left')
my_Screen.onkeypress(fun=snake.go_right, key='Right')
my_Screen.onkeypress(fun=snake.go_down, key='Down')
my_Screen.onkeypress(fun=snake.go_up, key='Up')

game_on = True

while game_on:
    my_Screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extending()

    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_on = False
        score.game_over()

    for piece in snake.my_snk[1:]:
        if snake.head.distance(piece) < 10:
            game_on = False
            score.game_over()

my_Screen.exitonclick()



