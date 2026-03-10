###
# EXERCISES (range)
###

# Exercise 1: Print numbers from 1 to 10
# Print the numbers from 1 to 10 (inclusive) using a for loop and range().
print("\nExercise 1:")
for i in range(1, 11):  # Remember that range does not include the upper limit
  print(i)

# Exercise 2: Print odd numbers from 1 to 20
# Print all odd numbers between 1 and 20 (inclusive) using a for loop and range().
print("\nExercise 2:")
for i in range(1, 21, 2):  # Step of 2 ensures that only odd numbers are generated
  print(i)

# Exercise 3: Print multiples of 5
# Print the multiples of 5 from 5 to 50 (inclusive) using a for loop and range().
print("\nExercise 3:")
for i in range(5, 51, 5):  # Step of 5 generates multiples of 5
  print(i)

# Exercise 4: Print numbers in reverse order
# Print the numbers from 10 to 1 (inclusive) in reverse order using a for loop and range().
print("\nExercise 4:")
for i in range(10, 0, -1):  # Negative step for reverse order
  print(i)

# Exercise 5: Sum of numbers in a range
# Calculate the sum of the numbers from 1 to 100 (inclusive) using a for loop and range().
print("\nExercise 5:")
total = 0
for i in range(1, 101):
  total += i
print(f"The sum of the numbers from 1 to 100 is: {total}")

# Exercise 6: Multiplication table
# Ask the user to enter a number.
# Print the multiplication table for that number (from 1 to 10) using a for loop and range().
print("\nExercise 6:")
number = int(input("Enter a number for the multiplication table: "))
for i in range(1, 11):
  print(f"{number} x {i} = {number * i}")