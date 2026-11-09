
# ============================================================
# DATABASE BASICS
# ============================================================

# A database is an organized collection of information.
#
# Examples:
# 1. Student database
# 2. Employee database
# 3. Banking database
# 4. Hospital database
# 5. E-commerce database
#
# Python can communicate with databases using SQL.


# ============================================================
# 1. WHAT IS A DATABASE?
# ============================================================

# Example: Student Database
#
# ID     Name       Age     Marks
# --------------------------------
# 1      Santhosh   22      85
# 2      Rahul      23      90
# 3      Priya      21      92
#
# A database stores this information permanently.


# ============================================================
# 2. WHAT IS SQL?
# ============================================================

# SQL stands for Structured Query Language.
#
# SQL is used to communicate with relational databases.
#
# Common SQL commands:
#
# CREATE  - Create database objects such as tables
# INSERT  - Add records
# SELECT  - Retrieve records
# UPDATE  - Modify records
# DELETE  - Remove records
# DROP    - Remove database objects


# ============================================================
# 3. WHAT IS A TABLE?
# ============================================================

# A table stores information in rows and columns.
#
# Example: students
#
# +----+----------+-----+-------+
# | id | name     | age | marks |
# +----+----------+-----+-------+
# | 1  | Santhosh | 22  | 85    |
# | 2  | Rahul    | 23  | 90    |
# | 3  | Priya    | 21  | 92    |
# +----+----------+-----+-------+
#
# Row    - One complete record
# Column - One type of information


# ============================================================
# 4. WHAT IS A PRIMARY KEY?
# ============================================================

# A primary key uniquely identifies each record.
#
# Example:
#
# id = 1
# id = 2
# id = 3
#
# Each student has a unique ID.
#
# A primary key must be unique and cannot be NULL.


# ============================================================
# 5. WHAT IS A FOREIGN KEY?
# ============================================================

# A foreign key connects one table to another.
#
# Example:
#
# students table:
# id | name
# 1  | Rahul
# 2  | Priya
#
# courses table:
# id | student_id | course
# 1  | 1          | Python
# 2  | 2          | Java
#
# student_id refers to the id in the students table.


# ============================================================
# 6. WHAT IS PYTHON + SQL?
# ============================================================

# Python application
#        |
#        v
# Database connection
#        |
#        v
# SQL query
#        |
#        v
# Database
#
# Python sends SQL commands to the database.
# The database executes those commands.
# Python receives the results.


# ============================================================
# 7. TYPES OF DATABASES
# ============================================================

# Relational databases:
# - MySQL
# - PostgreSQL
# - SQLite
# - Oracle Database
#
# NoSQL databases:
# - MongoDB
# - Redis
# - Cassandra
#
# This topic focuses on SQLite and MySQL.


# ============================================================
# 8. WHAT IS SQLITE?
# ============================================================

# SQLite is a lightweight relational database.
#
# Features:
# - Included with Python through sqlite3
# - No separate database server required
# - Stores data in a database file
# - Useful for learning and small applications


# ============================================================
# 9. WHAT IS MYSQL?
# ============================================================

# MySQL is a relational database management system.
#
# Features:
# - Uses a database server
# - Supports multiple users and applications
# - Commonly used in web applications
# - Can connect with Python using a connector package


# ============================================================
# DATABASE BASICS QUICK REVISION
# ============================================================

# Database:
# Organized collection of information.
#
# SQL:
# Structured Query Language.
#
# Table:
# Stores records in rows and columns.
#
# Primary key:
# Uniquely identifies a record.
#
# Foreign key:
# Connects related tables.
#
# CRUD:
# Create, Read, Update, Delete.
#
# SQLite:
# Lightweight database included with Python.
#
# MySQL:
# Relational database server.
