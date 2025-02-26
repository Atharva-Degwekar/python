# Day 30
# Recursion in python
# Recursion is the process of defining something in terms of itself
# It is a powerful tool for solving problems that have a recursive structure
# In real world the example of recursion is quite simple we can say that two parallel mirrors facing each others
# Lets take example

def factorial(n):
    '''This takes n as input and calculate the factorial of N'''
    if(n == 0 or n == 1):
        return 1
    else:
        return (n * factorial(n-1))

# Test the function and the recursion
print(factorial(5))

#rhis is how the above fn works
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 factorial(1)
# 5 * 4 * 3 * 2 * 1

# Quick Quiz
# Fibonacci series
# f(0) = 0
# f(1) = 1
# f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    if (n == 0 or n == 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(6))