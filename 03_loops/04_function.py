# 04 - Functions
# Reusable and parameterized blocks of code to perform specific tasks
###

from os import system
if system("clear") != 0: system("cls")

# """ Function definition

# def function_name(parameter1, parameter2, ...):
#   # docstring
#   # function body
#   return return_value  # optional

# """

# Example of a function to print something to the console
def greet():  # create
    print("Hello!")

greet() # invocation

# Example of a function with a parameter
def greet_person(name): # here pass param to the fucntion
    print(f"Hello {name}!")

greet_person("john") # here pass argument to the fucntion

# Functions with more parameters
def add(a, b):
    total = a + b
    return total

result = add(2, 3)
print(result)

# Document functions with docstrings
def subtract(a, b):
    """Subtracts two numbers and returns the result"""
    return a - b

print(subtract(3, 2))

# default parameters
def multiply(a, b = 2):
    return a * b

print(multiply(2))
print(multiply(2, 3))