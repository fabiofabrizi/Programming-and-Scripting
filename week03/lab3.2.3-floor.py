# This program floors a number that the user enters

import math

numberToFloor = float(input("Enter a float number, i.e. 4.0 :"))
flooredNum = math.floor(numberToFloor)

print("{} floored is {}".format(numberToFloor, flooredNum))