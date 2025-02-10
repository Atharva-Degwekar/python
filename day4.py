# Day 4
# Basic operators
# Python has the following basic operators:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic operators
# Arithmetic operators are used to perform mathematical operations.

print(5 + 3)  # Addition
print(5 - 3)  # Subtraction
print(5 * 3)  # Multiplication
print(5 / 3)  # Division
print(5 % 3)  # Modulus
print(5 ** 3)  # Exponentiation
print(5 // 3)  # Floor division

# Assignment operators
# Assignment operators are used to assign values to variables.

x = 5  # x = 5
x += 3  # x = x + 3
x -= 3  # x = x - 3
x *= 3  # x = x * 3
x /= 3  # x = x / 3
x %= 3  # x = x % 3
x **= 3  # x = x ** 3

# Comparison operators
# Comparison operators are used to compare two values.

print(5 == 5)  # True
print(5 != 5)  # False
print(5 > 3)  # True
print(5 < 3)  # False
print(5 >= 3)  # True

# Logical operators
# Logical operators are used to combine conditional statements.

print(5 > 3 and 5 < 3)  # False
print(5 > 3 or 5 < 3)  # True
print(not (5 > 3))  # False
print(not (5 < 3))  # True

# Identity operators
# Identity operators are used to check if two variables are the same object.

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is y)  # False
print(x is z)  # True
print(x is not y)  # True
print(x is not z)  # False

# Membership operators
# Membership operators are used to check if a sequence is present in an object.

fruits = ["apple", "banana"]
print("apple" in fruits)  # True
print("orange" not in fruits)  # True

# Bitwise operators
# Bitwise operators are used to perform bitwise operations on integers.
# The following are the bitwise operators in Python:
# & (AND)
# | (OR)
# ^ (XOR)
# ~ (NOT)
# << (Left shift)
# >> (Right shift)
# The following example demonstrates the use of bitwise operators:

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
print(a & b)  # 12 = 0000 1100
print(a | b)  # 61 = 0011 1101
print(a ^ b)  # 49 = 0011 0001
print(~a)  # -61 = 1100 0011
print(a << 2)  # 240 = 1111 0000
print(a >> 2)  # 15 = 0000 1111