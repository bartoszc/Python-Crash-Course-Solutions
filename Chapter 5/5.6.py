age = 18
person = None

if age < 2:
    person = 'baby'
elif age < 4:
    person = 'toddler'
elif age < 13:
    person = 'kid'
elif age < 20:
    person = 'teenager'
elif age < 65:
    person = "adult"
elif age >= 65:
    person = 'adult'

print(f'You are {person}')
