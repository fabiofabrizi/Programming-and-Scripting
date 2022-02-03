# Give the absolute value of a number
#
# https://docs.python.org/3/library/functions.html#abs
# works on int, float and complex numbers

number = float(input("Enter a number:"))
absoluteValue = abs(number)
print('The absolute value of {} is {}'.format(number, absoluteValue))