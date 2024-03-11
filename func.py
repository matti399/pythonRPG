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


def player_commands():
    # dictionary of all viable player inputs
    return {
        'go',
        'get',
        'exit',
        'status'
    }


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
    print('You Level is ' + str(Player.level))
    print('You have ' + str(Player.health) + '/10 Health left.')
    print('Inventory : ' + str(Player.inventory))
    print("---------------------------")


def check_player_input():
    while True:
        i = input()
        if str(i) in player_commands():
            return i
        else:
            print('This was not a valid input.')

