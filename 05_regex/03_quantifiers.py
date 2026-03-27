###
# 03 - Quantifiers
# Quantifiers are used to specify how many occurrences of a character or group of characters should be found in a string.
###

import re

# *: Can appear 0 or more times
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches) # ['aaa', '', 'a', ''] 0 or more times

# Exercise 1:
# How many words have 0 or more "a" followed by a "b"?

# +: One or more times
text = "dddd aaa ccc a bb aa casa"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches) # ['aaa', 'a', 'aa', 'a', 'a'] 1 or more times

# ?: Zero or one time
text = "aaabacb"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches) # ['ab', 'b']

# Exercise: Make the +34 optional in the following text
phone = "+34 688999999"

# {n}: Exactly n times
text = "aaaaaa         aa   aaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)

print(matches)

# {n, m}: From n to m times
text = "u uu uuu u"
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
print(matches)

# Exercise:
# Find words with 4 to 6 letters in the following text
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)

# Exercise
# Find words with more than 6 letters
words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)