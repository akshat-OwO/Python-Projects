from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        self.x_move = 10
        self.y_move = 10
        self.sleep = 0.1
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.speed('slowest')
    
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
    
    def bounce_x(self):
        self.x_move *= -1
        self.sleep *= 0.9

    def bounce_y(self):
        self.y_move *= -1
        self.sleep *= 0.9
    
    def out_of_bounds(self):
        self.home()
        self.bounce_x()
        self.sleep = 0.1
