import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Race")
screen.tracer(0)
screen.bgcolor("ghost white")

player = Player()
car_manger = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move_side_left, "A")


def play_game():
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manger.create_car()
        car_manger.move_cars()

        # detect collision with the car
        for car in car_manger.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        # detect if the player reached the end and reset the pos
        if player.player_is_reached():
            player.reset()
            car_manger.level_up()
            # update the levels of the game
            scoreboard.update_level()

    screen.exitonclick()


play_game()
