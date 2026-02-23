# clean terminal in each execution
import os
os.system("clear")


# conditional if
print("\nSimple conditional")

age = 18

if age >= 18:
    print("You are of legal age")
    print("Congratlations")


# if else
age2= 15 
if age2 >= 18:
    print("You are of legal age")
else:    
    print("You are underage")

# elif
note= 9 
if note >= 9:
    print("Excelent")
elif note >= 7:
    print("good")
elif note >= 5:
    print("approved")      
else:    
    print("You Lose")

# multiple condition
age3= 22
has_license = True

if age3 >= 18 and has_license:
    print("You can drive")
else:    
    print("You Can not drive")