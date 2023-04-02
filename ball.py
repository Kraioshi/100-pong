from turtle import Turtle
import random

NE = 45
NW = 135
SW = 225
SE = 315


class Ball:

    def __init__(self):
        self.balls = []
        self.create_ball()
        self.ball = self.balls[0]
        self.ball.setheading(random.randrange(45, 315, 90))

    def create_ball(self):
        ball = Turtle()
        ball.speed("slow")
        ball.shape("circle")
        ball.penup()
        ball.color("white")
        self.balls.append(ball)

    def initial_movement(self):
        self.ball.forward(10)

    # collision with walls
    def wall_collision(self):
        if self.ball.heading() == NE:
            self.ball.setheading(SE)
        elif self.ball.heading() == NW:
            self.ball.setheading(SW)
        elif self.ball.heading() == SW:
            self.ball.setheading(NW)
        elif self.ball.heading() == SE:
            self.ball.setheading(NE)

    # Collision with stick (with vertical wall for now xD)
    def stick_collision(self):
        if self.ball.heading() == NE:
            self.ball.setheading(NW)
        elif self.ball.heading() == NW:
            self.ball.setheading(NE)
        elif self.ball.heading() == SW:
            self.ball.setheading(SE)
        elif self.ball.heading() == SE:
            self.ball.setheading(SW)

    def reset(self):
        self.ball.home()
        self.ball.setheading(random.randrange(45, 360, 90))


if __name__ == "__main__":
    print(NE)
