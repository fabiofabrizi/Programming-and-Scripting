# Program (sub.py) that reads in two numbers 
# and subtracts the first one from the second one.

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

answer = x - y

# The below works - I wanted to try it a 'Simple' way before using {}
print(str(x) + " minus " + str(y) + " is " + str(answer))

# Can also substitute the actual variable names in the curly braces 
# print("{0} minus {1} is {2} ".format(x, y, answer))

print("{} minus {} is {} ".format(x, y, answer))

# NB - When the program is running and the user tries to enter a decimal, 
# it throws an error:
# ValueError: invalid literal for int() with base 10: '6.6'
# We could use float() instead of int.