# =========================================
# FUNCTIONS IN PYTHON
# =========================================
print("FUNCTIONS IN PYTHON\n")
print("Definition:")
print("A function is a block of code used to perform a specific task.\n")
# Function without parameter
def greet():
    print("Hello, welcome to Python")
greet()
print("\n-------------------------\n")
# Function with parameter
def display_name(name):
    print("My name is", name)
display_name("Santhu")
print("\n-------------------------\n")
# Function with return value
def add(a, b):
    return a + b
result = add(10, 5)
print("Sum is:", result)
print("---------------------------------\n")
def RefuntionCalling():
    greet()
    display_name("tanu")
    sum=add(10,20)
    print("sum is:",sum)
RefuntionCalling()
print("\nProgram Finished Successfully!")
print("---------------------------------\n")
