animals = [
    {'owner': 'Piotr', 'is_cute': True},
    {'owner': 'Bart', 'is_cute': True},
    {'owner': 'Michal', 'is_cute': False}]

for animal in animals:
    print(f"{animal.get('owner')}")
    print(f"{animal.get('is_cute')}")
    print('#####################')