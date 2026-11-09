
# ============================================================
# SQLITE DATABASE CONNECTION
# ============================================================

# sqlite3 is a built-in Python module.
# It allows Python applications to work with SQLite databases.

import sqlite3


# ============================================================
# 1. CONNECTING TO A DATABASE
# ============================================================

connection = sqlite3.connect("students.db")

print("Database connected successfully!")

connection.close()

# Output:
# Database connected successfully!

# If students.db does not exist,
# SQLite creates the database file automatically.


# ============================================================
# 2. CREATING A CONNECTION OBJECT
# ============================================================

connection = sqlite3.connect("students.db")

print(type(connection))

connection.close()

# Output:
# <class 'sqlite3.Connection'>


# ============================================================
# 3. CREATING A CURSOR
# ============================================================

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

print(type(cursor))

connection.close()

# Output:
# <class 'sqlite3.Cursor'>

# A cursor executes SQL statements.


# ============================================================
# 4. EXECUTING A SQL QUERY
# ============================================================

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("SELECT sqlite_version()")

version = cursor.fetchone()

print("SQLite Version:", version[0])

connection.close()

# Output:
# SQLite Version: Your installed SQLite version


# ============================================================
# 5. USING TRY AND FINALLY
# ============================================================

connection = None

try:
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    print("Database connected successfully!")

except sqlite3.Error as error:
    print("Database Error:", error)

finally:
    if connection is not None:
        connection.close()
        print("Database connection closed!")

# finally ensures the connection is closed
# whether an error occurs or not.


# ============================================================
# 6. USING THE WITH STATEMENT
# ============================================================

with sqlite3.connect("students.db") as connection:

    cursor = connection.cursor()

    cursor.execute("SELECT sqlite_version()")

    print(cursor.fetchone())

# The with statement manages the transaction.
# The connection should still be explicitly closed
# when it is no longer needed.


# ============================================================
# SQLITE CONNECTION QUICK REVISION
# ============================================================

# Import:
# import sqlite3
#
# Connect:
# connection = sqlite3.connect("students.db")
#
# Create cursor:
# cursor = connection.cursor()
#
# Execute query:
# cursor.execute("SELECT * FROM students")
#
# Save changes:
# connection.commit()
#
# Undo uncommitted changes:
# connection.rollback()
#
# Close:
# connection.close()