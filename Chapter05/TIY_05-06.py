age = int(input("What is your age? "))

if age < 2:
    person_type = 'a baby'
elif age >= 2 and age < 4:
    person_type = 'a toddler'
elif age >= 4 and age < 13:
    person_type = 'a kid'
elif age >= 13 and age < 20:
    person_type = 'a teenager'
elif age >= 20 and age < 65:
    person_type = 'an adult'
elif age >= 65:
    person_type = 'an elder'

print("You are {0}".format(person_type))
