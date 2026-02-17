### 02- types

# int
print("int:")
print(10)
print(type(10)) # <class 'int'>

print(0)
print(type(0)) # <class 'int'>

print(-5)
print(type(-5)) # <class 'int'>

print(1235648795642311210)
print(type(10)) # <class 'int'>

# +1, js dont do it
print(1235648795642311210)
print(1235648795642311210 + 1)

# float
print("float:")
print(type(3.14))
print(type(1.0)) # <class 'float'>

print(1e3) # 1000.0
print(type(1e3)) # <class 'float'>

# complex, part Real and part Imaginary
print("complex:")
print(type(1 + 2j))


# string, str
print("str:")
print(type("Hello"))

print(type("")) # empty is also str
print(type("123"))


print(type("""
  MiltiLine
""")) # multi is also str

# bool
print("bool:")
print(type(True)) # <class 'bool'>
print(type(False))
print(type(1 < 2))

# NoneType, similar to null or undefined (lack of value)
print("None:")
print(type(None)) # <class 'NoneType'>