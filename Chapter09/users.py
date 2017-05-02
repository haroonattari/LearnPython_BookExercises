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

class Privileges():

    def __init__(self, *privileges):
        self.__privileges = privileges

    def show_privileges(self):
        for privilege in self.__privileges:
            print(privilege)

class Admin(User):

    def __init__(self, first_name, last_name, user_id):
        super().__init__(first_name, last_name, user_id)
        self.__privileges = Privileges("can add post", "can delete post", "can ban user", "can create user")

    def show_privileges(self):
        print("{0} is an Admin with the following privileges".format(self.show_first_name()))
        self.__privileges.show_privileges()
