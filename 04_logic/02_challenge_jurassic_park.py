"""
In Jurassic Park, it has been observed that carnivorous dinosaurs, such as the terrifying T-Rex, lay an even number of eggs. Imagine you have a list of integers where each number represents the number of eggs laid by a dinosaur in the park.

Important: Only the eggs from carnivorous dinosaurs (T-Rex) are considered to be those numbers that are even.

Objective:
Write a Python function that receives a list of integers and returns the total sum of the eggs that belong to carnivorous dinosaurs (that is, the sum of all even numbers in the list).
"""

from os import system
if system("clear") != 0: system("cls")

# it gives us the remainder of the division: eggs % 2 == 0

def count_carnivore_dinosaur_eggs(egg_list) -> int:
    """
    This function receives a list of integers representing the number of eggs laid by different dinosaurs in Jurassic Park. The even numbers correspond to carnivores. It returns the total sum of all carnivore eggs.
    """
    total_carnivore_eggs = 0

    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivore_eggs += eggs

    # a shorter way to do it:
    # total_carnivore_eggs = sum(filter(lambda x: x % 2 == 0, egg_list))

    return total_carnivore_eggs

egg_list = [3, 4, 7, 5, 8]
print(count_carnivore_dinosaur_eggs(egg_list))  # 12