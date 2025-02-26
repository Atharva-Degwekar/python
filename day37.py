# Day 37
# Finally keyword
# finally is used when we want to execute certain task irrespective of the content that goes into try block or except block.
# finally keyword is used when we want to operate in functions as print statement can not be used in functions.

# finally use syntax
a = input("Enter the number")

print(f"The multiplication table of {a} is -:")

try:
    for i in range(1,11):
        print(f"{int(a)} X {int(i)} = {int(a)*i}\n")
except Exception as e:
        print(f" The program is not working because of this error {e}")
finally:
    for j in range(1,11):
        print(f"{int(12)} X {int(j)} = {int(12)*j}\n")

# Function case for finally use
def func1():
    try:
        l = [1,2,34,5]
        index = int(input("Enter the index you want to check"))
        print(l[index])
        return 1
    except:
        print("Index out of range")
        return 0
    finally:
        print("I am always there no matter what")
print("HEllo")
x = func1()
print(x)