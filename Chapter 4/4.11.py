pizzas = ['Pepperoni', 'Salami', 'Cheese']
friend_pizzas = pizzas[:]

friend_pizzas.append('Hawaii')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print('-------------------')
print("My friend’s favorite pizzas are")
for pizza in friend_pizzas:
    print(pizza)
