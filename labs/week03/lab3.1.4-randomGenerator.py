# program that prints out a random number between 1 and 10
import random

# https://docs.python.org/3/library/random.html
# The random module generates a list of pseudo-random numbers.

# Generate a random number between 1 and 10 (original)
# but I played about with the numbers
# number = random.randint(-10,50)
# print("here is a random number {}".format(number))

# And here is a random number generated a range determined by the user

x = int(input("Please enter a number: "))
y = int(input("Please enter another number: "))

number = random.randint(x,y)

# Simple version
# print("Here is a random number between "+ str(x) + " and " + str(y) + ": " + str(number))

# But this is the tidy version
print("Here is a random number between {} and {}: {}".format(x, y, number))