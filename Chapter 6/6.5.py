rivers = {
    'nile': 'egipt',
    'rio': 'brasil',
    'dune': 'hungary',
}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)