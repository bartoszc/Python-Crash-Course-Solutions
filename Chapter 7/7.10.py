vacations = {}

while True:
    name = input('Please, enter your name: ')
    place = input('If you could visit one place in the world, where would you go? ')
    vacations[name] = place

    answer = input('Do you want to continue the poll? (yes/no) ')
    if answer == 'no':
        break


for name, place in vacations.items():
    print(f'{name} wants to go to: {place}')