from turtle import Turtle
import random
NE = 45
NW = 135
SE = 225
SW = 315

class Ball:

    def __init__(self):
        self.balls = []
        self.create_ball()
        self.ball = self.balls[0]

    def create_ball(self):
        ball = Turtle()
        ball.speed("slow")
        ball.shape("arrow")
        ball.color("white")
        self.balls.append(ball)

    def initial_movement(self):
        self.ball.setheading(45)
        self.ball.forward(10)

    # collision with walls
    def collision(self):
        if self.ball.heading == 45:
            self.ball.setheading(315)
        elif self.ball.heading == 135:
            self.ball.setheading(225)
        elif self.ball.heading == 225:
            self.ball.setheading(135)
        elif self.ball.heading == 315:
            self.ball.setheading(45)

