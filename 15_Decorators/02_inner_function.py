# ============================================================
# INNER FUNCTION
# ============================================================
#
# An inner function is a function defined inside
# another function.
#
#
# Syntax:
#
# def outer():
#
#     def inner():
#         # inner function code
#
#     inner()
# ============================================================


# ============================================================
# 1. BASIC INNER FUNCTION
# ============================================================

def outer():

    def inner():
        print("Inside inner function")

    inner()


outer()


# Output:
# Inside inner function


# ============================================================
# 2. OUTER AND INNER FUNCTION
# ============================================================

def outer():

    print("Outer function")

    def inner():
        print("Inner function")

    inner()


outer()


# Output:
# Outer function
# Inner function


# ============================================================
# 3. INNER FUNCTION WITH PARAMETERS
# ============================================================

def outer(name):

    def inner():
        print("Hello", name)

    inner()


outer("Santhu")


# Output:
# Hello Santhu


# ============================================================
# 4. RETURNING INNER FUNCTION
# ============================================================

def outer():

    def inner():
        print("Inner function")

    return inner


result = outer()

result()


# Output:
# Inner function


# ============================================================
# 5. INNER FUNCTION WITH CALCULATION
# ============================================================

def calculator():

    def add(a, b):
        return a + b

    result = add(10, 20)

    print(result)


calculator()


# Output:
# 30


# ============================================================
# 6. INNER FUNCTION CAN ACCESS OUTER VARIABLES
# ============================================================

def outer():

    message = "Hello Python"

    def inner():
        print(message)

    inner()


outer()


# Output:
# Hello Python


# ============================================================
# QUICK REVISION
# ============================================================
#
# Inner Function
#     ↓
# A function defined inside another function.
#
#
# Outer Function
#     ↓
# Function that contains another function.
#
#
# Inner functions are commonly used when creating
# decorators.
# ============================================================