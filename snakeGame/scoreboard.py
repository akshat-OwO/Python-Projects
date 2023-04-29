from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_score()
    
    def update_score(self):
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 18, 'normal'))
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=('Arial', 18, 'normal'))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()