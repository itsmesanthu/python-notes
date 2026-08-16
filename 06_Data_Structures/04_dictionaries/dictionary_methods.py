# ==========================================
# DICTIONARY METHODS
# ==========================================


student = {
    "name": "Santhosh",
    "age": 21,
    "course": "Python",
    "city": "Bengaluru"
}


# ------------------------------------------
# 1. keys()
# ------------------------------------------
# Returns all keys.

print("Keys:", student.keys())


# ------------------------------------------
# 2. values()
# ------------------------------------------
# Returns all values.

print("Values:", student.values())


# ------------------------------------------
# 3. items()
# ------------------------------------------
# Returns key-value pairs.

print("Items:", student.items())


# ------------------------------------------
# 4. get()
# ------------------------------------------
# Returns value of a key.

print("Name:", student.get("name"))

print(
    "Salary:",
    student.get("salary", 0)
)


# ------------------------------------------
# 5. update()
# ------------------------------------------
# Adds new key-value pairs or updates
# existing values.

student.update({
    "age": 22,
    "salary": 50000
})

print("After update:", student)


# ------------------------------------------
# 6. pop()
# ------------------------------------------
# Removes a specific key and returns
# its value.

student = {
    "name": "Santhosh",
    "age": 21,
    "course": "Python"
}

removed = student.pop("age")

print("Removed value:", removed)
print("Dictionary:", student)


# ------------------------------------------
# 7. popitem()
# ------------------------------------------
# Removes the LAST inserted key-value pair.

student = {
    "name": "Santhosh",
    "age": 21,
    "course": "Python"
}

removed = student.popitem()

print("Removed:", removed)
print("Dictionary:", student)


# ------------------------------------------
# 8. setdefault()
# ------------------------------------------
# Returns the value of a key.
#
# If key doesn't exist, it creates the key
# with the given default value.

student = {
    "name": "Santhosh",
    "age": 21
}

student.setdefault("city", "Bengaluru")

print("After setdefault:", student)


# If key already exists,
# setdefault() does not change it.

student.setdefault("name", "Rahul")

print("After existing key:", student)


# ------------------------------------------
# 9. copy()
# ------------------------------------------

student = {
    "name": "Santhosh",
    "age": 21
}

new_student = student.copy()

print("Original:", student)
print("Copy:", new_student)


# ------------------------------------------
# 10. clear()
# ------------------------------------------

student = {
    "name": "Santhosh",
    "age": 21
}

student.clear()

print("After clear:", student)


# ------------------------------------------
# 11. fromkeys()
# ------------------------------------------
# Creates a dictionary from a list of keys.

keys = ["name", "age", "city"]

student = dict.fromkeys(keys)

print("Using fromkeys():", student)


# Give the same default value

student = dict.fromkeys(
    keys,
    "Unknown"
)

print("With default value:", student)


# ==========================================
# DICTIONARY METHOD SUMMARY
# ==========================================

print("\n========== DICTIONARY METHODS ==========")

print("keys()       -> Get all keys")
print("values()     -> Get all values")
print("items()      -> Get key-value pairs")
print("get()        -> Get value safely")
print("update()     -> Add/update values")
print("pop()        -> Remove specific key")
print("popitem()    -> Remove last item")
print("setdefault() -> Get/add default value")
print("copy()       -> Create copy")
print("clear()      -> Remove all items")
print("fromkeys()   -> Create dictionary from keys")