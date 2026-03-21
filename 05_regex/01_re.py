##
# 01 - Regular Expressions
#

""" Regular expressions are a sequence of characters that form a search pattern.
    They are used for searching text strings, data validation, etc. """

""" Why learn Regex?

- Advanced search: Find specific patterns in large texts quickly and accurately. (e.g., a Markdown editor using only Regex)

- Data validation: Ensure that user input such as email, phone number, etc. is correct.

- Text manipulation: Easily extract, replace, and modify parts of a text string
"""

# 1. Import the regular expressions module "re"
import re

# 2. Create a pattern, which is a string that describes what we want to find
pattern = "Hello"

# 3. The text where we want to search
text = "Hello world"

# 4. Use the search function from "re"
result = re.search(pattern, text)

if result:
    print("Pattern found in the text") # find "hello"
else:
    print("Pattern not found in the text")

# .group() returns the matched string
print(result.group()) # print "hello"

# .start() returns the starting position of the match
print(result.start())

# .end() returns the ending position of the match
print(result.end())

# EXERCISE 01
# Find the first occurrence of the word "AI" in the following text
# and indicate the start and end positions of the match.
text = "Everyone says that AI will take our jobs. But you just need to see how it can mess things up with Regex to be careful"
pattern = "AI"
found_ai = re.search(pattern, text)

if found_ai:
    print(f"Pattern found in the text at position {found_ai.start()} and ends at position {found_ai.end()}")
else:
    print("Pattern not found in the text")

# -----------------------

### Find all matches of a pattern
# .findall() returns a list with all matches

text = "I like Python. Python is awesome. Although Python is not that difficult, be careful with Python"
pattern = "Python"

matches = re.findall(pattern, text)

print(len(matches))

# -------------------------

# .finditer() returns an iterator with all match results

text = "I like Python. Python is awesome. Although Python is not that difficult, be careful with Python"
pattern = "Python"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())

# EXERCISE 02
# Find all occurrences of the word "midu" in the following text and indicate
# the start and end position of each match and how many times it appears.
text = "This is the Python course by midudev. Subscribe to midudev if you like this content! midu"

### Modifiers

# Modifiers are options that can be added to a pattern to change its behavior

# re.IGNORECASE: Ignore case sensitivity

text = "Everyone says that AI will take our jobs. But ai is not that bad. Long live Ai!"
pattern = "AI"
found = re.findall(pattern, text, re.IGNORECASE)

if found: 
    print(found)

# EXERCISE 03
# Find all occurrences of the word "python" in the following text, ignoring case.
text = "This is the Python course by midudev. Subscribe to python if you like this content! PYTHON"

### Replace text

# .sub() replaces all matches of a pattern in a text

text = "Hello, world! Hello again. Hello one more time."
pattern = "hello"
replacement = "Goodbye"

new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print(new_text)