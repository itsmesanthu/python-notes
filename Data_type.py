# =========================================
# DATA TYPES IN PYTHON
# =========================================

print("DATA TYPES IN PYTHON\n")

# -----------------------------------------
# DEFINITION
# -----------------------------------------
print("Definition:")
print("Data type defines the type of value stored in a variable.")
print("Variables store data like numbers, text, or True/False.\n")

# -----------------------------------------
# MAIN DATA TYPES
# -----------------------------------------
print("MAIN DATA TYPES:\n")

# Integer
print("1. Integer (int) - Whole numbers")
age = 21
print("Value:", age)
print("Data Type:", type(age), "\n")

# Float
print("2. Float (float) - Decimal numbers")
height = 5.8
print("Value:", height)
print("Data Type:", type(height), "\n")

# String
print("3. String (str) - Text data")
name = "Santhu"
print("Value:", name)
print("Data Type:", type(name), "\n")

# Boolean
print("4. Boolean (bool) - True or False")
is_student = True
print("Value:", is_student)
print("Data Type:", type(is_student), "\n")

# =========================================
# REAL WORLD EXAMPLE
# =========================================

print("REAL WORLD EXAMPLE: STUDENT INFORMATION SYSTEM\n")

student_name = "santhosh"     # string
student_age = 22           # integer
student_marks = 85.5       # float
is_passed = True           # boolean

print("Student Name:", student_name)
print("Student Age:", student_age)
print("Student Marks:", student_marks)
print("Passed Status:", is_passed)

print("\nChecking Data Types:")
print(type(student_name))
print(type(student_age))
print(type(student_marks))
print(type(is_passed))


# =========================================
# user intput checking the given intput is what type
# =========================================
str1=input("enter the vlue : ")
print(str1)
print(type(str1))