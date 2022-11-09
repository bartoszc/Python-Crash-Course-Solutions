cities = {'Prague':    {'country': 'Czechia', 'population': 13_000_000, 'fact': 'Has many bridges'},
          'Barcelona': {'country': 'Spain', 'population': 5_500_000, 'fact': 'By the sea'},
          'Warsaw':    {'country': 'Poland', 'population': 3_000_000, 'fact': 'Was destroyed during WWII'}}

for city, data in cities.items():
    print(f"Information about: {city}")
    print(f"{city} belongs to {data.get('country')}")
    print(f"{city} population is more or less: {data.get('population')}")
    print(f"Interesting fact about the city: {city} is that: {data.get('fact')}")
    print('#############################3')
