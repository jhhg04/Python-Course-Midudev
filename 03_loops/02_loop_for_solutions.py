###
# EXERCISES (for)
###

# Exercise 1: Print even numbers
# Print all even numbers from 2 to 20 (inclusive) using a for loop.
print("\nExercise 1:")
for number in range(2, 21, 2):  # range(start, end, step)
  print(number)

# Exercise 2: Calculate the average of a list
# Given the following list of numbers:
# numbers = [10, 20, 30, 40, 50]
# Calculate the average of the numbers using a for loop.
print("\nExercise 2:")
numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
  total += number
average = total / len(numbers)
print(f"The average is: {average}")

# Exercise 3: Find the maximum in a list
# Given the following list of numbers:
# numbers = [15, 5, 25, 10, 20]
# Find the maximum number in the list using a for loop.
print("\nExercise 3:")
numbers = [15, 5, 25, 10, 20]
maximum = numbers[0]  # Initialize with the first element
for number in numbers:
  if number > maximum:
    maximum = number
print(f"The maximum number is: {maximum}")

# Exercise 4: Filter strings by length
# Given the following list of words:
# words = ["casa", "arbol", "sol", "elefante", "luna"]
# Create a new list that contains only the words with more than 5 letters
# using a for loop and list comprehension.
print("\nExercise 4:")
words = ["casa", "arbol", "sol", "elefante", "luna"]
long_words = [word for word in words if len(word) > 5]
print(long_words)

# Exercise 5: Count words that start with a letter
# Given the following list of words:
# words = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Ask the user to enter a letter.
# Count how many words in the list start with that letter (case-insensitive).
print("\nExercise 5:")
words = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letter = input("Enter a letter: ").lower()  # Convert the letter to lowercase
counter = 0
for word in words:
  if word.lower().startswith(letter):  # Compare in lowercase
    counter += 1
print(f"There are {counter} words that start with the letter {letter}")