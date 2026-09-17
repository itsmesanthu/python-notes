# ============================================================
# next()
# ============================================================

# next() is used to get the next value from an iterator.
#
#
# Syntax:
#
# next(iterator)
# ============================================================


# ============================================================
# 1. BASIC next()
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
# 2. STOPITERATION
# ============================================================

numbers = [10, 20]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

# print(next(iterator))
#
# This causes:
#
# StopIteration
#
# because there are no more values.


# ============================================================
# 3. next() WITH DEFAULT VALUE
# ============================================================

numbers = [10, 20]

iterator = iter(numbers)

print(next(iterator, "No more values"))
print(next(iterator, "No more values"))
print(next(iterator, "No more values"))


# Output:
# 10
# 20
# No more values


# ============================================================
# 4. MANUALLY ITERATE USING next()
# ============================================================

numbers = [10, 20, 30]

iterator = iter(numbers)

while True:

    try:
        value = next(iterator)
        print(value)

    except StopIteration:
        break


# Output:
# 10
# 20
# 30


# ============================================================
# 5. next() WITH STRING
# ============================================================

name = "Python"

iterator = iter(name)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# Output:
# P
# y
# t


# ============================================================
# QUICK REVISION
# ============================================================

# next()
#     ↓
# Returns the next value from an iterator.
#
#
# If no value remains:
#     ↓
# StopIteration
#
#
# Default value can be provided:
#
# next(iterator, default)
# ============================================================