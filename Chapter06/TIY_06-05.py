rivers_of_country = {
    'nile': 'Egypt',
    'indus': 'Pakistan',
    'yangtze': 'China',
    'kabul': 'Afghanistan',
    'euphrates': 'Iraq',
}

for river, country in rivers_of_country.items():
    print("The {0} river runs through {1}".format(river.title(), country))

for river in rivers_of_country.keys():
    print("The {0} river".format(river.title()))

for country in rivers_of_country.values():
    print(country)