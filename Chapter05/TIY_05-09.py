users_list = ['haroon', 'farooq', 'jawed', 'abdul sattar', 'admin', '']

for user in users_list:
    if user == 'admin':
        print("Hello {0}, would you like to see a status report?".format(user.title()))
    elif user == '':
        print("We need to find some users!")
    else:
        print("Hello {0}, thank you for logging in again?".format(user.title()))
