from Dungeon import generate_dungeon
from func import *


Dungeon.current_map = generate_dungeon()
Dungeon.enemy_map = populate_rooms_with_enemies(Dungeon.current_map)
Dungeon.item_map = spread_out_items(Dungeon.current_map)
show_controls()
print('Enter your Player Name: ')
Player.name = input()
line_delimiter()
show_map(Dungeon.current_map)
show_location()
while True:
    player_input = input().lower().split(' ')

    match player_input[0]:
        case 'go':
            player_move(player_input[1])
        case 'get':
            if (Dungeon.item_map[Player.current_location]) == player_input[1]:
                Player.inventory.append(Dungeon.item_map[Player.current_location])
                print('You picked up a ' + Dungeon.item_map[Player.current_location])
                Dungeon.item_map.pop(Player.current_location)
            else:
                print('No Item like that.\n')
        case 'inventory':
            show_inventory()
        case 'location':
            show_location()
        case 'status':
            show_status()
        case 'map':
            show_map(Dungeon.current_map)
        case 'admin_map':
            print(Dungeon.current_map)
        case 'leave':
            if show_location() == 'Garden' and Player.inventory.__contains__('Exit_Key'):
                print('You got out of the Dungeon and Survived to live another day.\n')
                print('A save feature will be implemented later\n')
                print('Thank you for Playing\n')
                exit(0)
        case 'exit':
            exit(0)
        case _:
            print('This was not a valid input.')
            line_delimiter()
