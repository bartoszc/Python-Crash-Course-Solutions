friends = ['Thomas Edison', 'Elon Musk', 'Bill Gates']
print(f'Hello {friends[0]}, you are invited')
print(f'Hello {friends[1]}, you are invited')
print(f'Hello {friends[2]}, you are invited')


print(f'Unfortunately, {friends[0]}, is unable to come!')
friends[0] = 'Jack Dorsey'
print(f'Hello {friends[0]}, you are invited')
print(f'Hello {friends[1]}, you are invited')
print(f'Hello {friends[2]}, you are invited')