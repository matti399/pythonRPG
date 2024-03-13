from random import *
from copy import copy


def generate_dungeon():
    # generate a 5x5 grid of rooms with the start point in the top row
    # and the garden at the bottom end
    grid = [
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
    ]
    i = 0
    while i < randint(7, 9):
        if i == 0:
            location_pointer = randint(0, 4)
            grid[copy(location_pointer)] = 'Start_Hall'
        x = select_next_location(location_pointer)
        location_pointer = x
        if grid[x] == 0:
            select_room(grid, x)
            i += 1

    grid[location_pointer] = 'Garden'

    return grid


def select_next_location(location_pointer):
    current_room = copy(location_pointer)
    if current_room in (0, 5, 10, 15, 20):
        options = [current_room + 5, current_room + 1]
    elif current_room in (4, 9, 14, 19, 24):
        options = [current_room - 1, current_room + 5]
    else:
        options = [current_room - 1, current_room + 5, current_room + 1]

    return options[randint(0, len(options)-1)]


def select_room(grid, x):
    room_type = randint(1, 5)
    match room_type:
        case 1:
            grid[x] = 'Kitchen'
        case 2:
            grid[x] = 'Barracks'
        case 3:
            grid[x] = 'Hall'
        case 4:
            grid[x] = 'Tombs'
        case 5:
            grid[x] = 'Dining_Room'


class Dungeon:
    current_location = 'Start_Hall'
    possible_rooms = {
        'Start_Hall': {
            'enemies': 0,
            'danger_rating': 0
        },
        'Garden': {
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
    }
    possible_enemies = {
        'Skeleton': {
            'level': randint(1, 4),
            'health': '',
            'strength': '',
        },
        'Undead': {
            'level': randint(2, 6),
            'health': '',
            'strength': '',
        },
        'Reptilian_Humanoid': {
            'level': randint(4, 7),
            'health': '',
            'strength': '',
        },
        'Lich': {
            'level': randint(5, 9),
            'health': '',
            'strength': '',
        },
    }
