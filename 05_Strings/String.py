# =========================================
# STRINGS IN PYTHON
# =========================================

print("STRINGS IN PYTHON")

# -----------------------------------------
# DEFINITION
# -----------------------------------------
print("Definition:")
print("A string is a sequence of characters enclosed in quotes.")
print("Strings are used to store text data like names, messages, or sentences.")

# -----------------------------------------
# TYPES OF QUOTES IN STRING
# -----------------------------------------
print("\nTypes of quotes in Python strings:")

# 1. Single quotes
a = "Python"
print("Single quote example:", a)

# 2. Double quotes
b = "Programming"
print("Double quote example:", b)

# 3. Triple quotes (used for multiline text)
c = """Python is
easy to learn"""
print("Triple quote example:")
print(c)

# -----------------------------------------
# STRING VARIABLES
# -----------------------------------------
name = "Santhu"
message = "Welcome to Python"
print("\nName:", name)
print("Message:", message)
print("Data type of name:", type(name))

# -----------------------------------------
# REAL WORLD EXAMPLE
# -----------------------------------------
print("\nREAL WORLD EXAMPLE")
student_name = "santhosh g p"
college = "m s Engineering College"
email = "gpsanthosanthu@gmail.com"
print("Student Name:", student_name)
print("College:", college)
print("Email:", email)

# -----------------------------------------
# STRING INDEXING
# -----------------------------------------
print("\nSTRING INDEXING EXAMPLE")
word = "Python"
print("First letter:", word[0])
print("Second letter:", word[1])
print("Last letter:", word[-1])

# -----------------------------------------
# STRING SLICING
# -----------------------------------------
print("\nSTRING SLICING EXAMPLE")
text = "PythonProgramming"
print("First 6 letters:", text[0:6])
print("From index 6:", text[6:])
print("Middle part:", text[3:10])
print("Reverse of the word:", text[::-1])
print("Skipping characters:", text[0::2])
print("Negative indexing:", text[-8:-2])

# -----------------------------------------
# STRING METHODS
# -----------------------------------------
print("\nSTRING METHODS EXAMPLE")
course = "python programming"
print("Uppercase:", course.upper())
print("Lowercase:", course.lower())
print("Title case:", course.title())
print("Replace:", course.replace("python", "Java"))
print("Count of 'p':", course.count("p"))

# -----------------------------------------
# LOOP WITH STRING
# -----------------------------------------
print("\nLOOP WITH STRING")
for letter in word:
    print(letter)

print("\nProgram finished successfully!")

