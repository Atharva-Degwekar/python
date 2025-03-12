# Day 46
# os module in python
# The os module in python is built-in library that provides a way to interact with the operating system.
# It allows you to perform various operations such as creating and deleting directories, reading and writing files, and running system commands.
# Here are some common functions and methods provided by the os module:

import os

if (os.path.exists("data")):
    print("data directory already exists")
else:
    os.mkdir("data")
    print("data directory created")

# Now lets suppose I want to create 100 files in data directory I will not spare my time to create 100 files manually. 
# I will use python to create 100 files in data directory.
# Instead I will do it like this

for i in range(1,100):
    os.makedirs(f"data/Day {i+1}")
