from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('snakeGame/data.txt') as fhand:
            self.high_score = int(fhand.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center", font=('Arial', 18, 'normal'))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('snakeGame/data.txt', 'w') as fhand:
                fhand.write(str(self.high_score))
        self.score = 0
        self.update_score()
    
    def increase_score(self):
        self.score += 1
        self.update_score()