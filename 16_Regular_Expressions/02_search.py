# ============================================================
# re.search()
# ============================================================

# re.search() searches the entire string for a pattern.
#
# It returns the first matching occurrence.
#
#
# Syntax:
#
# re.search(pattern, string)
# ============================================================

import re


# ============================================================
# 1. BASIC SEARCH
# ============================================================

text = "I am learning Python"

result = re.search("Python", text)

print(result)


# ============================================================
# 2. CHECK WHETHER PATTERN EXISTS
# ============================================================

text = "Python is powerful"

result = re.search("Python", text)

if result:
    print("Found")
else:
    print("Not Found")


# Output:
# Found


# ============================================================
# 3. SEARCH FOR NUMBER
# ============================================================

text = "My age is 21"

result = re.search(r"\d+", text)

print(result.group())


# Output:
# 21


# ============================================================
# 4. SEARCH FOR FIRST DIGIT
# ============================================================

text = "My phone number is 9876543210"

result = re.search(r"\d", text)

print(result.group())


# Output:
# 9


# ============================================================
# 5. SEARCH WITH WORD PATTERN
# ============================================================

text = "Python programming language"

result = re.search(r"\w+", text)

print(result.group())


# Output:
# Python


# ============================================================
# 6. start() AND end()
# ============================================================

text = "I am learning Python"

result = re.search("Python", text)

print(result.start())
print(result.end())


# Output:
# 14
# 20


# ============================================================
# 7. group()
# ============================================================

text = "My age is 21"

result = re.search(r"\d+", text)

print(result.group())


# Output:
# 21


# ============================================================
# QUICK REVISION
# ============================================================
#
# re.search()
#     ↓
# Searches the entire string.
#
#
# result.group()
#     ↓
# Returns the matched text.
#
#
# result.start()
#     ↓
# Starting position.
#
#
# result.end()
#     ↓
# Ending position.
# ============================================================