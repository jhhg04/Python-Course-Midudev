###
# EXERCISES
###

# Exercise 1: Determine the larger of two numbers
# Ask the user to enter two numbers and display a message
# indicating which one is larger or if they are equal.
print("\nExercise 1:")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("The numbers are equal")

# Exercise 2: Simple calculator
# Ask the user to enter two numbers and an operation (+, -, *, /)
# Perform the operation and display the result (handle division by zero).
print("\nExercise 2:")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
else:
    print("Invalid operation.")

if 'result' in locals():  # Checks if the variable 'result' exists.
    print(f"The result is: {result}")

# Exercise 3: Leap year
# Ask the user to enter a year and determine whether it is a leap year.
# A leap year is divisible by 4, except if it is divisible by 100
# unless it is also divisible by 400.
print("\nExercise 3:")
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Exercise 4: Age categories
# Ask the user to enter an age and classify it as:
# - Baby (0–2 years old)
# - Child (3–12 years old)
# - Teenager (13–17 years old)
# - Adult (18–64 years old)
# - Senior (65 years or older)
print("\nExercise 4:")
age = int(input("Enter an age: "))

if 0 <= age <= 2:
    print("Baby")
elif 3 <= age <= 12:
    print("Child")
elif 13 <= age <= 17:
    print("Teenager")
elif 18 <= age <= 64:
    print("Adult")
elif age >= 65:
    print("Senior")
else:
    print("Invalid age.")