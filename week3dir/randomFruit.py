# Program to print out a random fruit 
# List of fruits to be randomly chosen from 
# determined by the programmer

import random
fruits = ['Apple', 'Orange', 'Banana', 'Pear']
# we want a random number between 0 and length-1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))