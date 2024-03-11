from Player import Player
from Dungeon import Dungeon
from func import *

# Main Program runtime
show_controls()
print('Enter your Player Name: ')
Player.name = input()
while True:
    show_location()
    player_input = check_player_input()
    if str(player_input) == 'exit':
        break

