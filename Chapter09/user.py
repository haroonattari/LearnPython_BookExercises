'''
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
'''


class User():

    def __init__(self, first_name, last_name, user_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__user_id = user_id
        self.__login_attempts = 0

    def show_first_name(self):
        return self.__first_name

    def describe_user(self):
        print("{2}: {0}, {1}".format(self.__last_name, self.__first_name, self.__user_id))

    def greet_user(self):
        print("Hi {0}, welcome to Python!".format(self.__first_name))

    def increment_login_attempts(self):
        self.__login_attempts += 1

    def reset_login_attempts(self):
        self.__login_attempts = 0

    def login_attempted(self):
        print("{0} has attempted login {1} time(s)".format(self.__first_name,self.__login_attempts))
