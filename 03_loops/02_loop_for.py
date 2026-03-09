###
# 02 - Loops (for)
# They allow you to execute a block of code repeatedly while iterating over an iterable or a list
###

from os import system
if system("clear") != 0: system("cls")

print("\nFor loop:")

# Iterate over a list
fruits = ["apple", "pear", "mandarin"]
for fruit in fruits:
    print(fruit)

# Iterate over anything that is iterable
string = "midudev"
for character in string:
    print(character)

# enumerate()
fruits = ["apple", "pear", "mandarin"]
for idx, value in enumerate(fruits):
    print(f"The index is {idx} and the fruit is {value}") # get the index position

# nested loops
letters = ["A", "B", "C"]
numbers = [1, 2, 3]

for letter in letters:
    for number in numbers:
        print(f"{letter}{number}")
