# Question 3 on the quiz
# Fabio Fabrizi

# Keep displaying the menu until the user picks q.
# sounds like a loop is needed.

from dis import dis


def displayMenu():
    print("What would you like to do? ")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter a/v/q: ").strip()
    return choice

def doAdd():
    # fill this in later
    print("in adding")
def doView():
    # fill this in later
    print("in viewing")

# main program
choice = displayMenu()
while (choice != 'q'):
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print("\n\nplease select either a, v or q")
    choice = displayMenu()