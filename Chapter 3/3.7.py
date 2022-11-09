friends = ['Thomas Edison', 'Elon Musk', 'Bill Gates']
print(f'Hello {friends[0]}, you are invited')
print(f'Hello {friends[1]}, you are invited')
print(f'Hello {friends[2]}, you are invited')
print('-------------------------------------------')
print('I just found a bigger table!')

friends.insert(0, 'JK Rowling')
friends.insert(1, 'Dan Brown')
friends.append('Tobias Forge')

print('-------------------------------------------')
print(f'Hello {friends[0]}, you are invited')
print(f'Hello {friends[1]}, you are invited')
print(f'Hello {friends[2]}, you are invited')
print(f'Hello {friends[3]}, you are invited')
print(f'Hello {friends[4]}, you are invited')
print(f'Hello {friends[5]}, you are invited')
print('-------------------------------------------')
print('Oh no! I can invite just two people!')

removed = friends.pop()
print(f'Sorry, {removed}, you are no longer invited')

removed = friends.pop()
print(f'Sorry, {removed}, you are no longer invited')

removed = friends.pop()
print(f'Sorry, {removed}, you are no longer invited')

removed = friends.pop()
print(f'Sorry, {removed}, you are no longer invited')

print('-------------------------------------------')
print(friends)
print('-------------------------------------------')
del friends[1]
del friends[0]
print(friends)