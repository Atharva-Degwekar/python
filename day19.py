# Day 19
# break and continue statement
# break statement enables a program to skip over a part of the code
# A break statement terminates the very loop it lies within.
# for eg

for i in range(1,101,1):
    print(i, end=" ")
    if (i==50):
        break
    else:
        print("Mississipi")
print("Bhot badiya")


# continue statement
# continue statement on the other hand skips the iteration

for i in range (12):
    if (i==10):
        print("iteration udd gaya")
        continue
    print("5 x",i,"=",5*i)
print("nice")