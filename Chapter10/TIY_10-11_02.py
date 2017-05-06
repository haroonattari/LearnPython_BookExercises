import json

filename = 'favourite_number.json'

try:
    with open(filename) as file_object:
        number = json.load(file_object)
        print("I know your favourite number. It's {0}".format(number))
except FileNotFoundError as fnfe:
    print("Error reading file. \n{0}".format(fnfe))

