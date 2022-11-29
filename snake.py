# Importing files
from turtle import Turtle


# Snake Class to create the snake shape and its movements
class Snake:

    # The starting positions field for the three turtles to make the snake shape
    starting_position = [(0, 0), (-20, 0), (-40, 0)]
    # segments field to collect multiple turtles in the shape of snake
    segments = []

    def __init__(self):
        self.create_snake()

    # Method to create the three turtles and position them next to each others
    def create_snake(self):
        for index in self.starting_position:
            self.add_segment(index)

    # Method to add all turtles together to form the snake shape
    def add_segment(self, index):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(index)
        self.segments.append(snake)

    # Method to help with the movement when the user
    # turn the snake left or right the head will go first then the rest
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Method to move the snake head first
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    # Methods up, down, left, and right to control the snake movements using keyboad arrows
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
