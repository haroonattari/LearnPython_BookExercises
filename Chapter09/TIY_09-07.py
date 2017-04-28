'''
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
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

class Admin(User):

    def __init__(self, first_name, last_name, user_id):
        super().__init__(first_name, last_name, user_id)
        self.__privileges = ["can add post", "can delete post", "can ban user", "can create user"]

    def show_privileges(self):
        print("{0} is an Admin with the following privileges".format(self.show_first_name()))
        for privilege in self.__privileges:
            print(privilege)

user1 = Admin('Haroon', 'Attari', 'haroonattari')

user1.show_privileges()