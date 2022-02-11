# Write a program that prompts the user to guess a number, the
# program should keep prompting the user to guess the number until the user
# gets the right one

# This is a modification of guess2.py that generates a random number 
# for the input each time
# Fabio Fabrizi

from random import randint


numberToGuess = randint(1, 100) # The range of numbers generated
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else: # I know it cant be equal or too low, so it must be too high
        print("too high")
    guess = int(input("Please guess again:"))
print("Well done! Yes the number was ", numberToGuess)