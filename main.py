from Player import Player
from Dungeon import Dungeon
from Dungeon import generate_dungeon
from func import *

# Main Program runtime
show_controls()
print('Enter your Player Name: ')
Player.name = input()
dungeon_map = generate_dungeon()
show_map(dungeon_map)
show_location()
while True:
    player_input = input()

    match player_input:
        case 'go':
            print('got there')
        case 'get':
            print('item get')
        case 'location':
            show_location()
        case 'status':
            show_status()
        case 'map':
            show_map(dungeon_map)
        case 'exit':
            break
        case _:
            print('This was not a valid input.')
