# Write a program (topthree.py) generates 10 random numbers (0-100) ,
# prints them out then prints out the top three.
#
# Fabio Fabrizi

# Use the randint() built-in function to generate some random numbers

import random
# I programming the general case
howMany = 10 # Because it's asking for 10 random numbers
topHowMany = 3 # These are the three highest values
rangeFrom = 0 
rangeto = 100
numbers = []

for i in range(0,10):
    numbers.append(random.randint(rangeFrom, rangeto))
print("{} random numbers\t {}".format(howMany, numbers))

# Play with copy() 
topOnes = numbers.copy()
# Sorting the list and reversing it so that the largest is first
topOnes.sort(reverse = True)
# Print the top three from 0 to the third element
# NB the element could be changed in the future by changing topHowMany
print ("The top {} are \t\t {}".format(topHowMany,topOnes[0:topHowMany]))