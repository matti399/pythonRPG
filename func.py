from Dungeon import Dungeon
from Player import Player
from copy import copy


def show_controls():
    # show how to control your Character
    print('''
Welcome to your own RPG Game
----------------------------

Get to the Garden with a key and a potion.
Avoid the monsters!

Commands:
go [north, south, west, east]
get [item]
location
status
map
exit
    ''')
    line_delimiter()


def show_location():
    # print the player's current status
    print('You are in the ' + Dungeon.current_map[Player.current_location])
    # print an item if there is one
    # if "item" in Dungeon.possible_rooms[Player.current_location]:
    #     print('You see a ' + Dungeon.possible_rooms[Player.current_location]['item'])
    line_delimiter()


def update_location():
    # print the player's current status
    print('You got to a ' + Dungeon.current_map[Player.current_location])
    # print an item if there is one
    # if "item" in Dungeon.possible_rooms[Player.current_location]:
    #     print('You see a ' + Dungeon.possible_rooms[Player.current_location]['item'])
    line_delimiter()


def show_status():
    # show the current player status
    print('Name: ' + str(Player.name))
    print('You Level is ' + str(Player.level))
    print('You have ' + str(Player.health) + '/10 Health left.')
    print('Inventory : ' + str(Player.inventory))
    line_delimiter()


def grid_neuter(grid):
    # format the grit and replace room names with braces
    grid_neutered = grid
    i = 0
    while i < 25:
        if i == Player.current_location:
            grid_neutered[i] = '[x]'
        elif grid[i] != 0:
            grid_neutered[i] = '[ ]'
        else:
            grid_neutered[i] = ' 0 '
        i += 1
    return grid_neutered


def show_map(grid):
    # show the map to the player
    x = grid_neuter(copy(grid))
    print('Map of the Current Level:')
    print(x[0] + x[1] + x[2] + x[3] + x[4])
    print(x[5] + x[6] + x[7] + x[8] + x[9])
    print(x[10] + x[11] + x[12] + x[13] + x[14])
    print(x[15] + x[16] + x[17] + x[18] + x[19])
    print(x[20] + x[21] + x[22] + x[23] + x[24])
    line_delimiter()


def player_move(movement_option):
    # move the player through the dungeon
    match movement_option:
        case 'north':
            if Player.current_location - 5 < 0:
                print('You can not go there.')
                line_delimiter()
            else:
                Player.current_location -= 5
                update_location()
        case 'south':
            if Player.current_location + 5 < 0:
                print('You can not go there.')
                line_delimiter()
            else:
                Player.current_location += 5
                update_location()
        case 'west':
            if Player.current_location in (0, 5, 10, 15, 20):
                print('You can not go there.')
                line_delimiter()
            else:
                Player.current_location -= 1
                update_location()
        case 'east':
            if Player.current_location in (4, 9, 14, 19, 24):
                print('You can not go there.')
                line_delimiter()
            else:
                Player.current_location += 1
                update_location()
        case _:
            print('This was not a valid input.')
            line_delimiter()


def line_delimiter():
    print('\n---------------------------\n')
