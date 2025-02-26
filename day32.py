# Day 32
# Methods of sets

# Update() and union()
# update and union methods print all items that are present in two sets
# union() method returns a new set whereas update method add items to existing sets.

# Example-:
cities = {"Mumbai" , "Tokyo" , "Hong Kong" , "Berlin"}
cities2 = {"Mumbai" , "Gangtok" , "Delhi" , "Seoul" , "Nagpur"}

# union() method
cities3 = cities.union(cities2)
print(cities3)

s = {1,2,3,5,7}
s1 = {2,4,6,8}

# update() method
s.update(s1)
print(s)

# intersection() and intersection_update()
# intersection() method returns a new set with elements common to the set and other.
# intersection_update() method removes elements from the set that are not present in other set.

# Example-:
s = {1,2,3,5,7}
s1 = {2,4,6,8}

# intersection() method
s2 = s.intersection(s1)
print(s2)

# intersection_update() method
s.intersection_update(s1)
print(s)

# symmetric_difference() and symmetric_difference_update()
# symmetric_difference() method returns a new set with elements that are in either the set but not in both.
# simply the common elements between set a and set b will be removed and only uncommon elements of set a and set b would be there.
# formula (a union b) - (a intersection b)
# symmetric_difference_update() method removes elements that are present in both sets.

s3 = {1,2,3,4,5,6,7,8,9,10}
s4 = {2,4,6,8,10}

#symmetric_difference()
s5 = s3.symmetric_difference(s4)
print(s5)

# symmetric_difference_update() method
s3.symmetric_difference_update(s4)
print(s3)

# difference and difference_update()
# difference() method returns a new set with elements that are in the set but not in other.
# simply it returns the values of only one set and also if both sets have common values they are original.
# difference_update() method removes elements from the set that are present in other set.
# formula (a - b)

s6 = {1,2,3,4,5,6,7,8}
s7 = {9,10,11,12,13}

# difference() method
print(s6.difference(s7))
print(s7.difference(s6))

# difference_update() method
s6.difference_update(s7)
print(s6)

s7.difference_update(s6)
print(s7)

# built-in-methods (additional)
# isdisjoint()
# isdisjoint() method returns True if two sets have a null intersection.
# i.e., they have no elements in common.
print(cities.isdisjoint(cities2))

c1 = {"Chennai"}
c2 = {"Bangalore"}
print(c1.isdisjoint(c2))

# issuperset()
# issuperset() method returns True if all elements of another set are present in the set.
# i.e., the set is a superset of the other set.
print(cities.issuperset(cities2))
print(cities2.issuperset(cities))

c3 = {"Mumbai", "Nagpur" ,"Pune"}
c4 = {"Mumbai", "Nagpur"}
print(c3.issuperset(c4))
print(c4.issuperset(c3))

# issubset()
# issubset() method returns True if all elements of another set are present in the set.
# i.e., the set is a subset of the other set.
print(c3.issubset(c2))
print(c2.issubset(c3))

# add()
# add() method adds a single element to the set.
# it can add only one element at a time.
c3.add("Tokyo")
print(c3)

# update()
# if you want to add one or more item simply create another set or any other iterable object (list,dict,tuple) and use update().
# update() method updates the set with the elements from another set or any other iterable object.
c3.update(c1)
print(c3)

# remove() / discard()
# remove() method removes a single element from the set.
# if the element is not present in the set, it raises a KeyError.
# discard() method removes a single element from the set.
# if the element is not present in the set, it do not raise a KeyError.
c3.remove("Tokyo")
print(c3)

# c3.remove("Tokyo")  # KeyError: 'Tokyo'
# print(c3)

# No Error
c3.discard("Tokyo")
print(c3)

# pop()
# pop() method removes and returns a random element from the set.
# if the set is empty, it raises a KeyError.
# however we can access the element that is pop if we use a different variable
item = c3.pop()
print(item)

# del
# del statement removes the element from the set.
# del not only deletes the element but can delete entire set.

del c3
# print(c3)   NameError: name 'c3' is not defined

# clear
# clear() method removes all elements from the set.
c1.clear()
print(c1)  # set()  # Output: set()  # Output: set()