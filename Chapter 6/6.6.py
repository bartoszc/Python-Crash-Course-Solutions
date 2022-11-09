favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

poll = ['Peter', 'Marrie', 'Molly', 'Sarah']

for people in poll:
    if people.lower() in favorite_languages:
        print('Thank you for your respond')
    else:
        print('Please, take a part in the poll')