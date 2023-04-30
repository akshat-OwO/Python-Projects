from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, cor):
        self.cor = cor
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(5, 1)
        self.goto(cor)
    
    def up(self):
        y = self.ycor() + 20
        self.goto(self.cor[0], y)
    
    def down(self):
        y = self.ycor() -20
        self.goto(self.cor[0], y)
        
