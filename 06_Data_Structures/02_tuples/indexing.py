# ==========================================
# TUPLE INDEXING
# ==========================================

numbers = (10, 20, 30, 40, 50)


# ------------------------------------------
# Positive Indexing
# ------------------------------------------

# Value:  10   20   30   40   50
# Index:   0    1    2    3    4

print("First:", numbers[0])
print("Second:", numbers[1])
print("Third:", numbers[2])
print("Fourth:", numbers[3])
print("Fifth:", numbers[4])


# ------------------------------------------
# Negative Indexing
# ------------------------------------------

# Value:       10   20   30   40   50
# Negative:    -5   -4   -3   -2   -1

print("Last:", numbers[-1])
print("Second last:", numbers[-2])
print("Third last:", numbers[-3])


# ------------------------------------------
# Tuple with Strings
# ------------------------------------------

students = ("Santhosh", "Rahul", "Kiran")

print("First student:", students[0])
print("Last student:", students[-1])


# ------------------------------------------
# Nested Tuple Indexing
# ------------------------------------------

students = (
    ("Santhosh", 21),
    ("Rahul", 22),
    ("Kiran", 20)
)

print("First student:", students[0])

print("First student's name:", students[0][0])

print("First student's age:", students[0][1])

print("Second student's name:", students[1][0])


# ------------------------------------------
# Index Error
# ------------------------------------------

numbers = (10, 20, 30)

# Valid indexes:
# 0, 1, 2
#
# numbers[5]
#
# This will give:
# IndexError


# ------------------------------------------
# Important: Tuple Cannot Be Changed
# ------------------------------------------

numbers = (10, 20, 30)

# numbers[0] = 100
# This will give:
# TypeError
# Because tuples are immutable.
