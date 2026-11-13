
# ============================================================
# RETRIEVE DATA USING SELECT
# ============================================================

import sqlite3


# ============================================================
# 1. CONNECT TO DATABASE
# ============================================================

connection = sqlite3.connect("students.db")

cursor = connection.cursor()


# ============================================================
# 2. SELECT ALL RECORDS
# ============================================================

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

# Example output:
# (1, 'Santhosh', 22, 85.0)
# (2, 'Rahul', 23, 90.0)


# ============================================================
# 3. SELECT SPECIFIC COLUMNS
# ============================================================

cursor.execute("SELECT name, marks FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

# Example output:
# ('Santhosh', 85.0)
# ('Rahul', 90.0)


# ============================================================
# 4. FETCH ONE RECORD
# ============================================================

cursor.execute("SELECT * FROM students")

student = cursor.fetchone()

print(student)

# fetchone() returns one row.
# Returns None when there are no more rows.


# ============================================================
# 5. FETCH MULTIPLE RECORDS
# ============================================================

cursor.execute("SELECT * FROM students")

students = cursor.fetchmany(3)

for student in students:
    print(student)

# fetchmany(3) gets up to three rows.


# ============================================================
# 6. FETCH ALL RECORDS
# ============================================================

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print(students)

# fetchall() returns all remaining rows.


# ============================================================
# 7. SELECT USING WHERE
# ============================================================

cursor.execute(
    "SELECT * FROM students WHERE marks > ?",
    (80,)
)

students = cursor.fetchall()

for student in students:
    print(student)


# ============================================================
# 8. SELECT USING ORDER BY
# ============================================================

cursor.execute(
    "SELECT * FROM students ORDER BY marks DESC"
)

students = cursor.fetchall()

for student in students:
    print(student)

# DESC = highest to lowest.
# ASC  = lowest to highest.


# ============================================================
# 9. SELECT USING LIMIT
# ============================================================

cursor.execute("SELECT * FROM students LIMIT 3")

students = cursor.fetchall()

for student in students:
    print(student)

# Returns at most three records.


# ============================================================
# 10. COUNT RECORDS
# ============================================================

cursor.execute("SELECT COUNT(*) FROM students")

count = cursor.fetchone()[0]

print("Total students:", count)


# ============================================================
# 11. GETTING AVERAGE MARKS
# ============================================================

cursor.execute("SELECT AVG(marks) FROM students")

average = cursor.fetchone()[0]

print("Average marks:", average)


# ============================================================
# 12. SEARCH BY STUDENT ID
# ============================================================

student_id = 1

cursor.execute(
    "SELECT * FROM students WHERE id = ?",
    (student_id,)
)

student = cursor.fetchone()

if student:
    print("Student found:", student)
else:
    print("Student not found")


# ============================================================
# 13. CLOSING CONNECTION
# ============================================================

connection.close()


# ============================================================
# SELECT QUICK REVISION
# ============================================================

# Select all:
# SELECT * FROM students
#
# Select columns:
# SELECT name, marks FROM students
#
# Filter:
# SELECT * FROM students WHERE marks > 80
#
# Sort:
# SELECT * FROM students ORDER BY marks DESC
#
# Limit:
# SELECT * FROM students LIMIT 3
#
# Count:
# SELECT COUNT(*) FROM students
#
# Average:
# SELECT AVG(marks) FROM students
#
# Fetch one:
# cursor.fetchone()
#
# Fetch multiple:
# cursor.fetchmany(3)
#
# Fetch all:
# cursor.fetchall()

