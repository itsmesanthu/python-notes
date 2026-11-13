
# ============================================================
# PYTHON AND MYSQL CONNECTION
# ============================================================

# MySQL is a relational database management system.
#
# Python can connect to MySQL using:
# mysql-connector-python
#
# Installation:
# python -m pip install mysql-connector-python

import mysql.connector


# ============================================================
# 1. CONNECT TO MYSQL DATABASE
# ============================================================

try:

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="college"
    )

    print("MySQL connected successfully!")

except mysql.connector.Error as error:

    print("MySQL connection error:", error)


# ============================================================
# 2. CREATE A CURSOR
# ============================================================

if connection.is_connected():

    cursor = connection.cursor()

    print("Cursor created successfully!")


# ============================================================
# 3. EXECUTE SELECT QUERY
# ============================================================

if connection.is_connected():

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    for student in students:
        print(student)


# ============================================================
# 4. INSERT DATA INTO MYSQL
# ============================================================

if connection.is_connected():

    cursor.execute(
        """
        INSERT INTO students (name, age, marks)
        VALUES (%s, %s, %s)
        """,
        ("Rahul", 23, 90)
    )

    connection.commit()

    print("Student inserted successfully!")

# Important:
# SQLite uses ? placeholders.
# MySQL Connector uses %s placeholders.


# ============================================================
# 5. UPDATE MYSQL DATA
# ============================================================

if connection.is_connected():

    cursor.execute(
        """
        UPDATE students
        SET marks = %s
        WHERE id = %s
        """,
        (95, 1)
    )

    connection.commit()

    print("Student updated successfully!")


# ============================================================
# 6. DELETE MYSQL DATA
# ============================================================

if connection.is_connected():

    cursor.execute(
        "DELETE FROM students WHERE id = %s",
        (1,)
    )

    connection.commit()

    print("Student deleted successfully!")


# ============================================================
# 7. CLOSE MYSQL CONNECTION
# ============================================================

if connection.is_connected():

    cursor.close()

    connection.close()

    print("MySQL connection closed!")


# ============================================================
# 8. IMPORTANT MYSQL CONNECTION NOTES
# ============================================================

# Before running this file:
#
# 1. Install MySQL Server.
# 2. Start the MySQL server.
# 3. Create a database named college.
# 4. Create a students table.
# 5. Replace your_password with your MySQL password.
# 6. Run this Python file.
#
# Example database creation in MySQL:
#
# CREATE DATABASE college;
#
# USE college;
#
# CREATE TABLE students (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(100) NOT NULL,
#     age INT,
#     marks DECIMAL(5,2)
# );


# ============================================================
# 9. SQLITE VS MYSQL
# ============================================================

# SQLite:
# import sqlite3
# sqlite3.connect("students.db")
# Placeholder: ?
#
# MySQL:
# import mysql.connector
# mysql.connector.connect(...)
# Placeholder: %s
#
# SQLite:
# Database is stored in a local file.
#
# MySQL:
# Connects to a running database server.


# ============================================================
# MYSQL QUICK REVISION
# ============================================================

# Install:
# python -m pip install mysql-connector-python
#
# Import:
# import mysql.connector
#
# Connect:
# mysql.connector.connect(...)
#
# Cursor:
# connection.cursor()
#
# Execute:
# cursor.execute(query, values)
#
# Save:
# connection.commit()
#
# Close cursor:
# cursor.close()
#
# Close connection:
# connection.close()
#
# Use %s placeholders with MySQL Connector.
# Never expose database passwords in public code.
