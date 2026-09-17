# ============================================================
# ITERABLE
# ============================================================

# An iterable is an object whose elements can be accessed
# one by one.
#
# Examples:
# 1. List
# 2. Tuple
# 3. String
# 4. Set
# 5. Dictionary
# 6. Range
#
# An iterable can be used with a for loop.
# ============================================================


# ============================================================
# 1. LIST AS ITERABLE
# ============================================================

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)


# Output:
# 10
# 20
# 30
# 40


# ============================================================
# 2. STRING AS ITERABLE
# ============================================================

name = "Python"

for char in name:
    print(char)


# Output:
# P
# y
# t
# h
# o
# n


# ============================================================
# 3. TUPLE AS ITERABLE
# ============================================================

numbers = (10, 20, 30)

for num in numbers:
    print(num)


# ============================================================
# 4. SET AS ITERABLE
# ============================================================

numbers = {10, 20, 30}

for num in numbers:
    print(num)


# ============================================================
# 5. DICTIONARY AS ITERABLE
# ============================================================

student = {
    "name": "Santhu",
    "age": 21,
    "marks": 85
}

for key in student:
    print(key)


# Output:
# name
# age
# marks


# ============================================================
# 6. range() AS ITERABLE
# ============================================================

numbers = range(1, 6)

for num in numbers:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5


# ============================================================
# 7. CHECK WHETHER OBJECT IS ITERABLE
# ============================================================

from collections.abc import Iterable

numbers = [1, 2, 3]

print(isinstance(numbers, Iterable))


# Output:
# True


# ============================================================
# ITERABLE QUICK REVISION
# ============================================================

# Iterable
#     ↓
# An object whose elements can be accessed one by one.
#
# Examples:
#     ↓
# list
# tuple
# string
# set
# dictionary
# range
#
# Main feature:
#     ↓
# Can be used in a for loop.
# ============================================================