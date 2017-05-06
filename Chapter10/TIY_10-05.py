print('Welcome Programmers!')
print('Why you like programming?')
print('In case you want to quit, write \'quit\' and enter')

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    while True:
        name = input('Enter your name or write \'quit\' to exit: ')

        if name.lower() == 'quit':
            break

        file_object.write("{0}\n".format(name.title()))

print('Program successfully terminated!')