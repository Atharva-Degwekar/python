# Day 13
# String Methods
# Python provides a set of built-in methods that we can use to alter and modify the strings.
# upper() - uppercase conversion
# lower() - lowercase conversion
# capitalize() - capitalizing the first char into uppercase and rest turning into lowercase, if already first is uppercase then it would remain same
# center() - aligning towards center
# lstrip() - removing leading chars (pehle lagne vale ya simply left most of the string)
# rstrip() - removing trailing chars (piche lagne vale ya simply right most of the string)
# strip() - removing whitespaces
# count() - counting number of occurrences
# find() - finding where the occurrence is
# endswith() - finding weather it ends with a particular set of chars or single char
# startswith() - finding weather it starts with a particular set of chars of single char
# index() - index is same as find but if not found it does not returns -1 but raise an exception
# isalnum() - check if your string have A-Z , a-z , 0-9 if any other chars except for this it returns false.
# isalpha() - checks if your string have A-Z , a-z if any other things returns false
# isdecimal() - checks if your string have 0-9 if any other things returns false
# isdigit() - checks if your string have 0-9 if any other things returns false
# islower() - checks if your string have a-z if any other things returns false
# isnumeric() - checks if your string have 0-9 if any other things returns false
# isprintable() - if the chars are printable then it returns true otherwise false
# isspace() - if there are whitespaces that is if we use space bars or tab button then it returns true otherwise false
# istitle() - if every word's first letter is uppercase then it returns true otherwise false
# isupper() - checks if your string have A-Z otherwise returns false
# swapcase()- converts uppercase to lowercase and lowercase to uppercase
# title() - converts every word's first letter to capital

a = "AtHaRvA"
b = "!!!welcome to my world!!!"
c = "CYPHERisMystic0929"
d = "Viperisnice"
e = "Viperisnice12345"
f = "1232141324"
g = "valorant"
h = "valorant\n"
i = "       "
j = "Indian Army"

# upper
print(a.upper())

# lower
print(a.lower())

# capitalize
print(b.capitalize())

# center
print(b.center(50,"!"))
print(b.center(50))

# rstrip
print(b.rstrip("!!!"))

# lstrip
print(b.lstrip("!!!"))

# strip
print(b.strip())

# count
print(b.count("e"))

# find
print(b.find("!!!"))

# endswith
print(b.endswith("!"))
print(b.endswith("!",4,9))

# startswith
print(b.startswith("!"))

# index
print(b.index("!!!"))
# print(b.index("jeak"))

# isalnum
print(c.isalnum())

# isalpha
print(d.isalpha())
print(e.isalpha())

# isnumeric , isdigit , isdecimal
print(f.isdecimal())
print(f.isdigit())
print(f.isnumeric())

# islower
print(g.islower())

# isprintable
print(g.isprintable())
print(h.isprintable())

# isspace
print(i.isspace())

# istitle
print(j.istitle())

# isupper
print(a.isupper())

# swapcase
print(a.swapcase())

# title
print(b.title())