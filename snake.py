from turtle import Turtle
POSITIONS = [(10, 0),(0, 0),(-10, 0)]
MOVE_DIST = 15

RIGHT = 0
LEFT = 180
DOWN = 270
UP = 90


class Snake:

    def __init__(self):
        self.my_snk = []
        self.create_snake()
        self.head = self.my_snk[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.ad_pieces(pos)

    def ad_pieces(self, pos):
        tom = Turtle("square")
        tom.penup()
        tom.color('white')
        tom.goto(pos)
        self.my_snk.append(tom)

    def extending(self):
        self.ad_pieces(self.my_snk[-1].position())

    def move(self):
        for piece in range(len(self.my_snk) -1, 0, -1):
            new_x = self.my_snk[piece - 1].xcor()
            new_y = self.my_snk[piece - 1].ycor()
            self.my_snk[piece].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def go_right(self):
        self.head.setheading(self.head.heading() - 90)

    def go_left(self):
        self.head.setheading(self.head.heading() + 90)

    def go_down(self):
        self.head.setheading(self.head.heading() - 90)

    def go_up(self):
        self.head.setheading(self.head.heading() + 90)


