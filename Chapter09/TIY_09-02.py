''''
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each instance.
'''

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.__restaurant_name = restaurant_name
        self.__cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("{0} has {1} cuisine type".format(self.__restaurant_name, self.__cuisine_type))

    def open_restaurant(self):
        print("{0} restaurant is open now!".format(self.__restaurant_name))



bakra_hotel = Restaurant('Bakra Hotel', 'Pakistani')
bakra_hotel.describe_restaurant()
bakra_hotel.open_restaurant()

keybees = Restaurant('Kaybees', 'Chinese')
keybees.describe_restaurant()
keybees.open_restaurant()

kolachi = Restaurant('Kolachi', 'Italian')
kolachi.describe_restaurant()
kolachi.open_restaurant()

