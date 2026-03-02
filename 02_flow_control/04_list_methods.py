###
# 04 - List Methods
# The most important methods for working with lists
###

from os import system
if system("clear") != 0: system("cls")

# Create a list with values
list1 = ['a', 'b', 'c', 'd']

# Add or insert elements into the list
list1.append('e')  # Adds an element to the end
print(list1)

list1.insert(1, '@')  # Inserts an element at the position specified as the first argument
print(list1)