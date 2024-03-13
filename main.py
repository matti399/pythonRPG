from Dungeon import generate_dungeon
from func import *

# Main Program runtime
Dungeon.current_map = generate_dungeon()
show_controls()
print('Enter your Player Name: ')
Player.name = input()
show_map(Dungeon.current_map)
show_location()
while True:
    player_input = input().lower().split(' ')

    match player_input[0]:
        case 'go':
            player_move(player_input[1])
        case 'get':
            print('item get')
        case 'location':
            show_location()
        case 'status':
            show_status()
        case 'map':
            show_map(Dungeon.current_map)
        case 'admin_map':
            print(Dungeon.current_map)
        case 'exit':
            break
        case _:
            print('This was not a valid input.')
