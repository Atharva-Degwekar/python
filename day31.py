# Day 31
# Sets in python
# A set is an unordered collection of unique elements that can be of any immutable data type such as
# integers, floats, strings, or tuples. Sets are mutable, meaning they can be modified after creation.

info = {"Carla" , 19 , False , 6.8 , 19}
print(info)
print(type(info))

# In o/p the order is different than it should be in the info block
# Hence we cannot use indexing to find out

# Quick Quiz
# Try to create an empty set and then find the type of that particular fn

empty = {}
print(type(empty))

# in the o/p of above code we can see that the type is of 'dict'.

# Why we actually needed set in python
# If we store some values in list it can be first easily changeable
# Second, it allows repeated values to store in the list and hence the memory is also getting more used
# Hence we need to use set in python to avoid these problems.

# We can access the items of set using for loop if we want to
# We can also use the len() function to get the number of items in the set.
# We can also use the in operator to check if an item is in the set or not.

# len fn
print(len(info), info)

# for loop
for i in info:
    if (i=="Carla"):
        print("Carla hai abhi bulata hu")
    else:
        pass
print("Hogaya checking")