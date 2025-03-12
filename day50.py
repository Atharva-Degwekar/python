# Day 50
# read(), readline(), readlines() and other file handling methods in Python.
# import os

# os.mkdir("txts")

# Readline() method and writeline() method
f = open("txts/my_file2.txt", "r")
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks of student {i} in maths are: {m1}")
    print(f"Marks of student {i} in science are: {m2}")
    print(f"Marks of student {i} in english are: {m3}")
f.close()

# Writelines() method
f = open("txts/my_file3.txt", "w")
f.writelines(["Hello\n", "World\n"])
f.close()