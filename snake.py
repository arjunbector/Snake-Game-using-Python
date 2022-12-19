from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)] # Positions of the first three elements of the snake.
MOVE_DISTANCE = 20 # Every time the snakes moves ahead by 20 units.
# Defining the head positions of the snake with respect to directions. 
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def createsnake(self):
        '''Creates a new snake.'''
        for i in STARTING_POSITIONS:
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(i)
            self.segments.append(new_segment)

    def __init__(self):
        self.segments = [] # List to store the segments of the snake.
        self.createsnake() # Create the snake.
        self.head = self.segments[0] # Naming the first element of the snake as head.
    
    
        
    def reset(self):
        '''Resets the game.'''
        for segment in self.segments:
            segment.goto(1000,1000) # When the game ends, all the elements go to a far location 
                                    # from the visible screen.
        self.segments.clear() # Removes every element from the segments list and make it an empty list.
        self.createsnake() # Again makes a new snake.
        self.head = self.segments[0] # Assigning the first element of the snake as the head.

    def move(self):
        '''Functioin moves the snake by a certain predefined MOVE_DISTANCE.'''
        for seg_num in range(len(self.segments)-1, 0, -1): # Accesing the segments list in reverse order.
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE) # Makes the snake to move a certain distance.


    def add_segment(self, position):
        '''Creates a new segment at the given position.'''
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        '''Add the new segment to the snake.'''
        self.add_segment(self.segments[-1].position())


    # Methods for directions. 
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
