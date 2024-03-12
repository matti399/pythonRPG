from Player import Player
from Dungeon import Dungeon


def show_controls():
    # show how to control your Character
    print('''
Welcome to your own RPG Game
----------------------------

Get to the Garden with a key and a potion.
Avoid the monsters!

Commands:
go [direction]
get [item]
status
exit
    ''')


def show_location():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + Dungeon.current_location)
    # print an item if there is one
    if "item" in Dungeon.possible_rooms[Dungeon.current_location]:
        print('You see a ' + Dungeon.possible_rooms[Dungeon.current_location]['item'])
    print("---------------------------")


def show_status():
    # show the current player status
    print('---------------------------')
    print('Name: ' + str(Player.name))
    print('You Level is ' + str(Player.level))
    print('You have ' + str(Player.health) + '/10 Health left.')
    print('Inventory : ' + str(Player.inventory))
    print("---------------------------")


def grid_neuter(grid):
    grid_neutered = grid
    i = 0
    while i < 25:
        if grid[i] == Dungeon.current_location:
            grid_neutered[i] = '[x]'
        elif grid[i] != 0:
            grid_neutered[i] = '[ ]'
        else:
            grid_neutered[i] = ' 0 '
        i += 1
    return grid_neutered


def show_map(grid):
    x = grid_neuter(grid)
    print('---------------------------')
    print('Map of the Current Level:')
    print(x[0] + x[1] + x[2] + x[3] + x[4])
    print(x[5] + x[6] + x[7] + x[8] + x[9])
    print(x[10] + x[11] + x[12] + x[13] + x[14])
    print(x[15] + x[16] + x[17] + x[18] + x[19])
    print(x[20] + x[21] + x[22] + x[23] + x[24])
    print('---------------------------')
