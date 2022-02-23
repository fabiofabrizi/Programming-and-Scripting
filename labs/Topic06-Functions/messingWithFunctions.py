# Lecture Follow along - Week 6
# Fabio Fabrizi

"""
def cube(number):
    print(number)
    return number **3

num = 6
answer = cube(num)
print("Cube of", num, " is", answer)
"""

# And expanded on some more to include the power as a variable:
def toPower(number, power = 3):
    print(number)
    return number ** power

num = 7
answer = toPower(num)
print("Power of", num, " is", answer)

answer = toPower(5, 2)
print(answer)