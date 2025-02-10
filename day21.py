# Day 21
# Function in Arguments

# There are 4 types of arguments which we can run:
# 1. Default arguments
# 2. Keyword arguments
# 3. Variable length arguments
# 4. Required arguments

# Default arguments are the arguments which are passed to the function with a default value.
# Keyword arguments are the arguments which are passed to the function with the keyword of the argument.
# Variable arguments are the arguments which are passed to the function with a variable number of arguments.
# Required arguments are the arguments which are passed to the function when it is called.

# Default arguments
def calculateAverage(a=3,b=9):
    Average = (a+b)/2
    print(Average)
calculateAverage()

# Keyword arguments
def calculateAverage(a,b):
    Average = (a+b)/2
    print(Average)
calculateAverage(a=3,b=9)

# Variable arguments
def Average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        Average = sum/len(numbers)
    print(Average)
Average(1,2,3,4,5,6,7,8,9,10)

# Required arguments
def calculateAverage(a,b):
    Average = (a+b)/2
    print(Average)
calculateAverage(3,9)

# Return Function
# Return function is used to return the value of expression back to the calling function.
# It is used to return one value from a function.

# Return Function
def Average(*numbers):
    sum  = 0
    for i in numbers:
        sum = sum + i
        return sum/len(numbers)
c = Average(4,5,6)
print(c)