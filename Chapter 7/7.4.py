
topping = ''
while True:
    topping = input('What topping add to your pizza? ')
    if topping == 'break':
        print('So, you decided to leave the program')
        break
    else:
        print(f'{topping} was added to your piiza')