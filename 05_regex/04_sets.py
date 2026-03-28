import re

# [:] Matches any character inside the brackets

username = "rub.$ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match:
  print("The username is valid:", match.group())
else:
  print("The username is not valid") # show this The username is not valid


# Find all vowels in a word
text = "Hello world"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches) # ['e', 'o', 'o']

# A regex to find the words man, fan, and ban
# but ignore the rest
text = "man ran fan ñan ban"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)
print(matches)

# Exercise:
# Now it gets trickier because some words match but don't start with those letters.
# We only want the words man, fan, and ban
text = "omniman fanatico man bandana"
# \b 

text = "22"
pattern = r"[4-9]"

matches = re.findall(pattern, text)
print(matches)


# Final exercise with everything learned
# Improve this: https://www.computerhope.com/jargon/r/regular-expression.png

## Look for corner cases that it doesn’t handle and fix them:
"lo.que+sea@shopping.online"
"michael@gov.co.uk"

# [^]: Matches any character NOT inside the brackets
text = "Hello world"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)