from random import *


def generate_dungeon():
    # generate a 5x5 grid of rooms with the start point in the top row
    # and the garden in the bottom row
    grid = [
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
    ]
    grid[randint(0, 4)] = 'Start_Hall'
    grid[randint(20, 24)] = 'Garden'
    return grid


class Dungeon:
    current_location = 'Start_Hall'
    possible_rooms = {
        'Start_Hall': {
            'enemies': 0,
            'danger_rating': 0
        },
        'Kitchen': {
            'enemies': 1,
            'danger_rating': 1
        },
        'Barracks': {
            'enemies': 2,
            'danger_rating': 1
        },
        'Hall': {
            'enemies': 2,
            'danger_rating': 1
        },
        'Tombs': {
            'enemies': 1,
            'danger_rating': 2
        },
        'Dining_Room': {
            'enemies': 1,
            'danger_rating': 3
        },
        'Garden': {
            'enemies': 0,
            'danger_rating': 0
        },
    }
