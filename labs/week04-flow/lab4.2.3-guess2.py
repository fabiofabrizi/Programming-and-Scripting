# Write a program that prompts the user to guess a number, the
# program should keep prompting the user to guess the number until the user
# gets the right one

# This is a modification of guess1.py that gives the user a hint by 
# telling them whether their guess was too high or too low.
# Fabio Fabrizi

numberToGuess = 30
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else: # I know it cant be equal or too low, so it must be too high
        print("too high")
    guess = int(input("Please guess again:"))
print("Well done! Yes the number was ", numberToGuess)