from turtle import Turtle

SHAPE = 'turtle'
COLOR = 'black'
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    Inherits or sub-classes from Turtle class of Turtle module;
    creates an instance of the Player class each time a Player
    object is created.
    """

    # class attributes
    # ...

    def __init__(self, direction):
        super().__init__()
        self.shape(name=SHAPE)
        self.color(COLOR)
        self.penup()
        # self.x, self.y = STARTING_POSITION
        # self.goto(x=self.x, y=self.y)
        # self.reset_position()
        self.ready_set_go()
        self.setheading(to_angle=direction)

    def move(self):
        self.forward(distance=MOVE_DISTANCE)

    def is_at_edge(self):
        if self.ycor() == FINISH_LINE_Y:
            # self.reset_position()
            self.ready_set_go()
            return True
        return False

    # def reset_position(self):
    def ready_set_go(self):
    # def go_to_start(self):
        self.goto(x=STARTING_POSITION)
