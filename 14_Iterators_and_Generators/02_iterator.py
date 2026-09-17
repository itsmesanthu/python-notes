# ============================================================
# ITERATOR
# ============================================================

# An iterator is an object that produces values one at a time.
#
# An iterator remembers its current position.
#
# An iterator is created from an iterable using iter().
#
#
# Syntax:
#
# iterator = iter(iterable)
# ============================================================


# ============================================================
# 1. CREATE AN ITERATOR
# ============================================================

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(iterator)


# ============================================================
# 2. GET VALUES FROM ITERATOR
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
# 3. ITERATOR REMEMBERS POSITION
# ============================================================

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

print(next(iterator))


# Output:
# 10
# 20
# 30


# ============================================================
# 4. ITERATOR WITH FOR LOOP
# ============================================================

numbers = [10, 20, 30]

iterator = iter(numbers)

for num in iterator:
    print(num)


# Output:
# 10
# 20
# 30


# ============================================================
# 5. ITERABLE VS ITERATOR
# ============================================================

numbers = [10, 20, 30]

iterator = iter(numbers)

print(numbers)
print(iterator)


# numbers → Iterable
# iterator → Iterator


# ============================================================
# ITERATOR QUICK REVISION
# ============================================================

# Iterable
#     ↓
# Object that can be iterated.
#
#
# Iterator
#     ↓
# Object that produces values one at a time.
#
#
# Create iterator:
#
# iterator = iter(iterable)
#
#
# Get next value:
#
# next(iterator)
# ============================================================