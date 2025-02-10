# day 14

# conditional operators
# < , > , <= , >= , == , !=
b = int(input("Enter your age"))
print(b>18)
print(b<18)
print(b>=18)
print(b<=18)
print(b==18)
print(b!=18)

# indentation - indentation is used to define a block of code

# if else , elif , else statements
# if else statements are used for decision making purposes and other logic based questions we can use.
# they can be used as a nested if else also if there is a big decision and inside it there are small decisions to take we can use nested if else

a = int(input("Enter your age"))
print("Your age is:",a)

if (a>18):
    print("You can drive")
elif (a==18):
    print("You still can drive")
else:
    print("Choti bacchi ho abhi!")
print("Bas holiya aaj ka")    # this will still print irrespective of if-elif-else statement

# nested if else:
# guessing game concept would be suffice
# if you are guessing a number and you are not sure about it you can use nested if else
print("Choose any number between 0-9")
num = int(input("enter the number"))
if (num==0):
    print("The number is between 0")
elif (num>0):
    if(num<5):
        print("the number is between 0-5")
    elif(num>5):
        print("num is between 5-9")
else:
    print("num is not between 0-9")