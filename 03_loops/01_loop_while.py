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
