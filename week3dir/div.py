# Program that reads in two numbers and
# outputs the integer answer and remainder

from math import remainder


x = int(input("Enter the first number: "))
y = int(input("Enter the number you want to divide by: "))

answer = x // y # This gives the integer answer
remainder = x % y # This gives the remainder

# My simple way below
# print(str(x) + " divided by " + str(y) + " is " + str(answer) + " remainder " + str(remainder))

# Variables can be placed in the curly braces, defaults to order that they're 
# entered in, i.e. x, y and ans
print("{} divided by {} is {} with remainder {}".format( x, y, answer, remainder))