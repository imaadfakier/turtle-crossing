import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

DIRECTIONS = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270,
}
# loop_count = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player(direction=DIRECTIONS['E'])

car_manager = CarManager(direction=DIRECTIONS['S'])

scoreboard = Scoreboard()

screen.onkey(fun=player.move, key='Up')

game_is_on = True

while game_is_on:
    # time.sleep(0.1)
    # time.sleep(car_manager.car_speed)  # <--- learnt something new
    time.sleep(0.1)
    # print(car_manager.car_speed)
    screen.update()

    # detect edge collision
    if player.is_at_edge():
        # player.go_to_start()
        car_manager.increase_car_speed()
        scoreboard.next_level()

    # n random cars  <-- learnt something new
    # if loop_count % 6 == 0:
    #     loop_count += 1
    # elif loop_count > 6:
    #     loop_count = 0
    # car_manager = CarManager(direction=DIRECTIONS['S'])
    # car_manager.create_car(direction=DIRECTIONS['S'])
    # car_manager.move()
    car_manager.create_car(direction=DIRECTIONS['S'])
    car_manager.move()

    # detect car cross
    # car_manager.has_crossed_road()

    # detect car collision
    for car in car_manager.cars:
        if player.distance(car) < 20:
        # if player.distance(car) < 15:
            # print('car collision detected')
            # scoreboard.turtle_is_squished()
            scoreboard.game_is_over()
            game_is_on = False

screen.exitonclick()
