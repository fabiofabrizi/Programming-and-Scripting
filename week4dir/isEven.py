# Program that prompts user to enter a number, and the program will
# tell the user whether the nunber is even or odd
#
# Author: Fabio Fabrizi


number = int(input("Please enter an integer: "))

if (number % 2)== 0:
    print ("{} is an even number.".format(number))
else:
    print("{} is an odd number.".format(number))