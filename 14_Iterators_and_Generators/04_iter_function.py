# ============================================================
# iter()
# ============================================================

# iter() is used to create an iterator from an iterable.
#
#
# Syntax:
#
# iterator = iter(iterable)
# ============================================================


# ============================================================
# 1. LIST TO ITERATOR
# ============================================================

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# Output:
# 10
# 20
# 30


# ============================================================
# 2. STRING TO ITERATOR
# ============================================================

name = "Santhu"

iterator = iter(name)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# Output:
# S
# a
# n


# ============================================================
# 3. TUPLE TO ITERATOR
# ============================================================

numbers = (100, 200, 300)

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ============================================================
# 4. range() TO ITERATOR
# ============================================================

numbers = range(1, 4)

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# Output:
# 1
# 2
# 3


# ============================================================
# 5. ITERATION USING iter() AND next()
# ============================================================

numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

while True:

    value = next(iterator, None)

    if value is None:
        break

    print(value)


# Output:
# 1
# 2
# 3
# 4
# 5


# ============================================================
# ITER() QUICK REVISION
# ============================================================

# iter()
#     ↓
# Converts an iterable into an iterator.
#
#
# Example:
#
# numbers = [1, 2, 3]
# iterator = iter(numbers)
#
# next(iterator)
#     ↓
# 1
# ============================================================