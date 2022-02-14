from turtle import Turtle

X_COORDINATES = [0, -20, -40]
STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 360


class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment_1 = Turtle("square")
        segment_1.penup()
        segment_1.color("white")
        segment_1.goto(position)
        self.segments.append(segment_1)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        pass

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
