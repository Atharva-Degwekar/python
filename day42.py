# Day 42
# Enumerate function in python
# Enumerate function is a built in function in python that allows you to loop over a sequence (such as a list, tuple or string) and get the index and value of each element in the sequence.
#  It is often used when you want to keep track of the index of the current element in the sequence.
# Basic example:
# This code snippet is demonstrating the use of the `enumerate` function in Python.
# e = "THERE IS NOTHING LEFT TO BE PRINT."
# fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
# for index, fruit in enumerate(fruits):
#     print(f"{index + 1}-:{fruit}")
# else:
#     print(f"Error 404,{e}")
# print("We can make anything from the fruits")


# if we want to spicify the index from where we want to start the index we can use the start parameter in the enumerate function.
# Example:
e = "THERE IS NOTHING LEFT TO BE PRINT."
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
for index, fruit in enumerate(fruits,start=1):
        
    if fruits:
        print(f"{index}-:{fruit}")
    else:
        print(f"Error 404,{e}")
        
print("We can make anything from the fruits")
