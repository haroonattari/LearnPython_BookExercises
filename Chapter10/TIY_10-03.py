print('Welcome Guests!')
print('Please enter your name here to get yourself registered for the seminar')

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    name = input('Enter your name or write \'quit\' to exit: ')

    file_object.write("{0}\n".format(name.title()))

print('Program successfully terminated!')