class Dungeon:
    current_location = 'Start_Hall'
    possible_rooms = {
        'Start_Hall': {
            'enemies': 0,
            'danger_rating': 0
        },
        'Kitchen': {
            'enemies': 1,
            'danger_rating': 1
        },
        'Barracks': {
            'enemies': 2,
            'danger_rating': 1
        },
        'Hall': {
            'enemies': 2,
            'danger_rating': 1
        },
        'Tombs': {
            'enemies': 1,
            'danger_rating': 2
        },
        'Dining_Room': {
            'enemies': 1,
            'danger_rating': 3
        },
        'Garden': {
            'enemies': 0,
            'danger_rating': 0
        },
    }
