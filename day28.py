# Day 28
# f-string method
# string formating in python can be done using format method
# It can also be printed directly by applying f in front of print string like - print(f"ajfia")

f = "I am {} and I am from {}."
print(f.format("Atharva" , "India"))

name = "atharva"
country = "India"
print(f"I am {name} and I am from {country}")

price = 49.9999
txt = f"The price of this t-shirt is only{price: .2f}."
print(txt)

# this is seen in python 3.6 version onwards
print(f"{2 * 30}")

# Use of double curly braces to show literal text
print(f"My name is {{bleh}}")