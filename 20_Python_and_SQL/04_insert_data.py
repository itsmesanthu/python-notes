
# ============================================================
# INSERT DATA INTO DATABASE
# ============================================================

import sqlite3


# ============================================================
# 1. CONNECT TO DATABASE
# ============================================================

connection = sqlite3.connect("students.db")

cursor = connection.cursor()


# ============================================================
# 2. INSERT ONE RECORD
# ============================================================

cursor.execute(
    """
    INSERT INTO students (name, age, marks)
    VALUES (?, ?, ?)
    """,
    ("Santhosh", 22, 85)
)

connection.commit()

print("Student inserted successfully!")

# Output:
# Student inserted successfully!

# Every time you run this script, another record is inserted.
# Use a fresh database or clear test records when practising.


# ============================================================
# 3. INSERT MULTIPLE RECORDS
# ============================================================

students = [
    ("Rahul", 23, 90),
    ("Priya", 21, 92),
    ("Aman", 22, 78)
]

cursor.executemany(
    """
    INSERT INTO students (name, age, marks)
    VALUES (?, ?, ?)
    """,
    students
)

connection.commit()

print("Multiple students inserted successfully!")


# ============================================================
# 4. INSERT USING A DICTIONARY
# ============================================================

student = {
    "name": "Sneha",
    "age": 24,
    "marks": 88
}

cursor.execute(
    """
    INSERT INTO students (name, age, marks)
    VALUES (:name, :age, :marks)
    """,
    student
)

connection.commit()

print("Student inserted using dictionary!")


# ============================================================
# 5. GETTING THE LAST INSERTED ID
# ============================================================

cursor.execute(
    """
    INSERT INTO students (name, age, marks)
    VALUES (?, ?, ?)
    """,
    ("Kiran", 22, 81)
)

connection.commit()

print("Last inserted ID:", cursor.lastrowid)

# lastrowid returns the ID of the last inserted row
# for this cursor's INSERT operation.


# ============================================================
# 6. SAFE PARAMETERIZED QUERIES
# ============================================================

# Correct approach:
name = "Rahul"

cursor.execute(
    "SELECT * FROM students WHERE name = ?",
    (name,)
)

print(cursor.fetchall())

# Incorrect approach:
#
# query = "SELECT * FROM students WHERE name = '" + name + "'"
# cursor.execute(query)
#
# Never build SQL queries by joining untrusted user input.
# Use placeholders and pass values separately.


# ============================================================
# 7. CLOSING CONNECTION
# ============================================================

connection.close()

print("Database connection closed!")


# ============================================================
# INSERT DATA QUICK REVISION
# ============================================================

# Insert one record:
# cursor.execute(
#     "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
#     ("Rahul", 23, 90)
# )
#
# Insert multiple records:
# cursor.executemany(query, records)
#
# Named placeholders:
# VALUES (:name, :age, :marks)
#
# Save changes:
# connection.commit()
#
# Last inserted ID:
# cursor.lastrowid
#
# Always use parameterized queries.
