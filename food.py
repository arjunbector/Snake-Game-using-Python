from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color('red')
        self.speed('fastest') 
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)
        self.refresh()
    
    def refresh(self):
        '''Sends the food / dot turtle to a random position.'''
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)
    