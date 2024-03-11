import Player


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
    inputs = [
        'go',
        'get',
        'exit',
        'status'
    ]


def show_location():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + current_room)
    # print an item if there is one
    if "item" in rooms[current_room]:
        print('You see a ' + rooms[current_room]['item'])
    print("---------------------------")


def show_status():
    print('---------------------------')
    print('You Level is ' + str(player.level))
    print('You have ' + str(player.health) + '/10 Health left.')
    print('Inventory : ' + str(player.inventory))
    print("---------------------------")


current_room = 'Hall'

rooms = {
    'Hall': {
        'south': 'Kitchen'
    },
    'Kitchen': {
        'north': 'Hall'
    }
}

# Main Program runtime
show_controls()
player = Player.Player
print('Enter your Player Name: ')
player.name = input()
while True:
    show_location()
    player_input = input()
    break
