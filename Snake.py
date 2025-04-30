import turtle
from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DIST= 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        # creating the snake
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for i in POSITIONS:
            self.new_snakes = Turtle()
            self.new_snakes .penup()
            self.new_snakes .shape('square')
            self.new_snakes .color('white')
            self.new_snakes.goto(i)
            self.snakes.append(self.new_snakes)


    def move(self):
        for seg_num in range(len(self.snakes)-1,0,-1):
            new_x = self.snakes[seg_num-1].xcor()
            new_y = self.snakes[seg_num -1].ycor()
            self.snakes[seg_num].goto(new_x,new_y)
        self.snakes[0].forward(DIST)

    def mv_right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)
    def mv_left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)
    def mv_up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)
    def mv_down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)
