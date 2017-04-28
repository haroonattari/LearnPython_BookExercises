''''
9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
'''

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.__restaurant_name = restaurant_name
        self.__cuisine_type = cuisine_type
        self.__number_served = number_served

    def describe_restaurant(self):
        print("{0} has {1} cuisine type".format(self.__restaurant_name, self.__cuisine_type))

    def open_restaurant(self):
        print("{0} restaurant is open now!".format(self.__restaurant_name))

    def set_number_served(self, number_served):
        self.__number_served = number_served

    def increment_number_served(self, number_served):
        self.__number_served += number_served

    def describe_number_served(self):
        print("{0} restaurant has served {1} customers so far".format(self.__restaurant_name, self.__number_served))



bakra_hotel = Restaurant('Bakra Hotel', 'Pakistani')

bakra_hotel.describe_restaurant()
bakra_hotel.open_restaurant()
bakra_hotel.describe_number_served()
bakra_hotel.set_number_served(10)
bakra_hotel.describe_number_served()
bakra_hotel.increment_number_served(5)
bakra_hotel.describe_number_served()

