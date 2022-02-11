# Program that prompts user to enter a number, and the program will
# tell the user whether the nunber is even or odd
#
# This is modified so that the user is continually prompted to 
# enter a number until they enter -1
# Author: Fabio Fabrizi

"""""
number = int(input("Please enter an integer: "))
while number != -1:
    if (number % 2)== 0:
        print ("{} is an even number.".format(number))
    else:
        print("{} is an odd number.".format(number))
else: print("You've entered -1")
"""

# Initialise
number = 0
# Put a condition for the loop to run
while number != -1:
    number = int(input("Please enter an integer: "))
    if number == -1:
        print("Well done, you entered the number to finish this program")
        break
    print("you entered " + str(number))