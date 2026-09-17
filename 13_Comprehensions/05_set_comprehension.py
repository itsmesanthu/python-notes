# ============================================================
# SET COMPREHENSION
# ============================================================

# Set comprehension is used to create a set
# using a short syntax.
#
# Sets automatically remove duplicate values.
#
#
# Syntax:
#
# {expression for item in iterable}
# ============================================================


# ============================================================
# 1. BASIC SET COMPREHENSION
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = {num ** 2 for num in numbers}

print(squares)


# Output:
# {1, 4, 9, 16, 25}


# ============================================================
# 2. REMOVE DUPLICATES
# ============================================================

numbers = [1, 2, 2, 3, 4, 4, 5, 5]

result = {num for num in numbers}

print(result)


# Output:
# {1, 2, 3, 4, 5}


# ============================================================
# 3. EVEN NUMBERS
# ============================================================

numbers = range(1, 11)

even_numbers = {
    num for num in numbers
    if num % 2 == 0
}

print(even_numbers)


# Output:
# {2, 4, 6, 8, 10}


# ============================================================
# 4. UNIQUE CHARACTERS
# ============================================================

word = "programming"

characters = {char for char in word}

print(characters)


# ============================================================
# 5. SET OF SQUARES
# ============================================================

numbers = [1, 2, 2, 3, 3, 4]

result = {num ** 2 for num in numbers}

print(result)


# Output:
# {1, 4, 9, 16}


# ============================================================
# QUICK REVISION
# ============================================================

# Set comprehension:
#
# {expression for item in iterable}
#
# Important:
# Sets automatically remove duplicate values.
# ============================================================