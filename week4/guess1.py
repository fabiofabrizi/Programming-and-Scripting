# Write a program that prompts the user to guess a number, the
# program should keep prompting the user to guess the number until the user
# gets the right one

# Fabio Fabrizi

numberToGuess = 30 # Initialise variable

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    print("Wrong")
    guess = int(input("Please guess again: "))
print("Well done! Yes, the number was ", numberToGuess)