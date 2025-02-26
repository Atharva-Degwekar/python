# Day 25
# Operations on tuples

# As tuples are immutable we have to make sure that we should convert the tuples into list and then perform all the operations to manipulate tuples
# We can use list() function to convert tuple into list

countries = ("India" , "USA" , "Israel" , "Russia" , "Switzerland")
print(countries)
print(type(countries))
temp = list(countries)
print(temp,type(temp))
temp.append("Japan")
temp.pop(3)
temp[3] = "Finland"
print(temp)
countries = tuple(temp)
print(countries)

# concatenation of tuples
c1 = (1,2,3)
c2 = (4,5,6)
c3 = c1 + c2
print(c3)

# Methods of tuples
# 1. count() - count the no of occurrences in the tuple
# 2. index() - returns the index of the first occurrence of the specified value
# 3. len() - returns the length of the tuple
# 4. max() - returns the largest item in the tuple
# 5. min() - returns the smallest item in the tuple
