from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read()) # Reads the data.txt file and returns the high score.
        self.color('white')
        self.penup()
        self.goto(0,250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        '''Clears the previous scoreboard and writes new one.'''
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}",move=False,align=ALIGNMENT,font=(FONT))
        


    def increase_score(self):
        '''Updates the score by 1.'''
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}") # Updates the high score in the data.txt
        self.score = 0 # After game ends, score becomes zero again.
        self.update_scoreboard()
    