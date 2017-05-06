print("Enter two numbers and I will add them for you")

num1 = input("First number: ")
num2 = input("Second number: ")

try:
    sumnum = int(num1) + int(num2)
    print("Sum of {0} and {1} is {2}".format(num1, num2, sumnum))
except ValueError:
    print("Error converting one of the provided numbers")

