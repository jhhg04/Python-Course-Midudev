###
# 01 - Loops (while)
# They allow you to execute a block of code repeatedly while a condition is true
###

from os import system
if system("clear") != 0: system("cls")

print("\n While loop:")

# Loop with a simple condition
counter = 0

while counter <= 5:
  print(counter)
  counter += 1  # This is super important to avoid an infinite loop

# Using the break keyword to exit the loop
print("\n While loop with break:")
counter = 0

while True:
  print(counter)
  counter += 1
  if counter == 5:
    break  # exits the loop

# continue skips the current iteration
# and continues with the loop
print("\n Loop with continue")
counter = 0
while counter < 10:
  counter += 1

  if counter % 2 == 0:
    continue

  print(counter)

# else, when does this condition execute?
print("\n While loop with else:")
counter = 0
while counter < 5:
  print(counter)
  counter += 1
else:
  print("The loop has finished")

# Ask the user for a number
# It must be positive, otherwise we keep asking
number = -1
while number < 0:
  number = int(input("Enter a positive number: "))
  if number < 0:
    print("The number must be positive. Try again.")

print(f"The number you entered is {number}")

number = -1
while number < 0:
  try:
    number = int(input("Enter a positive number: "))
    if number < 0:
      print("The number must be positive. Try again.")
  except:
    print("You must enter a valid number!")

print(f"The number you entered is {number}") 