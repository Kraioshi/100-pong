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
    time.sleep(0.2)
    ball.initial_movement()



screen.exitonclick()