from turtle import Turtle

FONT = ('Courier', 30, 'bold')
ALIGNMENT = 'right'


class LeftScore(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor('white')
        self.goto(x=75, y=125)
        self.update_left()

    def update_left(self):
        self.write(f"{self.score}", font=FONT, align='right')

    def add_left(self):
        self.score += 1
        self.clear()
        self.update_left()


class RightScore(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor('white')
        self.goto(x=-75, y=125)
        self.update_right()

    def update_right(self):
        self.write(f"{self.score}", font=FONT, align='left')

    def add_right(self):
        self.score += 1
        self.clear()
        self.update_right()





