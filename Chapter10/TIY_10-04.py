print('Welcome Guests!')
print('Please enter your name here to get yourself registered for the seminar')
print('In case you want to quit, write \'quit\' and enter')

filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    while True:
        name = input('Enter your name or write \'quit\' to exit: ')

        if name.lower() == 'quit':
            break

        file_object.write("{0}\n".format(name.title()))

print('Program successfully terminated!')