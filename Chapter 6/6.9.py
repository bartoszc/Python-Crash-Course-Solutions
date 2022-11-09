favorite_places = {'Piotr': ['Wroclaw', 'Lublin', 'NY'],
                   'Bart': ['Warszawa', 'Barcelona', 'Bergamo'],
                   'Michał': ['Puławy']}

for person, favorites in favorite_places.items():
    if len(favorites) == 1:
        print(f"{person}'s favorite place is: \n\t{favorites[0]}")
    else:
        print(f"{person}'s favorite places are:")
        for place in favorites:
            print('\t' + place)
