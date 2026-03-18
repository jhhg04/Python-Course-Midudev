###
# 04 - Dictionaries
# Dictionaries are collections of key-value pairs.
# They are used to store related data.
###

from os import system
if system("clear") != 0: system("cls")

# typical example of a dictionary
person = {
    "name": "midudev",
    "age": 25,
    "is_student": True,
    "grades": [7, 8, 9],
    "socials": {
        "twitter": "@midudev",
        "instagram": "@midudev",
        "facebook": "midudev"
    }
}

# accessing values
print(person["name"])
print(person["grades"][2])
print(person["socials"]["twitter"])

# modifying values
person["name"] = "madeval"
person["grades"][2] = 10

# completely remove a property
del person["age"]
# print(person)

is_student = person.pop("is_student")
print(f"is_student: {is_student}")
print(person)

# overwrite a dictionary with another dictionary
a = { "name": "miduev", "age": 25 }
b = { "name": "madeval", "is_student": True }

a.update(b)
print(a)

# check if a property exists
print("name" in person)   # False
print("nombre" in person) # True

# get all keys
print("\nkeys:")
print(person.keys())

# get all values
print("\nvalues:")
print(person.values())

# get both key and value
print("\nitems:")
print(person.items())

for key, value in person.items():
    print(f"{key}: {value}")