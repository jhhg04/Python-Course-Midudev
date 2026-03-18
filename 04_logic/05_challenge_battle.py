"""
You have two lists of numbers, list_a and list_b, both of the same length.

Each number in list_a "faces" the number in the same position in list_b.

- If the number in list_a is greater, its value is added to the next number in list_a.
- If the number in list_b is greater, its value is added to the next number in list_b.
- If both numbers are equal, both are removed and do not affect the next pair.

You must simulate these battles and return the final result:
- If a number remains in list_a at the end, return that number followed by the letter "a" (e.g., "3a").
- If a number remains in list_b at the end, return that number followed by the letter "b" (e.g., "2b").
- In case of a tie, return the letter "x".

list_a = [2, 4, 2]
list_b = [3, 3, 4]

result = battle(list_a, list_b)  # -> "2b"

# Explanation:
# - 2 vs 3: 3 wins (+1)
# - 4 vs 3+1: tie
# - 2 vs 4: 4 wins (+2)
# Result: "2b"

list_a = [4, 4, 4]
list_b = [2, 8, 2]

result = battle(list_a, list_b)  # -> "x"

# Explanation:
# - 4 vs 2: 4 wins (+2)
# - 4+2 vs 8: 8 wins (+2)
# - 4 vs 2+2: tie
# Result: "x"
"""

from os import system
if system("clear") != 0: system("cls")

# Brute force: try to find the solution directly.
# Hidden algorithms or calculations or formulas
# Dynamic programming: find a more efficient solution

def battle(list_a, list_b):
    points_a = sum(list_a)
    points_b = sum(list_b)
    return f"{points_a - points_b}a" if points_a > points_b else f"{points_b - points_a}b" if points_b > points_a else "x"


list_a = [4, 4, 4]
list_b = [2, 8, 2]
winner = battle(list_a, list_b)
print(winner)