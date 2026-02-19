my_name = "John"
my_age= 33

print(my_name)

# dynamic typing -> implicit type, can change in execution time

name="john"
print(name)

name= 33
print(name)

# strong typing, can convert
# print(10 + "2") # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# f strings
print(f"Hi {my_name}, I'm {my_age} years old ") # Hi John, I'm 33 years old
print(f"Hi {my_name}, I'm {my_age - 5} years old ") # Hi John, I'm 28 years old

# declare in line, Do not use this
nick, age, city = "John", 33, "Bogota"

# use snake case for declare vars
my_name_of_var = "ok"
