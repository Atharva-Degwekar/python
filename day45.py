# Day 45
# if __name__=="__main__": in python
# the if __name__=="__main__": statement in Python is used to check whether the current script is being run as the main program or if it is being imported as a module into another script.
# This can be useful if you want to have different behavior when the script is run directly versus when it is imported into another script.
# For example, you might have some code that you only want to run when the script is run directly, but not when it is imported.
# To do this, you can use the following structure:

def welcome():
    print("Hey there! Welcome to the world of Python.")
welcome()

if __name__=="__main__":
    welcome()