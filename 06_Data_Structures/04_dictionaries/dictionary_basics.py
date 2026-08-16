# ==========================================
# DICTIONARY BASICS
# ==========================================

# What is a Dictionary?
# A dictionary is a collection used to store
# data in KEY : VALUE pairs.
#
# Syntax:
#
# dictionary = {
#     key: value,
#     key: value
# }
#
# Example:
#
# student = {
#     "name": "Santhosh",
#     "age": 21
# }


# ------------------------------------------
# 1. Creating a Dictionary
# ------------------------------------------

student = {
    "name": "Santhosh",
    "age": 21,
    "course": "Python"
}

print("Student:", student)


# ------------------------------------------
# 2. Key : Value
# ------------------------------------------

student = {
    "name": "Santhosh",
    "age": 21
}

print("Name:", student["name"])
print("Age:", student["age"])


# ------------------------------------------
# 3. Keys Must Be Unique
# ------------------------------------------

student = {
    "name": "Santhosh",
    "age": 21,
    "age": 22
}

print(student)

# The second "age" replaces the first value.
#
# Output:
# {'name': 'Santhosh', 'age': 22}


# ------------------------------------------
# 4. Values Can Be Duplicate
# ------------------------------------------

students = {
    "student1": "Python",
    "student2": "Python",
    "student3": "Django"
}

print(students)


# ------------------------------------------
# 5. Different Data Types
# ------------------------------------------

data = {
    "name": "Santhosh",
    "age": 21,
    "marks": 85.5,
    "passed": True
}

print(data)


# ------------------------------------------
# 6. Dictionary with List
# ------------------------------------------

student = {
    "name": "Santhosh",
    "skills": ["Python", "Django", "SQL"]
}

print(student)


# ------------------------------------------
# 7. Dictionary with Tuple
# ------------------------------------------

student = {
    "name": "Santhosh",
    "marks": (80, 85, 90)
}

print(student)


# ------------------------------------------
# 8. Nested Dictionary
# ------------------------------------------

students = {
    "student1": {
        "name": "Santhosh",
        "age": 21
    },

    "student2": {
        "name": "Rahul",
        "age": 22
    }
}

print(students)


# ------------------------------------------
# 9. Empty Dictionary
# ------------------------------------------

empty_dictionary = {}

print("Empty dictionary:", empty_dictionary)


# ------------------------------------------
# 10. Create Dictionary using dict()
# ------------------------------------------

student = dict(
    name="Santhosh",
    age=21,
    course="Python"
)

print("Using dict():", student)


# ------------------------------------------
# 11. Dictionary Length
# ------------------------------------------

student = {
    "name": "Santhosh",
    "age": 21,
    "course": "Python"
}

print("Length:", len(student))


# ------------------------------------------
# 12. Check Key
# ------------------------------------------

print("name" in student)
print("salary" in student)


# ------------------------------------------
# 13. Mutable Dictionary
# ------------------------------------------
# Dictionaries are mutable.
# We can add, change and remove values.

student = {
    "name": "Santhosh",
    "age": 21
}

student["age"] = 22

print("After changing:", student)


# Add a new key

student["city"] = "Bengaluru"

print("After adding:", student)