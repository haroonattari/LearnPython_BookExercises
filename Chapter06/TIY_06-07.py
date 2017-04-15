person1 = {
    'first_name': 'Muhammad',
    'last_name': 'Haroon',
    'age': 43,
    'city': 'Karachi'
}

person2 = {
    'first_name': 'Hussain',
    'last_name': 'Ali',
    'age': 42,
    'city': 'Peshawar'
}

person3 = {
    'first_name': 'Shahzad',
    'last_name': 'Sarang',
    'age': 37,
    'city': 'Lahore'
}

people = [person1, person2, person3]

for person in people:
    print("Mr. {0} lives in {1}. His age is {2}".format(person['first_name'], person['city'], person['age']))