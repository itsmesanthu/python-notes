
# ============================================================
# DELETE DATA FROM DATABASE
# ============================================================

import sqlite3


# ============================================================
# 1. CONNECT TO DATABASE
# ============================================================

connection = sqlite3.connect("students.db")

cursor = connection.cursor()


# ============================================================
# 2. DELETE A STUDENT BY ID
# ============================================================

cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (1,)
)

connection.commit()

print("Student deleted successfully!")


# ============================================================
# 3. DELETE USING STUDENT NAME
# ============================================================

cursor.execute(
    "DELETE FROM students WHERE name = ?",
    ("Rahul",)
)

connection.commit()

print("Student deleted using name!")


# ============================================================
# 4. CHECK NUMBER OF DELETED ROWS
# ============================================================

cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (999,)
)

print("Deleted rows:", cursor.rowcount)

connection.commit()

# If no matching record exists, rowcount is normally 0.


# ============================================================
# 5. VIEW REMAINING RECORDS
# ============================================================

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)


# ============================================================
# 6. DELETE ALL RECORDS
# ============================================================

# WARNING:
# This removes every record from the table.
#
# cursor.execute("DELETE FROM students")
# connection.commit()
#
# The table structure remains.
# Its records are removed.


# ============================================================
# 7. DELETE VS DROP
# ============================================================

# DELETE:
# Removes records from a table.
#
# DROP TABLE:
# Removes the entire table, including its structure.
#
# Example:
#
# DELETE FROM students WHERE id = 1;
#
# DROP TABLE students;


# ============================================================
# 8. CLOSE CONNECTION
# ============================================================

connection.close()


# ============================================================
# DELETE QUICK REVISION
# ============================================================

# Delete one record:
# DELETE FROM students WHERE id = ?
#
# Delete all records:
# DELETE FROM students
#
# Affected rows:
# cursor.rowcount
#
# Save changes:
# connection.commit()
#
# DELETE removes records.
# DROP removes the table itself.
#
# Always use WHERE when deleting selected records.
