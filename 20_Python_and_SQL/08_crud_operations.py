
# ============================================================
# COMPLETE CRUD OPERATIONS
# ============================================================

import sqlite3


# ============================================================
# 1. DATABASE CONNECTION
# ============================================================

def connect_database():

    connection = sqlite3.connect("students.db")

    return connection


# ============================================================
# 2. CREATE TABLE
# ============================================================

def create_table():

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            marks REAL
        )
    """)

    connection.commit()
    connection.close()

    print("Table created successfully!")


# ============================================================
# 3. CREATE - INSERT STUDENT
# ============================================================

def add_student(name, age, marks):

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students (name, age, marks)
        VALUES (?, ?, ?)
        """,
        (name, age, marks)
    )

    connection.commit()

    print("Student added successfully!")

    connection.close()


# ============================================================
# 4. READ - DISPLAY ALL STUDENTS
# ============================================================

def display_students():

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if not students:
        print("No students found!")

    else:

        for student in students:
            print(student)

    connection.close()


# ============================================================
# 5. READ - SEARCH STUDENT
# ============================================================

def search_student(student_id):

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("Student found:", student)

    else:
        print("Student not found!")

    connection.close()


# ============================================================
# 6. UPDATE - MODIFY STUDENT MARKS
# ============================================================

def update_student(student_id, marks):

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE students
        SET marks = ?
        WHERE id = ?
        """,
        (marks, student_id)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Student updated successfully!")

    else:
        print("Student ID not found!")

    connection.close()


# ============================================================
# 7. DELETE - REMOVE STUDENT
# ============================================================

def delete_student(student_id):

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")

    else:
        print("Student ID not found!")

    connection.close()


# ============================================================
# 8. MAIN MENU
# ============================================================

def main():

    create_table()

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")

        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        try:

            if choice == "1":

                name = input("Enter student name: ").strip()

                age = int(input("Enter age: "))

                marks = float(input("Enter marks: "))

                if not name:
                    print("Name cannot be empty!")

                elif age < 1 or not 0 <= marks <= 100:
                    print("Please enter valid age and marks!")

                else:
                    add_student(name, age, marks)


            elif choice == "2":

                display_students()


            elif choice == "3":

                student_id = int(input("Enter student ID: "))

                search_student(student_id)


            elif choice == "4":

                student_id = int(input("Enter student ID: "))

                marks = float(input("Enter new marks: "))

                if not 0 <= marks <= 100:
                    print("Marks must be between 0 and 100!")

                else:
                    update_student(student_id, marks)


            elif choice == "5":

                student_id = int(input("Enter student ID: "))

                delete_student(student_id)


            elif choice == "6":

                print("Thank you for using the application!")

                break


            else:

                print("Invalid choice! Try again.")


        except ValueError:

            print("Please enter valid numeric values!")


# ============================================================
# 9. PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":

    main()


# ============================================================
# CRUD QUICK REVISION
# ============================================================

# CREATE:
# INSERT INTO students (...)
#
# READ:
# SELECT * FROM students
#
# UPDATE:
# UPDATE students SET marks = ? WHERE id = ?
#
# DELETE:
# DELETE FROM students WHERE id = ?
#
# Python functions:
# add_student()
# display_students()
# search_student()
# update_student()
# delete_student()
#
# Main entry point:
# if __name__ == "__main__":
#     main()
