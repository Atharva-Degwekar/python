# Day 22
# Introduction to Lists in Python

# List are ordered collection of data items
# They store multiple items in a single variable
# List items are separated by commas and enclosed within square brackets
# Lists are changeable meaning we can alter them after creation
# Lists are ordered meaning we can access items by their index

# Example-:
l1 = [1,2,3,4,5,6,7,8]
l2 = ["Red","Yellow","Blue","Green"]
print(type(l1))
print(type(l2))
print(l1,l2)

# Index wise selection and printing
print(l1[0])
print(l1[1])
print(l1[2])

# in list we can store any data type
details = ["Atharva", 18 , "FY B.TECH CSE", True , 10.00]
print(type(details),details)

# Negative indexing of lists
# Negative indexing means we start from the end of the list
print(l1[-1])
print(l1[-2])
print(l1[-3])
print(l1[-4])
print(l1[-5])
print(l1[-6])
print(l1[-7])
print(l1[-8])

# Avoiding negative indexing in lists
print(l1[len(l1)-3])    # output will give 6 same as print(l1[-3])

# in keywords using if else
if "Atharva" in details:
    print(True)
else:
    print(False)

# Checking particular letters in a given string
if "arv" in "Atharva":
    print("Yes, its present")
else:
    print("Cannot find!")

# Lists slicing
marks = [31,32,39,29,30,30,21,35]
print(max(marks))
print(min(marks))
print(marks[:])
print(marks[1:3])
print(marks[1:-1])

# here we say that last one is jump index it will skip the no of elements marks in this case it will choose alternate marks
print(marks[1:8:2])

# List comprehension
# List comprehension is a way to create a new list from an existing list or other iterable by applying an expression to each element.
# It is a more concise way to create lists.
# The basic syntax of list comprehension is as follows:

lst = [i for i in range(10)]
print(lst)

lst2 = [i*i for i in range(10)]
print(lst2)

lst2 = [i*i for i in range(10) if i%2==0]
print(lst2)

names = ["Bruno" , "Ed Sheeran" , "Enrique Iglasias" , "JB"]
names_with_r = [items for items in names if "r" in items]
names_with_i = [items for items in names if len(names) > 2]
print(names_with_r)
print(names_with_i)