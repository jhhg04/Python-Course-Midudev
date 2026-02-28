###
# SOLUTIONS
###

# Exercise 1: The secret message
# Given the following list:
# message = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Using slicing and concatenation, create a new list that contains only the message "secret".
print("\nExercise 1:")
message = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
secret = message[7:]
print(secret)

# Exercise 2: Swapping positions
# Given the following list:
# numbers = [10, 20, 30, 40, 50]
# Swap the first and last positions using only index assignment.
print("\nExercise 2:")
numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]  # Swap in a single line.
print(numbers)

# Exercise 3: The list sandwich
# Given the following lists:
# top_bread = ["top bread"]
# ingredients = ["ham", "cheese", "tomato"]
# bottom_bread = ["bottom bread"]
# Create a list called sandwich that contains the top bread,
# the ingredients, and the bottom bread, in that order.
print("\nExercise 3:")
top_bread = ["top bread"]
ingredients = ["ham", "cheese", "tomato"]
bottom_bread = ["bottom bread"]
sandwich = top_bread + ingredients + bottom_bread
print(sandwich)

# Exercise 4: Duplicating the list
# Given a list:
# lst = [1, 2, 3]
# Create a new list that contains the elements of the original list duplicated.
# Example: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
print("\nExercise 4:")
lst = [1, 2, 3]
duplicated_list = lst + lst
print(duplicated_list)

# Exercise 5: Extracting the middle
# Given a list with an odd number of elements, extract the element
# in the middle of the list using slicing.
# Example: lst = [10, 20, 30, 40, 50] -> The middle is 30
print("\nExercise 5:")
lst = [10, 20, 30, 40, 50]
middle = len(lst) // 2
print(lst[middle])

# Exercise 6: Partial reverse
# Given a list, reverse only the first half of the list
# (using slicing and concatenation).
# Example: lst = [1, 2, 3, 4, 5, 6] -> Result: [3, 2, 1, 4, 5, 6]
print("\nExercise 6:")
lst = [1, 2, 3, 4, 5, 6]
half = len(lst) // 2
reversed_list = lst[:half][::-1] + lst[half:]
print(reversed_list)