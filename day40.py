# Day40
# Exercise 4
# Secret Code
# Write a python program to translate a message into secret code language. Use the rules below to translate the message into secret code.
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
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

print(f"Enter the choice you want to go with: \n1. Encode \n2. Decode")
choice = int(input())

# Encoding the message
def encode(message):
    if len(message) >= 3:
        message = message[1:] + message[0]
        message = 'abc' + message + 'xyz'
    else:
        message = message[::-1]
    return message

# Decoding the message
def decode(message):
    if len(message) < 3:
        message = message[::-1]
    else:
        message = message[3:-3]
        message = message[-1] + message[:-1]
    return message

if choice == 1:
    message = input("Enter the message you want to encode: ")
    print(f"The encoded message is: {encode(message)}")
else:
    message = input("Enter the message you want to decode: ")
    print(f"The decoded message is: {decode(message)}")