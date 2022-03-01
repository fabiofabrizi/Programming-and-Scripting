# Second example from lecture
# Fabio Fabrizi

print("hi", 55, 343, [], {}, sep=":")

# flexible number of arguments

def flex1(*args):
    print(type(args))
    for x in args:
        print(x)

#flex1(1, 2, 3, "hi", [])

# keyword arguments
def flex2(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"key {key} is {value}")

flex2(age = 23, title = "hi")

def ave(*args):
    sumOfNumbers = sum(args)
    length = len(args)
    return sumOfNumbers / length

print(ave(2, 3, 4))