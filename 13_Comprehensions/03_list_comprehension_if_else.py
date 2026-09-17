# ============================================================
# LIST COMPREHENSION WITH IF ELSE
# ============================================================

# if-else can be used inside list comprehension
# to choose between two values.
#
#
# Syntax:
#
# [value_if_true if condition else value_if_false
#  for item in iterable]
# ============================================================


# ============================================================
# 1. EVEN OR ODD
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

result = [
    "Even" if num % 2 == 0 else "Odd"
    for num in numbers
]

print(result)


# Output:
# ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']


# ============================================================
# 2. POSITIVE OR NEGATIVE
# ============================================================

numbers = [10, -5, 7, -3, 8, -1]

result = [
    "Positive" if num >= 0 else "Negative"
    for num in numbers
]

print(result)


# Output:
# ['Positive', 'Negative', 'Positive',
#  'Negative', 'Positive', 'Negative']


# ============================================================
# 3. PASS OR FAIL
# ============================================================

marks = [90, 45, 67, 30, 80]

result = [
    "Pass" if mark >= 40 else "Fail"
    for mark in marks
]

print(result)


# Output:
# ['Pass', 'Pass', 'Pass', 'Fail', 'Pass']


# ============================================================
# 4. SQUARE EVEN NUMBERS AND CUBE ODD NUMBERS
# ============================================================

numbers = [1, 2, 3, 4, 5]

result = [
    num ** 2 if num % 2 == 0 else num ** 3
    for num in numbers
]

print(result)


# Output:
# [1, 4, 27, 16, 125]


# ============================================================
# QUICK REVISION
# ============================================================

# if-else comprehension
#
# [true_value if condition else false_value
#  for item in iterable]
# ============================================================