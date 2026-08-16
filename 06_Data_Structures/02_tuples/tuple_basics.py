# ==========================================
# TUPLE BASICS
# ==========================================

# What is a Tuple?
# A tuple is a collection data type in Python.
# It is used to store multiple values in a single variable.
#
# Tuple is:
# 1. Ordered
# 2. Immutable
# 3. Allows duplicate values
# 4. Can store different data types
# 5. Supports indexing
# 6. Supports slicing


# ------------------------------------------
# 1. Creating a Tuple
# ------------------------------------------

numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)


# ------------------------------------------
# 2. Ordered
# ------------------------------------------

numbers = (10, 20, 30, 40)

print("Ordered tuple:", numbers)


# ------------------------------------------
# 3. Immutable
# ------------------------------------------
# Immutable means we CANNOT change an element
# after creating the tuple.

numbers = (10, 20, 30)

print("Original tuple:", numbers)

# This is NOT allowed:
#
# numbers[0] = 100
#
# It will give:
# TypeError


# ------------------------------------------
# 4. Allows Duplicate Values
# ------------------------------------------

numbers = (10, 20, 10, 30, 10)

print("Tuple with duplicates:", numbers)


# ------------------------------------------
# 5. Different Data Types
# ------------------------------------------

data = (10, 3.14, "Python", True)

print("Different data types:", data)


# ------------------------------------------
# 6. Empty Tuple
# ------------------------------------------

empty_tuple = ()

print("Empty tuple:", empty_tuple)


# ------------------------------------------
# 7. Single Element Tuple
# ------------------------------------------
# IMPORTANT:
# A comma is required for a single-element tuple.

single = (10,)

print("Single element tuple:", single)
print("Type:", type(single))


# Without comma, it is an integer.

number = (10)

print("Type without comma:", type(number))


# ------------------------------------------
# 8. Tuple Length
# ------------------------------------------

numbers = (10, 20, 30, 40, 50)

print("Length:", len(numbers))


# ------------------------------------------
# 9. Check Element
# ------------------------------------------

print(20 in numbers)
print(100 in numbers)


# ------------------------------------------
# 10. Tuple with Strings
# ------------------------------------------

students = ("Santhosh", "Rahul", "Kiran")

print("Students:", students)


# ------------------------------------------
# 11. Nested Tuple
# ------------------------------------------

students = (
    ("Santhosh", 21),
    ("Rahul", 22),
    ("Kiran", 20)
)

print("Nested tuple:", students)


# ------------------------------------------
# 12. Tuple Packing
# ------------------------------------------
# Creating a tuple without brackets is called
# tuple packing.

student = "Santhosh", 21, "Python"

print("Packed tuple:", student)


# ------------------------------------------
# 13. Tuple Unpacking
# ------------------------------------------
# Taking values from a tuple into variables.

student = ("Santhosh", 21, "Python")

name, age, language = student

print("Name:", name)
print("Age:", age)
print("Language:", language)
