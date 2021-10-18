from turtle import Turtle

DISPLAY_TEXT = 'Level: '
# ALIGNMENT = 'left'
ALIGNMENT = 'center'
MOVE = False
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    Creates an instance of the Scoreboard class each time a CarManager
    object is created.
    """

    # class attributes

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-200, y=250)
        self.color('black')
        self.display_level()

    def display_level(self):
        # self.clear()
        self.write(arg=DISPLAY_TEXT + str(self.level), move=MOVE, align=ALIGNMENT, font=FONT)

    def next_level(self):
        self.clear()
        self.level += 1
        self.display_level()

    # def turtle_is_squished(self):
    def game_is_over(self):
        self.home()
        # self.goto(x=0, y=0)
        self.write(arg='GAME OVER', move=MOVE, align=ALIGNMENT, font=FONT)
