# Day 35
# For loop with else in python

# else block is not only limited to if loop it can be executed with for loop and while loop as well
# The else block in a for loop is executed when the loop iterates over all items in the

# # Example-:
# for i in range(2,10,2):
#     print(i)
# else:
#     print("Bye")
# print("End")

# This code snippet demonstrates the usage of the `else` block in a `for` loop in Python. In this
# specific case, the `for` loop iterates over a range of numbers from 0 to 9. However, there is a
# conditional check inside the loop that breaks the loop when `i` is equal to 5 using the `break`
# statement.
# Special case here the loop ends not breaks
# so else block will not execute
# for i in range(10):
#     print(i)
#     if(i==5):
#         break
# else:
#     print("Bye")
# print("End")

# # While loop
j = 0
while j < 10:
    print("\n",j)
    j = j + 1
else:
    print("\nBye")

# Same case with while loop also
j = 0
while j < 10:
    print(j)
    j = j + 1
    if j == 9:
        break
else:
    print("\nBye")