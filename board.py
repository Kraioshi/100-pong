from turtle import Turtle


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor('white')
        self.pensize(2)
        self.hideturtle()
        self.draw_board()

    def draw_board(self):
        self.goto(0, 199)
        self.goto(-370, 199)
        self.goto(-370, -200)
        self.goto(370, -200)
        self.goto(370, 199)
        self.goto(0, 199)
        self.goto(0, -200)


