# Day 18
# while loop
# as the name suggest while loop works exactly like that
# while loop executes the loop while the condition is True.
# As soon as the condition becomes False the interpreter comes out of the loop.

# Let's take an example
a = 0
while a < 10:
    print(a)
    a += 1   # its nothing but a = a + 1

# While loop nested
# we can have a while loop inside another while loop. This is called nested while loop.
# Let's take an example
i = 0
j = 1
k = 2
while i < 3:
    while j < 4:
        while k < 5:
            print(i, j , k)
            i += 1
            j += 1
            k += 1

# while and if loop
name = "ATHARVA"
if name =="ATHARVA":
    print("Hello Atharva")
    for char in name:
        print(char)
        while name != "ATHARVA":
            print("Atharva is amazing")
        continue
print("DONE")

# decrementing while loop
count = 10
while count >= 0:
    print(count)
    count -= 1
print("sorry you are done as the number is reached its bottom")