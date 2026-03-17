"""
Given an array of numbers and a number goal, find the first two numbers in the array that add up to the goal and return their indices. If no such combination exists, return None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

from os import system
if system("clear") != 0: system("cls")

# def find_first_sum(nums, goal):
#   # early return, a quick validation
#   if len(nums) == 0: return None

#   for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#       if nums[i] + nums[j] == goal:
#         return [i, j]

#   return None  # no combination found

def find_first_sum(nums, goal):
    seen = {}  # dictionary to store the number and its index

    for index, value in enumerate(nums):
        missing = goal - value
        if missing in seen: return [seen[missing], index]
        seen[value] = index  # store the current number since we haven't found the combination yet

    return None

nums = [4, 5, 6, 2]
goal = 8
result = find_first_sum(nums, goal)  # [2, 3]
print(result)