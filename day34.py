# Day 34
# Methods of Dictionaries
# 1. keys() - Returns a view object that displays a list of all keys available in the dictionaries
# 2. values() - Returns a view object that displays a list of all values available in the dictionaries
# 3. items() - Returns a view object that displays a list of a tuple of all key-value map pairs in the dictionary, sorted or unsorted
# 4. get() - Returns the value for the given key if it exists in the dictionary
# 5. pop() - Removes the item with the specified key and returns its value
# 6. popitem() - Removes and returns an arbitrary element from the dictionary
# 7. update() - Updates the dictionary with the items from another dictionary or from an iterable
# 8. clear() - Removes all elements from the dictionary
# 9. copy() - Returns a copy of the dictionary
# 10. fromkeys() - Creates a new dictionary with keys from sequence or mapping object and
# 11. setdefault() - Returns the value of the key if it exists in the dictionaries.

ep1 = {122: 49, 132: 98, 142: 78, 152: 89}
ep2 = {162: 51, 172: 90, 182: 78, 192: 81}

# update()
ep1.update(ep2)
print(ep1)

# copy()
ep3 = ep2.copy()
print(ep3)

# clear()
ep3.clear()
print(ep3)

# pop()
ep1.pop(122)
print(ep1)

# popitem()
ep4 = ep1.copy()
ep4.popitem()
print(ep4)

# del
del ep4

# setdefault()
ep5 = {1: 2, 3: 4}
print(ep5.setdefault(1, 5))

# fromkeys()
ep6 = dict.fromkeys([1, 2, 3, 4, 5])
print(ep6)