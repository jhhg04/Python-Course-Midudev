###
# 03 - Lists
# Mutable sequences of elements.
# They can contain elements of different types.
###

from os import system
if system("clear") != 0: system("cls")

# Creating lists
print("\nCreate lists")
list1 = [1, 2, 3, 4, 5]  # list of integers
list2 = ["apples", "pears", "bananas"]  # list of strings
list3 = [1, "hello", 3.14, True]  # list of mixed types

empty_list = []
list_of_lists = [[1, 2], ["sock", 4]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(list1)
print(list2)
print(list3)
print(empty_list)
print(list_of_lists)
print(matrix)

# Accessing elements by index
print("\nAccessing elements by index")
print(list2[0])   # apples
print(list2[1])   # pears
print(list2[-1])  # bananas
print(list2[-2])  # pears

print(list_of_lists[1][0])

# List slicing
list1 = [1, 2, 3, 4, 5]
print(list1[1:4])  # [2, 3, 4]
print(list1[:3])   # [1, 2, 3]
print(list1[3:])   # [4, 5]
print(list1[:])    # [1, 2, 3, 4, 5]

# The third parameter is the step
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list1[::2])   # return elements at even indices
print(list1[::-1])  # return the list in reverse order

# Modify a list
list1[0] = 20
print(list1)

# Add elements to a list
list1 = [1, 2, 3]

# longer and less efficient way
list1 = list1 + [4, 5, 6]
print(list1)

# shorter and more efficient way
list1 += [7, 8, 9]
print(list1)

# Get the length of a list
print("List length:", len(list1))

###
# EXERCISES
###

# Exercise 1: The secret message
# Given the following list:
# message = ["C", "o", "d", "e", " ", "s", "e", "c", "r", "e", "t"]
# Using slicing and concatenation, create a new list that contains only the message "secret".

# Exercise 2: Swapping positions
# Given the following list:
# numbers = [10, 20, 30, 40, 50]
# Swap the first and last positions using only index assignment.

# Exercise 3: The list sandwich
# Given the following lists:
# top_bread = ["top bread"]
# ingredients = ["ham", "cheese", "tomato"]
# bottom_bread = ["bottom bread"]
# Create a list called sandwich that contains the top bread, the ingredients,
# and the bottom bread, in that order.

# Exercise 4: Duplicating the list
# Given a list:
# lst = [1, 2, 3]
# Create a new list that contains the elements of the original list duplicated.
# Example: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Exercise 5: Extracting the middle
# Given a list with an odd number of elements, extract the element
# in the middle of the list using slicing.
# Example: lst = [10, 20, 30, 40, 50] -> The middle is 30

# Exercise 6: Partial reverse
# Given a list, reverse only the first half of the list
# (using slicing and concatenation).
# Example: lst = [1, 2, 3, 4, 5, 6] -> Result: [3, 2, 1, 4, 5, 6]