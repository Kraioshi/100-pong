from turtle import Turtle, Screen
from stick import StickOne, StickTwo
from board import Board
from ball import Ball
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


screen.listen()
screen.onkey(key="w", fun=stick_one.move_up)
screen.onkey(key="s", fun=stick_one.move_down)
screen.onkey(key="Up", fun=stick_two.move_up)
screen.onkey(key="Down", fun=stick_two.move_down)

TOP_LINE = [*range(-500, 500, 1)]

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.initial_movement()

    # Ball collision with walls
    if ball.ball.ycor() > 190 or ball.ball.ycor() < -190:
        ball.wall_collision()
    # Ball collision with verticals
    if ball.ball.xcor() > 361 or ball.ball.xcor() < -361:
        ball.stick_collision()

screen.exitonclick()