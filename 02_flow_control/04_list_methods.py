###
# 04 - List Methods
# The most important methods for working with lists
###

from os import system
if system("clear") != 0: system("cls")

# Create a list with values
list1 = ['a', 'b', 'c', 'd']

## Add or insert elements into the list

# Adds an element to the end
list1.append('e')  
print(list1)

# Inserts an element at the position specified as the first argument
list1.insert(1, '@')  
print(list1)

# Adds multiple elements to the end of the list
list1.extend(['😃', '😍'])  
print(list1)

## Remove elements from the list

# Removes the first occurrence of the string '@'
list1.remove('@')  
print(list1)

# Removes the last element from the list and returns it
ultimo = list1.pop()  
print(ultimo)
print(list1)

# Removes the second element from the list (index 1)
list1.pop(1)  
print(list1)