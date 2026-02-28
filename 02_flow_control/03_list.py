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
print(list2[-1])  # bananas, It goes from the end to the beginning.
print(list2[-2])  # pears

print(list_of_lists[1][0])

# List slicing, only a part of the list, taking the indices you want, 
# the top or final index is not taken into account.
list1 = [1, 2, 3, 4, 5]
print(list1[1:4])  # [2, 3, 4] ,taking the indices you want
print(list1[:3])   # [1, 2, 3] , from the beginning
print(list1[3:])   # [4, 5] , from the end
print(list1[:])    # [1, 2, 3, 4, 5], all

# The third parameter is the step
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list1[::2])   # [1, 3, 5, 7] ,return elements at even indices
print(list1[::-1])  # [8, 7, 6, 5, 4, 3, 2, 1] return the list in reverse order

# Modify a list
list1[0] = 20 # Only exits positions 
print(list1)

# Add elements to a list
list1 = [1, 2, 3] # init state

# longer and less efficient way
list1 = list1 + [4, 5, 6] # evoid use this one
print(list1)

# shorter and more efficient way
list1 += [7, 8, 9] # use this one
print(list1)

# Get the length of a list
print("List length:", len(list1))