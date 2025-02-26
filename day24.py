# Day 24
# Tuples
# Tuples are similar to lists, but they are immutable. This means that once a tuple is created, it cannot be changed.
# Tuples are defined by enclosing a sequence of values in parentheses,().
# Tuples are often used when a function needs to return multiple values.

tup = (1,2,3,4,5)
print(tup)
print(type(tup))
print(len(tup))

# Indexing
print(tup[0])  # prints 1
print(tup[1])  # prints 2
print(tup[2])  # prints 3
print(tup[3])  # prints 4
print(tup[4])  # prints 5
print(tup[1:2])

# Negative indexing
print(tup[-1])
print(tup[:-3])

# If else in
if 2 in tup:
    print("Got it")
else:
    print("nah!!")
