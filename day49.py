# day 49
# File Handling in python
# File handling is an important part of any web application.
# It is used to read and write data from a file.
# Python provides inbuilt functions for creating, writing and reading files.
# There are various modes in which you can open a file in python.
# The most common modes are:
# r - Read mode. Opens a file for reading only.
# w - Write mode. Opens a file for writing only.
# a - Append mode. Opens a file for appending data.
# r+ - Read and write mode. Opens a file for reading and writing.
# w+ - Write and read mode. Opens a file for writing and reading.
# a+ - Append and read mode. Opens a file for appending and reading.

f = open("my_file.txt", "r")
print(f)
# Output: <_io.TextIOWrapper name='my_file.txt' mode='r' encoding='cp1252'> this is the desc of the file

# reading a file
text = f.read()
print(text)
f.close()

# writing a file
# f = open("my_file.txt", "w")
# f.write("5. Be the part of the solution, not the problem.")
# f.close()
# This mode will overwrite the file content.
# Instead of write mode you can use append mode to add content to the file.

# Appending to a file
f = open("my_file.txt", "a")
f.write("6. Be the part of the solution, not the problem.")
f.close()

# Reading a file as a binary file.
f = open("my_file.txt", "rb")
