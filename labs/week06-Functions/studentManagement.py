# Question 2 from quiz.
# Write a function to print out menu of commands
# that the user can perform. 
# The function returns what the user chose.

def displayMenu():
    print("What would you like to do? ")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter a/v/q: ").strip()

    # Strips returns a copy of the string with the leading and trailing
    # whitespace removed. 

    return choice
# test the function
choice = displayMenu()
print("you chose {}".format(choice))