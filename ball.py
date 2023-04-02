from turtle import Turtle
import random
import time

NE = 45
NW = 135
SW = 225
SE = 315


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed('slow')
        self.shape('circle')
        self.penup()
        self.color('white')
        self.setheading(random.randrange(45, 315, 90))

    def initial_movement(self):
        self.forward(1)

    # collision with walls
    def wall_bounce(self):
        if self.heading() == 45:
            self.setheading(315)
        elif self.heading() == 315:
            self.setheading(45)
        elif self.heading() == 225:
            self.setheading(135)
        elif self.heading() == 135:
            self.setheading(225)

    # Collision with stick
    def stick_bounce(self):
        if self.heading() == 45:
            self.setheading(135)
            self.forward(5)
        elif self.heading() == 135:
            self.setheading(45)
            self.forward(5)

        elif self.heading() == 225:
            self.setheading(315)
            self.forward(5)

        elif self.heading() == 315:
            self.setheading(225)
            self.forward(5)


    def reset(self):
        self.home()
        self.setheading(random.randrange(45, 360, 90))


if __name__ == "__main__":
    print(NE)
