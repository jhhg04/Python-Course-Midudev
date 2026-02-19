# 03 casting types
# Transform type of a value to other

print("type conversion")

# print("100" + 2) # Error
# print(100 + "2") # Error
print("100" + str(2))
print(2 + int("100"))

# float to int
print(int(3.1416)) # remove decimal part

# int to bool
print(bool(0)) # only 0 is false
print(bool(1))
print(bool(-1))

# str to bool
print(bool("")) # only "" empty string is false
print(bool(" "))
print(bool("False"))

# round int, to the more close even->par, if is .5
print(round(2.5))  # 2
print(round(2.51))  # 3
print(round(3.5))  # 4
