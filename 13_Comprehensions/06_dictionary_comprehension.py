# ============================================================
# DICTIONARY COMPREHENSION
# ============================================================

# Dictionary comprehension is used to create
# dictionaries using a short syntax.
#
#
# Syntax:
#
# {key: value for item in iterable}
# ============================================================


# ============================================================
# 1. BASIC DICTIONARY COMPREHENSION
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = {
    num: num ** 2
    for num in numbers
}

print(squares)


# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ============================================================
# 2. CUBE DICTIONARY
# ============================================================

numbers = range(1, 6)

cubes = {
    num: num ** 3
    for num in numbers
}

print(cubes)


# Output:
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}


# ============================================================
# 3. DICTIONARY WITH CONDITION
# ============================================================

numbers = range(1, 11)

even_squares = {
    num: num ** 2
    for num in numbers
    if num % 2 == 0
}

print(even_squares)


# Output:
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# ============================================================
# 4. CREATE DICTIONARY FROM TWO LISTS
# ============================================================

names = ["Santhu", "Raj", "Kiran"]
marks = [85, 90, 75]

students = {
    name: mark
    for name, mark in zip(names, marks)
}

print(students)


# Output:
# {'Santhu': 85, 'Raj': 90, 'Kiran': 75}


# ============================================================
# 5. PASS OR FAIL DICTIONARY
# ============================================================

marks = {
    "Santhu": 85,
    "Raj": 35,
    "Kiran": 72,
    "Arun": 28
}

result = {
    name: "Pass" if mark >= 40 else "Fail"
    for name, mark in marks.items()
}

print(result)


# Output:
# {
# 'Santhu': 'Pass',
# 'Raj': 'Fail',
# 'Kiran': 'Pass',
# 'Arun': 'Fail'
# }


# ============================================================
# QUICK REVISION
# ============================================================

# Dictionary comprehension:
#
# {key: value for item in iterable}
#
# With condition:
#
# {key: value for item in iterable if condition}
# ============================================================