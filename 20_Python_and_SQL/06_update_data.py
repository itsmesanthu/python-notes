
# ============================================================
# UPDATE DATA IN DATABASE
# ============================================================

import sqlite3


# ============================================================
# 1. CONNECT TO DATABASE
# ============================================================

connection = sqlite3.connect("students.db")

cursor = connection.cursor()


# ============================================================
# 2. UPDATE STUDENT MARKS
# ============================================================

cursor.execute(
    """
    UPDATE students
    SET marks = ?
    WHERE name = ?
    """,
    (95, "Santhosh")
)

connection.commit()

print("Student marks updated successfully!")


# ============================================================
# 3. UPDATE MULTIPLE COLUMNS
# ============================================================

cursor.execute(
    """
    UPDATE students
    SET age = ?, marks = ?
    WHERE id = ?
    """,
    (23, 98, 1)
)

connection.commit()

print("Student details updated successfully!")


# ============================================================
# 4. UPDATE USING STUDENT ID
# ============================================================

student_id = 2
new_marks = 96

cursor.execute(
    """
    UPDATE students
    SET marks = ?
    WHERE id = ?
    """,
    (new_marks, student_id)
)

connection.commit()

print("Marks updated using student ID!")


# ============================================================
# 5. CHECK NUMBER OF AFFECTED ROWS
# ============================================================

cursor.execute(
    """
    UPDATE students
    SET marks = ?
    WHERE id = ?
    """,
    (99, 1)
)

print("Affected rows:", cursor.rowcount)

connection.commit()

# rowcount reports the number of rows affected
# by the most recent DML statement.
# Exact behaviour can depend on the database operation.


# ============================================================
# 6. VERIFY UPDATED DATA
# ============================================================

cursor.execute(
    "SELECT * FROM students WHERE id = ?",
    (1,)
)

student = cursor.fetchone()

print(student)


# ============================================================
# 7. IMPORTANT: WHERE CONDITION
# ============================================================

# Correct:
#
# UPDATE students
# SET marks = 95
# WHERE id = 1;
#
# Dangerous:
#
# UPDATE students
# SET marks = 95;
#
# Without WHERE, every record is updated!


# ============================================================
# 8. CLOSE CONNECTION
# ============================================================

connection.close()


# ============================================================
# UPDATE QUICK REVISION
# ============================================================

# Update one column:
# UPDATE students SET marks = ? WHERE id = ?
#
# Update multiple columns:
# UPDATE students SET age = ?, marks = ? WHERE id = ?
#
# Save:
# connection.commit()
#
# Affected rows:
# cursor.rowcount
#
# Always check the WHERE condition before updating.
