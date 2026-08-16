# ==========================================
# ACCESSING DICTIONARY VALUES
# ==========================================


student = {
    "name": "Santhosh",
    "age": 21,
    "course": "Python",
    "city": "Bengaluru"
}


# ------------------------------------------
# 1. Access using []
# ------------------------------------------

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])


# ------------------------------------------
# 2. Access using get()
# ------------------------------------------

print("Name:", student.get("name"))
print("Age:", student.get("age"))


# ------------------------------------------
# 3. Missing Key using []
# ------------------------------------------

# print(student["salary"])
#
# This gives:
# KeyError


# ------------------------------------------
# 4. Missing Key using get()
# ------------------------------------------
# get() returns None if key doesn't exist.

print("Salary:", student.get("salary"))


# ------------------------------------------
# 5. get() with Default Value
# ------------------------------------------

print(
    "Salary:",
    student.get("salary", 0)
)

# Output:
# Salary: 0


# ------------------------------------------
# 6. Check if Key Exists
# ------------------------------------------

if "name" in student:
    print("Name key exists")


if "salary" not in student:
    print("Salary key does not exist")


# ------------------------------------------
# 7. Access Nested Dictionary
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

print(
    "Student 1 name:",
    students["student1"]["name"]
)

print(
    "Student 1 age:",
    students["student1"]["age"]
)


# ------------------------------------------
# 8. Access List inside Dictionary
# ------------------------------------------

student = {
    "name": "Santhosh",
    "skills": [
        "Python",
        "Django",
        "SQL"
    ]
}

print("Skills:", student["skills"])

print("First skill:", student["skills"][0])

print("Second skill:", student["skills"][1])


# ------------------------------------------
# 9. Change a Value
# ------------------------------------------

student = {
    "name": "Santhosh",
    "age": 21
}

student["age"] = 22

print("Updated:", student)


# ------------------------------------------
# 10. Add New Value
# ------------------------------------------

student["city"] = "Bengaluru"

print("After adding city:", student)


# ------------------------------------------
# 11. Delete a Key
# ------------------------------------------

del student["city"]

print("After deleting city:", student)