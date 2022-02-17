"""
Create a program that puts 10 random numbers into a queue(list), the
program should then output all the values in the queue, then take the
numbers from the queue one at a time, print it and the current numbers still
in the queue. (the command pop(0) takes the first element out of a list)

"""
# Need to import the random module so that we can generate random numbers
import random

# Define the queue and initialise it.
queue = []

# Define a variable for the 10 random numbers - because this could always be changed later
numberOfRands = 10
rangeTo = 100 # The random number upper limit, i.e. no numbers above 100 will be generated

# At the start, put 10 random numbers into queue. NB 10 can be changed by changing variable.
for n in range(0, numberOfRands):
    queue.append(random.randint(0, rangeTo))

print("queue is {}".format(queue))

while len(queue) != 0:

    currentNumber = queue.pop(0) # Take the first element out the list
    print("current Number is {} and the queue is {} ". format(currentNumber, queue))

    print("The queue is now empty")

