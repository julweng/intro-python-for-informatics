# Assignment 2: Functions
# Julia Tzu-Ya Weng U07487022

# This program implements 3 functions to convert strings to integers, add 
# integers together, and cube the sum.

# to_number converts string to an int
def to_number(str):
    converted = int(str)
    return converted

# add_two adds two integers
def add_two(n1, n2):
    summed = n1 + n2
    return summed

# cube cubes a value
def cube(n):
    cubed = n**3
    return cubed

# Use the above functions in one statement
print cube(add_two(to_number('1'), to_number('2')))
