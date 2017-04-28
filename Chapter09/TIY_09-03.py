'''
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
'''


class User():

    def __init__(self, first_name, last_name, user_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__user_id = user_id

    def describe_user(self):
        print("{2}: {0}, {1}".format(self.__last_name, self.__first_name, self.__user_id))

    def greet_user(self):
        print("Hi {0}, welcome to Python!\n".format(self.__first_name))


user1 = User('Haroon', 'Attari', 'haroonattari')
user2 = User('Owais', 'Raza', 'owaisraza')
user3 = User('Junaid', 'Raza', 'junaidraza')

users = [user1, user2, user3]

for user in users:
    user.describe_user()
    user.greet_user()


