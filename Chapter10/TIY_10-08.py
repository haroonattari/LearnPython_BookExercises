cat_filename = 'cats1.txt'
dog_filename = 'dogs.txt'

try:

    with open(cat_filename) as cat_file:
        catlines = cat_file.readlines()
        print(catlines)

    with open(dog_filename) as dog_file:
        doglines = dog_file.readlines()
        print(doglines)

except FileNotFoundError as filenotfoundex:
    print("Error opening file, details follows\n",filenotfoundex)

