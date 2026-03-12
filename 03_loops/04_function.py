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
def greet_person(name):
    print(f"Hello {name}!")

greet_person("john")