# function input() allows obtain user data through the console.

print("Hi, What is your name?")
name = input()

print(f" Hi {name}, nice to meet you")

# without print is in sema line, must usar \n
age = input("Hi, How old are you?\n")
age = int(age) # if dont use this cast, shoe error because age is string
print(f"in five years, you will have {age + 5}, very nice")

# get several values in same time, seprate with split()
print("get several values in same time")
country, city = input("Where country an city do you live?\n").split()

print(f"You live in {country}, {city}")