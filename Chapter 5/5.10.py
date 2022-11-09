current_users = ['jeff', 'bill', 'tom', 'jared', 'anna']
new_users = ['Till', 'Richard', 'Bill', 'Tom', 'Olivier']

for user in new_users:
    if user.lower() in current_users:
        print('You need to choose a different username')
    else:
        print(f'This name - {user} is available')