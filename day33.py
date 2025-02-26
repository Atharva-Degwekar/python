# Day 33
# Dictionaries
# A dictionary is a collection of key-value pairs. It is an unordered collection of items, where
# each item is a pair of a key and a value.
# Dictionaries are mutable, meaning they can be changed after they are created.
# Dictionaries are defined by placing a series of key-value pairs within curly brackets {}.
# Each key-value pair is separated by a comma.
# Keys are unique identifiers for the values in a dictionary. They can be strings, integers, or
# any other immutable type.
# THEY ARE ALSO KNOWN AS HASH MAPS

# Example-:
info = {"Name": "Atharva",
        "Age": 19,
        "Occupation" : "IT engineer",
        "Salary": 15000000}

print(type(info) , info)
print(info["Occupation"])                # This will return an error in the case
print(info.get("Occupation"))            # This will not throw an error in this case even if we type something which is not present


# Using for loop to get access of all elements
for keys in info:                       # the loops will print same thing as values of dict.
    print(info[keys])
    print(f"The value of corresponding {keys} is {info[keys]}")

for values in info:                     # the loops will print same thing as values of dict.
    print(info[values])
    break

# WE CAN GET ALL ITEMS IN THE DICT BY USING .items()
print(info.items())

# we can access all the elements of the list using this particular type.
for keys,values in info.items():
    print(f"The value of corresponding key {keys} is {values}")