from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

class Snake:
    def __init__(self):
        self.turtles = []
        self.createSnake()
        
    def createSnake(self):
        for position in starting_positions:
            self.add_turtle(position)
    
    def add_turtle(self, position):
        turtle = Turtle('square')
        turtle.penup()
        turtle.color('white')
        turtle.setposition(position)
        self.turtles.append(turtle)
    
    def reset(self):
        for turtle in self.turtles:
            turtle.goto(1000, 1000)
        self.turtles.clear()
        self.createSnake()
    
    def extend(self):
        self.add_turtle(self.turtles[-1].position())
    
    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[i - 1].xcor()
            y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(x, y)
        self.turtles[0].forward(move_distance)

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)
