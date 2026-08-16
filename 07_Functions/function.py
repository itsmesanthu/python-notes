# =========================================
# FUNCTIONS IN PYTHON
# =========================================

print("FUNCTIONS IN PYTHON")
print("Definition:")
print("A function is a block of code used to perform a specific task.")


# Function without parameter
def greet():
    print("Hello, welcome to Python!")


greet()
print("\n-------------------------")


# Function with parameter
def display_name(name):
    print("My name is", name)


display_name("Santhu")
print("\n-------------------------")


# Function with return value
def add(a, b):
    return a + b


result = add(10, 5)
print("Sum is:", result)
print("---------------------------------")


def call_examples():
    greet()
    display_name("Tanu")
    total = add(10, 20)
    print("Total is:", total)


call_examples()
print("\nProgram finished successfully!")
print("---------------------------------")
