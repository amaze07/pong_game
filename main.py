from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

def restart():
    screen.reset()
    run_game()

def run_game():
    r_paddle = Paddle(350, 0)
    l_paddle = Paddle(-350, 0)
    ball = Ball()
    score = Scoreboard()

    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")
    screen.onkey(restart, "r")

    is_game_on = True
    while is_game_on:
        time.sleep(ball.ball_speed)
        screen.update()
        ball.move()

        # detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.y_bounce()

        # detect collision with right paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
            print("collision")
            ball.x_bounce()

        # detect a miss
        if ball.xcor() > 380:
            ball.reset_position()
            score.l_point()

        if ball.xcor() < -380:
            ball.reset_position()
            score.r_point()

run_game()

screen.exitonclick()