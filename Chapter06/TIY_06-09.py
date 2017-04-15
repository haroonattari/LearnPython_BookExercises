favorite_places = {
    'junaid': ['China', 'Japan', 'United States of America'],
    'haroon': ['Saudi Arabia', 'United Arab Emirates'],
    'farooq': ['Malaysia', 'Singapore', 'Australia'],
}

for key in favorite_places.keys():
    print(key.title())
    for place in favorite_places[key]:
        print(place)
    print("\n")

