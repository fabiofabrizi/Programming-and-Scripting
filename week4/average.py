# Write a program (average.py) that keeps reading numbers until the user
# enters a 0. (the program should append each of them into a list)
# The program should then print out each of the numbers entered and the
# average of them. (Use a list)
# 
# Fabio Fabrizi

numbers = [] # Set the empty list 

number = int(input("enter number (0 to quit): "))

while number != 0:
    numbers.append(number) # We add the number entered to the list

    # Read the next number and check if 0
    number = int(input("Please enter another number (0 to quit): "))

# Now we're out the loop - (see chapter 2 in ATBSWP)
# We can start the task of averaging
# First, print out all numbers that the user entered 
for value in numbers: # Loops through each element in array.
    print(value)

# Average is going to be a float.
average = float(sum(numbers)) / len(numbers)
print("The average is {} ".format(average))