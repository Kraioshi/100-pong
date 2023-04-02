from turtle import Turtle

POSITIONS_ONE = \
    [(-340, 40), (-340, 30), (-340, 20), (-340, 10), (-340, 0), (-340, -10), (-340, -20), (-340, -30), (-340, -40)]
POSITIONS_TWO = \
    [(340, 40), (340, 30), (340, 20), (340, 10), (340, 0), (340, -10), (340, -20), (340, -30), (340, -40)]
MIN_Y = -180
MAX_Y = 180


class StickOne:

    def __init__(self):
        self.segments = []
        self.create_pad()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.head.setheading(90)
        self.tail.setheading(270)

    def create_pad(self):
        for position in POSITIONS_ONE:
            pad = Turtle()
            pad.shape('square')
            pad.color('white')
            pad.speed('fastest')
            pad.penup()
            #
            pad.shapesize(stretch_len=0.5, stretch_wid=0.5)
            #
            pad.goto(position)
            self.segments.append(pad)

    def move_up(self):
        y = self.head.ycor()
        if y < MAX_Y:
            for seg_num in self.segments:
                seg_num.setheading(90)
                seg_num.forward(20)

    def move_down(self):
        y = self.tail.ycor()
        if y > MIN_Y:
            for seg_num in self.segments[::-1]:
                seg_num.setheading(270)
                seg_num.forward(20)


class StickTwo:

    def __init__(self):
        self.segments = []
        self.create_pad()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.head.setheading(90)
        self.tail.setheading(270)


    def create_pad(self):
        for position in POSITIONS_TWO:
            pad = Turtle()
            pad.shape('square')
            pad.color('white')
            pad.speed('fastest')
            pad.penup()
            pad.goto(position)
            pad.shapesize(stretch_len=0.5, stretch_wid=0.5)
            self.segments.append(pad)

    def move_up(self):
        y = self.head.ycor()
        if y < MAX_Y:
            for seg_num in self.segments:
                seg_num.setheading(90)
                seg_num.forward(20)

    def move_down(self):
        y = self.tail.ycor()
        if y > MIN_Y:
            for seg_num in self.segments[::-1]:
                seg_num.setheading(270)
                seg_num.forward(20)
