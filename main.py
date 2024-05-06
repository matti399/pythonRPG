from Dungeon import generate_dungeon
from func import *

# anmerkungen für Herrn Schneemann
# wie besprochen werden Items im Dungeon zufällig verteilt
# ab und an tritt beim Starten des programms ein sporadischer fehler auf
# sollte dies bei ihnen der Fall sein probieren sie es bitte erneut, ich versichere ihnen das Program funktioniert
# sollten sie irgendwelche anmerkungen/fragen/befähigungen für/an mich haben können sie mich unter matti39963@googlemail.com erreichen

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
    user_input = input().strip()
    player_input = user_input.split()

    if player_input is None:
        print('This was not a valid input.')
        line_delimiter()

    match player_input[0]:
        case 'go':
            if Dungeon.enemy_map[Player.current_location] != 0 and Dungeon.enemy_map[Player.current_location] != []:
                print('There are Enemies in this Room, either sneak past them or fight them.')
            else:
                player_move(player_input[1])
        case 'get':
            if Dungeon.enemy_map[Player.current_location] != 0 and Dungeon.enemy_map[Player.current_location] != []:
                print('There are Enemies in this Room, they guard the Item.')
            else:
                if (Dungeon.item_map[Player.current_location]) == player_input[1]:
                    Player.inventory.append(Dungeon.item_map[Player.current_location])
                    print('You picked up a ' + Dungeon.item_map[Player.current_location])
                    Dungeon.item_map.pop(Player.current_location)
                else:
                    print('No Item like that.\n')
        case 'inventory':
            show_inventory()
        case 'sneak':
            player_move(player_input[1])
        case 'stats':
            if Dungeon.enemy_map[Player.current_location] != 0 and Dungeon.enemy_map[Player.current_location] != []:
                enemy_stats()
            else:
                print('There are no Enemies in this Room.')
        case 'attack':
            if Dungeon.enemy_map[Player.current_location] != 0 and Dungeon.enemy_map[Player.current_location] != []:
                player_attack(player_input[1])
            else:
                print('There are no Enemies in this Room.')
        case 'location':
            show_location()
        case 'status':
            show_status()
        case 'map':
            show_map(Dungeon.current_map)
        case 'admin_map':
            print(Dungeon.current_map)
        case 'admin_enemy':
            print(Dungeon.enemy_map)
        case 'admin_items':
            print(Dungeon.item_map)
        case 'leave':
            if Dungeon.current_map[Player.current_location] == 'Garden' and Player.inventory.__contains__('exit_key'):
                print('You got out of the Dungeon and Survived to live another day.\n')
                print('A save feature will be implemented later\n')
                print('Thank you for Playing\n')
                exit(0)
            elif Dungeon.current_map[Player.current_location] == 'Laboratory' and Player.inventory.__contains__('BookOfLife') and Player.inventory.__contains__('Beam-O-Mat'):
                print('You got out of the Dungeon and Survived to live another day.\n')
                print('A save feature will be implemented later\n')
                print('Thank you for Playing\n')
                exit(0)
            else:
                print('You have not yet met the conditions to leave this place, keep searching you will find them.')
        case _:
            print('This was not a valid input.')
            line_delimiter()
