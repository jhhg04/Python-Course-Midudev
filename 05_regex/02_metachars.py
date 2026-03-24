###
# 02 - Metacharacters
# Metacharacters are special symbols with specific meanings in regular expressions
###

import re

# 1. The dot (.)
# Matches any character except a newline

text = "Hello world, H0la again, H$la once more"
pattern = "H.la"  # Hola, H0la, H$la

found = re.findall(pattern, text)

if found:
  print(found)
else:
  print("Pattern not found")


text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"

matches = re.findall(pattern, text)
print(matches)

# --------------------

text = "Hello world, H0la again, H$la once more"
pattern = r"H.la"  # Hola, H0la, H$la

found = re.findall(pattern, text)

if found:
  print(found)
else:
  print("Pattern not found")


# How to use backslash to escape special characters
text = "My house is white. And the car is black."
pattern = r"\."

matches = re.findall(pattern, text)

print(matches)

# \d: matches any digit (0-9)

text = "The phone number is 123456789"
found = re.findall(r'\d{9}', text)

print(found)

# Exercise: Detect if there is a Spanish phone number using the +34 prefix

text = "My phone number is +34 688999999 write it down, okay?"
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
if found: print(f"I found the phone number {found.group()}")

# \w: matches any alphanumeric character (a-z, A-Z, 0-9, _)

text = "el_rubius_69"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# \s: matches any whitespace (space, tab, newline)
text = "Hello world\nHow are you?\t"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)

# ^: matches the beginning of a string
username = "423_name%22"
pattern = r"^\w"  # validate username

valid = re.search(pattern, username)

if valid: print("The username is valid")
else: print("The username is not valid")

phone = "+34 688999999"
pattern = r"^\+\d{1,3} "

valid = re.search(pattern, phone)

if valid: print("The phone number is valid")
else: print("The phone number is not valid")

# $: matches the end of a string
text = "Hello world."
pattern = r"world$"

valid = re.search(pattern, text)

if valid: print("The string is valid")
else: print("The string is not valid")

# EXERCISE
# Validate that an email is from Gmail
text = "miduga@hotmail.com"
pattern = r"@gmail.com$"
valid = re.search(pattern, text)

if valid: print("The email is a valid Gmail")
else: print("The email is not valid")

# EXERCISE:
# We have a list of files, we need to find filenames with .txt extension
files = "file1.txt file2.pdf midu-of.webp secret.txt"

# \b: matches the beginning or end of a word
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"

found = re.findall(pattern, text)
print(found)

# |: matches one option or another
fruits = "banana, pineapple, apple, avocado, palta, pear, avocado, avocado"
pattern = r"palta|avocado|p..a|\b\w{7}\b"

matches = re.findall(pattern, fruits)
print(matches)