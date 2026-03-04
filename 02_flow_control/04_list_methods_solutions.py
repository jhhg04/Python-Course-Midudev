###
# EXERCISES
###

# Exercise 1: Add and modify elements
# Create a list with numbers from 1 to 5.
# Add the number 6 at the end using append().
# Insert the number 10 at position 2 using insert().
# Modify the first element of the list so that it becomes 0.
print("\nExercise 1:")
lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.insert(2, 10)
lista[0] = 0
print(lista)  # Output: [0, 2, 10, 3, 4, 5, 6]

# Exercise 2: Combine and clean lists
# Create two lists:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extend lista_a with lista_b using extend().
# Remove the first occurrence of number 1 in lista_a using remove().
# Remove the element at index 3 in lista_a using pop(). Print the removed element.
# Completely clear lista_b using clear().
print("\nExercise 2:")
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
lista_a.remove(1)
removed_element = lista_a.pop(3)
print(f"Removed element: {removed_element}")  # Output: Removed element: 5
lista_b.clear()
print("List a:", lista_a)  # Output: List a: [2, 3, 4, 6, 1, 2]
print("List b:", lista_b)  # Output: List b: []

# Exercise 3: Slicing and deletion with del
# Create a list with numbers from 1 to 10.
# Use slicing and del to remove elements from index 2 to 5 (not including 5).
# Print the resulting list.
print("\nExercise 3:")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista[2:5]
print(lista)  # Output: [1, 2, 6, 7, 8, 9, 10]

# Exercise 4: Sort and count
# Create a list with the following numbers: [5, 2, 8, 1, 9, 4, 2].
# Sort the list in ascending order using sort().
# Count how many times number 2 appears in the list using count().
# Check if number 7 is in the list using in.
print("\nExercise 4:")
lista = [5, 2, 8, 1, 9, 4, 2]
lista.sort()
count_twos = lista.count(2)
is_seven_present = 7 in lista
print(f"Sorted list: {lista}")  # Output: Sorted list: [1, 2, 2, 4, 5, 8, 9]
print(f"Count of 2: {count_twos}")  # Output: Count of 2: 2
print(f"Is 7 present?: {is_seven_present}")  # Output: Is 7 present?: False

# Exercise 5: Copy vs Reference
# Create a list called original with numbers [1, 2, 3].
# Create a copy of the original list called copia_1 using slicing.
# Create another copy called copia_2 using copy().
# Create a reference to the original list called referencia.
# Modify the first element of referencia to 10.
# Print the four lists (original, copia_1, copia_2, referencia) and observe the changes.
print("\nExercise 5:")
original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10
print(f"Original: {original}")        # Output: Original: [10, 2, 3]
print(f"Copy 1 (slicing): {copia_1}") # Output: Copy 1 (slicing): [1, 2, 3]
print(f"Copy 2 (copy()): {copia_2}")  # Output: Copy 2 (copy()): [1, 2, 3]
print(f"Reference: {referencia}")     # Output: Reference: [10, 2, 3]

# Exercise 6: Sort strings without case sensitivity.
# Create a list with the following strings: ["Manzana", "pera", "BANANA", "naranja"].
# Sort the list without distinguishing between uppercase and lowercase.
print("\nExercise 6:")
strings = ["Manzana", "pera", "BANANA", "naranja"]
strings.sort(key=str.lower)
print(strings)  # Output: ['BANANA', 'Manzana', 'naranja', 'pera']