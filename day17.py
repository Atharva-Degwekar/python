# day 17

# loop
# sometimes a programmer wants to execute a group of statements a certain number of times
# this can be done using loops. Based on this loops are further classified into following types:
# 1. for loop
# 2. while loop
# 3. nested loop
# 4. break and continue statement
# 5. pass statement

# For loop:
# The for loop is used to iterate over a sequence (such as a list, tuple, dictionary or other iterable objects).
# It iterates over the sequence and executes a block of code for each item in the sequence.

# The syntax of for loop is as follows:
name = 'ATHARVA'
for i in name:
    print(i, end=' , ')

# Now lets take a nested loop example of for and if
for char in name:
    print(i)
    if (char == 'A'):
        print(char,"Awesome")
    elif (char == 'T'):
        print(char,"Talented")
    elif (char == 'H'):
        print(char,"Hardworking")
    elif (char == 'A'):
        print(char,"Attitude")
    elif (char == 'R'):
        print(char,"Righteous")
    elif (char == 'V'):
        print(char,"Vail")
    elif (char =='A'):
        print(char,"Amphere")
    else:
        print(char,"Atharva is awesome")


# nested for loops
colors = ["Red" , "Blue" , "Aqua", "Green"]
print(colors)

for color in colors:
    print(color)
    for i in color:
        print(i)
        if color == "Aqua":
            print("My favorite color is", color)

# Now for number printing
num = int(input("Enter the numbers you want to print"))
for i in range(num):
    print(i)

# for k+1 args

for k in range(num):
    print(k+1)


# step function just works as how many to skip the numbers or difference between the numbers you want to print here 2 works as the step fn.
for j in range(1,12,2):
    print(j)

# multiplication tables
n = int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j)

# for a single table
num = int(input("enter the number of which you want a table: "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)
