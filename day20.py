# Day 20
# Functions in python

# Function is a reuseable block of code which is used to perform any specific task.
# Function can be called anytime once defined to reduce redundancy in code.
# Functions can be accessed by the word def.
# and is called using return function.

# Example-:
def greet(name):
    return f"Hello,{name}"
print(greet("Atharva"))

# Example 2-:
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if (a>b):
        print("The first number is Greater than second")
    elif (a==b):
        print("The numbers are equal")
    else:
        print("The second number is Greater than or equal to first")

# pass is used when I want to write the code body later on and it ensures that the code runs smoothly.
# even if the function is defined or a code is defined w/o body.
# pass is used in functions, classes etc.

def isLesser(a,b):
    pass

a = 22
b = 21
calculateGmean(a,b)
isGreater(a,b)

c = 25
d = 30
calculateGmean(c,d)
isGreater(c,d)

e = 50
f = 50
calculateGmean(e,f)
isGreater(e,f)

# there are two types of functions
# 1. Built-in functions
# 2. User-defined functions
# Built-in functions are the functions which are already defined in python and are used to perform specific task.
# User-defined functions are the functions which are defined by the user to perform specific task.