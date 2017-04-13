numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

for number in numbers:
    if number == 1:
        print("{0}st".format(number))
    elif number == 2:
        print("{0}nd".format(number))
    elif number == 3:
        print("{0}rd".format(number))
    elif number > 3:
        print("{0}th".format(number))
