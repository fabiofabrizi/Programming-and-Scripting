# This program rounds a number

# This is for other attempts at rounding using math.floor() and math.ceil()
import math

numberToRound = float(input("Enter a float number:")) 
roundedNumber = round(numberToRound)
print ( '{} rounded is {}'.format(numberToRound,roundedNumber))

# Rounded down
# print(math.floor(numberToRound))

# Rounded up
# print(math.ceil(numberToRound))