from turtle import Turtle


class Board:

    def __init__(self):
        self.draw_board()

    def draw_board(self):
        chalk = Turtle()
        chalk.pencolor('white')
        chalk.pensize(2)
        chalk.hideturtle()
        chalk.goto(0, 199)
        chalk.goto(-370, 199)
        chalk.goto(-370, -199)
        chalk.goto(370, -199)
        chalk.goto(370, 199)
        chalk.goto(0, 199)
        chalk.goto(0, -199)

