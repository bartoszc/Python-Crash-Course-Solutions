sandwich_orders = ['Pastrami', 'Elvis', 'Snack', 'Pastrami', 'Burger', 'Chief', 'Pastrami']
finished_sandwiches = []

print('We are ran out of Pastrami!')
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich.')
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print('Finished: ' + sandwich)

