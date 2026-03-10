###
# 03 - range()
# It allows you to create a sequence of numbers. It can be useful for for-loops, but not only for that
###

from os import system
if system("clear") != 0: system("cls")

print("\nrange():")

# Generate a sequence of numbers from 0 to 9
for num in range(10):
    print(num)

# range(start, end)
for num in range(5, 10):
    print(num)

# range(start, end, step)
for num in range(0, 1000, 5):
    print(num)

# negative range
for num in range(-5, 0):
    print(num)  

# countdown range
for num in range(10, 0, -1):
    print(num)

# not create list
for num in range(0, 444):
    print(num)

# create list
nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

# This would be to do something five times
for _ in range(5):
    print("do something five times")