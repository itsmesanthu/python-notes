# ============================================================
# REGULAR EXPRESSIONS
# ============================================================

# Regular Expression (Regex) is a sequence of characters
# used to search, match, and manipulate text.
#
# Python provides the 're' module for regular expressions.
#
#
# Regular expressions are mainly used for:
#
# 1. Searching text
# 2. Finding patterns
# 3. Extracting data
# 4. Validating input
# 5. Replacing text
# 6. Splitting text
# ============================================================


# ============================================================
# 1. IMPORT re MODULE
# ============================================================

import re


# ============================================================
# 2. BASIC SEARCH
# ============================================================

text = "I am learning Python"

result = re.search("Python", text)

print(result)


# Output will be similar to:
# <re.Match object; span=(14, 20), match='Python'>


# ============================================================
# 3. SEARCH FOR A WORD
# ============================================================

text = "Python is easy to learn"

result = re.search("easy", text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")


# Output:
# Pattern found


# ============================================================
# 4. PATTERN NOT FOUND
# ============================================================

text = "Python is easy to learn"

result = re.search("Java", text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")


# Output:
# Pattern not found


# ============================================================
# 5. RAW STRING
# ============================================================

# Raw strings are commonly used with regular expressions.
#
# Example:
#
# r"\d"
#
# instead of:
#
# "\\d"


pattern = r"\d"

text = "My 3 age is 21"

result = re.search(pattern, text)

print(result.group())


# Output:
# 2


# ============================================================
# 6. BASIC REGEX SYMBOLS
# ============================================================

# \d
#     ↓
# Matches a digit.
#
#
# \w
#     ↓
# Matches a word character.
#
#
# \s
#     ↓
# Matches whitespace.
#
#
# .
#     ↓
# Matches almost any character.
#
#
# ============================================================
# QUICK REVISION
# ============================================================
#
# import re
#     ↓
# Imports Python's regular expression module.
#
#
# Main functions:
#
# re.search()
# re.match()
# re.findall()
# re.split()
# re.sub()
# ============================================================