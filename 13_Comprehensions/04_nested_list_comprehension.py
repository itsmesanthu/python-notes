# ============================================================
# NESTED LIST COMPREHENSION
# ============================================================

# Nested list comprehension is used when we have
# nested loops or nested lists.
#
# It is useful for:
# 1. Working with matrices
# 2. Flattening nested lists
# 3. Creating tables
# 4. Working with multiple loops
# ============================================================


# ============================================================
# 1. FLATTEN A NESTED LIST
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [num for row in matrix for num in row]

print(result)


# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# ============================================================
# 2. NORMAL NESTED LOOP
# ============================================================

result = []

for row in matrix:
    for num in row:
        result.append(num)

print(result)


# ============================================================
# 3. CREATE A MATRIX
# ============================================================

matrix = [
    [num for num in range(1, 4)]
    for row in range(3)
]

print(matrix)


# Output:
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


# ============================================================
# 4. MULTIPLICATION TABLE
# ============================================================

table = [
    [i * j for j in range(1, 4)]
    for i in range(1, 4)
]

print(table)


# Output:
# [[1, 2, 3],
#  [2, 4, 6],
#  [3, 6, 9]]


# ============================================================
# 5. NESTED LOOP WITH CONDITION
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = [
    num
    for row in matrix
    for num in row
    if num % 2 == 0
]

print(result)


# Output:
# [2, 4, 6]


# ============================================================
# QUICK REVISION
# ============================================================

# Nested comprehension:
#
# [expression
#  for outer_item in outer_iterable
#  for inner_item in inner_iterable]
# ============================================================