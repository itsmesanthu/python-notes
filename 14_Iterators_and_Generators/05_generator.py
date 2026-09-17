# ============================================================
# GENERATOR
# ============================================================

# A generator is a special type of iterator.
#
# It generates values one at a time instead of storing
# all values in memory at once.
#
# Generators are created using:
#
# 1. yield
# 2. Generator expressions
#
# Generators are useful when working with large amounts
# of data.
# ============================================================


# ============================================================
# 1. BASIC GENERATOR FUNCTION
# ============================================================

def numbers():

    yield 1
    yield 2
    yield 3


result = numbers()

print(result)


# ============================================================
# 2. GET VALUES USING next()
# ============================================================

result = numbers()

print(next(result))
print(next(result))
print(next(result))


# Output:
# 1
# 2
# 3


# ============================================================
# 3. GENERATOR WITH FOR LOOP
# ============================================================

def numbers():

    yield 1
    yield 2
    yield 3


for num in numbers():
    print(num)


# Output:
# 1
# 2
# 3


# ============================================================
# 4. GENERATOR WITH range()
# ============================================================

def generate_numbers():

    for num in range(1, 6):
        yield num


for num in generate_numbers():
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5


# ============================================================
# 5. GENERATOR FOR SQUARES
# ============================================================

def squares():

    for num in range(1, 6):
        yield num ** 2


for value in squares():
    print(value)


# Output:
# 1
# 4
# 9
# 16
# 25


# ============================================================
# GENERATOR QUICK REVISION
# ============================================================

# Generator
#     ↓
# Special type of iterator.
#
#
# Main keyword:
#     ↓
# yield
#
#
# Advantages:
#     ↓
# 1. Saves memory
# 2. Produces values one at a time
# 3. Useful for large data
# 4. Supports lazy evaluation
# ============================================================