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
age2 = 15 
if age2 >= 18:
    print("You are of legal age")
else:    
    print("You are underage")

# elif
note = 9 
if note >= 9:
    print("Excelent")
elif note >= 7:
    print("good")
elif note >= 5:
    print("approved")      
else:    
    print("You Lose")

# multiple condition -> and
age3 = 22
has_license = True

if age3 >= 18 and has_license:
    print("You can drive")
else:    
    print("You Can not drive")

# multiple condition -> or
age4 = 22
if age4 >= 18 or has_license:
    print("You can drive")
else:    
    print("You Can not drive")

# negation -> not
is_weekend = False

if not is_weekend:
    print("John go to work!!!")

# anidate condition
age5 = 20
has_money = True

if age5 >= 18:
    if has_money:
        print("You can go Disco")
    else:    
        print("You must stay at home")
else:    
    print("You can not enter in Disco")  

# changing the previous flow
age6 = 20

if age6 < 18:
    print("You can not enter in Disco")  
elif has_money:
    print("You can go Disco")
else:    
    print("You must stay at home")
    
# boolean
number = 5
if number: # True
    print("The number is not zero")

number = 0
if number: # False
    print("Here never enter")

name = "John"
if number: # True
    print("The name is not empty")

name = ""
if number: # False
    print("Here never enter")

# assignation = and comparation ==   
number = 2 # assignation
is_two = number == 2 # comparation

if is_two:
    print("The number is 2")

# the ternary condition
# single-line form of if

age = 17
message = "he is of legal age" if age >= 18 else "he is a minor"
print(message)