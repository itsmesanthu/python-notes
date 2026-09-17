# ============================================================
# LIST COMPREHENSION
# ============================================================

# List comprehension is a short and simple way to create
# a new list from an existing iterable.
#
# It is mainly used for:
# 1. Creating lists
# 2. Applying an expression to each item
# 3. Filtering values
# 4. Writing shorter and cleaner code
#
#
# Syntax:
#
# [expression for item in iterable]
# ============================================================


# ============================================================
# 1. BASIC LIST COMPREHENSION
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]

print(squares)


# Output:
# [1, 4, 9, 16, 25]


# ============================================================
# 2. NORMAL FOR LOOP VS COMPREHENSION
# ============================================================

# Normal way:

numbers = [1, 2, 3, 4, 5]

squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)


# List comprehension:

squares = [num ** 2 for num in numbers]

print(squares)


# ============================================================
# 3. USING range()
# ============================================================

numbers = [num for num in range(1, 11)]

print(numbers)


# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ============================================================
# 4. CREATING CUBES
# ============================================================

numbers = [1, 2, 3, 4, 5]

cubes = [num ** 3 for num in numbers]

print(cubes)


# Output:
# [1, 8, 27, 64, 125]


# ============================================================
# 5. CONVERTING STRINGS
# ============================================================

names = ["santhu", "raj", "kiran", "arun"]

upper_names = [name.upper() for name in names]

print(upper_names)


# Output:
# ['SANTHU', 'RAJ', 'KIRAN', 'ARUN']


# ============================================================
# 6. STRING LENGTH
# ============================================================

names = ["santhu", "raj", "kiran", "arun"]

lengths = [len(name) for name in names]

print(lengths)


# Output:
# [6, 3, 5, 4]


# ============================================================
# QUICK REVISION
# ============================================================

# List comprehension
#     ↓
# [expression for item in iterable]
#
# Example:
#
# squares = [num ** 2 for num in numbers]
# ============================================================