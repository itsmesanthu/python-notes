
# ============================================================
# CREATE TABLE USING PYTHON AND SQLITE
# ============================================================

import sqlite3


# ============================================================
# 1. CONNECT TO DATABASE
# ============================================================

connection = sqlite3.connect("students.db")

cursor = connection.cursor()


# ============================================================
# 2. CREATE A TABLE
# ============================================================

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        marks REAL
    )
""")

connection.commit()

print("Students table created successfully!")

connection.close()

# Output:
# Students table created successfully!


# ============================================================
# 3. UNDERSTANDING THE SQL DATA TYPES
# ============================================================

# INTEGER:
# Stores integer values.
# Example: 22
#
# REAL:
# Stores floating-point values.
# Example: 85.5
#
# TEXT:
# Stores text.
# Example: "Rahul"
#
# BLOB:
# Stores binary data.
#
# NULL:
# Represents a missing or unknown value.


# ============================================================
# 4. UNDERSTANDING TABLE CONSTRAINTS
# ============================================================

# PRIMARY KEY:
# Uniquely identifies a record.
#
# AUTOINCREMENT:
# Automatically generates increasing integer IDs
# when used with an INTEGER PRIMARY KEY in SQLite.
#
# NOT NULL:
# Prevents a column from storing NULL.
#
# UNIQUE:
# Prevents duplicate values.
#
# DEFAULT:
# Provides a default value when one is not supplied.
#
# CHECK:
# Validates a condition.


# ============================================================
# 5. CREATE TABLE WITH MORE CONSTRAINTS
# ============================================================

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        salary REAL DEFAULT 0,
        age INTEGER CHECK(age >= 18)
    )
""")

connection.commit()

print("Employees table created successfully!")

connection.close()


# ============================================================
# 6. CHECKING TABLE INFORMATION
# ============================================================

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("PRAGMA table_info(students)")

columns = cursor.fetchall()

for column in columns:
    print(column)

connection.close()

# Shows:
# Column ID, name, data type, constraints and other details.


# ============================================================
# 7. CHECKING TABLES IN DATABASE
# ============================================================

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
""")

tables = cursor.fetchall()

for table in tables:
    print(table[0])

connection.close()

# Output may include:
# students
# employees


# ============================================================
# CREATE TABLE QUICK REVISION
# ============================================================

# Connect:
# sqlite3.connect("students.db")
#
# Cursor:
# connection.cursor()
#
# Create table:
# CREATE TABLE IF NOT EXISTS students (...)
#
# Save:
# connection.commit()
#
# Check columns:
# PRAGMA table_info(students)
#
# Check tables:
# SELECT name FROM sqlite_master WHERE type='table'
