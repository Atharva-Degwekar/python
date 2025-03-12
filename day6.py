# Variables and data types
"------------------------"
# Variables
"------------------------"
# A variable is a name given to a value. It is a way to store a value in memory so that it can be used later in the program.

# Variables are used to store data that can be used in the program.

# Variables can store different types of data such as numbers, strings, lists, and dictionaries.

# Variables can be assigned a value using the assignment operator (=).

# The variable name is on the left side of the assignment operator and the value is on the right.

# Example:
x = 5
y = "Hello, World!"
print(x)  # Output: 5
print(y)  # Output: Hello, World!

# Data types
"------------------------"
# Python has several built-in data types that are used to store different types of data.

# The most common data types are:
# - int: Integer numbers
# - float: Floating-point numbers
# - str: Strings
# - list: Lists
# - tuple: Tuples
# - dict: Dictionaries
# - bool: Boolean values (True or False)
# - NoneType: None
# You can check the data type of a variable using the type() function.

# Example:
x = 5
y = 5.0
z = "Hello, World!"
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'str'>

# Type conversion
"------------------------"
# You can convert one data type to another using type conversion functions.

# The most common type conversion functions are:

# - int(): Convert to integer

# - float(): Convert to float

# - str(): Convert to string

# Example:
x = 5
y = 5.0
z = "5"
a = [1, 2, 3]
b = {"name": "Alice", "age": 25}
print(int(y))  # Output: 5
print(float(x))  # Output: 5.0
print(str(x))  # Output: "5"
print(type(a))  # Output: <class 'list'>
print(type(b))  # Output: <class 'dict'>

# Lists and dictionaries
"------------------------"
# Lists and dictionaries are two common data types used in Python.

# Lists are used to store multiple values in a single variable.

# Lists are ordered, changeable, and allow duplicate values.

# Lists are created using square brackets [].

# Lists are mutable, which means you can change the values of a list after it has been created.

# Example:
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ["apple", "banana", "cherry"]

# Dictionaries are used to store key-value pairs in a single variable.

# Dictionaries are unordered, changeable, and do not allow duplicate keys.

# Dictionaries are created using curly braces {}.

# Dictionaries are mutable, which means you can change the values of a dictionary after it has been created.
# Example:
person = {"name": "Alice", "age": 25}
print(person)  # Output: {"name": "Alice", "age": 25}

# Tuple
# A tuple is a collection of values that is ordered and immutable.

# Tuples are created using parentheses ().

# Tuples are similar to lists, but they cannot be changed after they are created.

# Example:
fruits = ("apple", "banana", "cherry")
print(fruits)  # Output: ("apple", "banana", "cherry")