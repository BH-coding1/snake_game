from turtle import *
Font= ('Courier',24,'normal')
ALIGNMENT = 'center'
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color('White')
        self.goto(0,270)
        with open('My_file.txt','r') as file:
            score = file.read()
            self.high_score= int(score)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f'Score :{self.score} High Score :{self.high_score}',font= Font,align=ALIGNMENT)
        self.score += 1
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('My_file.txt','w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update_score()
