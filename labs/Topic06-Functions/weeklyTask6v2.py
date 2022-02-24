# This is an attempt at the task for Week 6.
# Write a program that takes a positive floating-point number as it's input 
# and outputs an guessimation of it's square root.
# A function called sqrt has to be created - not allowed to use the built-in 
# square root function.
# I looked at the following websites for the calculations:
# https://www.school-for-champions.com/algebra/square_root_guess.htm#.YheTzOjP0Q8
# https://en.wikipedia.org/wiki/Newton%27s_method

# I'm going to check whether the user enters a positive float and if not, prompt them to do so.
# I'm also going to set guess initially to 5, but will check as I go along how close the 
# iteration is to the square root of num, then stop.
# As we're talking of iterations, a loop is needed. 

# Author: Fabio Fabrizi

# Formula:
# √num = 0.5*(guess + (num/guess))

def newtonSquareRoot(num):
    guess=0.5*num
    better=0.5*(guess+num/guess)
    while better!=guess:
        guess=better
        better=0.5*(guess+num/guess)
    return guess
print(newtonSquareRoot(64))