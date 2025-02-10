# Day 9
# Typecasting
# Typecasting is the process of converting the data type of a variable to another data type.
# Python provides several built-in functions for typecasting.
# The most common typecasting functions are:
# - int(): Convert to integer
# - float(): Convert to float
# - str(): Convert to string
# Example:
x = "5"
y = 5
z = 5.0
print(int(x))  # Output: 5
print(float(y))  # Output: 5.0
print(str(z))  # Output: "5.0"
# Typecasting is useful when you want to perform operations on variables of different data types.
# There are two types of typecasting:
# - Implicit typecasting: Python automatically converts the data type of a variable to another data type.
# - Explicit typecasting: You explicitly convert the data type of a variable to another data type using typecasting functions.
# Example:
x = 5
y = 5.0
z = "5"
print(x + y)  # Output: 10.0
print(x + int(z))  # Output: 10
print(str(x) + z)  # Output: "55"
# In the above example, Python automatically converts the integer variable x to a float before performing addition.