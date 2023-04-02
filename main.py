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
    time.sleep(0.02)
    ball.initial_movement()

    # Ball collision with walls
    if ball.ball.ycor() > 190 or ball.ball.ycor() < - 190:
        ball.wall_collision()

    # Ball collision with verticals
    if ball.ball.xcor() > 361:
        r_score.add_right()
        time.sleep(0.03)
        ball.reset()
    elif ball.ball.xcor() < -361:
        l_score.add_left()
        time.sleep(0.03)
        ball.reset()

    # Ball collision with sticks
    for segments in stick_two.segments:
        if segments.distance(ball.ball) < 10:
            ball.stick_collision()
    for segments in stick_one.segments:
        if segments.distance(ball.ball) < 10:
            ball.stick_collision()


screen.exitonclick()