# Follow along from the tutorial - 'Refactor'
# Fabio Fabrizi

# Read in two numbers and multiply them

"""
num1 = int(input("Enter a number "))
num2 = int(input("And another "))

answer = num1 * num2

print(f"answer is {answer}")
"""

# Modified version to catch exceptions
# But notice how we're duplicating the code
# Great example to put into a function
"""
num1 = False
while (num1 == False):
    try:
        num1 = int(input("Enter a number "))
    except ValueError:
        print("That was not a number ", end="")

num2 = False
while (num2 == False):
    try:
        num2 = int(input("Enter a number "))
    except ValueError:
        print("That was not a number ", end="")

answer = num1 * num2
print(f"answer is {answer}")
"""

# Code above put into a function:
"""
def readNum():
    num = False
    while (num == False):
        try:
            num = int(input("Enter a number "))
        except ValueError:
            print("That was not a number ", end="")
    return num

num1 = readNum()
num2 = readNum()

answer = num1 * num2
print(f"answer is {answer}")
"""

# And improved again
# See how it's simplified with the use of a message
def readNum(message = "Enter a number: "):
    num = False
    while (num == False):
        try:
            num = int(input(message))
        except ValueError:
            print("That was not a number, ", end="")
    return num

num1 = readNum()
num2 = readNum("enter second number: ")

answer = num1 * num2
print(f"answer is {answer}")
