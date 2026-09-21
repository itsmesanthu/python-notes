# ============================================================
# REGEX SPECIAL CHARACTERS
# ============================================================

# Regular expressions provide special characters
# and character classes to create patterns.
# ============================================================

import re


# ============================================================
# 1. \d - DIGIT
# ============================================================

text = "Age: 21"

result = re.findall(r"\d", text)

print(result)


# Output:
# ['2', '1']


# ============================================================
# 2. \d+ - ONE OR MORE DIGITS
# ============================================================

text = "Age: 21, Roll: 105"

result = re.findall(r"\d+", text)

print(result)


# Output:
# ['21', '105']


# ============================================================
# 3. \w - WORD CHARACTER
# ============================================================

text = "Python_123"

result = re.findall(r"\w", text)

print(result)


# ============================================================
# 4. \w+ - ONE OR MORE WORD CHARACTERS
# ============================================================

text = "Python_123"

result = re.findall(r"\w+", text)

print(result)


# Output:
# ['Python_123']


# ============================================================
# 5. \s - WHITESPACE
# ============================================================

text = "Python is easy"

result = re.findall(r"\s", text)

print(result)


# ============================================================
# 6. . - ANY CHARACTER
# ============================================================

text = "cat"

result = re.findall(r"c.t", text)

print(result)


# Output:
# ['cat']


# ============================================================
# 7. ^ - START OF STRING
# ============================================================

text = "Python is easy"

result = re.search(r"^Python", text)

print(result)


# Match found because Python is at the beginning.


# ============================================================
# 8. $ - END OF STRING
# ============================================================

text = "I love Python"

result = re.search(r"Python$", text)

print(result)


# Match found because Python is at the end.


# ============================================================
# 9. [] - CHARACTER SET
# ============================================================

text = "apple banana orange"

result = re.findall(r"[aeiou]", text)

print(result)


# Finds vowels.


# ============================================================
# 10. [0-9] - DIGITS
# ============================================================

text = "Python123"

result = re.findall(r"[0-9]", text)

print(result)


# Output:
# ['1', '2', '3']


# ============================================================
# 11. [a-z] - LOWERCASE LETTERS
# ============================================================

text = "Python"

result = re.findall(r"[a-z]", text)

print(result)


# ============================================================
# 12. [A-Z] - UPPERCASE LETTERS
# ============================================================

text = "Python"

result = re.findall(r"[A-Z]", text)

print(result)


# Output:
# ['P']


# ============================================================
# 13. * - ZERO OR MORE
# ============================================================

text = "abbb"

result = re.findall(r"ab*", text)

print(result)


# Output:
# ['abbb']


# ============================================================
# 14. + - ONE OR MORE
# ============================================================

text = "abbb"

result = re.findall(r"ab+", text)

print(result)


# Output:
# ['abbb']


# ============================================================
# 15. ? - ZERO OR ONE
# ============================================================

text = "color colour"

result = re.findall(r"colou?r", text)

print(result)


# Output:
# ['color', 'colour']


# ============================================================
# 16. {n} - EXACT NUMBER OF TIMES
# ============================================================

text = "12345"

result = re.findall(r"\d{3}", text)

print(result)


# Output:
# ['123']


# ============================================================
# 17. {n,m} - RANGE
# ============================================================

text = "123456789"

result = re.findall(r"\d{2,4}", text)

print(result)


# ============================================================
# 18. | - OR
# ============================================================

text = "Python Java C"

result = re.findall(r"Python|Java", text)

print(result)


# Output:
# ['Python', 'Java']


# ============================================================
# 19. () - GROUP
# ============================================================

text = "My age is 21"

result = re.search(r"age is (\d+)", text)

print(result.group(1))


# Output:
# 21


# ============================================================
# QUICK REVISION
# ============================================================
#
# \d
#     ↓
# Digit
#
# \w
#     ↓
# Word character
#
# \s
#     ↓
# Whitespace
#
# .
#     ↓
# Any character
#
# ^
#     ↓
# Start
#
# $
#     ↓
# End
#
# []
#     ↓
# Character set
#
# *
#     ↓
# Zero or more
#
# +
#     ↓
# One or more
#
# ?
#     ↓
# Zero or one
#
# {n}
#     ↓
# Exactly n times
#
# {n,m}
#     ↓
# Between n and m times
#
# |
#     ↓
# OR
#
# ()
#     ↓
# Group
# ============================================================