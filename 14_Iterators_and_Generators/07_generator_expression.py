# ============================================================
# GENERATOR EXPRESSION
# ============================================================

# A generator expression is similar to a list comprehension,
# but it creates a generator instead of a list.
#
#
# List comprehension:
#
# [expression for item in iterable]
#
#
# Generator expression:
#
# (expression for item in iterable)
# ============================================================


# ============================================================
# 1. BASIC GENERATOR EXPRESSION
# ============================================================

numbers = (num ** 2 for num in range(1, 6))

print(numbers)


# ============================================================
# 2. GET VALUES USING next()
# ============================================================

numbers = (num ** 2 for num in range(1, 6))

print(next(numbers))
print(next(numbers))
print(next(numbers))


# Output:
# 1
# 4
# 9


# ============================================================
# 3. GENERATOR EXPRESSION WITH FOR LOOP
# ============================================================

numbers = (num ** 2 for num in range(1, 6))

for num in numbers:
    print(num)


# Output:
# 1
# 4
# 9
# 16
# 25


# ============================================================
# 4. GENERATOR EXPRESSION WITH CONDITION
# ============================================================

numbers = (
    num
    for num in range(1, 11)
    if num % 2 == 0
)

for num in numbers:
    print(num)


# Output:
# 2
# 4
# 6
# 8
# 10


# ============================================================
# 5. LIST COMPREHENSION VS GENERATOR EXPRESSION
# ============================================================

# List comprehension:

squares_list = [
    num ** 2
    for num in range(1, 6)
]

print(squares_list)


# Generator expression:

squares_generator = (
    num ** 2
    for num in range(1, 6)
)

print(squares_generator)


# List stores all values in memory.
#
# Generator produces values one at a time.


# ============================================================
# 6. SUM USING GENERATOR EXPRESSION
# ============================================================

numbers = (num ** 2 for num in range(1, 6))

result = sum(numbers)

print(result)


# Output:
# 55


# ============================================================
# 7. LARGE RANGE
# ============================================================

numbers = (num for num in range(1, 1000000))

# Values are generated only when required.
#
# This is more memory-efficient than creating
# a list containing all values at once.


# ============================================================
# GENERATOR EXPRESSION QUICK REVISION
# ============================================================

# Generator expression:
#
# (expression for item in iterable)
#
#
# With condition:
#
# (expression for item in iterable if condition)
#
#
# Main advantage:
#     ↓
# Values are generated one at a time.
# ============================================================