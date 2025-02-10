# Day 12
# String slicing
# Given a string, find the first and last occurrence of a character in the string.
# If the character is not found, return -1 for both the first and last occurrence.
# strings are also known as array as we can access the elements from the strings.
# Now we can access the elements of strings by slicing and also we can check for how many chars are there in a particular string
# we can also check the length of the string by using len() function in python.

# the below code access the length of the chars
name = ("Atharva, Varun, Tara")
print(len(name))

# Slicing
print(name[0:10])
print(name[:5])
print(name[5:])

# Negative slicing
print(name[-5:])
print(name[:-3])
print(name[-3:len(name)-2])


# Quick Quiz!!

name2 = ("Harry")
print(name2[-4:-2])

# Output: