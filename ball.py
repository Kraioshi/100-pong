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
        if self.heading() == NE:
            self.setheading(SE)
        elif self.heading() == NW:
            self.setheading(SW)
        elif self.heading() == SW:
            self.setheading(NW)
        elif self.heading() == SE:
            self.setheading(NE)

    # Collision with stick
    def stick_bounce(self):
        if self.heading() == NE:
            self.setheading(NW)
            self.forward(20)
        elif self.heading() == NW:
            self.setheading(NE)
            self.forward(20)

        elif self.heading() == SW:
            self.setheading(SE)
            self.forward(20)

        elif self.heading() == SE:
            self.setheading(SW)
            self.forward(20)


    def reset(self):
        self.home()
        self.setheading(random.randrange(45, 360, 90))


if __name__ == "__main__":
    print(NE)
