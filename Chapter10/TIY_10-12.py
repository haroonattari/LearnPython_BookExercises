import json

def read_favourite_number(filename):

    try:
        with open(filename) as file_object:
            number = json.load(file_object)
        return number
    except FileNotFoundError as fnfe:
        number = ask_favourite_number(filename)
        return number

def ask_favourite_number(filename):

    try:
        number = input("Let us now your favourite number: ")
        with open(filename, 'w') as file_object:
            json.dump(number, file_object)
        return number
    except FileNotFoundError as fnfe:
        print("Error writing to file. \n{0}".format(fnfe))


filename = 'new_favourite_number.json'

number = read_favourite_number(filename)

print("I know your favourite number. It's {0}".format(number))


