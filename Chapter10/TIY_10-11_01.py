import json

filename = 'favourite_number.json'

number = input("Let us know your favourite number: ")

try:
    with open(filename, 'w') as file_object:
        json.dump(number, file_object)
except FileNotFoundError as fnfe:
    print("Error writing file. \n{0}".format(fnfe))

