# =========================================
# STRINGS IN PYTHON
# =========================================
print("STRINGS IN PYTHON\n")
# -----------------------------------------
# DEFINITION
# -----------------------------------------
print("Definition:")
print("A string is a sequence of characters enclosed in quotes.")
print("Strings are used to store text data like names, messages, or sentences.\n")
# -----------------------------------------
# TYPES OF QUOTES IN STRING
# -----------------------------------------
print("Types of Quotes in Python Strings:\n")
# 1. Single Quotes
a = 'Python'
print("Single Quote Example:", a)
# 2. Double Quotes
b = "Programming"
print("Double Quote Example:", b)
# 3. Triple Quotes (used for multiline text)
c = '''Python is
easy to learn'''
print("Triple Quote Example:")
print(c)
print("\n")
# -----------------------------------------
# STRING VARIABLES
# -----------------------------------------
name = "Santhu"
message = "Welcome to Python"
print("Name:", name)
print("Message:", message)
print("Data Type of name:", type(name))
print("\n")
# -----------------------------------------
# REAL WORLD EXAMPLE
# -----------------------------------------
print("REAL WORLD EXAMPLE\n")
student_name = "santhosh g p"
college = "m s Engineering College"
email = "gpsanthosanthu@gmail.com"
print("Student Name:", student_name)
print("College:", college)
print("Email:", email)
print("\n")
# -----------------------------------------
# STRING INDEXING
# -----------------------------------------
print("STRING INDEXING EXAMPLE\n")
word = "Python"
print("First letter:", word[0])
print("Second letter:", word[1])
print("Last letter:", word[-1])
print("\n")
# -----------------------------------------
# STRING SLICING
# -----------------------------------------
print("STRING SLICING EXAMPLE\n")
text = "PythonProgramming"
print("First 6 letters:", text[0:6])
print("From index 6:", text[6:])
print("Middle part:", text[3:10])
print("revers the word :", text[::-1])
print("skiping :",text[0::2])
print("negative index using : ",text[-8:-2])
print("\n")
# -----------------------------------------
# STRING METHODS
# -----------------------------------------
print("STRING METHODS EXAMPLE\n")
course = "python programming"
print("Uppercase:", course.upper())
print("Lowercase:", course.lower())
print("Title case:", course.title())
print("Replace:", course.replace("python", "Java"))
print("Count of 'p':", course.count("p"))
print("\n")
# -----------------------------------------
# LOOP WITH STRING
# -----------------------------------------
print("LOOP WITH STRING\n")
word = "Python"
for letter in word:
    print(letter)
print("\nProgram Finished Successfully!")
s="-----------------------------------------"
print(len(s))