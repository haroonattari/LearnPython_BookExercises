favourite_numbers = {
    'haroon': [304, 305, 306, 307],
    'farooq': [414, 415, 416, 417],
    'jawed': [501, 502],
    'abdul sattar': [503, 504, 505]
}

for friend, favourite_numbers in favourite_numbers.items():
    print(friend)
    for favourite_number in favourite_numbers:
        print(favourite_number)

