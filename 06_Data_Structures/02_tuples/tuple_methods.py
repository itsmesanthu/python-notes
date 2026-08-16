# ==========================================
# TUPLE METHODS
# ==========================================


# ------------------------------------------
# 1. count()
# ------------------------------------------
# count() returns how many times a value
# appears in the tuple.

numbers = (10, 20, 10, 30, 10, 40)

result = numbers.count(10)

print("Count of 10:", result)

# Output:
# 3


# Another example

names = (
    "Santhosh",
    "Rahul",
    "Santhosh",
    "Kiran",
    "Santhosh"
)

print("Count of Santhosh:", names.count("Santhosh"))

# Output:
# 3


# ------------------------------------------
# 2. index()
# ------------------------------------------
# index() returns the first position of
# the specified value.

numbers = (10, 20, 30, 40, 50)

position = numbers.index(30)

print("Index of 30:", position)

# Output:
# 2


# ------------------------------------------
# index() with duplicate values
# ------------------------------------------

numbers = (10, 20, 10, 30, 10)

print("Index of 10:", numbers.index(10))

# Output:
# 0
#
# It returns the FIRST occurrence.


# ------------------------------------------
# 3. len()
# ------------------------------------------
# len() is a built-in function, not a
# tuple method.

numbers = (10, 20, 30, 40, 50)

print("Length:", len(numbers))


# ------------------------------------------
# 4. max()
# ------------------------------------------

numbers = (10, 50, 20, 80, 30)

print("Maximum:", max(numbers))


# ------------------------------------------
# 5. min()
# ------------------------------------------

print("Minimum:", min(numbers))


# ------------------------------------------
# 6. sum()
# ------------------------------------------

print("Sum:", sum(numbers))


# ------------------------------------------
# 7. sorted()
# ------------------------------------------
# sorted() returns a LIST.

numbers = (50, 20, 40, 10, 30)

sorted_numbers = sorted(numbers)

print("Original tuple:", numbers)
print("Sorted list:", sorted_numbers)


# ------------------------------------------
# 8. Reverse Tuple
# ------------------------------------------
# reversed() returns an iterator.
# tuple() converts it back into a tuple.

numbers = (10, 20, 30, 40)

reversed_tuple = tuple(reversed(numbers))

print("Reversed tuple:", reversed_tuple)


# ------------------------------------------
# 9. Tuple Concatenation
# ------------------------------------------

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print("Combined tuple:", result)


# ------------------------------------------
# 10. Tuple Repetition
# ------------------------------------------

numbers = (1, 2, 3)

result = numbers * 2

print("Repeated tuple:", result)


# ==========================================
# TUPLE METHOD SUMMARY
# ==========================================

print("\n========== TUPLE SUMMARY ==========")

print("count() -> Counts occurrences")
print("index() -> Finds first index")


# ==========================================
# OTHER USEFUL FUNCTIONS
# ==========================================

print("len()    -> Finds length")
print("max()    -> Finds maximum")
print("min()    -> Finds minimum")
print("sum()    -> Finds total")
print("sorted() -> Returns sorted list")