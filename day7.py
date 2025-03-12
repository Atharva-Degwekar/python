# Day 7
# Create a calculator that can add, subtract, multiply or divide depending upon the input from the user.

a = int(input("Enter the first nhumber: "))
b = int(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ")
if op =="+":
    print(int(a + b))
elif op =="-":
    print(int(a - b))
elif(op =="*"):
    print(int(a * b))
elif (op=="/"):
    print(int(a / b))
else:
    print("Bhai kya kar raha hai yaar tu!")