users = {
    'sunny': {
        'first': 'emily',
        'last': 'perry',
        'location': 'London',
    },

    'docker': {
        'first': 'brian',
        'last': 'griffin',
        'location': 'rhode island',
        },
    }

for username, user_info in users.items():
    print(f'\nUsername:{username}')
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name:{full_name.title()}")
    print(f"\tLoation:{location.title()}")