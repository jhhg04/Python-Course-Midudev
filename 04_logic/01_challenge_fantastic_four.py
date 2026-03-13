"""
Is the Alliance Between Reed Richards and Johnny Storm Balanced?

In the Fantastic Four universe, unity and balance between powers are essential to face any challenge. In this problem, we will focus on two of its members:

Reed Richards (Mr. Fantastic), represented by the letter R.
Johnny Storm (The Human Torch), represented by the letter J.

Objective:

Create a Python function that receives a text string. This function must count how many times the letter R (for Reed Richards) and how many times the letter J (for Johnny Storm) appear in the string.

- If the number of R and the number of J are equal, the alliance between mind and fire is considered balanced and the function must return True.
- If the quantities are not equal, the function must return False.
- If neither letter appears in the string, the balance is considered maintained (0 = 0), so the function must return True.
"""

from os import system
if system("clear") != 0: system("cls")

text = "RRRRJJJjjjrrr"

def check_is_balanced(text):
  text = text.upper()

  # easily count how many times a letter appears
  count_r = text.count("R")  # Reed Richards
  count_j = text.count("J")  # Johnny Storm

  print(f"count_r: {count_r} count_j: {count_j}")

  # if count_r == count_j:
  #   return True
  # else:
  #   return False

  return count_r == count_j

print(check_is_balanced("RRJJ"))
print(check_is_balanced("RRRRJJ"))
print(check_is_balanced("RRJJJJJJ"))
print(check_is_balanced("awwwaqAQAQA"))