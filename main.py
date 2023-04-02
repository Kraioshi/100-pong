from turtle import Screen
from stick import StickOne, StickTwo
from board import Board
from ball import Ball
from scoreboard import LeftScore, RightScore
import time

screen = Screen()
screen.screensize(760, 400)
screen.title("Pong")
screen.bgcolor('black')
screen.tracer(0)

stick_one = StickOne()
stick_two = StickTwo()
board = Board()
ball = Ball()
l_score = LeftScore()
r_score = RightScore()

screen.listen()
screen.onkey(key="w", fun=stick_one.move_up)
screen.onkey(key="s", fun=stick_one.move_down)
screen.onkey(key="Up", fun=stick_two.move_up)
screen.onkey(key="Down", fun=stick_two.move_down)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0)
    ball.initial_movement()

    # Ball bouncing off the walls
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.wall_bounce()

    # Adding score if ball crossed vertical line
    if ball.xcor() > 380:
        r_score.add_right()
        time.sleep(0.1)
        ball.reset()
    elif ball.xcor() < -380:
        l_score.add_left()
        time.sleep(0.1)
        ball.reset()

    # Ball bouncing off the sticks
    for segments in stick_two.segments:
        if segments.distance(ball) < 50 and ball.xcor() > 320:
            ball.stick_bounce()
    for segments in stick_one.segments:
        if segments.distance(ball) < 40 and ball.xcor() < -320:
            ball.stick_bounce()


screen.exitonclick()
