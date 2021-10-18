from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# class CarManager(Turtle):
class CarManager:
    # """
    # Inherits or sub-classes from Turtle class of Turtle module;
    # creates an instance of the CarManager class each time a CarManager
    # object is created.
    # """
    """
    Creates an instance of the CarManager class each time a CarManager
    object is created.
    """

    # class attributes
    # ...

    def __init__(self, direction):
        # super().__init__()
        # self.shape(name='square')
        # self.color(COLORS[randint(0, len(COLORS) - 1)])
        # self.shapesize(stretch_wid=1, stretch_len=2)
        # self.setheading(to_angle=direction)
        # self.penup()
        # self.goto(x=400, y=randint(-250, 250))
        self.cars = []
        # self.create_car(direction)
        # self.car_speed = 0.1
        self.car_speed = MOVE_INCREMENT  # <--- learnt something new

    def create_car(self, direction):
        if randint(1, 6) != 1:
            return
        car = Turtle(shape='square')
        car.shape(name='square')
        car.color(COLORS[randint(0, len(COLORS) - 1)])
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(to_angle=direction)
        car.penup()
        car.goto(x=400, y=randint(-250, 250))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            # car.forward(MOVE_INCREMENT)
            car.forward(self.car_speed)

    # def has_crossed_road(self):
    #     for car in self.cars:
    #         if car.xcor() < -300:
    #             car.clear()

    def increase_car_speed(self):
        # self.car_speed *= 0.9
        # self.car_speed *= 0.5
        self.car_speed += MOVE_INCREMENT
