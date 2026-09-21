# ============================================================
# re.match()
# ============================================================

# re.match() checks for a pattern only at the
# beginning of the string.
#
#
# Syntax:
#
# re.match(pattern, string)
# ============================================================

import re


# ============================================================
# 1. MATCH AT BEGINNING
# ============================================================

text = "Python is easy"

result = re.match("Python", text)

print(result)


# Output:
# Match object


# ============================================================
# 2. MATCH FAILS IF PATTERN IS NOT AT BEGINNING
# ============================================================

text = "I am learning Python"

result = re.match("Python", text)

print(result)


# Output:
# None


# ============================================================
# 3. CHECK MATCH
# ============================================================

text = "Python programming"

result = re.match("Python", text)

if result:
    print("Matched")
else:
    print("Not matched")


# Output:
# Matched


# ============================================================
# 4. MATCH NUMBER
# ============================================================

text = "12345 Python"

result = re.match(r"\d+", text)

print(result.group())


# Output:
# 12345


# ============================================================
# 5. MATCH WORD
# ============================================================

text = "Python programming"

result = re.match(r"\w+", text)

print(result.group())


# Output:
# Python


# ============================================================
# 6. search() VS match()
# ============================================================

text = "I am learning Python"

result1 = re.search("Python", text)

result2 = re.match("Python", text)

print(result1)
print(result2)


# search()
#     ↓
# Searches anywhere in the string.
#
#
# match()
#     ↓
# Checks only from the beginning.
#
#
# ============================================================
# QUICK REVISION
# ============================================================
#
# re.match()
#     ↓
# Checks the beginning of a string.
#
#
# re.search()
#     ↓
# Searches anywhere in a string.
# ============================================================