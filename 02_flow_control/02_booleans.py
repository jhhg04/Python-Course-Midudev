# clean terminal in each execution
import os
os.system("clear")

# comparison operators
print("\nComparison operators")
print("5 > 3:", 5 > 3)  # True
print("5 < 3:", 5 < 3)  # False
print("5 == 5:", 5 == 5)  # True (equality)
print("5 != 3:", 5 != 3)  # True (inequality)
print("5 >= 3:", 5 >= 3)  # True (greater than or equal to)
print("5 <= 3:", 5 <= 3)  # False (less than or equal to)

# string comparison
# It only compares the first string; if it's equal, it moves on to the second, and so on.
# It also distinguishes between lowercase and uppercase letters.
print("\nString comparison")
print("'manzana' < 'pera':", "manzana" < "pera")  # True
print("'Hola' == 'hola':", "Hola" == "hola")  # False

# logical operators
print("\nLogical operators")
print("True and True:", True and True )  # True
print("True and False:", True and False )  # False
print("True or True:", True or True )  # True
print("True or False:", True or False )  # False
print("not True:", not True )  # False
print("not False:", not False )  # True

# Truth tables (just for reference):
print("\nTruth tables:")

print("\nand:")
print("A      B      A and B")
print("True   True  ", True and True)
print("True   False ", True and False)
print("False  True  ", False and True)
print("False  False ", False and False)

print("\nor:")
print("A      B      A or B")
print("True   True  ", True or True)
print("True   False ", True or False)
print("False  True  ", False or True)
print("False  False ", False or False)

print("\nnot:")
print("A      not A")
print("True  ", not True)
print("False ", not False)
