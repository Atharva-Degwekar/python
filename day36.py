# Day 36
# Exception Handling / Error Handling
# Try, Except, Finally Blocks
# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs
# Exception handling deals with these events to avoid the program or system crashing and without this process,
# exceptions would disrupt the normal operation of program

# Exceptions in Python
# Python has a built-in exception handling mechanism that allows you to handle runtime errors and exceptions(something in the program goes wrong)
# When these exceptions occurs, the Python interpreter stops the current process and passes it to the calling process until it is handled.
# If not handled the program will crash

# Python try, except
# The try block contains the code that might raise an exception.
# The except block contains the code that will be executed if an exception is raised in the try block.
# The finally block contains the code that will be executed regardless of whether an exception is raised or not

# Syntax:

a = input("Enter the number")

print(f"The multiplication table of {a} is -:")

try:
    for i in range(1,11):
        print(f"{int(a)} X {int(i)} = {int(a)*i}\n")
except Exception as e:
        print(f" The program is not working because of this error {e}")
finally:
    for j in range(1,11):
        print(f"{int(12)} X {int(j)} = {int(12)*j}\n")

# We can handle specific type of errors in python.
# For example, we can handle ValueError, TypeError, ZeroDivisionError, etc.

try:
    num = int(input("Enter the number"))
    a = ([6,4])
    print(a[num])
except ValueError as v:
    print(f"Oops! You haven't entered the value in int {v}")
except IndexError as i:
    print(f"Oops! You haven't entered the value in int {i}")