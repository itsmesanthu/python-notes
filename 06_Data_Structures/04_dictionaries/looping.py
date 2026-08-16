# ==========================================
# LOOPING THROUGH DICTIONARIES
# ==========================================


student = {
    "name": "Santhosh",
    "age": 21,
    "course": "Python",
    "city": "Bengaluru"
}


# ------------------------------------------
# 1. Loop Through Keys
# ------------------------------------------

for key in student:
    print(key)


# ------------------------------------------
# 2. Loop Through Keys using keys()
# ------------------------------------------

for key in student.keys():
    print("Key:", key)


# ------------------------------------------
# 3. Loop Through Values
# ------------------------------------------

for value in student.values():
    print("Value:", value)


# ------------------------------------------
# 4. Loop Through Key and Value
# ------------------------------------------
# items() gives both key and value.

for key, value in student.items():
    print(key, ":", value)


# ------------------------------------------
# 5. Print Dictionary Nicely
# ------------------------------------------

for key, value in student.items():
    print(f"{key} = {value}")


# ------------------------------------------
# 6. Loop with Condition
# ------------------------------------------

marks = {
    "Math": 85,
    "Python": 90,
    "SQL": 75,
    "Django": 88
}

for subject, mark in marks.items():

    if mark >= 80:
        print(subject, "-> Good")


# ------------------------------------------
# 7. Find Total Marks
# ------------------------------------------

total = 0

for mark in marks.values():
    total += mark

print("Total marks:", total)


# ------------------------------------------
# 8. Find Highest Mark
# ------------------------------------------

highest = 0

for mark in marks.values():

    if mark > highest:
        highest = mark

print("Highest mark:", highest)


# ------------------------------------------
# 9. Nested Dictionary Loop
# ------------------------------------------

students = {
    "student1": {
        "name": "Santhosh",
        "age": 21
    },

    "student2": {
        "name": "Rahul",
        "age": 22
    },

    "student3": {
        "name": "Kiran",
        "age": 20
    }
}


for student_id, details in students.items():

    print("\nStudent ID:", student_id)

    for key, value in details.items():

        print(key, ":", value)


# ------------------------------------------
# 10. Dictionary of Students and Marks
# ------------------------------------------

marks = {
    "Santhosh": 90,
    "Rahul": 85,
    "Kiran": 78,
    "Arun": 92
}


for name, mark in marks.items():

    print(name, "scored", mark)


# ------------------------------------------
# 11. Find Students Who Scored > 80
# ------------------------------------------

for name, mark in marks.items():

    if mark > 80:
        print(name, "scored above 80")


# ------------------------------------------
# 12. Dictionary Comprehension
# ------------------------------------------
# Create a dictionary using comprehension.

numbers = [1, 2, 3, 4, 5]

squares = {
    num: num * num
    for num in numbers
}

print("Squares:", squares)


# ------------------------------------------
# 13. Dictionary Comprehension with if
# ------------------------------------------

even_squares = {
    num: num * num
    for num in numbers
    if num % 2 == 0
}

print("Even squares:", even_squares)