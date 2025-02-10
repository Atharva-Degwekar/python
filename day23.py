# Day 23
# List methods

# 1. list.sort() - Sorts the list into ascending order
l = [12,392,492,1239,414918,1324,2,12,2]
l.sort()
print(l)

# Descending order
l.sort(reverse=True)
print(l)

# 2. list.append() - Adds the element at the ending of the list
l.append(21)
print(l)

# 3. list.reverse() - Reversing of the list from original list
l.reverse()
print(l)

# 4. list.index() - Gives the particular index of the list
l.index(12)
print(l)

# 5. list.count() - Returns the count of occurrence of element
l.count(2)
print(l)

# 6. list.copy() - Returns the copy of the original list so that we can perform operations on the list which we are not sure of such that original list do not gets modified
l1 = l.copy()
l1[0] = 0
print(l1)

# 7. list.insert() - Inserts an element at particular index
l.insert(0, 213)
print(l)

# 8. list.extend() - This method is used to add entire list, dict, tuple, string into the other list
colors = ["violet", "Indigo" , "Blue"]
Rainbow = ["Green" , "Yellow" , "Orange" , "Red"]
colors.extend(Rainbow)
print(colors)

# Concatenation of lists
colors = ["violet", "Indigo" , "Blue"]
Rainbow = ["Green" , "Yellow" , "Orange" , "Red"]
nature = colors + Rainbow
print(nature)