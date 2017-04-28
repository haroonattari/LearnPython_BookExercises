'''
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
'''


class User():

    def __init__(self, first_name, last_name, user_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__user_id = user_id
        self.__login_attempts = 0

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

user1 = User('Haroon', 'Attari', 'haroonattari')
user2 = User('Owais', 'Raza', 'owaisraza')
user3 = User('Junaid', 'Raza', 'junaidraza')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()

user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()


users = [user1, user2, user3]

for user in users:
    user.describe_user()
    user.greet_user()
    user.login_attempted()


