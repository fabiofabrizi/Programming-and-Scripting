# Program that reads in a students percentage and prints out a grade
# 
# Author: Fabio Fabrizi


percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    print("Pleae enter a number between 0 and 100")
elif percentage < 40:
    print("Fail")
elif percentage < 49.5:
    print("Pass")
elif percentage < 59.5:
    print("Merit1")
elif percentage < 69.5:
    print("Merit2")
else:
    print("Distinction")