# ==========================================
# SET BASICS
# ==========================================

# What is a Set?
# A set is a collection data type in Python.
# It is used to store UNIQUE values.
#
# Characteristics:
# 1. Unordered
# 2. Mutable
# 3. Does not allow duplicates
# 4. Can contain different data types
# 5. Does NOT support indexing
# 6. Does NOT support slicing


# ------------------------------------------
# 1. Creating a Set
# ------------------------------------------

numbers = {10, 20, 30, 40, 50}

print("Set:", numbers)


# ------------------------------------------
# 2. Unordered
# ------------------------------------------
# Sets do not maintain a fixed index/order
# for accessing elements.

numbers = {10, 20, 30, 40}

print("Set:", numbers)


# ------------------------------------------
# 3. Duplicate Values
# ------------------------------------------
# Duplicate values are automatically removed.

numbers = {10, 20, 10, 30, 20, 40}

print("Set with duplicates:", numbers)

# Output contains unique values:
# {10, 20, 30, 40}


# ------------------------------------------
# 4. Mutable
# ------------------------------------------
# We can add or remove elements.

numbers = {10, 20, 30}

numbers.add(40)

print("After adding:", numbers)


# ------------------------------------------
# 5. Different Data Types
# ------------------------------------------

data = {10, 3.14, "Python", True}

print("Different data types:", data)


# ------------------------------------------
# 6. Empty Set
# ------------------------------------------
# IMPORTANT:
# {} creates an empty DICTIONARY.
#
# To create an empty set:
# set()

empty_set = set()

print("Empty set:", empty_set)

print("Type:", type(empty_set))


# ------------------------------------------
# 7. Set from a List
# ------------------------------------------

numbers = [10, 20, 20, 30, 30, 40]

unique_numbers = set(numbers)

print("List:", numbers)
print("Set:", unique_numbers)


# ------------------------------------------
# 8. Set from a String
# ------------------------------------------

word = "python"

letters = set(word)

print("Letters:", letters)


# ------------------------------------------
# 9. Membership Checking
# ------------------------------------------

numbers = {10, 20, 30, 40}

print(20 in numbers)
print(100 in numbers)

print(20 not in numbers)


# ------------------------------------------
# 10. Length of Set
# ------------------------------------------

numbers = {10, 20, 30, 40, 50}

print("Length:", len(numbers))


# ------------------------------------------
# 11. No Indexing
# ------------------------------------------

numbers = {10, 20, 30, 40}

# This is NOT allowed:
#
# print(numbers[0])
#
# Sets do not support indexing.


# ------------------------------------------
# 12. Loop Through Set
# ------------------------------------------

numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)


# ------------------------------------------
# 13. Set with Strings
# ------------------------------------------

students = {"Santhosh", "Rahul", "Kiran"}

print("Students:", students)


# ------------------------------------------
# 14. Frozen Set
# ------------------------------------------
# frozenset() creates an immutable set.
# We cannot add or remove elements.

numbers = frozenset([10, 20, 30])

print("Frozen set:", numbers)

# numbers.add(40)       # ❌ Not allowed
# numbers.remove(10)    # ❌ Not allowed
