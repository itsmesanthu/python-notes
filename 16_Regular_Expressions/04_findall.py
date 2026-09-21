# ============================================================
# re.findall()
# ============================================================

# re.findall() returns all non-overlapping matches
# of a pattern in a string.
#
#
# Syntax:
#
# re.findall(pattern, string)
# ============================================================

import re


# ============================================================
# 1. FIND ALL WORDS
# ============================================================

text = "Python is easy and Python is powerful"

result = re.findall("Python", text)

print(result)


# Output:
# ['Python', 'Python']


# ============================================================
# 2. FIND ALL NUMBERS
# ============================================================

text = "I have 10 apples and 20 oranges"

result = re.findall(r"\d+", text)

print(result)


# Output:
# ['10', '20']


# ============================================================
# 3. FIND ALL SINGLE DIGITS
# ============================================================

text = "My numbers are 12345"

result = re.findall(r"\d", text)

print(result)


# Output:
# ['1', '2', '3', '4', '5']


# ============================================================
# 4. FIND ALL WORDS
# ============================================================

text = "Python is very easy"

result = re.findall(r"\w+", text)

print(result)


# Output:
# ['Python', 'is', 'very', 'easy']


# ============================================================
# 5. FIND ALL VOWELS
# ============================================================

text = "Python Programming"

result = re.findall(r"[aeiouAEIOU]", text)

print(result)


# Output:
# ['o', 'o', 'a', 'i']


# ============================================================
# 6. COUNT OCCURRENCES
# ============================================================

text = "Python Python Python Java"

result = re.findall("Python", text)

print(len(result))


# Output:
# 3


# ============================================================
# QUICK REVISION
# ============================================================
#
# re.findall()
#     ↓
# Finds ALL matching occurrences.
#
#
# Returns:
#     ↓
# A list of matches.
#
#
# Example:
#
# re.findall(r"\d+", "Age 21, Roll 10")
#
# Output:
#
# ['21', '10']
# ============================================================