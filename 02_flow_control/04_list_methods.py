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

# Forcefully remove an index
del list1[-1] # -1 is the last one
print(list1)

# Removes all elements from the list
list1.clear()  
print(list1)

# Remove a range of elements
list1 = ['🐼', '🐨', '🐶', '😿', '🐹']
del list1[1:3]  # Removes elements from index 1 up to 3 (not including index 3)
print(list1)

## More useful methods

# Sorting lists
print('Sorting lists by modifying the original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

# Sorting lists by creating a new list
print('Sorting lists by creating a new list')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# Sorting a list of strings (all lowercase)
print("Sorting a list of strings (all lowercase)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

# Sorting a list of strings (mix of uppercase and lowercase)
print("Sorting a list of strings (mix of uppercase and lowercase)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

## More useful things

# Size of the list 
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals))  # Size of the list -> 4

# times appears
print(animals.count('🐶'))  # How many times '🐶' appears -> 2