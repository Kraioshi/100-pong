from turtle import Turtle, Screen
from stick import StickOne, StickTwo

screen = Screen()
screen.screensize(700, 400)
screen.title("Pong")
screen.bgcolor('black')
screen.tracer(0)


stick_one = StickOne()
stick_two = StickTwo()

screen.listen()
screen.onkey(key="w", fun=stick_one.move_up)
screen.onkey(key="s", fun=stick_one.move_down)
screen.onkey(key="Up", fun=stick_two.move_up)
screen.onkey(key="Down", fun=stick_two.move_down)


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()