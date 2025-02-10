# day 16
# match case statements
# to implement switch cases like characteristics very similar to if-else functionality, we use a match case in python.
# A match statement will compare a given variable's value to different shapes, also referred to as the pattern
# The main idea is to keep on comparing the variable with all the present patterns until it fits into one
# The match case consist of 3 main entities:
# 1. The match keyword
# 2. One or more case clauses
# 3. Expression for each caseThe case clause consists of a pattern to be matched to the variable a condition to be evaluated if the pattern matches and a set
# of statements to be executed if the patterns matches.

x = int(input("Enter the number"))

match x:
    case 0:
        print("Zero")
    case 2:
        print("Two")
    case 5:
        print("five")
    case _:
        print(x)