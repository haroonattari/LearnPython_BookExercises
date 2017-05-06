print("Continue entering numbers and I will add them for you")

numlist = []

while True:
    try:
        number = input("Enter number: ")

        if int(number) == 0:
            break

        numlist.append(int(number))

    except ValueError:
        print("Error converting last provided number")

if len(numlist) > 1:
    print("Sum of {0} numbers entered is {1}".format(len(numlist), sum(numlist)))

