# Day 48
# Local variable and global variable in Python
# A variable declared inside a function is a local variable.
# A variable declared outside a function is a global variable.
# Local variables are only accessible inside the function that declares them.
# Global variables are accessible throughout the program.
# Example:

x = 4
print(x)

def Hello():
    x = 5
    print(f"The local variable is {x}") # Local variable is accessible inside the function
print(x)
Hello()

print(f"The global variable is {x}") # Global variable is accessible outside the function

# Global Keyword
# If you want to modify a global variable inside a function, you can use the global keyword.

x = 10
print(x)

def my_fn():
    global x
    x = 20
    print(f"Inside the function, the global variable is {x}")
my_fn()

print(x)  # Now the global variable is modified inside the function.
