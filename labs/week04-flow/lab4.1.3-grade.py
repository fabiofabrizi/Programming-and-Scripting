# program to read in a student's percentage mark and prints out corresponding 
# the grade (check that the percentage is valid:
#
# Author: Fabio Fabrizi

percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
    # Setting up the marks here.
elif percentage < 40:
    print("Fail")
elif percentage < 50: 
 print ("Pass")
elif percentage < 60: 
 print ("Merit1")
elif percentage < 70: 
 print ("Merit2")
else: 
 print ("Distinction")