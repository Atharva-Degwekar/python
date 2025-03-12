# Day 47
# Solution for Exercise 4

# Secret Code
# Write a python program to translate a message into secret code language. Use the rules below to translate the message into secret code.
# Coding:
# if the word contains at-least 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode the message. Then it should ask for the message and print the coded/decoded message.

# coding:
# Choice weather the user wants to decode or encode the message
import random

string = input("Enter Message you want : ")
print(f"Enter the choice you want to go with: \n1. Encode \n2. Decode")
choice = int(input())
word = string.split()

if choice == 1:
    nword = []
    for word in string.split():
        if len(word) >= 3:
            r1 = random.choice("abcdefghijklmnopqrstuvwxyz")
            r2 = random.choice("abcdefghijklmnopqrstuvwxyz")
            new_word = r1 + word[1:] + word[0] + r2  # Encoding correctly
            nword.append(new_word)
        else:
            nword.append(word[::-1])
    print("Encoded:", " ".join(nword))

else:
    nword = []
    for word in string.split():
        if len(word) < 3:
            nword.append(word[::-1])
        else:
            new_word = word[1:-1]  # Remove only 1 character from start & end
            new_word = new_word[-1] + new_word[:-1]  # Shift last letter to front
            nword.append(new_word)
    print("Decoded:", " ".join(nword))
