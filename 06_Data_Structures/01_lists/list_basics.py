# ==========================================
# LIST BASICS
# ==========================================

# What is a List?
# A list is a collection data type in Python
# used to store multiple values in a single variable.

numbers = [10, 20, 30, 40, 50]

print("Numbers:", numbers)


# ------------------------------------------
# 1. Ordered
# ------------------------------------------

numbers = [10, 20, 30, 40]

print("Ordered list:", numbers)


# ------------------------------------------
# 2. Mutable
# ------------------------------------------
# Mutable means we can change the list.

numbers[0] = 100

print("After changing:", numbers)


# ------------------------------------------
# 3. Allows Duplicate Values
# ------------------------------------------

numbers = [10, 20, 10, 30, 10]

print("Duplicates allowed:", numbers)


# ------------------------------------------
# 4. Different Data Types
# ------------------------------------------

data = [10, 3.14, "Python", True]

print("Different data types:", data)


# ------------------------------------------
# 5. Empty List
# ------------------------------------------

empty_list = []

print("Empty list:", empty_list)


# ------------------------------------------
# 6. Length of List
# ------------------------------------------

numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))


# ------------------------------------------
# 7. Check Element
# ------------------------------------------

print(20 in numbers)
print(100 in numbers)


# ------------------------------------------
# 8. Nested List
# ------------------------------------------

students = [
    ["Santhosh", 21],
    ["Rahul", 22],
    ["Kiran", 20]
]

print("Nested list:", students)
