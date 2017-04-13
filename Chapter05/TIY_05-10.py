current_users = ['haroon', 'farooq', 'jawed', 'abdul sattar', 'admin', '']
new_users = ['haroon', 'owais', 'junaid', 'JAWED']

for user in new_users:
    if user.lower() in current_users:
        print("that username ({0}) has already been taken.".format(user))
    else:
        print("{0} is available".format(user))