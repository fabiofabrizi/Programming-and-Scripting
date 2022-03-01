# This is the extra question
# Take in an amount in dollars (float) 
# and return absolute value in cent


dollar = float(input("Enter a dollar amount, ie 15.99: "))

cents = abs(int(dollar * 100))

print("{} in cents is {}".format(dollar, cents))