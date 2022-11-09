peoples = [
    {'name': 'Piotr', 'age': 33, 'city': 'Wroclaw', 'is_a_programmer': True},
    {'name': 'Bart', 'age': 33, 'city': 'Lublin', 'is_a_programmer': True},
    {'name': 'Michal','age': 34, 'city': 'Pulawy', 'is_a_programmer': False}]

for people in peoples:
    print(f"A person name is: {people.get('name')}")
    print(f"A person age is: {people.get('age')}")
    print(f"A person city is: {people.get('city')}")
    print(f"Is a programmer?: {people.get('is_a_programmer')}")
    print('#####################3')