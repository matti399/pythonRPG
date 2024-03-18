from random import randint
from Dungeon import Dungeon
from Player import Player
from copy import copy
from math import ceil


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
leave
exit !exits Game without saving!
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


def populate_rooms_with_enemies(current_map):
    monster_map = copy(current_map)
    for index, room in enumerate(monster_map):
        if room != 0:
            enemies_in_room = []
            enemy_count = randint(0, Dungeon.possible_rooms[room]['enemies'])
            danger_level = Dungeon.possible_rooms[room]['danger_rating']
            i = 0
            while i < enemy_count:
                enemy = Dungeon.possible_enemies[randint(0, danger_level)]
                match enemy:
                    case 'Skeleton':
                        level = int(randint(1, 4))
                        health = ceil(level * 1.5)
                        strength = ceil(level * 1.2)
                        enemies_in_room.append(['Skeleton', level, health, strength])
                    case 'Undead':
                        level = randint(2, 6)
                        health = ceil(level * 1.6)
                        strength = ceil(level * 1.4)
                        enemies_in_room.append(['Skeleton', level, health, strength])
                    case 'Reptilian_Humanoid':
                        level = randint(4, 7)
                        health = ceil(level * 2)
                        strength = ceil(level * 1.6)
                        enemies_in_room.append(['Skeleton', level, health, strength])
                    case 'Lich':
                        level = randint(5, 9)
                        health = ceil(level * 1.3)
                        strength = ceil(level * 2)
                        enemies_in_room.append(['Skeleton', level, health, strength])
                i += 1
            monster_map[index] = enemies_in_room
    return monster_map


def spread_out_items(current_map):
    # spread the items across the rooms, allways put the Sword in the Start_Hall
    item_map = copy(current_map)
    i = 0
    while i < 4:
        x = randint(0, 23)
        if item_map[x] != 0 and item_map[x] != 'Start_Hall' and item_map[x] != 'Garden':
            if not Dungeon.possible_item.__contains__(item_map[x]):
                item_map[x] = Dungeon.possible_item[i]
                i += 1
    for room in item_map:
        if item_map[room] == 'Start_Hall':
            item_map[room] = 'Sword'
        if not Dungeon.possible_item.__contains__(item_map[room]):
            item_map = 0

    return item_map


def dd(x):
    print(x)
    exit(0)



def line_delimiter():
    print('\n---------------------------\n')
